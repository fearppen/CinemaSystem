from repository.records_repository import RecordsRepositorySQLAlchemy


class RecordsService:
    records_repository = RecordsRepositorySQLAlchemy()

    def get_all(self):
        return {"records": [item.to_dict
                            (only=("id", "purchase_date", "record_type_id", "ticket_id", "user_id"))
                            for item in self.records_repository.get_all()]}

    def get_record(self, record_id):
        record = self.records_repository.get_record(record_id)
        if record:
            return {"record": [item.to_dict
                               (only=("id",
                                      "purchase_date",
                                      "record_type_id",
                                      "ticket_id",
                                      "user_id"))
                               for item in [record]]}

    def add(self, record):
        self.records_repository.add(record)
        return {"success": "ok"}

    def update(self, record_id, record):
        if self.records_repository.get_record(record_id):
            self.records_repository.update(record_id, record)
            return {"success": "ok"}
        return {"error": "not found"}

    def delete(self, record_id):
        if self.records_repository.get_record(record_id):
            self.records_repository.delete(record_id)
            return {"success": "ok"}
        return {"error": "not found"}
