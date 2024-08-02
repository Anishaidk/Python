"""CHAPTER 9 – FILE I/O
The random-access memory is volatile, and all its contents are lost once a program
terminates. In order to persist the data forever, we use files.
A file is data stored in a storage device. A python program can talk to the file by reading
content from it and writing content to it
TYPE OF FILES.
There are 2 types of files:
1. Text files (.txt, .c, etc)
2. Binary files (.jpg, .dat, etc)
Python has a lot of functions for reading, updating, and deleting files.
OPENING A FILE
Python has an open() function for opening files. It takes 2 parameters: filename and
mode."""
# open("filename", "mode of opening(read mode by default)")
# open("this.txt", "r")

"""Reading from a File
Once we have a file object, we can use various methods to read from the file.
The read() method reads the entire contents of the file and returns it as a string."""
f = open("this.txt", "r")
# Read its contents
text = f.read()
# Print its contents
print(text)
print(type(text))
# Close the file
f.close()
# OTHER METHODS TO READ THE FILE.
# We can also use f.readline() function to read one full line at a time.
# f.readline() # Read one line from the file.
"""Modes in file
There are various modes in which we can open files.
read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.
write (w): This mode opens the file for writing only and creates a new file if the file does not exist.
append (a): This mode opens the file for appending only and creates a new file if the file does not exist.
create (x): This mode creates a file and gives an error if the file already exists.
text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).
binary (b): used to handle binary files (images, pdfs, etc)."""
"""WRITE FILES IN PYTHON
In order to write to a file, we first open it in write or append mode after which, we use
the python’s f.write() method to write to the file!"""
# Open the file in write mode
f = open("this.txt", "w")
# Write a string to the file
f.write("this is Good")
# write function will overwrite whatever was present in the file earlier
# Close the file
f.close()
# APPENDING TO A FILE
f=open("this.txt","a")
f.write("\ni am Anisha JHA")
f.close()
"""Closing a File
It is important to close a file after you are done with it. This releases the resources used by the file and allows other programs to access it.
To close a file, you can use the close() method.
"""
f = open('this.txt', 'r')
# ... do something with the file
f.close()
"""The 'with' statement
Alternatively, you can use the with statement to automatically close the file after you are done with it."""
with open("this.txt", "r") as f:# with is a function
# Read the contents of the file
    text = f.read()
# Print the contents
print(text)
"""readlines() method
The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop."""
f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    print(line)
    if not line:
        break
    # print("ijfhvedcdsn",line)
# The readlines() method reads all the lines of the file and returns them as a list of strings.
"""writelines() method
The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.
Here's an example of how to use the writelines() method:"""
f = open('myfile.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()
"""This will write the strings in the lines list to the file myfile.txt. The \n characters are used to add newline characters to the end of each string.
Keep in mind that the writelines() method does not add newline characters between the strings in the sequence. If you want to add newlines between the strings, you can use a loop to write each string separately:"""
f = open('myfile.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()
"""seek() and tell() functions
In Python, the seek() and tell() functions are used to work with file objects and their positions within a file. These functions are part of the built-in io module, which provides a consistent interface for reading and writing to various file-like objects, such as files, pipes, and in-memory buffers."""
"""seek() function
The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes, and you can move either forward or backward from the current position. For example:"""
with open('file.txt', 'r') as f:
  # Move to the 10th byte in the file
  f.seek(10)
  # Read the next 5 bytes
  data = f.read(5)
  """tell() function
The tell() function returns the current position within the file, in bytes. This can be useful for keeping track of your location within the file or for seeking to a specific position relative to the current position. For example:"""
with open('file.txt', 'r') as f:
  # Read the first 10 bytes
  data = f.read(10)

  # Save the current position
  current_position = f.tell()

  # Seek to the saved position
  f.seek(current_position)
  """truncate() function
When you open a file in Python using the open function, you can specify the mode in which you want to open the file. If you specify the mode as 'w' or 'a', the file is opened in write mode and you can write to the file. However, if you want to truncate the file to a specific size, you can use the truncate function.

Here is an example of how to use the truncate function:"""
with open('sample.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)

with open('sample.txt', 'r') as f:
  print(f.read())