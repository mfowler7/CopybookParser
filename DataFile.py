class DataFile:
    def __init__(self, data_file_path):
        self.data_file_path = data_file_path

    def get_line(self, line_number):
        with open(self.data_file_path) as df:
            line = df.readline()
            return line.split('|')
