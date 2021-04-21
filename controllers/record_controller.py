from flask_restful import Resource

from services.records_service import RecordsService


class RecordResource(Resource):
    record_service = RecordsService()

    def get(self, record_id):
        return {"record":
                    [item.to_dict(only=("id", "purchase_date", "record_type_id", "ticket_id", "user_id"))
                     for item in self.record_service.get_record(record_id)]}

    def post(self, record):
        self.record_service.add(record)
        return {'success': 'OK'}

    def put(self, record_id, record):
        self.record_service.update(record_id, record)
        return {'success': 'OK'}

    def delete(self, record_id):
        self.record_service.delete(record_id)
        return {'success': 'OK'}


class RecordListResources(Resource):
    record_service = RecordsService()

    def get(self):
        return {"records":
                    [item.to_dict(only=("id", "purchase_date", "record_type_id", "ticket_id", "user_id"))
                     for item in self.record_service.get_all()]}
