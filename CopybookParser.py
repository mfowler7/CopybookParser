from CopyBookField import CopyBookField

class CopybookParser:
    def __init__(self, copybook):
        self.copybook = copybook
        self.current_field = None
        self.copybook_fields = []

    def parse_fields(self):
        with open(self.copybook.cpybook_path, 'r') as cpybook:
            for line in cpybook:
                stripped_line = line[6:].strip()
                self.process_line(stripped_line)

    def process_line(self, line):
        if self.is_comment(line):
            return
        if self.is_new_record(line):
            self.copybook_fields.append(self.current_field)
            field = self.create_copybook_field(line)
            self.current_field = field
        if self.is_sub_record(line):
            pass
            # sub_record = self.create_copybook_subfield(line)
            # self.current_field.default_values.append(sub_record)

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
        sub_fields = line.split(' ')

        level = sub_fields[0]
        name = sub_fields[1]
        pic_value = sub_fields[3]

        return CopyBookField(level, name, pic_value)

    def create_copybook_subfield(self, line):
        pass