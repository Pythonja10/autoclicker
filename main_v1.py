import keyboard
import mouse
import time

def inversion():
      global flag
      flag=not flag

def start():
      global flag,pause
      flag = False
      pause = 0.01
      keyboard.add_hotkey('`',inversion)
      while 1:
            if flag:
                  mouse.click(button='left')
                  time.sleep(pause)

if __name__=='__main__':
      start()
