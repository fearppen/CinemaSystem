from repository.record_types_repository import RecordTypesRepositorySQLAlchemy


class RecordTypeService:
    def get_all(self):
        return RecordTypesRepositorySQLAlchemy.get_all()

    def get_record_type(self, record_type_id):
        return RecordTypesRepositorySQLAlchemy.get_record_type(record_type_id)
