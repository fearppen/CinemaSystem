from repository.record_types_repository import RecordTypesRepositorySQLAlchemy


class RecordTypeService:
    record_types_repository = RecordTypesRepositorySQLAlchemy()

    def get_all(self):
        return self.record_types_repository.get_all()

    def get_record_type(self, record_type_id):
        return [self.record_types_repository.get_record_type(record_type_id)]
