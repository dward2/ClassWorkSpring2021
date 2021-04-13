from pymodm import MongoModel, fields


class ImageRecord(MongoModel):
    net_id = fields.CharField()
    id_no = fields.IntegerField()
    image = fields.CharField()