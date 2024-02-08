import pyautogui as pt

try:
   while True:
      x, y = pt.position()
      print(f"X={x}, Y={y}")

except KeyboardInterrupt:
    print("Program stopped with Ctrl + C")