#open file
file_1 = open("python-file-handling/my-file.txt","r")

# file_1 = open("python-file-handling/my-file1.txt","r") - file ek nati hinda error some comman has to create file
# FileNotFoundError: [Errno 2] No such file or directory: 'python-file-handling/my-file1.txt'

#reade krnne read()
read_content = file_1.read()

# one line read readline() - txt file eke opne wen tna -curser ek tiyen tan idan next line caractor ek (\n -next line ek wenkm ewa desply krnwa)
# read_content = file_1.readline()

#lines okkom read krnw ew set wenne array ekk atule -list type eken 
#read_content = file_1.readlines()
#out -['I love progrsmming \n', 'hello world']

print(read_content)
print(type(read_content))
# resourse relece krnne close krm
file_1.close()

# ## 02 
# with open("python-file-handling/my-file.txt","r") as file:
#     content = file.read()
#     print(content)