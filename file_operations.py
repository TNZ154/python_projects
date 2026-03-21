
"""Here is a file attached. You have to perform the following operations of File Handling using Python

"""
# ) Take two file names from the user:

# a) First file → the file where content will be added.

# b) Second file → the file whose content will be copied.

# 2) Open both files in read mode:

# a) Read and print the content of the first file.

# b) Read and print the content of the second file.

# c) Close both files.

# 3) Open the first file in append mode and the second file in read mode:

# a) Read the second file’s content.

# b) Write (append) it into the first file.

# 4) Move the cursor back to the beginning using `seek(0)`:

# a) This helps to read the full updated content from the start.

# 5) Print the content of both files after appending.

# 6) Close both files to save and finish.
file = input("Enter the name of the first file (where content will be added): ")
file2 = input("Enter the name of the second file (whose content will be copied): ")
x = open(file, 'r')
y = open(file2, 'r')
print(x.read())
print(y.read())
x.close()
y.close()
x = open(file, 'a')
y = open(file2, 'r')
print(y.read())
x.close()
y.close()