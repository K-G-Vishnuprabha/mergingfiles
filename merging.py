source_file = "source1.txt"
file2="file2.txt"
merge_file='merging.txt'
try:
    with open(source_file, 'r') as src:
        content = src.read()
    with open(file2, 'r') as f2:
       content1 = f2.read()
    with open(merge_file, 'w') as mg:
        mg.write(content+"\n"+content1)
    print("File merged successfully.")
except FileNotFoundError:
    print(f"Error: The file '{source_file}','{file2}' was not found.")
