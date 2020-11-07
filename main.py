import PyInstaller.__main__
import os
import datetime
import shutil

fmt = '%Y%m%d%H%M%S' 
time = input("How long would you like the lock to run for (in minutes)?")
code = input("Enter Code:")
start =  datetime.datetime.now()
now_string = start.strftime(fmt)
#read template file and write new file
with open("template.py") as f:
    content = f.readlines()
    with open("new.py", 'w') as new_f:
        content = ["start_time='"+now_string+"'"] + content
        content = ["time_length="+time] + content
        content = ["code='"+code+"'"] + content
        write_string = "\n".join(content)
        new_f.write(write_string)




package_name = "template"

PyInstaller.__main__.run(['--name=%s' % package_name,'--onefile','new.py',])

#clean up
os.remove('new.py')

try:
    shutil.copyfile("dist/template.exe", "new_lock.exe")
    shutil.rmtree("__pycache__")
    shutil.rmtree("build")
    shutil.rmtree("dist")
    os.remove("template.spec")
    print("Your new lock is called new_lock.exe")
    input()
except:
    print("Error cleaning up data")
    print("If you cannot find your exe, look in the dist folder")

