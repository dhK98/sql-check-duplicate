## 구조 설계

-   file\_date.py
    -   SQL 파일데이터의 반복횟수를 저장하기 위한 클래스
-   check\_duplicate\_v1.py
    -   SQL 파일을 분석하여 데이터를 가져오는 클래스
-   produce\_file.py
    -   가져온 SQL 데이터를 파일로 만드는 클래스
-   main.py
    -   check\_duplicate 객체를 생성하여 데이터를 가져옴
    -   가져온 SQL 데이터를 파일로 생성

---

### 상세 파일

-   모든 코드를 설명하지는 못하고 SQL 분석 코드만 설명

**file-data.py**

```
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

-   데이터는 list 형태로 저장(붙어있는 SQL문을 저장하기 위해)
-   recursion\_number라는 반복횟수를 두고 객체 생성시, 1로 초기화
-   내부 프로퍼티를 좀 더 가독성을 높이기 위해 function 작성
```

**check-duplicate\_v1.py**

```
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

                  # q1, q2 잔여 데이터 처리 로직
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
```

-   DuplicateChecker 클래스는 fileData를 배열 형태로 데이터를 저장 -> 클래스 생성시, 초기화
-   analyze\_sql\_file 함수는 SQL 파일을 읽어 데이터를 클래스 내부에 저장하는 역할을 한다.
-   `def compare_with_data(self, strings: deque): while strings: if len(self.q2) <= 0: add_data = strings.popleft() self.q2.append(add_data)`

```
def compare_with_data(self, strings: deque):
        while strings:
            if len(self.q2) <= 0:
                add_data = strings.popleft()
                self.q2.append(add_data)


            elif len(self.q1) <= 0:
                self.q1.append(self.q2.popleft())


            else:
                if self.q1 == self.last_refer and len(self.pre_stack) == 0:
                    fd = self.get_last_datafile()
                    fd.add_recursion()
                    self.q1.clear()
                elif self.q1 == self.q2:
                    self.produce_pre_stack_data()
                    fd = self.add_file_data()
                    fd.add_data_for_arr(self.q1.copy())
                    fd.add_recursion()
                    self.last_refer = self.q1.copy()
                    self.q1.clear()
                    self.q2.clear()
                else:
                    if self.q1[0] == self.q2[0] and len(self.q1) > len(self.q2):
                        is_same = True
                        for idx,el in enumerate(self.q2):
                            if self.q1[idx] != el:
                                is_same = False  
                        if is_same:
                            for _ in range(len(self.q1)-len(self.q2)):
                                add_data = strings.popleft()
                                self.q2.append(add_data)
                        if self.q1 != self.q2:
                            self.q1.append(self.q2.popleft())
                            self.pre_stack += self.q1.copy()
                            self.q1.clear()
                        continue
                    else:
                        q1_q2_intersection = self.ordered_intersection(self.q1,self.q2)
                        if len(q1_q2_intersection) > 0 :
                            for num in q1_q2_intersection:
                                self.sort_with_intersection(num)
                                if (len(self.q1) <= 0 and len(self.q2) <= 0 ) or (self.q1[0] == num and self.q2[0] == num) :
                                    break
                        else:                        
                            self.q1.append(self.q2.popleft())
```

-   compare\_with\_data 함수는 실제 SQL 데이터를 큐 두개에 넣어 비교하는 기능을 수행한다.
-   큐 두개를 q1,q2 라고 간략하게 네이밍

1.  초기 q1 과 q2가 비어있을 때, q1에 데이터 1개 q2에 데이터를 1개 넣는다.(순서를 지켜 push)
2.  q1의 데이터가 마지막으로 참조된 중복 데이터와 동일하다면 q1을 비어주고, 마지막 참조 데이터의 recurtion\_number를 1 더해준다.
3.  2번의 조건에 충족하지 못할때 q1과 q2의 큐가 완전히 같은지 비교한다(python이라 == 부호로 비교가능), 만약 같을시, 이전 데이터를 먼저 FileData로 만든 후 배열에 넣어주고, q1 또는 q2의 데이터를 FileData로 만들어 배열에 넣어주고 recurtion\_number를 1 더해준다.그 후 q1과 q2를 비워준다.
4.  위의 2,3 조건에 도달하지 못할때, 두개의 데이터가 중복되는 경우를 찾고 해당 데이터가 큐의 0번째 인덱스에 올때까지 q1데이터를 이전데이터 정리 큐로, q2 데이터는 q1 끝으로 밀어준다. 이 때 두개의 큐가 0 보다 클경우 다음 반복문으로 넘긴다.
5.  두개의 큐에서 중복되는 데이터가 없을 경우 q2 첫번째 데이터를 q1의 끝으로 밀어준다.

```
 def sort_with_intersection(self, num):
        while self.q1[0] != num and len(self.q1) > 0:
            self.pre_stack.append(self.q1.popleft())
        while self.q2[0] != num and len(self.q2) > 0:
            self.q1.append(self.q2.popleft())


def ordered_intersection(self,arr1, arr2):
    set2 = set(arr2)  # 두 번째 배열을 집합으로 변환하여 검색 시간 단축
    intersection = [num for num in arr1 if num in set2]  # 첫 번째 배열의 순서를 유지하며 교집합 구하기
    return intersection
```

---

### 실행방법

1.  python 3 이상 버전 설치
2.  sql 파일 경로 설정 - main.py 내부 테스트 파일 이름 설정
    
    ```
    test_file_path = "./test/test1.sql"
    ```
    
3.  명령어 실행
    
    ```
    python3 main.py
    ```
    
4.  테스트파일명 + 숫자의 파일명으로 /copy\_files 경로에 파일 생성

---

### 파일 생성 예제

테스트 파일

```
CREATE TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
ALTER TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
CREATE TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
CREATE TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
ALTER TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
CREATE TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
CREATE TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
ALTER TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
CREATE TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
ALTER TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
CREATE TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
ALTER TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
ALTER TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
CREATE TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
```

생성파일

```
CREATE TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
ALTER TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
CREATE TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
CREATE TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
ALTER TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
CREATE TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
DECLARE
     L_CNT NUMBER:=0;
 BEGIN
     LOOP
         L_CNT:=L_CNT+1;
         EXIT WHEN L_CNT>=3;
        CREATE TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
        ALTER TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
    END LOOP;
 END;
ALTER TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
CREATE TABLE T1(n1 NUMBER(4) primary key, v1 varchar(20));
```

#### Github Link

\- 전체 코드 : [https://github.com/dhK98/sql-check-duplicate](https://github.com/dhK98/sql-check-duplicate)
