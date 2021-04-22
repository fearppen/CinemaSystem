from flask_restful import Resource

from services.records_service import RecordsService


class RecordResource(Resource):
    record_service = RecordsService()

    def get(self, record_id):
        return self.record_service.get_record(record_id)

    def post(self, record):
        return self.record_service.add(record)

    def put(self, record_id, record):
        return self.record_service.update(record_id, record)

    def delete(self, record_id):
        return self.record_service.delete(record_id)


class RecordListResources(Resource):
    record_service = RecordsService()

    def get(self):
        return self.record_service.get_all()
