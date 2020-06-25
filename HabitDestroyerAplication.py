import tkinter as tk
from tkinter import filedialog,Text
import os,time,ctypes
from datetime import datetime as dt
import sys
from tkinter import *
#print(sys.version)
#polih

hosts_temp="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","https://20xx.io/nxc/#login","youtube.com","https://www.youtube.com/","https://twitter.com","https://twitter.com/home","https://www.youtube.com/feed/subscriptions","https://discord.com/","https://discord.com/app","https://discord.com/channels/@me","www.youtube.com"]

timeInDay = 6
timeOutDay = 17
timeInNight = 23
timeOutNight = 5

extreme = False
buttonWait = 500
boolShutDown = False

DisableMinuteLeft = 100000
freeNavigation = False

def HabitDestroyer():
	global extreme
	ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\Users\Felix\Desktop\pythonScript\aplication\obamaWork.jpg" , 0)
	if extreme.get() == True:
		os.system("TASKKILL /f /im Discord.exe")
		os.system("TASKKILL /f /im Dolphin.exe")
		os.system("TASKKILL /f /im steam.exe")

def NightNight():
	global extreme
	ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\Users\Felix\Desktop\pythonScript\aplication\obamaSleeping.jpg" , 0)
	#FindProgram('Discord.exe')
	#FindProgram('Dolphin.exe')
	if extreme.get() == True:
		if dt.now() > dt(dt.now().year,dt.now().month,dt.now().day,23):
			os.startfile(r'C:\Users\Felix\Desktop\videoAndBlogsIdeas\Writing\Write.docx', 'open')

	os.system("TASKKILL /f /im Discord.exe")
	os.system("TASKKILL /f /im Dolphin.exe")
	os.system("TASKKILL /f /im steam.exe")
	os.system("TASKKILL /f /im Spotify.exe")
	os.system("TASKKILL /f /im Chrome.exe")

def hostsFileAragement():
	with open(hosts_path,'r+') as file:
		content=file.read()
		for website in website_list:
			if website in content:
				pass
			else:
				file.write(redirect+" "+ website+"\n")

def hostsFileAragement2():
		with open(hosts_path,'r+') as file:
			content=file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()
	
def getTasks(name):
    r = os.popen('tasklist /v').read().strip().split('\n')
    #print ('# of tasks is %s' % (len(r)))
    for i in range(len(r)):
        s = r[i]
        if name in r[i]:
            #print ('%s in r[i]' %(name))
            return r[i]
    return []

def FindProgram(imgName):
	if __name__ == '__main__':

	    	r = getTasks(imgName)
	    	if r:
	        	#print('%s is Running or Unknown' % (imgName))
	        	os.system("TASKKILL /F /IM" + " " + imgName)

def loopingClock():
	global freeNavigation
	global DisableMinuteLeft
	while True:
		if dt(dt.now().year,dt.now().month,dt.now().day,timeInDay) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,timeOutDay):
			#print("working hours")
			hostsFileAragement()
			HabitDestroyer()
		elif dt(dt.now().year,dt.now().month,dt.now().day,timeInNight) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day + 1,timeOutNight):
			#print("sleeping hours")
			hostsFileAragement()
			NightNight()
		else:
			hostsFileAragement2()
			#print("fun hours")
			ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\Users\Felix\Desktop\pythonScript\aplication\obama.jpg" , 0)

		if freeNavigation == True:
			#print("before")
			root.after(int(DisableMinuteLeft),loopingClock)
			#print("after")
			freeNavigation = False
			DisableMinuteLeft /= 2	
		else:
			#print("lopping")
			root.after(5000,loopingClock)
		break		

def Display_time():
	curent_time = time.strftime('%H:%M:%S')
	clock_label['text'] = curent_time
	root.after(1000,Display_time)

#----------------------------------------------------------------------

root =  tk.Tk()
root.attributes('-alpha', 0.0)
window = tk.Toplevel(root)
window.overrideredirect(1)

textForTimer = "Disable" + " : " +str(DisableMinuteLeft) 
def TimerStuff():
	global DisableMinuteLeft
	global freeNavigation
	freeNavigation = True
	textForTimer = "Disable" + " : " +str('%g'%(DisableMinuteLeft)) + " seconde"
	DisableApp['text'] = textForTimer

canvas = tk.Canvas(window,height=1920,width=1080,bg='#090913')
canvas['height'] = 185
canvas['width'] = 650
canvas.pack()

background_image =tk.PhotoImage(file='bg.png')
background_label =tk.Label(window,image=background_image)
background_label.place(relwidth=1,relheight=1)

frame = tk.Frame(window, bg = '#090913')
frame.place(relx = 0.5,rely =0.1, relwidth=0.9,relheight=0.8, anchor='n')

DisableApp = tk.Button(frame,text = textForTimer,bg='#090913',fg='#a7aab8',font='Pixeled 7',command= TimerStuff)
DisableApp.place(relx=0,rely=0.37, relwidth=0.25,relheight=0.25)

clock_label = tk.Label(frame, font='Pixeled 30',fg ='#a7aab8', bg='#090913')
clock_label.place(relx=0.3,rely=0.3, relwidth=0.5,relheight=0.5)

extreme = BooleanVar()
extreme.set(False)
extreme.trace('w', lambda *_: print("The value was changed"))

cb = Checkbutton(frame, text = "Extreme mode", variable = extreme,bg='#090913',fg='#a7aab8',font='Pixeled 7')
cb.place(relx=0,rely=0.65, relwidth=0.25,relheight=0.25)

Display_time()
loopingClock()

window.mainloop()


'''
apps = []

def addApp():
	filename= filedialog.askopenfilename(initialdir="/", title="Select File",
		filetypes=(("executables","*.exe"), ("all files","*.*")))
	apps.append(filename)
	print(filename)
	for app in apps:
		label = tk.Label(frame,text=app, bg="gray")
		label.pack()

def runApps():
	for app in apps:
		os.starfile(app)
		'''