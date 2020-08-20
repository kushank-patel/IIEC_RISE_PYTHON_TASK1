import os
import pyttsx3
pyttsx3.speak("write down here what application do you want to open")
while True:
	print()
	print("Search For any Applications :" , end="")
	p = input()
        
	
	#notepad
	if (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("notepad" in p) or ("text editor" in p) or ("NOTEPAD" in p) or ("TEXT EDITOR" in p)):
	   os.system("notepad")

	#paint
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("paint" in p) or ("mspaint" in p) or ("PAINT" in p) or ("MSPAINT" in p)):
	   os.system("mspaint")

	#windows mediaplayer
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("media" in p) or ("player" in p) or ("MEDIA" in p) or ("PLAYER" in p)):
	   os.system("wmplayer")

	#google chrome
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("google" in p) or ("chrome" in p) or ("www.google.com" in p) or ("GOOGLE" in p) or ("CHROME" in p) or ("WWW.GOOGLE.COM" in p)):
	   os.system("chrome")
        
	#control panel
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("control panel" in p) or ("computer" in p) or ("control" in p) or ("CONTROL PANEL" in p) or ("COMPUTER" in p) or ("CONTROL" in p)):
	   os.system("control panel")
	
	#sublime
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("sublime" in p) or ("sublime text" in p) or ("text editor" in p) or ("SUBLIME" in p) or ("SUBLIME TEXT" in p) or ("TEXT EDITOR" in p)):
	   os.system("sublime_text")
        
	#Internet explorer
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("explorer" in p) or ("Internet" in p) or ("search engine" in p) or ("EXPLORER" in p) or ("INTERNET" in p) or ("SEARCH ENGINE" in p)):
	   os.system("iexplore")
	
	#windows photo viewer
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("windows" in p) or ("photo" in p) or ("WINDOWS" in p) or ("PHOTO" in p)):
	   os.system("ImagingDevices")
	
	#git
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("git" in p) or ("GIT" in p)) :
	   os.system("bash")

	#10Teamviewer
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("team" in p) or ("teamviewer" in p) or ("remotedesktopprotocol" in p) or ("rdp" in p) or ("TEAM" in p) or ("TEAMVIEWER" in p) or ("REMOTEDESKTOPPROTOCOL" in p) or ("RDP" in p)):
	   os.system("teamviewer")

	#sqlyog
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("yog" in p) or ("sqlyog" in p) or ("database" in p) or ("sql" in p) or ("YOG" in p) or ("SQLYOG" in p) or ("DATABASE" in p)):
	   os.system("sqlyog")
	
	#virtualbox
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("virtualbox" in p) or ("guest os" in p) or ("vmbox" in p) or ("VIRTUALBOX" in p) or ("GUEST OS" in p) or ("VMBOX" in p)):
	   os.system("virtualbox")

	#vlc
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("vlc" in p) or ("vlc player" in p) or ("video lan client" in p) or ("VLC" in p) or ("VLC PLAYER" in p) or ("VIDEO LAN CLIENT" in p)):
	   os.system("vlc")

	#anaconda version
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("anaconda" in p) or ("version" in p) or ("conda version" in p) or ("ANACONDA" in p) or ("VERSION" in p) or ("CONDA VERSION" in p)):
	   os.system("_conda -V")

	#anaconda help
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("condahelp" in p) or ("help" in p) or ("conda help" in p) or ("CONDAHELP" in p) or ("HELP" in p) or ("CONDA HELP" in p)):
	   os.system("_conda -h")

	#python
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("python" in p) or ("python code" in p) or ("python environment" in p) or ("PYTHON" in p) or ("OYTHON CODE" in p) or ("PYTHON ENVIRONMENTS" in p)):
	   os.system("python")	
	
	#Driverbooster
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("driver" in p) or ("booster" in p) or ("DRIVER" in p) or ("BOOSTER" in p)):
	   os.system("driverbooster")

	#microsoft edge
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or ("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("msedge" in p) or ("edge" in  p) or ("microsoft edge" in p) or ("MSEDGE" in p) or ("EDGE" in p) or ("MICROSOFT EDGE" in p)):
	   os.system("msedge")		
	
	#eclipse
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("eclipse" in p) or ("java ide" in p) or ("ECLIPSE" in p) or ("JAVA IDE" in p)):
	   os.system("eclipse")	   	
   	 	
	#20winRAR
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("winrar" in p) or ("extend file" in p) or ("WINRAR" in p) or ("EXTEND FILE" in p)):
	   os.system("winRAR")	 

        #www.facebook.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("facebook" in p) or ("fb" in p) or ("www.facebook.com" in p) or ("fblogin" in p) or ("FACEBOOK" in p) or ("FB" in p) or ("WWW.FACEBOOK.COM" in p) or ("FBLOGINE" in p)):
	   os.system("chrome www.facebook.com")

	#www.youtube.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("youtube" in p) or ("video" in p) or ("www.youtube.com" in p) or ("YOUTUBE" in p) or ("VIDEO" in p) or ("WWW.YOUTUBE.COM" in p)):
	   os.system("chrome www.youtube.com")
	
	#www.amazon.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("amazon" in p) or ("shopping" in p) or ("www.amazon.com" in p) or ("AMAZON" in p) or ("SHOPPING" in p) or ("WWW.AMAZON.COM " in p)):
	   os.system("chrome www.amazon.com")

	#www.gmail.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("gmail" in p) or ("email id" in p) or ("www.gmail.com" in p) or ("GMAIL" in p) or ("EMAIL ID" in p) or ("WWW.GMAIL.COM" in p)):
	   os.system("chrome www.gmail.com")
	
        #www.weather.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("weather today" in p) or ("temperature" in p) or ("www.weather.com" in p) or ("weather" in p)):
	   os.system("chrome www.weather.com")
	
	#www.ebay.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("ebay" in p) or ("www.ebay.com" in p) or ("buy&sell" in p) or ("EBAY" in p) or ("WWW.EBAY.COM" in p) or ("BUY&SELL" in p)):
	   os.system("chrome www.ebay.com")
	
	#www.netflix.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("netflix" in p) or ("series" in p) or ("www.netflix.com" in p) or ("NETFLIX" in p) or ("SERIES" in p) or ("WWW.NETFLIX.COM" in p)):
	   os.system("chrome www.netflix.com")
	
        #www.linkedin.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("linkedin" in p) or ("linkedin web" in p) or ("www.linkedin.com" in p) or ("LINKEDIN" in p) or ("LINKEDIN WEB" in p) or ("WWW.LINKEDIN.COM" in p)):
	   os.system("chrome www.linkedin.com")
	
	#www.pinterest.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("pin" in p) or ("pinterest" in p) or ("www.pinterest.com" in p) or ("PIN" in p) or ("PINTEREST" in p) or ("WWW.PINTEREST.COM" in p)):
	   os.system("chrome www.pinterest.com")

	
	#30www.airbnb.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("air" in p) or ("airbnb" in p) or ("www.airbnb.com" in p) or ("AIR" in p) or ("AIRBNB" in p) or ("WWW.AIRBNB.COM" in p)):
	   os.system("chrome www.airbnb.com")

	#www.spotify.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("spotify" in p) or ("music online" in p) or ("www.spotify.com" in p) or ("SPOTIFY" in p) or ("MUSIC ONLINE" in p) or ("WWW.SPOTIFY.COM" in p)):
	   os.system("chrome www.spotify.com")

	#www.stackoverflow.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("stack" in p) or ("overflow" in p) or ("www.stackoverflow.com" in p) or ("STACK" in p) or ("OVERFLOW" in p) or ("WWW.STACKOVERFLOW.COM" in p)):
	   os.system("chrome www.stackoverflow.com")

	#www.instagram.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("insta" in p) or ("instagram" in p) or ("www.instagram.com" in p) or ("INSTA" in p) or ("INSTAGRAM" in p) or ("WWW.INSTAGRAM.COM" in p)):
	   os.system("chrome www.instagram.com")

	#www.adobe.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("adobe" in p) or ("criativecloud" in p) or ("www.adobe.com" in p) or ("ADOBE" in p) or ("CRIATIVECLOUD" in p) or ("WWW.ADOBE.COM" in p)):
	   os.system("chrome www.adobe.com")

	#www.bookmyshow.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("bookmy" in p) or ("myshow" in p) or ("movie ticket" in p) or ("www.bookmyshow.com" in p) or ("BOOKMY" in p) or ("MYSHOW" in p) or ("MOVIE TICKET" in p) or ("WWW.BOOKMYSHOW" in p)):
	   os.system("chrome www.bookmyshow.com")

	#www.hotstar.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("hotstar" in p) or ("star" in p) or ("www.hotstar.com" in p) or ("HOTSTAR" in p) or ("STAR" in p) or ("WWW.HOTSTAR.COM" in p)):
	   os.system("chrome www.hotstar.com")
	
	#www.apple.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("apple" in p) or ("applestore" in p) or ("www.apple.com" in p) or ("APPLE" in p) or ("APPLESTORE" in p) or ("WWW.APPLE.COM" in p)):
	   os.system("chrome www.apple.com")

	#www.blogger.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("blogger" in p) or ("blog" in p) or ("www.blogger.com" in p) or ("BLOGGER" in p) or ("BLOG" in p) or ("WWW.BLOGGER" in p)):
	   os.system("chrome www.blogger.com")	
	
	#www.wikipedia.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("wiki" in p) or ("wikipedia" in p) or ("www.wikipedia.com" in p) or ("WIKI" in p) or ("WIKIPEDIA" in p) or ("WWW.WIKIPEDIA.COM" in p)):
	   os.system("chrome www.wikipedia.com")
	
	#www.mozilla.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("mozilla" in p) or ("firefox" in p) or ("www.morzilla.com" in p) or ("MORZILLA" in p) or ("FIREFOX" in p) or ("WWW.MORZILLA.COM" in p)):
	   os.system("chrome www.mozilla.com")
	
	#www.dropbox.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("drop" in p) or ("dropbox" in p) or ("www.dropbox.com" in p) or ("DROP" in p) or ("DROPBOX" in p) or ("WWW.DROPBOX" in p)):
	   os.system("chrome www.dropbox.com")

	#www.paypal.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("paypal" in p)  or ("www.paypal.com" in p) or ("PAYPAL" in p) or ("WWW.PAYPAL.COM" in p)):
	   os.system("chrome www.paypal.com")

	#www.w3schools.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("w3schools" in p) or ("learning" in p) or ("www.w3schools.com" in p) or ("W3SCHOOLS" in p) or ("LEARNING" in p) or ("WWW.W3SCHOOLS.COM" in p)):
	   os.system("chrome www.w3schools.com")

        #www.wix.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("wix" in p) or ("www.wix.com" in p) or ("WIX" in p) or ("WWW.WIX.COM" in p)):
	   os.system("chrome www.wix.com")
	
	#www.twitter.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("twitter" in p) or ("www.twitter.com" in p) or ("TWITTER" in p) or ("WWW.TWITTER.COM" in p)):
	   os.system("chrome www.twitter.com")

	#www.coursera.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("coursera" in p) or ("courseraonline course" in p) or ("www.coursera.com" in p) or ("COURSERA" in p) or ("COURSERAONLINE COURSE" in p) or ("WWW.COURSERA.COM" in p)):
	   os.system("chrome www.coursera.com")

	#www.udemy.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("udemy" in p) or ("www.udemy.com" in p) or ("UDEMY" in p) or ("WWW.UDEMY.COM" in p)):
	   os.system("chrome www.udemy.com")

	#www.byjus.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("byjus" in p) or ("byjuslearning" in p) or ("www.byjus.com" in p) or ("BYJUS" in p) or ("BYJUSLEARNING" in p)or ("WWW.BYJUS.COM" in p)):
	   os.system("chrome www.byjus.com")
	
	#www.prime.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("prime" in p) or ("primevideos" in p) or ("www.prime.com" in p) or ("PRIME" in p) or ("PRIMEVIDEOS" in p) or ("WWW.PRIME.COM" in p)):
	   os.system("chrome www.prime.com")
	
	#50www.myntra.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("myntra" in p) or ("mytrashopping" in p) or ("www.myntra.com" in p) or ("MYNTRA" in p) or ("MYNTRASHOPPING" in p) or ("WWW.MYNTRA.COM" in p)):
	   os.system("chrome www.myntra.com")
	
	#www.filpkart.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("flipkart" in p) or ("flipkartshopping" in p) or ("www.flipkart.com" in p) or ("FLIPKART" in p) or ("FLIPKARTSHOPPING" in p) or ("WWW.FLIPKART.COM" in p)):
	   os.system("chrome www.filpkart.com")
	
	#www.jio cinema.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("jiocinema" in p) or ("jio" in p) or ("www.jiocinema.com" in p) or ("JIOCINEMA" in p) or ("JIO" in p) or ("WWW.JIOCINEMA.COM" in p)):
	   os.system("chrome www.jiocinema.com")

	#www.quora.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("quora" in p) or ("quoralearning" in p) or ("www.quora.com" in p) or ("QUORA" in p) or ("QUORALEARNING" in p) or ("WWW.QUORA.COM" in p)):
	   os.system("chrome www.quora.com")

	#www.brainly.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("brainly" in p) or ("www.brainly.com" in p) or ("BRAINLY" in p) or ("WWW.BRAINLY.COM" in p)):
	   os.system("chrome www.brainly.com")

	#www.grammarly.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("grammarly" in p) or ("www.grammarly.com" in p) or ("GRAMMAELY" in p) or ("GRAMMARLY.COM" in p)):
	   os.system("chrome www.grammarly.com")
	
	#www.zomato.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("zomato" in p) or ("zomatofood" in p) or ("www.zomato.com" in p) or ("ZOMATO" in p) or ("ZOMATOFOOD" in p) or ("WWW.ZOMATO.COM" in p)):
	   os.system("chrome www.zomato.com")

	#www.ubereats.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("ubereats" in p) or ("ubereatsfood" in p) or ("foodordering" in p) or ("www.ubereats.com" in p) or ("UBEREATS" in p) or ("UBEREATSFOOD" in p) or ("FOODORDERING" in p) or ("WWW.UBEREATS.COM" in p)):
	   os.system("chrome www.ubereats.com")

	#www.grubhub.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("grubhub" in p) or ("grubhubfood" in p) or ("grubhubfoodordering" in p) or ("www.grubhub.com" in p) or ("GRUBHUB" in p) or ("GRUBHUBFOOD" in p) or ("GRUBHUBFOODORDERING" in p) or ("WWW.GRUBHUB.COM" in p)):
	   os.system("chrome www.grubhub.com")

	#www.doordash.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("doordash" in p) or ("doordashfood" in p) or ("doordashfoodordering" in p) or ("www.doordash.com" in p) or ("DOORDAH" in p) or ("DOORDASHFOOD" in p) or ("DOORDASHFOODORDERING" in p) or ("WWW.DOORDASH.COM" in p)):
	   os.system("chrome www.doordash.com")

	#60www.justeat.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("justeat" in p) or ("justeatfood" in p) or ("justeatfoodordering" in p) or ("www.justeat.com" in p) or ("JUSTEAT" in p) or ("JUSTEATFOOD" in p) or ("JUSTEATFOODORDERING" in p) or ("WWW.JUSTEAT.COM" in p)):
	   os.system("chrome www.justeat.com")
	
	#www.swiggy.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("swiggy" in p) or ("swiggyfood" in p) or ("swiggyfoodordering" in p) or ("www.swiggy.com" in p) or ("SWIGGY" in p) or ("SWIGGYFOOD" in p) or ("SWIGGYORDERING" in p) or ("WWW.SWIGGY.COM" in p)):
	   os.system("chrome www.swiggy.com")

	#www.dominos.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("dominos" in p) or ("dominosfood" in p) or ("dominosfoodordering" in p) or ("www.dominos.com" in p) or ("DOMINOS" in p) or ("DOMINOSFOOD" in p) or ("DOMINOORDERINGFOOD" in p) or ("WWW.DOMINOS.COM" in p)):
	   os.system("chrome www.dominos.com")

	#www.pizzahut.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("pizzahut" in p) or ("pizzahutfood" in p) or ("pizzahutfoodordering" in p) or ("www.pizzahut.com" in p) or ("PIZZAHUT" in p) or ("PIZZAHUTFOOD" in p) or ("PIZZAHUTFOODORDERING" in p) or ("WWW.PIZZAHUT.COM" in p)):
	   os.system("chrome www.pizzahut.com")

	#www.cnn.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("cnn" in p) or ("cnnnews" in p) or ("www.cnn.com" in p) or ("CNN" in p) or ("CNNNEWS" in p) or ("WWW.CNN.COM" in p)):
	   os.system("chrome www.cnn.com")

	#www.cbsnews.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("cbsnews" in p) or ("www.cbsnews.com" in p) or ("CBSNEWS" in p) or ("WWW.CBSNEWS.COM" in p)):
	   os.system("chrome www.cbsnews.com")

	#www.bbcnewsindia.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("bbcnewsindia" in p) or ("Nbbcnews" in p) or ("www.bbcnewsindia.com" in p) or ("BBCNEWSINDIA" in p) or ("WWW.BBCNEWSINDIA.COM" in p)):
	   os.system("chrome www.bbcnewsindia.com")
	
	#www.indiatoday.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("indiatoday" in p) or ("www.indiatoday.com" in p) or ("INDIATODAY" in p) or ("WWW.INDIATODAY.COM" in p)):
	   os.system("chrome www.indiatoday.com")

	#www.hdfc bank.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("hdfcbank" in p) or ("www.hdfcbank.com" in p) or ("HDFCBANK" in p) or ("WWW.HDFCBANK.COM" in p)):
	   os.system("chrome www.hdfcbank.com")

	#www.icici bank.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("icici" in p) or ("icicibank" in p) or ("www.icicibank.com" in p) or ("ICICI" in p) or ("ICICIBANK" in p) or ("WWW.ICICI.COM" in p)):
	   os.system("chrome www.icicibank.com")

	#70www.axis bank.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("axis" in p) or ("axisbank" in p) or ("www.axisbank.com" in p) or ("AXIS" in p) or ("AXISBANK" in p) or ("WWW.AXIS.COM" in p)):
	   os.system("chrome www.axisbank.com")

	#www.bankofindia.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("bankofindia" in p) or ("boi" in p) or ("www.bankofindia.com" in p) or ("BANKOFINDIA" in p) or ("BOI" in p) or ("WWW.BANKOFINDIA.COM" in p)):
	   os.system("chrome www.bankofindia.com")

	#www.zoom.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("zoom" in p) or ("zoomapp" in p) or ("www.zoom.com" in p) or ("ZOOM" in p) or ("ZOOMAPP" in p) or ("WWW.ZOOM.COM" in p)):
	   os.system("chrome www.zoom.com")

	#www.justdial.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("justdial" in p) or ("www.justdial.com" in p) or ("JUSTDIAL" in p) or ("WWW.JUSTDIAL.COM" in p)):
	   os.system("chrome www.justdial.com")
	
	#www.samsung.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("samsung" in p) or ("www.samsung.com" in p) or ("SAMSUNG" in p) or ("WWW.SAMSUNG" in p)):
	   os.system("chrome www.samsung.com")

	#www.discord.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("discord" in p) or ("www.discord.com" in p) or ("DISCORD" in p) or ("WWW.DISCORD.COM" in p)):
	   os.system("chrome www.discord.com")

	#www.phonepe.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("phonepe" in p) or ("www.phonepe.com" in p) or ("PHONEPE" in p) or ("WWW.PHONEPE" in p)):
	   os.system("chrome www.phonepe.com")

	#www.whatsapp.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("whatsapp" in p) or ("www.whatsapp.com" in p) or ("WHATSAPP" in p) or ("WWW.WHATSAPP.COM" in p)):
	   os.system("chrome www.whatsapp.com")
	
	#www.duo.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("duo" in p) or ("www.duo.com" in p) or ("DUO" in p) or ("WWW.DUO.COM" in p)):
	   os.system("chrome www.duo.com")

	#www.telegram.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("telegram" in p) or ("www.telegram.com" in p) or ("TELEGRAM" in p) or ("WWW.TELEGRAM.COM" in p)):
	   os.system("chrome www.telegram.com")

	#80www.savan.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("savan" in p) or ("www.savan.com" in p) or ("SAVAN" in p) or ("WWW.SAVAN.COM" in p)):
	   os.system("chrome www.savan.com")

	#www.reddit.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("reddit" in p) or ("www.reddit.com" in p) or ("REDDIT" in p) or ("WWW.REDDIT.COM" in p)):
	   os.system("chrome www.reddit.com")

	#www.backstage.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("backstage" in p) or ("www.backstage.com" in p) or ("BACKSTAGE" in p) or ("WWW.BACKSTAGE.COM" in p)):
	   os.system("chrome www.backstage.com")

	
	#www.blender.com
	elif (("run" in p) or ("open" in p) or("find" in p) or ("show" in p) or ("get me" in p) or ("give me" in p) or ("execute" in p) or ("findout" in p) or ("search" in p) or ("looking for" in p) or ("RUN" in p) or ("OPEN" in p) or("FIND" in p) or ("SHOW" in p) or ("GET ME" in p) or ("GIVE ME" in p) or ("EXECUTE" in p) or ("FINDOUT" in p) or ("SEARCH" in p) or ("LOOKING FOR" in p)) and (("blender" in p) or ("www.blender.com" in p) or ("BLENDER" in p) or ("WWW.BLENDER.COM" in p)):
	   os.system("chrome www.blender.com")

	elif ("exit" in p) or ("terminate" in p) or ("quit" in p ) or ("leaving" in p) or ("end" in p) or ("close" in p) or ("stop" in p) or ("finish" in p) or ("hold" in p) or ("EXIT" in p) or ("TERMINAL" in p) or ("QUIT" in p ) or ("LEAVING" in p) or ("END" in p) or ("CLOSE" in p) or ("STOP" in p) or ("FINISH" in p) or ("HOLD" in p):
	   break 
	   

	else:
	   pyttsx3.speak("invalid input please try again")
	   print("invalid input")
	
	