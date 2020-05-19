class CopyBookCompare:
    def __init__(self, copybook, data_file):
        self.copybook = copybook
        self.data_file = data_file

    def compare_copybook_with_data(self):
        for field in self.copybook.copybook_fields:
            if field.name == "FILLER":
                pass
            else:
                print(f"Field: {field.name}")

    def display_first_line(self):
        pass
