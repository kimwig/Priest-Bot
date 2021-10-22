import pyautogui
import wmi
import keyboard

pyautogui.PAUSE = 0
f = wmi.WMI()
flag = 0

while True:

    for process in f.Win32_Process():
        if "MinecraftLauncher.exe" == process.Name:

            pyautogui.rightClick()
            pyautogui.press("ctrl")
            flag = 1

            if keyboard.read_key == "f":
                print("Exiting program")
                break

    if flag == 0:
        print("Minecraft is not running")

        if keyboard.read_key() == "f":
            print("Exiting program")
            break

        continue
