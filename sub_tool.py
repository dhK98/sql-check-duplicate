def is_same_string(string1,string2):
    return string1 == string2




def compare_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        content1 = file1.read()
        content2 = file2.read()

    if content1 == content2:
        print("두 파일의 내용이 동일합니다.")
    else:
        print("두 파일의 내용이 다릅니다.")

compare_files("cc1.c", "cc3.c")
