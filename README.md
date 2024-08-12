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

### 상세 코드 설명
링크: [메인 로직 설명 링크](https://5virak.tistory.com/16)


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
