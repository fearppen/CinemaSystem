from flask_restful import Resource

from services.record_types_service import RecordTypeService


class RecordTypesResource(Resource):
    record_type_service = RecordTypeService()

    def get(self, record_type_id):
        return {"record_type": [item.to_dict(only=("id", "title"))
                                for item in
                                self.record_type_service.get_record_type(record_type_id)]}


class RecordTypesListResources(Resource):
    record_type_service = RecordTypeService()

    def get(self):
        return {"record_types": [item.to_dict(only=("id", "title"))
                                 for item in self.record_type_service.get_all()]}
