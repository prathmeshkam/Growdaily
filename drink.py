import time
from tkinter import *


obj = Tk()
obj.geometry("800x800")

def pri():
    from plyer import notification #From plyer module i import a notification class
    import time
    st = int(e.get())
    rt = int(e1.get())
    lt = int(e2.get())
    i = lt * 1000
    if __name__ == '__main__':
        while i>0:
            notification.notify(
                    title = "🥛Please Drink Water Now (Approx.200ml)!!",
                    message ="Drinking Water Helps to Maintain the Balance of Body Fluids.",
                    timeout= st,
                    app_icon = "D:\Practise Program PY\Project\icon.ico",
                    app_name = "Become a Fit",
                    )
            i = i - 200
            time.sleep(rt)
        notification.notify(
                    title = "You completed your target👍",
                    message ="We reqiure a approximetly 3 litre water a day.",
                    timeout= 20,
                    app_icon = "D:\Practise Program PY\Project\success.ico",
                    
                    )

        
l = Label(obj,text="Provides a details",bg='#90EE90',fg='black',padx=2,pady=2)    
l.place(x=330,y=30)
l = Label(obj,text="Enter the Notification stay timing(in Sec)",bg='black',fg='white',padx=5,pady=5,font= ('times new roman', 10))
l.place(x=100,y=60)
e = Entry(obj,)
e.place(x=350,y=63)

l = Label(obj,text="Enter the Notification return timing(in Sec)",bg='black',fg='white',padx=5,pady=5,font= ('times new roman', 10))
l.place(x=100,y=90)
e1 = Entry(obj)
e1.place(x=350,y=93)

l = Label(obj,text="Enter water you want to take (In litre)",bg='black',fg='white',padx=5,pady=5,font= ('times new roman', 10))
l.place(x=100,y=120)
e2 = Entry(obj)
e2.place(x=350,y=123)

b = Button(obj,text='Submit' ,command=pri,padx=5,pady=5)
b.place(x=250,y=160)

b = Button(obj,text='Exit' ,command=obj.destroy,padx=5,pady=5)
b.place(x=330,y=160)

obj.mainloop()















            



        


# def notify(staytime):
#     notification.notify(
#             title = "🥛Please Drink Water Now!!",
#             message ="Drinking Water Helps to Maintain the Balance of Body Fluids.",
#             timeout= staytime,
#             app_icon = "D:\Practise Program PY\Project\icon.ico",
#             ticker = "Drink Water Please",
#             )
        


# if __name__ == '__main__':
#     while True:
#         notify(10)
#         time.sleep(6)