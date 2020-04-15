import CopyBookParser
from CopyBookCompare import CopyBookCompare
from DataFile import DataFile 


def main():
    cpybook_path = 'test.cpy'
    data_file_path = 'test.txt'
    
    cpybook_parser = CopyBookParser.CopyBookParser(cpybook_path, data_file_path)
    cpybook = cpybook_parser.create_copybook()
    data_file = DataFile(data_file_path)

    #cpybook_comparer = CopyBookCompare(cpybook, data_file)
    field1 = cpybook.copybook_fields[0].to_string()
    print("First field: {}".format(field1))

if __name__ == "__main__":
    main()