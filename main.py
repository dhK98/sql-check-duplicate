from lib.check_duplicate_v1 import DuplicateChecker 
from lib.produce_file import FileProducer

def main():
    print("start check duplicate")
    duplicate_checker = DuplicateChecker()
    file_path = "./test/test1.sql"
    duplicate_checker.analyze_sql_file(file_path)
    print(len(duplicate_checker.data_arr))
    print("================result=================")
    for i in range(len(duplicate_checker.data_arr)):
        # print(duplicate_checker.data_arr[i].data)
        # split = duplicate_checker.data_arr[i].data[0].split(';')
        # print("--start split--")
        # print(len(split))
        # for j in range(len(split)):
        #     print(f" {split[j]} \n")
        # print("--end split--")

        print(duplicate_checker.data_arr[i].data)
        print(duplicate_checker.data_arr[i].recursion_number)
    
    print(f"rest que1: {duplicate_checker.q1}")
    print(f"rest que1: {duplicate_checker.q2}")
    file_producer = FileProducer(duplicate_checker.data_arr)
    file_producer.create_file('copyfile1.sql')
main()