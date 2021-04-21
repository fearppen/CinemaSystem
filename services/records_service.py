from repository.records_repository import RecordsRepositorySQLAlchemy


class RecordsService:
    records_repository = RecordsRepositorySQLAlchemy()

    def get_all(self):
        return self.records_repository.get_all()

    def get_record(self, record_id):
        return [self.records_repository.get_record(record_id)]

    def add(self, record):
        return self.records_repository.add(record)

    def update(self, record_id, record):
        return self.records_repository.update(record_id, record)

    def delete(self, record_id):
        return self.records_repository.delete(record_id)
