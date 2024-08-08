import lib.file_data as file_data
from itertools import combinations
from collections import deque

# require: pip install numpy
import numpy as np

class DuplicateChecker:
    
    def __init__(self):
        self.data_arr: list[file_data.FileData] = []
        self.last_refer = []
        self.pre_stack = []
        self.q1 = deque()
        self.q2 = deque()

    def analyze_sql_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                merged_lines = self.merge_multiline_statements(lines)
                que = deque(merged_lines)
                self.compare_with_data(que)

                if len(self.q1) > 0 and self.q1 == self.last_refer and len(self.pre_stack) <= 0:
                    fd = self.get_last_datafile()
                    fd.add_recursion()
                    self.q1.clear()
                if  len(self.q2) > 0 and self.q2 == self.last_refer and len(self.pre_stack) <= 0 and len(self.q1) <= 0:
                    fd = self.get_last_datafile()
                    fd.add_recursion()
                    self.q2.clear()
                if len(self.q1) > 0 and len(self.q2) > 0 and self.q1 == self.q2 :
                    if len(self.pre_stack) > 0:
                        pre_fd = self.add_file_data()
                        pre_fd.add_data_for_arr(self.pre_stack.copy())
                        self.pre_stack.clear()
                    fd = self.add_file_data()
                    fd.add_data_for_arr(self.q1.copy())
                    fd.add_recursion()
                    self.q1.clear()
                    self.q2.clear()
                rest_data = []
                if len(self.pre_stack) > 0:
                    rest_data += list(self.pre_stack.copy())
                    self.pre_stack.clear()
                if len(self.q1) > 0:
                    rest_data += list(self.q1.copy())
                    self.q1.clear()
                if len(self.q2) > 0:
                    rest_data += list(self.q2.copy())
                    self.q2.clear()
                if len(rest_data) > 0:
                    rest_fd = self.add_file_data()
                    rest_fd.add_data_for_arr(rest_data)

        except FileNotFoundError:
            print(f"Error: The file '{file_path}' does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def merge_multiline_statements(self, lines):
        merged_lines = []
        statement = ''
        for line in lines:
            stripped_line = line.strip()
            if stripped_line.endswith(';'):
                statement += ' ' + stripped_line
                merged_lines.append(statement.strip())
                statement = ''
            else:
                statement += ' ' + stripped_line
        if statement:
            merged_lines.append(statement.strip())
        return merged_lines

    def normalize_query(self, query):
        return ' '.join(query.lower().strip().split())

    def is_same_at_endpoint(self, p_arr, c_arr):
        return p_arr[len(p_arr)-len(c_arr):] == c_arr if p_arr and c_arr  else False

    def compare_with_data(self, strings: deque):
        while strings:
            # print("-------------------------------------------start-------------------------------------------")
            # print("start self.q1")
            # print(self.q1)
            # print("start self.q2")
            # print(self.q2)
            if len(self.q2) <= 0:
                add_data = strings.popleft()
                # print(f"add data: {add_data}")
                self.q2.append(add_data)

    
            elif len(self.q1) <= 0:
                self.q1.append(self.q2.popleft())


            else:
                # 1. check 
                if self.q1 == self.last_refer and len(self.pre_stack) == 0:
                    # print('-------------------select 1------------------')
                    # q1 
                    fd = self.get_last_datafile()
                    fd.add_recursion()
                    self.q1.clear()
                    # print("end self.q1")
                    # print(self.q1)
                    # print("end self.q2")
                    # print(self.q2)

                elif self.q1 == self.q2:
                    # print('----------------select 2-------------------')
                    self.produce_pre_stack_data()
                    fd = self.add_file_data()
                    fd.add_data_for_arr(self.q1.copy())
                    fd.add_recursion()
                    self.last_refer = self.q1.copy()
                    self.q1.clear()
                    self.q2.clear()
                    # print("end self.q1")
                    # print(self.q1)
                    # print("end self.q2")
                    # print(self.q2)

                else:
                    if self.q1[0] == self.q2[0] and len(self.q1) > len(self.q2):
                        is_same = True
                        # print('-----------select 3-------------')
                        for idx,el in enumerate(self.q2):
                            if self.q1[idx] != el:
                                is_same = False  
                        if is_same:
                            # print('---------------select 3-1----------------')
                            for _ in range(len(self.q1)-len(self.q2)):
                                add_data = strings.popleft()
                                # print(f"add data: {add_data}")
                                self.q2.append(add_data)
                        if self.q1 != self.q2:
                            self.q1.append(self.q2.popleft())
                            self.pre_stack += self.q1.copy()
                            self.q1.clear()
                        # print("end self.q1")
                        # print(self.q1)
                        # print("end self.q2")
                        # print(self.q2)
                        continue
                    else:
                        q1_q2_intersection = self.ordered_intersection(self.q1,self.q2)
                        if len(q1_q2_intersection) > 0 :
                            # print('-----------select 4-------------')
                            for num in q1_q2_intersection:
                                self.sort_with_intersection(num)
                                if len(self.q1) > 0 and len(self.q2) > 0:
                                    # while len(self.q1) != len(self.q2):

                                    continue
                                else:
                                    # print("end self.q1")
                                    # print(self.q1)
                                    # print("end self.q2")
                                    # print(self.q2)
                                    break
                        else:
                            # print('-----------select 5-------------')
                            # print("end self.q1")
                            # print(self.q1)
                            # print("end self.q2")
                            # print(self.q2)
                        # 싹다 pre_stack 으로 정리
                        
                            self.q1.append(self.q2.popleft())

                        # print("end self.q1")
                        # print(self.q1)
                        # print("end self.q2")
                        # print(self.q2)

            # print("-------------------------------------------end-------------------------------------------")
                # check stack1 endpoint with stack2 start
    def produce_pre_stack_data(self):
        if self.pre_stack and len(self.pre_stack) > 0:
            fd = self.add_file_data()
            fd.add_data_for_arr(self.pre_stack.copy())
            self.pre_stack.clear()

    def sort_with_intersection(self, num):
            while self.q1[0] != num and len(self.q1) > 0:
                self.pre_stack.append(self.q1.popleft())
            while self.q2[0] != num and len(self.q2) > 0:
                self.q1.append(self.q2.popleft())
            

    def ordered_intersection(self,arr1, arr2):
        set2 = set(arr2)  # 두 번째 배열을 집합으로 변환하여 검색 시간 단축
        intersection = [num for num in arr1 if num in set2]  # 첫 번째 배열의 순서를 유지하며 교집합 구하기
        return intersection
        

    def is_sublist(self,sublist, mainlist):
        sublist_length = len(sublist)
        for i in range(len(mainlist) - sublist_length + 1):
            if mainlist[i:i + sublist_length] == sublist:
                return (True,i)
        return (False,0)

    def add_file_data(self):
        fd = file_data.FileData()
        self.data_arr.append(fd)
        return fd
    
    def get_last_datafile(self):
        return self.data_arr[-1]
    
    # def is_same_sql(stack[]):
