from flask import jsonify
from flask_restful import Resource

from services.records_service import RecordsService


class RecordResource(Resource):
    def get(self, record_id):
        return jsonify({"record": [item.to_dict for item in RecordsService.get_record(record_id)]})

    def post(self, record):
        RecordsService.add(record)
        return jsonify({'success': 'OK'})

    def put(self, record_id, record):
        RecordsService.update(record_id, record)
        return jsonify({'success': 'OK'})

    def delete(self, record_id):
        RecordsService.delete(record_id)
        return jsonify({'success': 'OK'})


class RecordListResources(Resource):
    def get(self):
        return jsonify({"records": [item.to_dict for item in RecordsService.get_all()]})
