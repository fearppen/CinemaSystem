from flask import jsonify
from flask_restful import Resource

from services.record_types_service import RecordTypeService


class RecordTypesResource(Resource):
    def get(self, record_type_id):
        return jsonify({"record_type": [item.to_dict for item in
                                        RecordTypeService.get_record_type(record_type_id)]})


class RecordTypesListResources(Resource):
    def get(self):
        return jsonify({"record_types": [item.to_dict for item in RecordTypeService.get_all()]})
