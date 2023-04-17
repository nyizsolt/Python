import os


class CSVExporter:

    def write_to_csv(self, list, file_name):
        with open("export" + os.sep + file_name + ".csv", "w", encoding="utf-8") as file:
            for row in list:
                file.write(self.list_to_comma_separated_string(row) + "\n")

    def list_to_comma_separated_string(self, list):
        return ','.join(list)
