import CopyBookParser
from CopyBookCompare import CopyBookCompare
from DataFile import DataFile 


def main():
    cpybook_path = 'text.cpy'
    data_file_path = 'test.txt'
    
    cpybook_parser = CopyBookParser.CopyBookParser(cpybook_path, data_file_path)
    cpybook = cpybook_parser.create_copybook()
    data_file = DataFile(data_file_path)

    cpybook_comparer = CopyBookCompare(cpybook, data_file)
