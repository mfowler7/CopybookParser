class CopyBookField:
    def __init__(self, name, data_type, size):
        self.name = name
        # The PIC X/9 - How to store negative/decimal values (i.e. -9(11)v99)
        self.data_type = data_type
        # PIC X(20) - only store the '20'
        self.size = size
        # The '10' Level records beneath the '05' Level records
        self.default_values = []
