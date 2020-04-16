class CopyBook:
    def __init__(self, copybook_path):
        self.copybook_fields = []
        # Use current directory for testing
        self.copybook_path = copybook_path

    def display_copybook_fields(self, show_with_attrs=False):
        print("\n\nCopybook Fields:")
        for field in self.copybook_fields:
            if show_with_attrs:
                field_content = field.to_string()
            else:
                field_content = field.name
            print("  {}".format(field_content))

    def set_fields(self, fields):
        self.copybook_fields = fields
