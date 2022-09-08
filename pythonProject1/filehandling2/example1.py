# # a file named "geek", will be opened with the reading mode.
# file = open('ggggg.txt', 'r')
# # This will print every line one by one in the file
# for each in file:
# 	print (each)
# 	print('-------------')
# #Python code to illustrate read() mode
# file = open("ggggg.txt", "r")
# print (file.read())
# print('-------------')
# # # Python code to illustrate read() mode character wise
# file = open("ggggg.txt", "r")
# print (file.read(10))
# print('------------------')
# # Python code to create a file
file = open('gegk.txt','w')
file.write("This is the write command\n")
file.write("It allows us to\nwrite in a \nparticular file\naadhi")
file.close()
print('-----------------------')


# # # Python code to illustrate append() mode
# file = open('geek1.txt','a')
# file.write("\nThis will add this line")
# file.close()
# # """"""
# # # Python code to illustrate with()
# with open("ggggg.txt") as file:
# 	data = file.read()
# # do something with dataA
# # """"""
# # # Python code to illustrate with() alongwith write()
# # with open("file.txt", "w") as f:
# # 	f.write("Hello World!!!")
# # """"""""
# # # Python code to illustrate split() function
# # with open("file.text", "r") as file:
# # 	data = file.readlines()
# # 	for line in data:
# # 		word = line.split()
# # 		print (word)
# # """"""""