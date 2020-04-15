from CopyBookField import CopyBookField
from CopyBook import CopyBook
from re import sub


class CopyBookParser:
    def __init__(self, copybook_path, data_file_path):
        self.copybook_path = copybook_path
        self.data_file = data_file_path
        self.current_field = None
        self.copybook_fields = []

    def create_copybook(self):
        cpybook = CopyBook(self.copybook_path)
        self.parse_fields_from_copybook()
        cpybook.set_fields(self.copybook_fields)

        return cpybook

    def parse_fields_from_copybook(self):
        with open(self.copybook_path, 'r') as cpybook:
            for line in cpybook:
                stripped_line = line[6:].strip()
                self.process_line(stripped_line)

    def process_line(self, line):
        if self.is_blank_line(line) or self.is_comment(line):
            return

        if self.is_new_record(line):
            if self.current_field is not None:
                self.copybook_fields.append(self.current_field)
            
            field = self.create_copybook_field(line)
            self.current_field = field

        if self.is_sub_record(line):
            pass
            # sub_record = self.create_copybook_subfield(line)
            # self.current_field.default_values.append(sub_record)

    def is_blank_line(self, line):
        return not line

    def is_comment(self, line):
        return line[6] == '*'

    def is_new_record(self, line):
        if len(line) >= 2:
            return line[0:2] == '05'

        return False

    def is_sub_record(self, line):
        if len(line) >= 2:
            return line[0:2] == '10'

        return False

    def create_copybook_field(self, line):
        formatted_line = sub(' +', ' ', line).rstrip('.')

        sub_fields = formatted_line.split(' ')

        print("sub fields: {}".format(sub_fields))

        if len(sub_fields) > 2:
            level = sub_fields[0]
            name = sub_fields[1]
            pic_value = "{} {}".format(sub_fields[2], sub_fields[3])
            #value = sub_fields[4] + sub_fields[5]

            return CopyBookField(level, name, pic_value)
        else:
            return None

    def create_copybook_subfield(self, line):
        pass
