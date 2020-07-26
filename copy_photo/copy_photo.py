with open('photo1.png','rb') as file1:
    data = file1.read()

with open('code.txt', 'wb') as file2:
    file2.write(data)
# with open('photo2.png','wb') as file2:
#     file2.write(data)