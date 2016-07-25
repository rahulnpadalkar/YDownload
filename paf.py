import pafy
import urllib
from bs4 import BeautifulSoup
import webbrowser
from tkinter import Tk
from tkinter import filedialog
import os


def downloadsingleaudio(url):
		dobj = pafy.new(url)
		aobj = dobj.getbestaudio()
		root = Tk()
		root.withdraw()
		filename = filedialog.askdirectory()
		print("-------------------------------------------------------------")
		print("Now Downloading:"+dobj.title)
		print("Size is %s" % aobj.get_filesize())
		fileloc = aobj.download(filepath=filename,quiet=True)
		print("Audio downloaded at: "+filename)
		print("Do you want to open the download folder?\n1.Yes\n2.No")
		opp = int(input())
		if(opp==1):
			os.startfile(filename)
		else:
			print("Thank you for using!")



def downloadsinglevideo(url):
	dobj = pafy.new(url)
	aobj = dobj.getbest()
	root = Tk()
	root.withdraw()
	filename = filedialog.askdirectory()
	print("-------------------------------------------------------------")
	print("Now Downloading:"+dobj.title)
	print("Size is %s" % aobj.get_filesize())
	print("Video resolution is: "+aobj.resolution)
	fileloc = aobj.download(filepath=filename,quiet=Fal)
	print("Video downloaded at: "+filename)
	print("Do you want to open the download folder?\n1.Yes\n2.No")
	opp = int(input())
	if(opp==1):
		os.startfile(filename)
	else:
		print("Thank you for using!")


def ncs():
    ncsurl = "https://www.youtube.com/user/NoCopyrightSounds/videos"
    ncspop = "https://www.youtube.com/user/NoCopyrightSounds/videos?flow=grid&view=0&sort=p"
    print("Choose your video sorting order:\n1.Date Added *newest\n2.Most Popular\n")
    vs = int(input())
    if(vs ==1):
        reducecode(ncsurl)
        
    else:
        reducecode(ncspop)
    


def majc():
    majurl = "https://www.youtube.com/user/majesticcasual/videos"
    majpop = "https://www.youtube.com/user/majesticcasual/videos?flow=grid&sort=p&view=0"
    print("Choose your video sorting order:\n1.Date Added *newest\n2.Most Popular\n")
    vs = int(input())
    if(vs ==1):
        reducecode(majurl)
        
    else:
        reducecode(majpop)


def hero():
    hero = "https://www.youtube.com/user/HEROboard/videos"
    heropop = "https://www.youtube.com/user/HEROboard/videos?sort=p&flow=grid&view=0"
    print("Choose your video sorting order:\n1.Date Added *newest\n2.Most Popular\n")
    vs = int(input())
    if(vs ==1):
        reducecode(hero)
        
    else:
        reducecode(heropop)

def vidscrape(ncssoup):
    i=1
    j=1
    print("Enter the number of results you want (number between 1-30)")
    ll = int(input())
    if (ll > 30):
        print ("Max reults that can be retrived are 30")
    elif (ll < 0):
        print ("May the force be with you!")
    else:
        for vid in ncssoup.findAll(attrs={'class':'yt-uix-sessionlink yt-uix-tile-link  spf-link  yt-ui-ellipsis yt-ui-ellipsis-2'},limit = ll):
            title = vid['title']
            abslink = 'https://www.youtube.com'+vid['href']
            myvid = pafy.new('https://www.youtube.com'+vid['href'])
            lyk = str(myvid.likes)
            dlyk = str(myvid.dislikes)
            views = str(myvid.viewcount)
            ncsvidlinks.insert(i,abslink)
            i=i+1
            print (j,"."+title+"\n"+"LIKES: "+lyk+"\t"+"DISLIKES: "+dlyk+"\t"+"VIEWCOUNT: "+views+"\n")
            j=j+1
        


def download(splittracklist,filename):
    
    for new in range(len(splittracklist)):
        dindex=splittracklist[new]
        dlink = ncsvidlinks[dindex]
        print(dlink)
        dobj = pafy.new(dlink)
        aobj = dobj.getbestaudio()
        print("-------------------------------------------------------")
        print("Now Downloading:"+dobj.title)
        print("Size is %s" % aobj.get_filesize())
        fileloc = aobj.download(filepath=filename,quiet=True)
    

def reducecode(url):
     ncsresponse = urllib.request.urlopen(url)
     ncshtml = ncsresponse.read()
     ncssoup = BeautifulSoup(ncshtml, 'html.parser')
     vidscrape(ncssoup)
     print ("Enter the track numbers you want to download (Space in between 2 numbers)")
     seltracks = input()
     root = Tk()
     root.withdraw()
     filename = filedialog.askdirectory()
     splittracklist = seltracks.split()
     splittracklist = [int(a) for a in splittracklist]
     download(splittracklist,filename)
     print("Audio downloaded at: "+filename)
     print("Do you want to open the download folder?\n1.Yes\n2.No")
     opp = int(input())
     if(opp==1):
         os.startfile(filename)
     else:
         print("Thank you for using!")
        


def downloadsinglevideofile(url):
	dobj = pafy.new(url)
	aobj = dobj.getbest()
	root = Tk()
	root.withdraw()
	filename = filedialog.askdirectory()
	print("-------------------------------------------------------------")
	print("Now Downloading:"+dobj.title)
	print("Size is %s" % aobj.get_filesize())
	print("Video resolution is: "+aobj.resolution)
	fileloc = aobj.download(filepath=filename,quiet=False)


def downloadplaylist(url):
	print("Give a download location")
	root = Tk()
	root.withdraw()
	filename = filedialog.askdirectory()
	playlist = pafy.get_playlist(url)
	playlen = len(playlist['items'])
	i=0
	while i < playlen:
		pafyobj = playlist['items'][i]['pafy']
		aobj = pafyobj.getbest()
		print("---------------------------------------------------------")
		print("Now Downloading: "+pafyobj.title)
		print("Size is: %s" % aobj.get_filesize)
		print("Video Resolution is: "+aobj.resolution)
		fileloc = aobj.download(filepath=filename,quiet=False)

	print("Videos downloaded at: "+filename)
	print("Do you want to open the download location?\n1.Yes\n2.No")
	ch = int(input())
	if ch == 1:
		os.startfile(filename)
	else:
		print("Thank you for using this script!")
		print("EAT................SLEEP..................CODE...................REPEAT")




print ("What do you want to download:\n1.Audio\n2.Video")
dwnldch = input()

if dwnldch == '1':
	print ("Choose your music channel:\n1.NCS\n2.Majestic Casual\n3.Heroboard\n4.No, I have my download link")
	ch = input()
	ncsvidlinks = ['Garbage']

	if ch == '1':
		ncs()
	elif ch == '2':
		majc()
	elif ch == '3':
		hero()
	else:
		print("Enter the url (Playlist support coming soon!):\n")
		dwnlurl = input()
		print(dwnlurl)
		downloadsingleaudio(dwnlurl)

else:
	print("Method of inserting video url:\n1.I have a url\n2.I have a file with all download url in it.\n3.Download Playlist")
	method = int(input())
	if method == 1:
		print("Enter videourl:\n")
		dwnldurl = input()
		downloadsinglevideo(dwnldurl)
		print("EAT................SLEEP..................CODE...................REPEAT")
	elif method == 3:
		print("Enter playlist url")
		dwnlurl = input()
		downloadplaylist(dwnlurl)
		print("EAT................SLEEP..................CODE...................REPEAT")
	else:
		print("Open file location:")
		root = Tk()
		root.withdraw()
		filename = filedialog.askopenfilename(filetypes=[("Text files","*.txt")])
		lines = [line.rstrip('\n') for line in open(filename)]
		for i in range(len(lines)):
			print(lines[i])
			downloadsinglevideofile(lines[i])
		print("Video downloaded at: "+filename)
		print("Do you want to open the download folder?\n1.Yes\n2.No")
		opp = int(input())
		if(opp==1):
			os.startfile(filename)
		else:
			print("Thank you for using!")
			print("EAT................SLEEP..................CODE...................REPEAT")
