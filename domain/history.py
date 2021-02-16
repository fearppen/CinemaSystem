from domain.record import Record


class History:
    def __init__(self):
        self.records = []

    def get_records(self):
        return self.records

    def set_records(self, records: list):
        self.records = records

    def add_record(self, record: Record):
        self.records.append(record)

    def remove_record(self, index: int):
        self.records.pop(index)
