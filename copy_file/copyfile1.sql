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
