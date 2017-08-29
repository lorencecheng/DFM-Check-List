import tkinter
top = tkinter.Tk()
L1=tkinter.Label(top,text="User Name")
L1.pack(side="left")
'''
side定义停靠在父组件的哪一边上。
“top”, “bottom”, “left”, “right”
（默认为”top”）
'''
E1=tkinter.Entry(top,bd=1)
E1.pack(side="right")
top.mainloop()
