from CopyBookField import CopyBookField
from CopyBook import CopyBook
from re import sub


class CopyBookParser:
    def __init__(self, copybook_path, data_file_path):
        self.copybook_path = copybook_path
        self.data_file = data_file_path
        self.current_master_record = None
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
        if self.is_blank_line(line) or self.is_comment(line):
            return

        if self.is_master_record(line):
            self.current_master_record = self.create_master_record(line)

        if self.is_sub_record(line):
            sub_record = self.create_copybook_record(line)
            self.current_master_record.sub_records.append(sub_record)

        if self.is_record(line):
            record = self.create_copybook_record(line)
            self.copybook_records.append(record)

    def is_blank_line(self, line):
        return not line

    def is_comment(self, line):
        return line[6] == '*'

    # Record that doesn't have a 'PIC' defined, but has sub-records
    def is_master_record(self, line):
        return "PIC" not in line

    # Record that has a 'PIC' defined, and has a master record
    def is_sub_record(self, line):
        return self.current_master_record is not None and "PIC" in line

    # Stand-alone record. Does not have a master record, and is defined with a 'PIC' clause
    def is_record(self, line):
        return self.current_master_record is None and "PIC" in line

    # Create CopyBookField object model for each line in copybook file
    def create_copybook_record(self, line):
        cpybook_line_fields = self.format_copybook_line(line)

        if len(cpybook_line_fields) < 5:
            print("Invalid copybook line")
        else:
            level = cpybook_line_fields[0]
            name = cpybook_line_fields[1]
            pic_value = "{} {}".format(cpybook_line_fields[2], cpybook_line_fields[3])

            if len(cpybook_line_fields) > 5:
                value = cpybook_line_fields[4] + cpybook_line_fields[5]
            else:
                value = None

            return CopyBookField(level, name, pic_value, value)
        
        return None

    # Copybook Record that doesn't have a PIC defined, but has sub-records
    def create_master_record(self, line):
        cpybook_line_fields = self.format_copybook_line(line)

        if len(cpybook_line_fields) < 2:
            print("Invalid copybook line")
        else:
            level = cpybook_line_fields[0]
            name = cpybook_line_fields[1]

            return CopyBookField(level, name)

        return None

    # Strip extra spaces, punctation from copybook line, split into a list
    def format_copybook_line(self, line):
        return sub(' +', ' ', line).rstrip('.').split(' ')