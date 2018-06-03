import requests
import re
import xbmc
import xbmcaddon
from process import Menu

addon_id = 'plugin.video.epiphany'
ADDON = xbmcaddon.Addon(id=addon_id)


def calender(url):
	from datetime import datetime
	today = datetime.now().strftime("%d")
	this_month = datetime.now().strftime("%m")
	this_year = datetime.now().strftime("%y")
	todays_number = (int(this_year)*100)+(int(this_month)*31)+(int(today))
	HTML = requests.get(url).content
	match = re.compile('<span class="dayofmonth">.+?<span class=".+?">(.+?)</span>(.+?)</span>(.+?)</div>',re.DOTALL).findall(HTML)
	for Day_Month,Date,Block in match:
		Date = Date.replace('\n','').replace('  ','').replace('	','')
		Day_Month = Day_Month.replace('\n','').replace('  ','').replace('	','')
		Final_Name = Day_Month.replace(',',' '+Date+' ')
		split_month = Day_Month+'>'
		Month_split = re.compile(', (.+?)>').findall(str(split_month))
		for item in Month_split:
			month_one = item.replace('January','1').replace('February','2').replace('March','3').replace('April','4').replace('May','5').replace('June','6')
			month = month_one.replace('July','7').replace('August','8').replace('September','9').replace('October','10').replace('November','11').replace('December','12')
		show_day = Date.replace('st','').replace('th','').replace('nd','').replace('rd','')
		shows_number = (int(this_year)*100)+(int(month)*31)+(int(show_day))
		if todays_number > shows_number > (todays_number -8):
			Menu(Final_Name,'',22,'','','',Block,'','','','')

def TV_Calender_Prog(extra):
	match = re.compile('<span class="show">.+?<a href=".+?">(.+?)</a>:.+?</span>.+?<a href=".+?" title=".+?">(.+?)</a>',re.DOTALL).findall(str(extra))
	for prog, ep in match:
		ep = ' - Season '+ep.replace('x',' Episode ')
		try:season,episode = re.findall('Season (.+?) Episode (.+?)>',str(ep)+'>')[0]
		except:season='';episode=''
		if ADDON.getSetting('autoplay')=='true':Folder = False
		else: Folder = True
		Menu(prog,'',1,'','','','','',season,episode,prog+ep,Folder=Folder)
