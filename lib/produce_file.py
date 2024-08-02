import lib.file_data as file_data

class FileProducer:
    def __init__(self) -> None:
            self.data_arr: list[file_data.FileData] = []

    def create_file(self):
        try:
            if not self.data_arr or len(self.data_arr) <= 0:
                raise Exception("not exist data")
            # formater => create sql
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' does not exist.")
        except PermissionError:
             print('no permission for cmd')
        except Exception as e:
            print(f"An error occurred: {e}")

    
    def create_sql(self, data: file_data.FileData):
        recursion_number = data.recursion_number
        if recursion_number == 0:
             pass
        else:
             pass