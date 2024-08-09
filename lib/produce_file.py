import lib.file_data as file_data
import os

class FileProducer:
    data_arr: list[file_data.FileData]
    def __init__(self, data_arr) -> None:
        self.data_arr = data_arr

    def create_file(self, file_name):
        try:
            if not os.path.exists('./copy_files'):
                os.mkdir('copy_files')
            idx = 1
            while True:
                file_name_idx = f"{file_name}_{idx}"
                if not os.path.exists('./copy_files/'+file_name_idx):
                    break
                idx += 1
            include_path_file_name = f"./copy_files/{file_name_idx}"
            if not self.data_arr or len(self.data_arr) <= 0:
                raise Exception("not exist data")
            # formater => create sql
            if os.path.exists(include_path_file_name):
                raise FileExistsError
            with open(include_path_file_name, 'w', encoding='utf-8') as file:
                for data in self.data_arr:
                    file.write(self.data_arr_to_sql(data))

        except Exception as e:
            print(f"An error occurred: {e}")

    
    def data_arr_to_sql(self, data: file_data.FileData):
        recursion_number = data.recursion_number
        if recursion_number == 1:
            return ''.join([string+"\n" for string in data.data])
        else:
            string_data = ''
            string_data += f"DECLARE\n \tL_CNT NUMBER:=0;\n BEGIN\n \tLOOP\n \t\tL_CNT:=L_CNT+1;\n \t\tEXIT WHEN L_CNT>={recursion_number};\n"
            for data_el in data.data:
                string_data += ("\t\t"+data_el+"\n")
            string_data += "\tEND LOOP;\n END;\n"
            return string_data
        (file_name_idx)