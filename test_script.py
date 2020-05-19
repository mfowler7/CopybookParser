import CopyBookParser
from CopyBookCompare import CopyBookCompare
from DataFile import DataFile 


def main():
    cpybook_path = 'test.cpy'
    data_file_path = 'test.txt'
    
    # Create object model to represent the Copybook
    cpybook_parser = CopyBookParser.CopyBookParser(cpybook_path, data_file_path)
    cpybook = cpybook_parser.create_copybook()
    
    # Create object model to represent the Data File
    data_file = DataFile(data_file_path)

    cpybook_comparer = CopyBookCompare(cpybook, data_file)
    cpybook_comparer.compare_copybook_with_data()

if __name__ == "__main__":
    main()