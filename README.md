### SQL 압축 파일 생성기

### 실행방법

1. python 3 이상 버전 설치
2. sql 파일 경로 설정 - main.py 내부 테스트 파일 이름 설정
   ```python
   test_file_path = "./test/test1.sql"
   ```
3. 명령어 실행
   ```python
   python3 main.py
   ```
4. 테스트파일명 + 숫자의 파일명으로 /copy_files 경로에 파일 생성

### 파일 생성 예제

테스트 파일

```sql
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

```sql
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
