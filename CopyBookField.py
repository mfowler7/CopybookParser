class CopyBookField:
    def __init__(self, level, name, pic_value=None, value=None):
        self.level = level
        self.name = name
        # The PIC X/9 - How to store negative/decimal values (i.e. -9(11)v99)
        self.pic_value = pic_value
        # PIC X(20) - only store the '20'
        self.size = 0
        # The '10' Level records beneath the '05' Level records
        self.sub_records = []
        # 88 Level Records
        self.default_fields = []

    def to_string(self):
        return f"{self.level}   {self.name}   {self.pic_value}"
