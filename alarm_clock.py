from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
from time import sleep
from pygame import mixer
from threading import Thread

#colours
col1='#080808' #vampire_black
col2='#E8000D' #ku_crimson_red
col3='#DCF3E5' #pearl_white

#window
window = Tk()
window.title("ALARM")
window.geometry('350x600')
window.configure(bg=col1)

#frame_up
frame_line=Frame(window, width=400, height=10, bg=col2)
frame_line.grid(row=0, column=0)

frame_body=Frame(window, width=400, height=700, bg=col1)
frame_body.grid(row=1, column=0)

#configuring_frame_body

#image
img=Image.open('clock_2.png')
img=ImageTk.PhotoImage(img)

app_image=Label(frame_body, height=300, width=300, image=img, bg=col1,)
app_image.place(x=23.2, y=10)

#hour
hour = Label(frame_body, text = "Hour", height=1,font=('TheBoldFont 15 bold'), bg=col1, fg=col2)
hour.place(x=25, y=350)

c_hour = Combobox(frame_body, width=3, font=('TheBoldFont 15 '))
c_hour['values'] = ('00','01','02','03','04','05','06','07','08','09','10','11','12')
c_hour.current(0)
c_hour.place(x=29, y=380)

#min
min = Label(frame_body, text = "Min", height=1,font=('TheBoldFont 15 bold'), bg=col1, fg=col2)
min.place(x=105, y=350)

c_min = Combobox(frame_body, width=3, font=('TheBoldFont 15 '))
c_min['values'] = ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59')
c_min.current(0)
c_min.place(x=109, y=380)

#sec
sec = Label(frame_body, text = "Sec", height=1,font=('TheBoldFont 15 bold'), bg=col1, fg=col2)
sec.place(x=185, y=350)

c_sec = Combobox(frame_body, width=3, font=('TheBoldFont 15 '))
c_sec['values'] = ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59')
c_sec.current(0)
c_sec.place(x=189, y=380)

#period
period = Label(frame_body, text = "Period", height=1,font=('TheBoldFont 15 bold'), bg=col1, fg=col2)
period.place(x=265, y=350)

c_period = Combobox(frame_body, width=3, font=('TheBoldFont 15 '))
c_period['values'] = ('AM', 'PM')
c_period.current(0)
c_period.place(x=269, y=380)

def activate_alarm():
    t = Thread(target=alarm)
    t.start()

def deactivate_alarm():
    mixer.music.stop()
    alarm_hour = c_hour.current(0)
    alarm_minute= c_min.current(0)
    alarm_sec= c_sec.current(0)
    alarm_period= c_period.current(0)

#activate
selected = IntVar()

rad1 = Radiobutton(frame_body, font=('TheBoldFont 10 bold'), value = 1, text = 'Activate', bg=col2, fg=col1, command = activate_alarm, variable = selected)
rad1.place(x=55, y=480)

rad2 = Radiobutton(frame_body, font=('TheBoldFont 10 bold'), value = 2, text = 'Deactivate', bg=col2, fg=col1, command = deactivate_alarm,variable = selected)
rad2.place(x=195, y=480)

def sound_alarm():
    mixer.music.load('alarm_audio.mp3')
    mixer.music.play()

def alarm():
    while True:
        control=1

        alarm_hour = c_hour.get()
        alarm_minute= c_min.get()
        alarm_sec= c_sec.get()
        alarm_period= c_period.get()
        alarm_period = str(alarm_period).upper()

        now = datetime.now()

        hour=now.strftime('%I')
        minute=now.strftime('%M')
        second=now.strftime('%S')
        period=now.strftime('%p')

        if control == 1:
            if alarm_period == period and alarm_hour == hour and alarm_minute == minute and alarm_sec == second:
                sound_alarm()
        sleep(1)

mixer.init()
window.mainloop()