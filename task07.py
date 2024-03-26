#1)a
from datetime import datetime
current_time_stamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
print("Current date & time : ", current_time_stamp)
#1)b
str_current_datetime = str(current_time_stamp)
file_name = str_current_datetime+".txt"
file = open(file_name, 'w')
print("File created : ", file.name)
file.close()


#2
f=open(r"E:\Automation testing\Task file\creat.txt","w")
f.write("This is python task 07")
f=open(r"E:\Automation testing\Task file\creat.txt","r")
file_content=f.read()
print("File Content:\n", file_content)