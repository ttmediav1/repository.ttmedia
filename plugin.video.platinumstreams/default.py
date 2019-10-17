 #############Imports#############
import xbmc,xbmcaddon,xbmcgui,xbmcplugin,base64,os,re,unicodedata,requests,time,string,sys,urllib,urllib2,json,urlparse,datetime,zipfile,shutil
from resources.modules import client,control,tools,user
from datetime import date
import xml.etree.ElementTree as ElementTree


#################################
service_name =  'Platinum Streams'
#############Defined Strings#############
icon             = xbmc.translatePath(os.path.join('special://home/addons/' + user.id+'/media/',  'icon.png'))
fanart           = xbmc.translatePath(os.path.join('special://home/addons/' + user.id+'/media/',  'fanart.jpg'))
background       = xbmc.translatePath(os.path.join('special://home/addons/' + user.id+'/media/',  'background.jpg'))
live		     = xbmc.translatePath(os.path.join('special://home/addons/' + user.id+'/media/',  'live.jpg'))
catch	 	     = xbmc.translatePath(os.path.join('special://home/addons/' + user.id+'/media/',  'cu.jpg'))
Moviesod	 	 = xbmc.translatePath(os.path.join('special://home/addons/' + user.id+'/media/',  'movie.jpg'))
Tvseries	 	 = xbmc.translatePath(os.path.join('special://home/addons/' + user.id+'/media/',  'tv.jpg'))
iconextras       = xbmc.translatePath(os.path.join('special://home/addons/' + user.id+'/media/',  'iconextras.png'))
iconsettings     = xbmc.translatePath(os.path.join('special://home/addons/' + user.id+'/media/',  'iconsettings.png'))
iconlive		 = xbmc.translatePath(os.path.join('special://home/addons/' + user.id+'/media/',  'iconlive.png'))
iconcatchup	     = xbmc.translatePath(os.path.join('special://home/addons/' + user.id+'/media/',  'iconcatchup.png'))
iconMoviesod	 = xbmc.translatePath(os.path.join('special://home/addons/' + user.id+'/media/',  'iconmovies.png'))
iconTvseries	 = xbmc.translatePath(os.path.join('special://home/addons/' + user.id+'/media/',  'icontvseries.png'))
iconsearch	     = xbmc.translatePath(os.path.join('special://home/addons/' + user.id+'/media/',  'iconsearch.png'))
iconaccount	     = xbmc.translatePath(os.path.join('special://home/addons/' + user.id+'/media/',  'iconaccount.png'))
icontvguide	     = xbmc.translatePath(os.path.join('special://home/addons/' + user.id+'/media/',  'iconguide.png'))

username     	 = control.setting('Username')
password     	 = control.setting('Password')

live_url     	 = '%s:%s/enigma2.php?username=%s&password=%s&type=get_live_categories'%(user.host,user.port,username,password)
vod_url      	 = '%s:%s/enigma2.php?username=%s&password=%s&type=get_vod_categories'%(user.host,user.port,username,password)
series_url       = '%s:%s/enigma2.php?username=%s&password=%s&type=get_series_categories'%(user.host,user.port,username,password)
panel_api    	 = '%s:%s/panel_api.php?username=%s&password=%s'%(user.host,user.port,username,password)
play_url     	 = '%s:%s/live/%s/%s/'%(user.host,user.port,username,password)


Guide = xbmc.translatePath(os.path.join('special://home/addons/addons/'+user.id+'/resources/catchup', 'guide.xml'))
GuideLoc = xbmc.translatePath(os.path.join('special://home/addons/addons/'+user.id+'/resources/catchup', 'g'))

advanced_settings           =  xbmc.translatePath('special://home/addons/'+user.id+'/resources/advanced_settings')
advanced_settings_target    =  xbmc.translatePath(os.path.join('special://home/userdata','advancedsettings.xml'))

KODIV        = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
#########################################

def buildcleanurl(url):
	url = str(url).replace('USERNAME',username).replace('PASSWORD',password)
	return url
def start():
	if username=="":
		usern = userpopup()
		passw= passpopup()
		control.setSetting('Username',usern)
		control.setSetting('Password',passw)
		xbmc.executebuiltin('Container.Refresh')
		auth = '%s:%s/enigma2.php?username=%s&password=%s&type=get_vod_categories'%(user.host,user.port,usern,passw)
		auth = tools.OPEN_URL(auth)
		if auth == "":
			line1 = "Incorrect Login Details"
			line2 = "Please Re-enter" 
			line3 = "" 
			xbmcgui.Dialog().ok('Attention', line1, line2, line3)
			start()
		else:
			line1 = "Login Sucsessfull"
			line2 = "Welcome to "+user.name 
			line3 = ('[B][COLOR white]%s[/COLOR][/B]'%usern)
			xbmcgui.Dialog().ok(user.name, line1, line2, line3)
			tvguidesetup()
			addonsettings('ADS2','')
			xbmc.executebuiltin('Container.Refresh')
			home()
	else:
		auth = '%s:%s/enigma2.php?username=%s&password=%s&type=get_vod_categories'%(user.host,user.port,username,password)
		auth = tools.OPEN_URL(auth)
		if not auth=="":
			
			tools.addDir('Live TV','live',1,iconlive,background,'')
			tools.addDir('Catchup TV','url',12,iconcatchup,background,'')
			tools.addDir('Movies','vod',3,iconMoviesod,background,'')
			tools.addDir('TV Series','live',18,iconTvseries,background,'')
			
			if xbmc.getCondVisibility('System.HasAddon(pvr.iptvsimple)'):
				tools.addDir('TV Guide','pvr',7,icon,background,'')
			tools.addDir('Search','url',5,iconsearch,background,'')
			tools.addDir('Settings','url',8,iconsettings,background,'')
			tools.addDir('Extras','url',16,iconextras,background,'')
			tools.addDir('Account Information','url',6,iconaccount,background,'')
				
def home():
	
	tools.addDir('Account Information','url',6,icon,background,'')
	tools.addDir('Live TV','live',1,icon,background,'')
	tools.addDir('TV Series','live',18,icon,background,'')
	
	if xbmc.getCondVisibility('System.HasAddon(pvr.iptvsimple)'):
		tools.addDir('TV Guide','pvr',7,icon,background,'')
	tools.addDir('Catchup TV','url',12,icon,background,'')
	tools.addDir('vod','vod',3,icon,background,'')
	tools.addDir('Search','',5,icon,background,'')
	tools.addDir('Settings','url',8,icon,background,'')
	tools.addDir('Extras','url',16,icon,background,'')
		
def livecategory(url):
	
	open = tools.OPEN_URL(live_url)
	all_cats = tools.regex_get_all(open,'<channel>','</channel>')
	
	for a in all_cats:
		name = tools.regex_from_to(a,'<title>','</title>')
		name = base64.b64decode(name)
		url1  = tools.regex_from_to(a,'<playlist_url>','</playlist_url>').replace('<![CDATA[','').replace(']]>','')
		if xbmcaddon.Addon().getSetting('hidexxx')=='true':
			tools.addDir('%s'%name,url1,2,icon,live,'')
		else:
			if not 'XXX |' in name:
				tools.addDir('%s'%name,url1,2,icon,background,'')
				

def series_cats(url):	# added by @ShaneysRepo
	open = tools.OPEN_URL(series_url)
	all_cats = tools.regex_get_all(open,'<channel>','</channel>')
	for a in all_cats:
		name = tools.regex_from_to(a,'<title>','</title>')
		name = base64.b64decode(name)
		url1  = tools.regex_from_to(a,'<playlist_url>','</playlist_url>').replace('<![CDATA[','').replace(']]>','')
		if xbmcaddon.Addon().getSetting('hidexxx')=='true':
			tools.addDir('%s'%name,url1,25,icon,background,'')
		else:
			if not 'XXX |' in name:
				tools.addDir('%s'%name,url1,25,icon,background,'')
		
def Livelist(url):
	url  = buildcleanurl(url)
	open = tools.OPEN_URL(url)
	
	all_cats = tools.regex_get_all(open,'<channel>','</channel>')
	for a in all_cats:
		name = tools.regex_from_to(a,'<title>','</title>')
		name = base64.b64decode(name)
		xbmc.log(str(name))
		name = re.sub('\[.*?min ','-',name)
		thumb= tools.regex_from_to(a,'<desc_image>','</desc_image>').replace('<![CDATA[','').replace(']]>','')
		url1  = tools.regex_from_to(a,'<stream_url>','</stream_url>').replace('<![CDATA[','').replace(']]>','')
		desc = tools.regex_from_to(a,'<description>','</description>')
		if xbmcaddon.Addon().getSetting('hidexxx')=='true':
			tools.addDir(name,url1,4,thumb,background,base64.b64decode(desc))
		else:
			if not 'XXX:' in name:
				if not 'XXX vod:' in name:
					tools.addDir(name,url1,4,thumb,background,base64.b64decode(desc))
		
	
def serieslist(url): # Added by @ShaneysRepo
	url  = buildcleanurl(url)
	open = tools.OPEN_URL(url)
	series = tools.regex_from_to(open,'<category_title>','</category_title>').replace('<![CDATA[','').replace(']]>','')
	all_cats = tools.regex_get_all(open,'<channel>','</channel>')
	for a in all_cats:
		name = tools.regex_from_to(a,'<title>','</title>')
		name = base64.b64decode(name)
		xbmc.log(str(name))
		name = re.sub('\[.*?min ','-',name)
		thumb= tools.regex_from_to(a,'<desc_image>','</desc_image>').replace('<![CDATA[','').replace(']]>','')
		url1  = tools.regex_from_to(a,'<playlist_url>','</playlist_url>').replace('<![CDATA[','').replace(']]>','')
		desc = tools.regex_from_to(a,'<description>','</description>')
		if xbmcaddon.Addon().getSetting('hidexxx')=='true':
			tools.addDir(name,url1,19,thumb,background,'')
		else:
			if not 'XXX:' in name:
				if not 'XXX vod:' in name:
					tools.addDir(name,url1,19,thumb,background,'')
					
					
def series_options(url): # Added by @ShaneysRepo
	url  = buildcleanurl(url)
	open = tools.OPEN_URL(url)
	series = tools.regex_from_to(open,'<category_title>','</category_title>').replace('<![CDATA[','').replace(']]>','')
	all_cats = tools.regex_get_all(open,'<channel>','</channel>')
	for a in all_cats:
		name = tools.regex_from_to(a,'<title>','</title>')
		name = base64.b64decode(name)
		xbmc.log(str(name))
		name = re.sub('\[.*?min ','-',name)
		thumb= tools.regex_from_to(a,'<desc_image>','</desc_image>').replace('<![CDATA[','').replace(']]>','')
		url1  = tools.regex_from_to(a,'<playlist_url>','</playlist_url>').replace('<![CDATA[','').replace(']]>','')
		desc = tools.regex_from_to(a,'<description>','</description>')
		if xbmcaddon.Addon().getSetting('hidexxx')=='true':
			tools.addDir(url1,url1,20,thumb,background,base64.b64decode(desc))
		else:
			if not 'XXX:' in name:
				if not 'XXX vod:' in name:
					tools.addDir(name,url1,20,thumb,background,base64.b64decode(desc))


def season_list(url): # Added by @ShaneysRepo
	url  = buildcleanurl(url)
	open = tools.OPEN_URL(url)
	series = tools.regex_from_to(open,'<category_title>','</category_title>').replace('<![CDATA[','').replace(']]>','')
	all_cats = tools.regex_get_all(open,'<channel>','</channel>')
	for a in all_cats:
		name = tools.regex_from_to(a,'<title>','</title>')
		name = base64.b64decode(name)
		xbmc.log(str(name))
		name = re.sub('\[.*?min ','-',name)
		thumb= tools.regex_from_to(a,'<desc_image>','</desc_image>').replace('<![CDATA[','').replace(']]>','')
		url1  = tools.regex_from_to(a,'<stream_url>','</stream_url>').replace('<![CDATA[','').replace(']]>','')
		desc = tools.regex_from_to(a,'<description>','</description>')
		if xbmcaddon.Addon().getSetting('hidexxx')=='true':
			tools.addDir(url1,url1,4,thumb,background,base64.b64decode(desc))
		else:
			if not 'XXX:' in name:
				if not 'XXX vod:' in name:
					tools.addDir(name,url1,4,thumb,background,base64.b64decode(desc))

					
	
def vod(url):
	if url =="vod":
		open = tools.OPEN_URL(vod_url)
	else:
		url  = buildcleanurl(url)
		open = tools.OPEN_URL(url)
	all_cats = tools.regex_get_all(open,'<channel>','</channel>')
	for a in all_cats:
		if '<playlist_url>' in open:
			name = tools.regex_from_to(a,'<title>','</title>')
			url1  = tools.regex_from_to(a,'<playlist_url>','</playlist_url>').replace('<![CDATA[','').replace(']]>','')
			tools.addDir(str(base64.b64decode(name)).replace('?',''),url1,3,icon,background,'')
		else:
			if xbmcaddon.Addon().getSetting('meta') == 'true':
				try:
					name = tools.regex_from_to(a,'<title>','</title>')
					name = base64.b64decode(name)
					thumb= tools.regex_from_to(a,'<desc_image>','</desc_image>').replace('<![CDATA[','').replace(']]>','')
					url  = tools.regex_from_to(a,'<stream_url>','</stream_url>').replace('<![CDATA[','').replace(']]>','')
					desc = tools.regex_from_to(a,'<description>','</description>')
					desc = base64.b64decode(desc)
					plot = tools.regex_from_to(desc,'PLOT:','\n')
					cast = tools.regex_from_to(desc,'CAST:','\n')
					ratin= tools.regex_from_to(desc,'RATING:','\n')
					year = tools.regex_from_to(desc,'RELEASEDATE:','\n').replace(' ','-')
					year = re.compile('-.*?-.*?-(.*?)-',re.DOTALL).findall(year)
					runt = tools.regex_from_to(desc,'DURATION_SECS:','\n')
					genre= tools.regex_from_to(desc,'GENRE:','\n')
					tools.addDirMeta(str(name).replace('[/COLOR][/B].','.[/COLOR][/B]'),url,4,thumb,background,plot,str(year).replace("['","").replace("']",""),str(cast).split(),ratin,runt,genre)
				except:pass
				xbmcplugin.setContent(int(sys.argv[1]), 'vod')
			else:
				name = tools.regex_from_to(a,'<title>','</title>')
				name = base64.b64decode(name)
				thumb= tools.regex_from_to(a,'<desc_image>','</desc_image>').replace('<![CDATA[','').replace(']]>','')
				url  = tools.regex_from_to(a,'<stream_url>','</stream_url>').replace('<![CDATA[','').replace(']]>','')
				desc = tools.regex_from_to(a,'<description>','</description>')
				tools.addDir(name,url,4,thumb,background,base64.b64decode(desc))
				
				
		
##############################################
#### RULE NO.1 - DONT WRITE CODE THAT IS  ####
#### ALREADY WRITTEN AND PROVEN TO WORK :)####
##############################################


def catchup():
    listcatchup()
		
def listcatchup():
	open = tools.OPEN_URL(panel_api)
	all  = tools.regex_get_all(open,'{"num','direct')
	for a in all:
		if '"tv_archive":1' in a:
			name = tools.regex_from_to(a,'"epg_channel_id":"','"').replace('\/','/')
			thumb= tools.regex_from_to(a,'"stream_icon":"','"').replace('\/','/')
			id   = tools.regex_from_to(a,'stream_id":"','"')
			if not name=="":
				tools.addDir(name,'url',13,thumb,background,id)
			

def tvarchive(name,description):
    days = 7
	
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    date3 = datetime.datetime.now() - datetime.timedelta(days)
    date = str(date3)
    date = str(date).replace('-','').replace(':','').replace(' ','')
    APIv2 = base64.b64decode("JXM6JXMvcGxheWVyX2FwaS5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmYWN0aW9uPWdldF9zaW1wbGVfZGF0YV90YWJsZSZzdHJlYW1faWQ9JXM=")%(user.host,user.port,username,password,description)
    link=tools.OPEN_URL(APIv2)
    match = re.compile('"title":"(.+?)".+?"start":"(.+?)","end":"(.+?)","description":"(.+?)"').findall(link)
    for ShowTitle,start,end,DesC in match:
        ShowTitle = base64.b64decode(ShowTitle)
        DesC = base64.b64decode(DesC)
        format = '%Y-%m-%d %H:%M:%S'
        try:
            modend = dtdeep.strptime(end, format)
            modstart = dtdeep.strptime(start, format)
        except:
            modend = datetime.datetime(*(time.strptime(end, format)[0:6]))
            modstart = datetime.datetime(*(time.strptime(start, format)[0:6]))
        StreamDuration = modend - modstart
        modend_ts = time.mktime(modend.timetuple())
        modstart_ts = time.mktime(modstart.timetuple())
        FinalDuration = int(modend_ts-modstart_ts) / 60
        strstart = start
        Realstart = str(strstart).replace('-','').replace(':','').replace(' ','')
        start2 = start[:-3]
        editstart = start2
        start2 = str(start2).replace(' ',' - ')
        start = str(editstart).replace(' ',':')
        Editstart = start[:13] + '-' + start[13:]
        Finalstart = Editstart.replace('-:','-')
        if Realstart > date:
            if Realstart < now:
                catchupURL = base64.b64decode("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(user.host,user.port,username,password,description)
                ResultURL = catchupURL + str(Finalstart) + "&duration=%s"%(FinalDuration)
                kanalinimi = "[B][COLOR white]%s[/COLOR][/B] - %s"%(start2,ShowTitle)
                tools.addDir(kanalinimi,ResultURL,4,icon,background,DesC)

	
					
def DownloaderClass(url, dest):
    dp = xbmcgui.DialogProgress()
    dp.create('Fetching latest Catch Up',"Fetching latest Catch Up...",' ', ' ')
    dp.update(0)
    start_time=time.time()
    urllib.urlretrieve(url, dest, lambda nb, bs, fs: _pbhook(nb, bs, fs, dp, start_time))

def _pbhook(numblocks, blocksize, filesize, dp, start_time):
        try: 
            percent = min(numblocks * blocksize * 100 / filesize, 100) 
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024) 
            kbps_speed = numblocks * blocksize / (time.time() - start_time) 
            if kbps_speed > 0: 
                eta = (filesize - numblocks * blocksize) / kbps_speed 
            else: 
                eta = 0 
            kbps_speed = kbps_speed / 1024 
            mbps_speed = kbps_speed / 1024 
            total = float(filesize) / (1024 * 1024) 
            mbs = '[B][COLOR white]%.02f MB of less than 5MB[/COLOR][/B]' % (currently_downloaded)
            e = '[B][COLOR white]Speed:  %.02f Mb/s ' % mbps_speed  + '[/COLOR][/B]'
            dp.update(percent, mbs, e)
        except: 
            percent = 100 
            dp.update(percent) 
        if dp.iscanceled():
            dialog = xbmcgui.Dialog()
            dialog.ok(user.name, 'The download was cancelled.')
				
            sys.exit()
            dp.close()
#####################################################################

def tvguide():
		xbmc.executebuiltin('ActivateWindow(TVGuide)')
def stream_video(url):
	url = buildcleanurl(url)
	url = str(url).replace('USERNAME',username).replace('PASSWORD',password)
	liz = xbmcgui.ListItem('', iconImage='DefaultVideo.png', thumbnailImage=icon)
	liz.setInfo(type='Video', infoLabels={'Title': '', 'Plot': ''})
	liz.setProperty('IsPlayable','true')
	liz.setPath(str(url))
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
	
	
def searchdialog():
	search = control.inputDialog(heading='Search '+user.name+':')
	if search=="":
		return
	else:
		return search

	
def search():
	if mode==3:
		return False
	text = searchdialog()
	if not text:
		xbmc.executebuiltin("XBMC.Notification([B][COLOR white][B]Search is Empty[/B][/COLOR][/B],Aborting search,4000,"+icon+")")
		return
	xbmc.log(str(text))
	open = tools.OPEN_URL(panel_api)
	all_chans = tools.regex_get_all(open,'{"num":','epg')
	for a in all_chans:
		name = tools.regex_from_to(a,'name":"','"').replace('\/','/')
		url  = tools.regex_from_to(a,'"stream_id":"','"')
		thumb= tools.regex_from_to(a,'stream_icon":"','"').replace('\/','/')
		if text in name.lower():
			tools.addDir(name,play_url+url+'.ts',4,thumb,background,'')
		elif text not in name.lower() and text in name:
			tools.addDir(name,play_url+url+'.ts',4,thumb,background,'')

	
def settingsmenu():
	if xbmcaddon.Addon().getSetting('meta')=='true':
		META = '[B][COLOR lime]ON[/COLOR][/B]'
	else:
		META = '[B][COLOR red]OFF[/COLOR][/B]'
	tools.addDir('Edit Advanced Settings','ADS',10,icon,background,'')
	tools.addDir('META for vod is %s'%META,'META',10,icon,background,META)
	tools.addDir('Log Out','LO',10,icon,background,'')
	

def addonsettings(url,description):
	url  = buildcleanurl(url)
	if   url =="CC":
		tools.clear_cache()
	elif url =="AS":
		xbmc.executebuiltin('Addon.OpenSettings(%s)'%user.id)
	elif url =="ADS":
		dialog = xbmcgui.Dialog().select('Edit Advanced Settings', ['Enable Fire TV Stick AS','Enable Fire TV AS','Enable 1GB Ram or Lower AS','Enable 2GB Ram or Higher AS','Enable Nvidia Shield AS','Disable AS'])
		if dialog==0:
			advancedsettings('stick')
			xbmcgui.Dialog().ok(user.name, 'Set Advanced Settings')
		elif dialog==1:
			advancedsettings('firetv')
			xbmcgui.Dialog().ok(user.name, 'Set Advanced Settings')
		elif dialog==2:
			advancedsettings('lessthan')
			xbmcgui.Dialog().ok(user.name, 'Set Advanced Settings')
		elif dialog==3:
			advancedsettings('morethan')
			xbmcgui.Dialog().ok(user.name, 'Set Advanced Settings')
		elif dialog==4:
			advancedsettings('shield')
			xbmcgui.Dialog().ok(user.name, 'Set Advanced Settings')
		elif dialog==5:
			advancedsettings('remove')
			xbmcgui.Dialog().ok(user.name, 'Advanced Settings Removed')
	elif url =="ADS2":
		dialog = xbmcgui.Dialog().select('Select Your Device Or Closest To', ['Fire TV Stick ','Fire TV','1GB Ram or Lower','2GB Ram or Higher','Nvidia Shield'])
		if dialog==0:
			advancedsettings('stick')
			xbmcgui.Dialog().ok(user.name, 'Set Advanced Settings')
		elif dialog==1:
			advancedsettings('firetv')
			xbmcgui.Dialog().ok(user.name, 'Set Advanced Settings')
		elif dialog==2:
			advancedsettings('lessthan')
			xbmcgui.Dialog().ok(user.name, 'Set Advanced Settings')
		elif dialog==3:
			advancedsettings('morethan')
			xbmcgui.Dialog().ok(user.name, 'Set Advanced Settings')
		elif dialog==4:
			advancedsettings('shield')
			xbmcgui.Dialog().ok(user.name, 'Set Advanced Settings')
	elif url =="tv":
		dialog = xbmcgui.Dialog().yesno(user.name,'Would You like us to Setup the TV Guide for You?')
		if dialog:
			pvrsetup()
			xbmcgui.Dialog().ok(user.name, 'PVR Integration Complete, Restart Kodi For Changes To Take Effect')
	elif url =="ST":
		xbmc.executebuiltin('Runscript("special://home/addons/'+user.id+'/resources/modules/speedtest.py")')
	elif url =="META":
		if 'ON' in description:
			xbmcaddon.Addon().setSetting('meta','false')
			xbmc.executebuiltin('Container.Refresh')
		else:
			xbmcaddon.Addon().setSetting('meta','true')
			xbmc.executebuiltin('Container.Refresh')
	elif url =="US":
		if 'ON' in description:
			xbmcaddon.Addon().setSetting('hideUS','true')
			xbmc.executebuiltin('Container.Refresh')
		else:
			xbmcaddon.Addon().setSetting('hideUS','true')
			xbmc.executebuiltin('Container.Refresh')
	elif url =="XXX":
		if 'ON' in description:
			xbmcaddon.Addon().setSetting('hidexxx','true')
			xbmc.executebuiltin('Container.Refresh')
		else:
			xbmcaddon.Addon().setSetting('hidexxx','true')
			xbmc.executebuiltin('Container.Refresh')		
			
	elif url =="LO":
		xbmcaddon.Addon().setSetting('Username','')
		xbmcaddon.Addon().setSetting('Password','')
		xbmc.executebuiltin('XBMC.ActivateWindow(Videos,addons://sources/video/)')
		xbmc.executebuiltin('Container.Refresh')
	elif url =="UPDATE":
		if 'ON' in description:
			xbmcaddon.Addon().setSetting('update','false')
			xbmc.executebuiltin('Container.Refresh')
		else:
			xbmcaddon.Addon().setSetting('update','true')
			xbmc.executebuiltin('Container.Refresh')
	elif url == "SL":
		from resources.modules import shortlinks
		shortlinks.showlinks()
	
		
def advancedsettings(device):
	if device == 'stick':
		file = open(os.path.join(advanced_settings, 'stick.xml'))
	elif device == 'firetv':
		file = open(os.path.join(advanced_settings, 'firetv.xml'))
	elif device == 'lessthan':
		file = open(os.path.join(advanced_settings, 'lessthan1GB.xml'))
	elif device == 'morethan':
		file = open(os.path.join(advanced_settings, 'morethan1GB.xml'))
	elif device == 'shield':
		file = open(os.path.join(advanced_settings, 'shield.xml'))
	elif device == 'remove':
		os.remove(advanced_settings_target)
	
	try:
		read = file.read()
		f = open(advanced_settings_target, mode='w+')
		f.write(read)
		f.close()
	except:
		pass
		
	
def pvrsetup():
	correctPVR()
	return
		
		
def asettings():
	choice = xbmcgui.Dialog().yesno(user.name, 'Please Select The RAM Size of Your Device', yeslabel='Less than 1GB RAM', nolabel='More than 1GB RAM')
	if choice:
		lessthan()
	else:
		morethan()
	

def morethan():
		file = open(os.path.join(advanced_settings, 'morethan.xml'))
		a = file.read()
		f = open(advanced_settings_target, mode='w+')
		f.write(a)
		f.close()

		
def lessthan():
		file = open(os.path.join(advanced_settings, 'lessthan.xml'))
		a = file.read()
		f = open(advanced_settings_target, mode='w+')
		f.write(a)
		f.close()
		
		
def userpopup():
	kb =xbmc.Keyboard ('', 'heading', True)
	kb.setHeading('Enter Username')
	kb.setHiddenInput(False)
	kb.doModal()
	if (kb.isConfirmed()):
		text = kb.getText()
		return text
	else:
		return False

		
def passpopup():
	kb =xbmc.Keyboard ('', 'heading', True)
	kb.setHeading('Enter Password')
	kb.setHiddenInput(False)
	kb.doModal()
	if (kb.isConfirmed()):
		text = kb.getText()
		return text
	else:
		return False
		
		
def accountinfo():
		open = tools.OPEN_URL(panel_api)
		username   = tools.regex_from_to(open,'"username":"','"')
		password   = tools.regex_from_to(open,'"password":"','"')
		status     = tools.regex_from_to(open,'"status":"','"')
		connects   = tools.regex_from_to(open,'"max_connections":"','"')
		active     = tools.regex_from_to(open,'"active_cons":"','"')
		expiry     = tools.regex_from_to(open,'"exp_date":"','"')
		if not expiry=="":
			expiry     = datetime.datetime.fromtimestamp(int(expiry)).strftime('%d/%m/%Y - %H:%M')
			expreg     = re.compile('^(.*?)/(.*?)/(.*?)$',re.DOTALL).findall(expiry)
			for day,month,year in expreg:
				month     = tools.MonthNumToName(month)
				year      = re.sub(' -.*?$','',year)
				expiry    = month+' '+day+' - '+year
		else:
			expiry = 'Unlimited'
			
		ip        = tools.getlocalip()
		tools.addDir('[B][COLOR white]Username :[/COLOR][/B] '+username,'','',icon,background,'')
		tools.addDir('[B][COLOR white]Password :[/COLOR][/B] '+password,'','',icon,background,'')
		tools.addDir('[B][COLOR white]Expiry Date:[/COLOR][/B] '+expiry,'','',icon,background,'')
		tools.addDir('[B][COLOR white]Account Status :[/COLOR][/B] %s'%status,'','',icon,background,'')
		tools.addDir('[B][COLOR white]Current Connections:[/COLOR][/B] '+ active,'','',icon,background,'')
		tools.addDir('[B][COLOR white]Allowed Connections:[/COLOR][/B] '+connects,'','',icon,background,'')
		tools.addDir('[B][COLOR white]Local IP Address:[/COLOR][/B] '+ip,'','',icon,background,'')
		tools.addDir('[B][COLOR white]Kodi Version:[/COLOR][/B] '+str(KODIV),'','',icon,background,'')
		

		
	
def correctPVR():

	addon         = xbmcaddon.Addon(user.id)
	username_text = addon.getSetting(id='Username')
	password_text = addon.getSetting(id='Password')
	PvrEnable     = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
	jsonSetPVR 	  = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
	IPTVon 	      = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
	nulldemo      = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
	loginurl      = user.host+':'+user.port+"/get.php?username=" + username_text + "&password=" + password_text + "&type=m3u_plus&output=ts"
	EPGurl        = user.host+':'+user.port+"/xmltv.php?username=" + username_text + "&password=" + password_text
	
	xbmc.executeJSONRPC(PvrEnable)
	xbmc.executeJSONRPC(jsonSetPVR)
	xbmc.executeJSONRPC(IPTVon)
	xbmc.executeJSONRPC(nulldemo)
	
	moist = xbmcaddon.Addon('pvr.iptvsimple')
	moist.setSetting(id='m3uUrl', value=loginurl)
	moist.setSetting(id='epgUrl', value=EPGurl)
	moist.setSetting(id='m3uCache', value="false")
	moist.setSetting(id='epgCache', value="false")
	xbmc.executebuiltin("Container.Refresh")

	
def tvguidesetup():
		dialog = xbmcgui.Dialog().yesno(user.name,'Would You like Sorthern IPTV to Setup the TV Guide for You?')
		if dialog:
				pvrsetup()
				xbmcgui.Dialog().ok(user.name, 'You are all done mate! , Restart Kodi For Changes To Take Effect')

def num2day(num):
	if num =="0":
		day = 'monday'
	elif num=="1":
		day = 'tuesday'
	elif num=="2":
		day = 'wednesday'
	elif num=="3":
		day = 'thursday'
	elif num=="4":
		day = 'friday'
	elif num=="5":
		day = 'saturday'
	elif num=="6":
		day = 'sunday'
	return day
	
def extras():
	tools.addDir('Run a Speed Test','ST',10,icon,background,'')
	tools.addDir('Setup PVR Guide','tv',10,icon,background,'')
	tools.addDir('Clear Cache','CC',10,icon,background,'')
	

params=tools.get_params()
url=None
name=None
mode=None
iconimage=None
description=None
query=None
type=None

try:
	url=urllib.unquote_plus(params["url"])
except:
	pass
try:
	name=urllib.unquote_plus(params["name"])
except:
	pass
try:
	iconimage=urllib.unquote_plus(params["iconimage"])
except:
	pass
try:
	mode=int(params["mode"])
except:
	pass
try:
	description=urllib.unquote_plus(params["description"])
except:
	pass
try:
	query=urllib.unquote_plus(params["query"])
except:
	pass
try:
	type=urllib.unquote_plus(params["type"])
except:
	pass

if mode==None or url==None or len(url)<1:
	start()

elif mode==1:
	livecategory(url)
	
elif mode==2:
	Livelist(url)
	
elif mode==3:
	vod(url)
	
elif mode==4:
	stream_video(url)
	
elif mode==5:
	search()
	
elif mode==6:
	accountinfo()
	
elif mode==7:
	tvguide()
	
elif mode==8:
	settingsmenu()
	
elif mode==9:
	xbmc.executebuiltin('ActivateWindow(busydialog)')
	tools.Trailer().play(url) 
	xbmc.executebuiltin('Dialog.Close(busydialog)')
	
elif mode==10:
	addonsettings(url,description)
	
elif mode==11:
	pvrsetup()
	
elif mode==12:
	catchup()

elif mode==13:
	tvarchive(name,description)
	
elif mode==14:
	listcatchup2()
	
elif mode==15:
	ivueint()
	
elif mode==16:
	extras()
	
elif mode==18:
	series_cats(url)

elif mode==25:
	serieslist(url)
	
elif mode==19:
	series_options(url)

elif mode==20:
	season_list(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))