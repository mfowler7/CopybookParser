from CopyBookField import CopyBookField

class CopyBook:
    def __init__(self):
        # Every '05' Level Record in a Copybook
        self.cpybook_fields = []
        # Use current directory for testing
        self.cpybook_path = '.'

    def display_cpybook_fields(self, show_with_attrs = False):
        print("\n\nCopybook Fields:")
        for field in self.cpybook_fields:
            if show_with_attrs:
                field_content = field.to_string()
            else:
                field_content = field.name
            print("  {}".format(field_content))