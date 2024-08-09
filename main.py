from lib.check_duplicate_v1 import DuplicateChecker 
from lib.produce_file import FileProducer

def main():
    print("start check duplicate")
    duplicate_checker = DuplicateChecker()
    test_file_path = "./test/test1.sql"
    duplicate_checker.analyze_sql_file(test_file_path)
    file_name = test_file_path.split('/')[-1]
    print(len(duplicate_checker.data_arr))
    print("================result=================")
    for i in range(len(duplicate_checker.data_arr)):
        print(duplicate_checker.data_arr[i].data)
        print(duplicate_checker.data_arr[i].recursion_number)
    file_producer = FileProducer(duplicate_checker.data_arr)
    file_producer.create_file(file_name)
main()