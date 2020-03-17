class CopyBook:
    def __init__(self):
        # Every '05' Level Record in a Copybook
        self.cpybook_fields = []
        # Use current directory for testing
        self.cpybook_path = '.'

    def parse_fields(self):
        with open(self.cpybook_path, 'r') as cpybook:
            for line in cpybook:
                stripped_line = line[6:].strip()
                self.process_line(stripped_line)

    def process_line(self, line):
        if self.is_comment(line):
            return
        if self.is_new_record(line):
            pass
        if self.is_sub_record(line):
            pass

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

    def display_cpybook_fields(self, show_with_attrs = False):
        print("\n\nCopybook Fields:")
        for field in self.cpybook_fields:
            if show_with_attrs:
                field_content = field.to_string()
            else:
                field_content = field.name
            print("  {}".format(field_content))