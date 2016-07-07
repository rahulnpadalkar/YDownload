import pafy
import urllib
from bs4 import BeautifulSoup
import webbrowser
from tkinter import Tk
from tkinter import filedialog
import os

 
 
print ("Choose your music channel:\n1.NCS\n2.Majestic Casual\n3.Heroboard")

ch = input()
ncsvidlinks = ['Garbage']

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
        print (new)
        dindex=splittracklist[new]
        print (dindex)
        dlink = ncsvidlinks[dindex]
        dobj = pafy.new(dlink)
        aobj = dobj.getbestaudio()
        print("Size is %s" % aobj.get_filesize())
        fileloc = aobj.download(filepath=filename,quiet=True)
    
        

def reducecode(url):
     ncsresponse = urllib.request.urlopen(url)
     ncshtml = ncsresponse.read()
     ncssoup = BeautifulSoup(ncshtml, 'html.parser')
     vidscrape(ncssoup)
     print ("Enter the track numbers you want to download (Space in between 2 numbers)")
     seltracks = input()
     print("I am here!")
     root = Tk()
     print("Tk() ran")
     root.withdraw()
     print("Window withdrwan")
     filename = filedialog.askdirectory()
     print("file should be selected now")
     print (filename)
     splittracklist = seltracks.split()
     splittracklist = [int(a) for a in splittracklist]
     print(splittracklist)
     download(splittracklist,filename)
     print("Audio downloaded at: "+filename)
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


    
if ch == '1':
    ncs()

elif ch == '2':
    majc()

else:
    hero()


    
    




