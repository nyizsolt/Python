from csv_exporter import CSVExporter
from db import DB


class ConverterController:

    def __init__(self):
        self.db = DB()
        self.csv_exporter = CSVExporter()

    def export_tables(self, table_name_list):
        for table_name in table_name_list:
            rows = self.db.find_all_rows_in_table(table_name)
            self.csv_exporter.write_to_csv(rows,table_name)

    def find_all_table_names(self):
        return self.db.find_all_table_names()
