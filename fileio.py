with open('myfile.txt') as f:
    full_text = f.read()

print full_text

myfile_text_plus_hello = full_text + "\nHello from fileio.py"

with open('testwrite.txt', 'w') as f:
    f.write(myfile_text_plus_hello)