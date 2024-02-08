import pyautogui as gui
import time

gui.moveTo(1172, 705) #cek pointer untuk mengarahkan mouse
gui.click() #ketika sudah ditetapkan koordinat, mouse akan diklik pada area tsb

# gunakan perulangan dengan for hingga 80
for i in range(80):
   gui.write("Test")    #menuliskan kata "Test"
   time.sleep(0.1)      #memberi jeda 0.1 second
   gui.press("Enter")   #memberi perintah enter baris baru