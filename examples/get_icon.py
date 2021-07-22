
import win32com.client
shell = win32com.client.Dispatch("WScript.Shell")
ShortCut = shell.CreateShortCut('C:\Programs\rufus_atalho.lnk')
icon_location = ShortCut.IconLocation
print(f"ícone: {icon_location}")

# from win32com.client import gencache
# shell = gencache.EnsureDispatch('Shell.Application')
# print(shell)

# import win32com.client
# shell = win32com.client.Dispatch("WScript.Shell")
# shortcut = shell.CreateShortcut("shortcut.lnk")
# shortcut.TargetPath = "C:\\Users\\Alex Caranha\\Documents\\Books\\Kivy"
# print(shortcut.IconLocation)
# shortcut.Save()