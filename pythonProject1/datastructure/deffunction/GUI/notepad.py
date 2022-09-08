from tkinter import *
root=Tk()
root.title('my notepad')
root.geometry('400x700')
menubar=Menu(root)
root.config(menu=menubar)
filemenu=Menu(menubar)
editmenu=Menu(menubar)
viewmenu=Menu(menubar)
menubar.add_cascade(label='file',menu=filemenu,underline=0)
menubar.add_cascade(label='edit',menu=editmenu,underline=0)
menubar.add_cascade(label='view',menu=viewmenu,underline=0)
submenu=Menu(viewmenu,tearoff=0)
aa=Menu(filemenu,tearoff=0)
aa.add_command(label='print file')
filemenu.add_cascade(label='print',menu=aa)

filemenu.add_command(label='new')
filemenu.add_command(label='new window')
filemenu.add_command(label='open')
filemenu.add_command(label='save')
filemenu.add_command(label='save as')
editmenu.add_command(label='undo')
editmenu.add_command(label='cut')
editmenu.add_command(label='copy')
editmenu.add_command(label='paste')
viewmenu.add_cascade(label='zoom',menu=submenu)
submenu.add_command(label='zoom in')
submenu.add_command(label='zoom out')
root.mainloop()















# l={'c','c++','java','scala','python','.net'}
# print(l)
# q,*w,d=l
# print(q)
# print(w)
# print(d)

# a="That will be 5976 dollars"
# l=[]
# for b in a:
#     if (b>=chr(65) and b<=chr(90)) or (b>=chr(97) and b<=chr(122)) or (b==chr(32)):
#         print("",end="")
#     else:
#         l.append(b)
# print(l)

