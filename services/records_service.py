from repository.records_repository import RecordsRepositorySQLAlchemy


class RecordsService:
    def get_all(self):
        return RecordsRepositorySQLAlchemy.get_all()

    def get_record(self, record_id):
        return RecordsRepositorySQLAlchemy.get_record(record_id)

    def add(self, record):
        return RecordsRepositorySQLAlchemy.add(record)

    def update(self, record_id, record):
        return RecordsRepositorySQLAlchemy.update(record_id, record)

    def delete(self, record_id):
        return RecordsRepositorySQLAlchemy.delete(record_id)
