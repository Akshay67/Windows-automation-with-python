from pywinauto import application
import time

app=application.Application()

app.start("notepad.exe")
#time.sleep(3)
app.notepad.edit.TypeKeys("Hello World")
#if len(app.notepad.edit.TypeKeys(""))>1:
app.notepad.MenuSelect("File -> SaveAs..")
app.SaveAs.edit.SetText("Hello.txt")
app.SaveAs.Save.Click()
time.sleep(2)      
if app.SaveAs.Yes.Exists():
    app.Save.Yes.Click()

else:
    app.notepad.MenuSelect("File -> Exit")
