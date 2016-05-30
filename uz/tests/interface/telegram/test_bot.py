import time
from datetime import datetime

import mock
import pytest

from uz.tests import Awaitable

from uz.interface.telegram import tg_bot
from uz.scanner import UknkownScanID


CHAT_ID = 'chat_id'


def tg_message(text):
    return {
        'chat': {
            'id': CHAT_ID,
            'type': 'private',
        },
        'from': {'first_name': 'n/a', 'id': 'user_id'},
        'message_id': int(time.time()),
        'text': text
    }


def get_reply(send_message_mock):
    args, kwargs = send_message_mock.call_args_list[0]
    return args[1]


@pytest.mark.asyncio
async def test_list_trains(source_station, destination_station, train):
    tg_bot.send_message = send_message = mock.MagicMock(return_value=Awaitable())
    date = datetime(2016, 7, 21)
    command = '/trains {} {} {}'.format(
        date.strftime('%Y-%m-%d'), source_station.title, destination_station.title)
    with mock.patch('uz.interface.serializer.Deserializer.load',
                    return_value=Awaitable((date, source_station, destination_station))) as load, \
            mock.patch('uz.client.client.UZClient.list_trains',
                       return_value=Awaitable([train])) as list_trains:
        await tg_bot._process_message(tg_message(command))
    load.assert_called_once_with({
        'date': date.strftime('%Y-%m-%d'),
        'source': source_station.title,
        'destination': destination_station.title})
    list_trains.assert_called_once_with(date, source_station, destination_station)
    msg = get_reply(send_message)
    title = 'Trains from %s to %s on %s:' % (
        source_station, destination_station, date.date())
    assert msg.startswith(title)
    assert train.info() in msg


@pytest.mark.asyncio
@pytest.mark.parametrize('is_ok', [True, False])
async def test_status(is_ok):
    scan_id = 'id1234'
    scanner = mock.MagicMock()
    if is_ok:
        scanner.status.return_value = (attempts, error) = (10, 'i am error')
    else:
        scanner.status.side_effect = UknkownScanID()
    tg_bot.send_message = send_message = mock.MagicMock(return_value=Awaitable())
    tg_bot.set_scanner(scanner)
    await tg_bot._process_message(tg_message('/status {}'.format(scan_id)))
    scanner.status.assert_called_once_with(scan_id)
    if is_ok:
        send_message.assert_called_once_with(
            CHAT_ID, 'No attempts: {}\nLast error message: {}'.format(attempts, error))
    else:
        send_message.assert_called_once_with(
            CHAT_ID, 'Unknown scan id: {}'.format(scan_id))


@pytest.mark.asyncio
@pytest.mark.parametrize('is_ok', [True, False])
async def test_abort_scan(is_ok):
    scan_id = 'id4321'
    scanner = mock.MagicMock()
    if is_ok:
        scanner.abort.return_value = True
    else:
        scanner.abort.side_effect = UknkownScanID()
    tg_bot.send_message = send_message = mock.MagicMock(return_value=Awaitable())
    tg_bot.set_scanner(scanner)
    await tg_bot._process_message(tg_message('/abort {}'.format(scan_id)))
    scanner.abort.assert_called_once_with(scan_id)
    if is_ok:
        send_message.assert_called_once_with(
            CHAT_ID, 'OK')
    else:
        send_message.assert_called_once_with(
            CHAT_ID, 'Unknown scan id: {}'.format(scan_id))


@pytest.mark.asyncio
@pytest.mark.parametrize('ct_letter', [None, 'C2'])
async def test_scan(source_station, destination_station, ct_letter):
    scan_id = 'id1234'
    date = datetime(2016, 10, 7)
    train_num = '744K'
    command = '/scan {} {} {} {}'.format(
        date.strftime('%Y-%m-%d'), source_station, destination_station, train_num)
    if ct_letter:
        command += ' {}'.format(ct_letter)

    scanner = mock.MagicMock()
    scanner.add_item.return_value = Awaitable(scan_id)
    tg_bot.send_message = send_message = mock.MagicMock(return_value=Awaitable())
    tg_bot.set_scanner(scanner)

    with mock.patch('uz.interface.serializer.Deserializer.load',
                    return_value=Awaitable((date, source_station, destination_station))) as load:
        await tg_bot._process_message(tg_message(command))
    load.assert_called_once_with({
        'date': date.strftime('%Y-%m-%d'),
        'source': source_station.title,
        'destination': destination_station.title,
        'train_num': train_num,
        'ct_letter': ct_letter})
    scanner.add_item.assert_called_once_with(
        mock.ANY, 'Firstname', 'Lastname', date, source_station, destination_station,
        train_num, ct_letter)
    expected = ('Scanning tickets for train {} from {} to {} on {}.\n'
                'To monitor scan status use command:\n'
                '/status {}').format(
        train_num, source_station, destination_station, date.date(), scan_id)
    send_message.assert_called_once_with(CHAT_ID, expected)


@pytest.mark.asyncio
async def test_hello():
    tg_bot.send_message = send_message = mock.MagicMock(return_value=Awaitable())
    await tg_bot._process_message(tg_message('hi'))
    send_message.assert_called_once_with(
        CHAT_ID, 'Hello! I am UZ Tickets Bot! Use /help to see what I can')


@pytest.mark.asyncio
async def test_help_msg():
    tg_bot.send_message = send_message = mock.MagicMock(return_value=Awaitable())
    await tg_bot._process_message(tg_message('/help'))
    send_message.assert_called_once_with(CHAT_ID, 'Help is on it\'s way!')