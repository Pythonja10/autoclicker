import keyboard
import mouse
import time

def inversion():
      global flag
      flag=not flag

def inp():
      s1,s2,s3=float(input('Введите паузу между кликами\n')),input('Введите символ активации автокликера\n'),\
                input('Введите кнопку мыши\n')
      s1=max(s1,0.001)
      return s1,s2,s3


def start():
      global flag
      flag = False
      try:
            pause,key,mauskey = inp()
      except:
            print('Ошибка ввода данных!')
            return
      try:
            keyboard.add_hotkey(key,inversion)
      except:
            print('Данная кнопка отсутвует на этой раскладке клавиатуры!\nПерезапустите программу.')
            return
      while 1:
            if flag:
                  try:
                        mouse.click(button=mauskey)
                  except:
                        print('Введена несуществующая кнопка!')
                        return
                  try:
                        time.sleep(pause)
                  except:
                        print('Введено неверное время!')
                        return

if __name__=='__main__':
      start()
