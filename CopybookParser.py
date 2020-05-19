from CopyBookField import CopyBookField
from CopyBook import CopyBook
from re import sub


class CopyBookParser:
    def __init__(self, copybook_path, data_file_path):
        self.copybook_path = copybook_path
        self.data_file = data_file_path
        self.copybook_records = []

    # Create CopyBook Model Object - copybook file as input
    def create_copybook(self):
        cpybook = CopyBook(self.copybook_path)
        self.parse_fields_from_copybook()
        cpybook.set_fields(self.copybook_records)

        return cpybook

    # Open copybook file input, read each line into model object
    def parse_fields_from_copybook(self):
        with open(self.copybook_path, 'r') as cpybook:
            for line in cpybook:
                stripped_line = line[6:].strip()
                self.process_line(stripped_line)

    # Determine what each line of the copybook is
    def process_line(self, line):
        if self.is_blank_line(line) or self.is_comment(line) or self.is_88_level(line):
            return
        else:
            record = self.create_copybook_record(line)
            if record:
                self.copybook_records.append(record)

    def is_blank_line(self, line):
        return not line

    def is_comment(self, line):
        return line[0] == '*'

    def is_88_level(self, line):
        return '88' in line

    # Create CopyBookField object model for each line in copybook file
    def create_copybook_record(self, line):
        cpybook_line_fields = self.format_copybook_line(line)

        if len(cpybook_line_fields) > 2:
            level = cpybook_line_fields[0]
            name = cpybook_line_fields[1]
            pic_value = f"{cpybook_line_fields[2]} {cpybook_line_fields[3]}"

            return CopyBookField(level, name, pic_value)

    # Strip extra spaces, punctation from copybook line, split into a list
    def format_copybook_line(self, line):
        return sub(' +', ' ', line).rstrip('.').split(' ')