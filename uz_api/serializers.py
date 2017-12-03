class Serializer:
    @staticmethod
    def serialize(objects):
        return [obj.to_dict() for obj in objects]
