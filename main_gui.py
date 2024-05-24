from tkinter import *
import keyboard
import mouse
import threading
from time import sleep
from tkinter.messagebox import showinfo,showerror

options = {'font1':('Zhizn',10,'bold'),'font2':('Zhizn',20,'bold'),'font3':('Zhizn',15,'bold'),'font4':('Arial',15,'bold italic')\
           ,'bg':'WhiteSmoke','fg':'DodgerBlue'}

def clicker():
      global key,mousekey,pause,tik
      flag=False
      while 1:
            if not tik:
                  return
            if flag:
                  mouse.click(button=mousekey)
            try:
                  if keyboard.is_pressed(key):
                        flag = not flag
                        sleep(0.5)
            except:
                  pass
            sleep(pause)

def cbtn12():
      global tik
      thread=threading.Thread(target=clicker)
      tik=not tik
      if tik: btn12.config(text='❌')
      else: btn12.config(text='✅')
      thread.start()

def option():
      global key,mousekey,pause,options,window,lbl1_w,entry1,btn1_w,lbl2_w,entry2,btn2_w,\
             lbl3_w,entry3,btn3_w,lbl4_w,entry4,btn4_w,lbl5_w,entry5,btn5_w
      window=Toplevel()
      window.geometry('300x200+150+150')
      window.title('autoclicker-pgs-options')
      window.minsize(300,200)

      window.bind('<Configure>',config1)

      lbl1_w=Label(window,text=f'кнопка - ',font=options['font4'],bg=options['bg'],fg=options['fg'])
      lbl1_w.place(relx=0,rely=0,relwidth=0.4,relheight=0.2)

      entry1 = Entry(window,font=options['font4'],width=7,bg=options['bg'],fg=options['fg'])
      entry1.place(relx=0.4,rely=0,relwidth=0.4,relheight=0.2)
      entry1.insert('end',f'{key}')

      def opt_btn1():
            global entry1,key,mousekey,pause
            key=entry1.get()
            lbl.config(text=f'кнопка:\n{key}')
            with open('options/basic.txt','w', encoding='utf-8') as txt:
                  txt.write('\n'.join([key,mousekey,str(pause)]))
            showinfo('Информация','Измение сохранено')
      
      btn1_w= Button(window,text='✔',font=(options['font3'][0],options['font4'][1],options['font3'][2]),
                     bg=options['bg'],fg=options['fg'],command=opt_btn1)
      btn1_w.place(relx=0.8,rely=0,relwidth=0.2,relheight=0.2)

      lbl2_w=Label(window,text=f'кн. мышки - ',font=options['font4'],bg=options['bg'],fg=options['fg'])
      lbl2_w.place(relx=0,rely=0.2,relwidth=0.4,relheight=0.2)

      entry2 = Entry(window,font=options['font4'],width=7,bg=options['bg'],fg=options['fg'])
      entry2.place(relx=0.4,rely=0.2,relwidth=0.4,relheight=0.2)
      entry2.insert('end',f'{mousekey}')

      def opt_btn2():
            global entry2,key,mousekey,pause
            mousekey=entry2.get()
            with open('options/basic.txt','w', encoding='utf-8') as txt:
                  txt.write('\n'.join([key,mousekey,str(pause)]))
            showinfo('Информация','Измение сохранено')
            
      btn2_w= Button(window,text='✔',font=(options['font3'][0],options['font4'][1],options['font3'][2]),
                     bg=options['bg'],fg=options['fg'],command=opt_btn2)
      btn2_w.place(relx=0.8,rely=0.2,relwidth=0.2,relheight=0.2)

      lbl3_w=Label(window,text=f'пауза - ',font=options['font4'],bg=options['bg'],fg=options['fg'])
      lbl3_w.place(relx=0,rely=0.4,relwidth=0.4,relheight=0.2)

      entry3 = Entry(window,font=options['font4'],width=7,bg=options['bg'],fg=options['fg'])
      entry3.place(relx=0.4,rely=0.4,relwidth=0.4,relheight=0.2)
      entry3.insert('end',f'{pause}')
      
      def opt_btn3():
            global entry3,key,mousekey,pause
            pause=entry3.get()
            try:
                  pause=max(float(pause),0.01)
            except:
                  showerror('Ошибка','Введено не вещественное число')
                  return
            with open('options/basic.txt','w', encoding='utf-8') as txt:
                  txt.write('\n'.join([key,mousekey,str(pause)]))
            showinfo('Информация','Измение сохранено')
            
      btn3_w= Button(window,text='✔',font=(options['font3'][0],options['font4'][1],options['font3'][2]),
                     bg=options['bg'],fg=options['fg'],command=opt_btn3)
      btn3_w.place(relx=0.8,rely=0.4,relwidth=0.2,relheight=0.2)

      lbl4_w=Label(window,text=f'фон - ',font=options['font4'],bg=options['bg'],fg=options['fg'])
      lbl4_w.place(relx=0,rely=0.6,relwidth=0.4,relheight=0.2)

      entry4 = Entry(window,font=options['font4'],width=7,bg=options['bg'],fg=options['fg'])
      entry4.place(relx=0.4,rely=0.6,relwidth=0.4,relheight=0.2)
      entry4.insert('end',f'{options["bg"]}')
      
      def opt_btn4():
            global entry4,options
            bg=entry4.get()
            with open('options/bg.txt','w', encoding='utf-8') as txt:
                  txt.write(bg)
            options['bg']=bg
            showinfo('Информация','Измение сохранено')

      btn4_w= Button(window,text='✔',font=(options['font3'][0],options['font4'][1],options['font3'][2]),
                     bg=options['bg'],fg=options['fg'],command=opt_btn4)
      btn4_w.place(relx=0.8,rely=0.6,relwidth=0.2,relheight=0.2)

      lbl5_w=Label(window,text=f'цвет текста - ',
                   font=(options['font4'][0],options['font4'][1]//3*2,options['font4'][2]),
                   bg=options['bg'],fg=options['fg'])
      lbl5_w.place(relx=0,rely=0.8,relwidth=0.4,relheight=0.2)

      entry5 = Entry(window,font=options['font4'],width=7,bg=options['bg'],fg=options['fg'])
      entry5.place(relx=0.4,rely=0.8,relwidth=0.4,relheight=0.2)
      entry5.insert('end',f'{options["fg"]}')

      def opt_btn5():
            global entry5,options
            fg=entry5.get()
            with open('options/fg.txt','w', encoding='utf-8') as txt:
                  txt.write(fg)
            options['fg']=fg
            showinfo('Информация','Измение сохранено')
            
      btn5_w= Button(window,text='✔',font=(options['font3'][0],options['font4'][1],options['font3'][2]),
                     bg=options['bg'],fg=options['fg'],command=opt_btn5)
      btn5_w.place(relx=0.8,rely=0.8,relwidth=0.2,relheight=0.2)
      
def cl():
      global tik
      tik=0
      win.destroy()

def config1(event):
      if event.widget == window:
            options['font4']=('Arial',int(window.geometry().split('x')[0])//20,'bold italic')
            lbl1_w.config(font=options['font4'])
            entry1.config(font=options['font4'])
            btn1_w.config(font=(options['font3'][0],options['font4'][1],options['font3'][2]))
            lbl2_w.config(font=options['font4'])
            entry2.config(font=options['font4'])
            btn2_w.config(font=(options['font3'][0],options['font4'][1],options['font3'][2]))
            lbl3_w.config(font=options['font4'])
            entry3.config(font=options['font4'])
            btn3_w.config(font=(options['font3'][0],options['font4'][1],options['font3'][2]))
            lbl4_w.config(font=options['font4'])
            entry4.config(font=options['font4'])
            btn4_w.config(font=(options['font3'][0],options['font4'][1],options['font3'][2]))
            lbl5_w.config(font=(options['font4'][0],options['font4'][1]//3*2,options['font4'][2]))
            entry5.config(font=options['font4'])
            btn5_w.config(font=(options['font3'][0],options['font4'][1],options['font3'][2]))


def config(event):
      global options
      if event.widget == win:
            options['font1']=('Zhizn',int(win.geometry().split('x')[0])//7,'bold')
            options['font2']=('Zhizn',int(win.geometry().split('x')[0])//5,'bold')
            options['font3']=('Zhizn',int(win.geometry().split('x')[0])//10,'bold')
            lbl.config(font=options['font1'])
            btn11.config(font=options['font2'])
            btn12.config(font=options['font2'])
            btn2.config(font=options['font3'])
            btn3.config(font=options['font3'])

def init():
      with open('options/basic.txt','r', encoding='utf-8') as txt:
            s=txt.read()
      key,mousekey,pause=s.split('\n')
      try:
            pause=float(pause)
            pause=max(pause,0.01)
      except:
            with open('options/basic.txt','w', encoding='utf-8') as txt:
                  txt.write('\n'.join([key,mousekey,'0.01']))
            showerror('Error','Задана неправильная пауза!')
            pause=0.01
      
      return key,mousekey,pause

def options_init():
      global options
      with open('options/bg.txt','r',encoding='utf-8') as txt:
            options['bg']=txt.read()
      with open('options/fg.txt','r',encoding='utf-8') as txt:
            options['fg']=txt.read()

def start():
      global key,mousekey,options,win,lbl,btn11,btn12,btn2,btn3,tik,pause
      key,mousekey,pause=init()
      options_init()
      tik=False
      
      win=Tk()
      win.geometry('180x200+100+100')
      win.title('autoclicker-pgs')
      win.minsize(180,200)
      win.config(bg=options['bg'])

      win.bind('<Configure>',config)
      #print(win.geometry())
      options['font1']=('Zhizn',int(win.geometry().split('x')[0])//7,'bold')
      options['font2']=('Zhizn',int(win.geometry().split('x')[0])//5,'bold')
      options['font3']=('Zhizn',int(win.geometry().split('x')[0])//10,'bold')

      lbl=Label(win,text=f'кнопка:\n{key}',font=options['font1'],bg=options['bg'],fg=options['fg'])
      lbl.place(relx=0,rely=0,relwidth=1,relheight=0.4)

      btn11=Button(win,text='⚙',font=options['font2'],command=option,bg=options['bg'],fg=options['fg'])
      btn11.place(relx=0.5,rely=0.4,relwidth=0.5,relheight=0.4)

      btn12=Button(win,text='✅',font=options['font2'],command=cbtn12,bg=options['bg'],fg=options['fg'])
      btn12.place(relx=0,rely=0.4,relwidth=0.5,relheight=0.4)

      btn2=Button(win,text='выход',font=options['font3'],command=cl,bg=options['bg'],fg=options['fg'])
      btn2.place(relx=0,rely=0.8,relwidth=0.8,relheight=0.2)

      cbtn3=lambda: showinfo('Автокликер-Справка','Нажмите на галочку, чтобы включить режим автоклира.\n\
Нажмите на выбранный Вами символ (по умолчанию `), чтобы запустить клики, выбранной кнопкой мыши.\n\
Нажмите ещё раз, чтобы выключить. Нажмите на крестик, чтобы выйти из режима автокликера.')
      
      btn3=Button(win,text='?',font=options['font3'],command=cbtn3,bg=options['bg'],fg=options['fg'])
      btn3.place(relx=0.8,rely=0.8,relwidth=0.2,relheight=0.2)
      
      win.protocol('WM_DELETE_WINDOW', cl)
      
      win.mainloop()

if __name__=='__main__':
      start()
