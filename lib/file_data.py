from lib.common import Common

class FileData:
    recursion_number: int
    data: list

    def __init__(self) -> None:
        self.recursion_number = 1
        self.data = []
    
    def add_data_at_end(self,string:str):
        self.data.append(string)

    def get_data(self):
        return self.data
    
    def add_data_for_arr(self, string_arr:list[str]):
        self.data.extend(string_arr)

    def add_recursion(self):
        self.recursion_number += 1
