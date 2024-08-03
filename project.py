from tkinter import *
import xml.etree.ElementTree as ET
from functions import *


root = Tk()
root.geometry('600x400+500+200')
root.title('Helper')




main_menu = Menu(root)

file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Темная тема', command=lambda: load_and_apply_theme('Dark', root, ))
file_menu.add_command(label='Светлая тема', command=lambda: load_and_apply_theme('Light', root, ))
file_menu.add_separator()
file_menu.add_command(label='Выход', command=lambda: quit_programm(root))
main_menu.add_cascade(label='Меню', menu=file_menu)



root.config(menu=main_menu)
root.mainloop()