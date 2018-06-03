# -*- coding: utf-8 -*-

"""
    Addon for genrating xml files from TMDB, IMDB, and Trakt list numbers
    Copyright (C) 2018, TonyH

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
#----------------------------------------------------------------


import os
import urlparse
import time
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import requests,re,json
from unidecode import unidecode
import koding
from koding import Add_Dir 
from koding import route, Run


addon_id     = xbmcaddon.Addon().getAddonInfo('id')
dialog       = xbmcgui.Dialog()
home_folder  = xbmc.translatePath('special://home/')
addon_folder = os.path.join(home_folder,'addons')
art_path     = os.path.join(addon_folder,addon_id)
xml_path     = os.path.join(art_path,'xmls')
debug        = koding.Addon_Setting('debug')
tmdb_api_key = koding.Addon_Setting(setting='TMDB_api',addon_id=addon_id)
trakt_client_id = koding.Addon_Setting(setting='Trakt_api',addon_id=addon_id)
trakt_user_name = koding.Addon_Setting(setting='Trakt_user',addon_id=addon_id)
Text_color = koding.Addon_Setting(setting='Text_color',addon_id=addon_id)
bold_value = koding.Addon_Setting(setting='bold_type',addon_id=addon_id)
User_Agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'

@route(mode="main")
def Main_Menu():
    Add_Dir(name='Directions', mode='directions', folder=False, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'))
    Add_Dir(name='Settings', url="", mode='settings', folder=False, icon=os.path.join(art_path,'settings.png'), fanart=os.path.join(art_path,'fanart.jpg'))
    Add_Dir(name='TMDB Lists', url = "", mode='tmdb', folder=False, icon=os.path.join(art_path,'tmdb.png'), fanart=os.path.join(art_path,'fanart.jpg'))
    Add_Dir(name='IMDB Lists', url="", mode='imdb', folder=False, icon=os.path.join(art_path,'imdb.png'), fanart=os.path.join(art_path,'fanart.jpg'))
    Add_Dir(name='Trakt Lists', url="", mode='trakt', folder=False, icon=os.path.join(art_path,'trakt.png'), fanart=os.path.join(art_path,'fanart.jpg'))
    
@route(mode="directions")
def display_directions():
    koding.Text_Box('Directions','1. Open the settings and enter your TMDB api key and, Trakt user name and Client key.\n'
                                 'The TMDB api key is needed for ALL lists.\n'
                                 '2. Click on TMDB, IMDB, or Trakt Lists and you will be promted for a folder name.\n'
                                 'This will create a folder in the addons/xmls/ folder with the name that you chose.\n'
                                 'The xmls will be created in this folder.\n'
                                 '3. Enter your list number or list name in the dialog box.\n'
                                 'Trakt lists require a user name with a matching list name.\n'
                                 'Both are in the url, example: https://trakt.tv/users/tony5856/lists/test-movies.\n'
                                 'The user name goes in the settings, and the list name in the popup dialog box.\n'
                                 '4. The xmls will be created in your specified folder along with a txt file\n'
                                 'called missing_art. This is a list of the movies, tv shows, or episodes that\n'
                                 'did not return any artwork.\n'
                                 '5. Put the xmls on your host or locally and link to them from your main.xml\n'
                                 '6. Tv shows in the generated xml will need a link to the location of\n'
                                 'the seasons xml for that show. The seasons xml will need a link to the location\n'
                                 'of the episodes xml.')

@route(mode="settings")
def open_settings():
    koding.Open_Settings("","",click=True,stop_script=True)

@route(mode="trakt",args=["url"])
def trakt_info(url):
    try:
        folder_name = output_folder()
        list_number3 = koding.Keyboard(heading='Trakt List Name')
        list_name = list_number3.replace(" ","-")
        user = trakt_user_name.replace(" ","-")
        headers = {
            'Content-Type': 'application/json',
            'trakt-api-version': '2',
            'trakt-api-key': trakt_client_id}
        url = "https://api.trakt.tv/users/%s/lists/%s/items/" % (user,list_name)
        count = 0
        dp = xbmcgui.DialogProgress()
        dp.create("[COLOR ghostwhite]Writing XML's....  [/COLOR]")        
        if user == "user-name":
            print "no"
        else:      
            html = requests.get(url,headers=headers).json()
            for res in html:   
                media = res['type']
                length = len(media)
                count = count + 1
                progress(length,count,dp)                 
                if media == 'movie':
                    info = res['movie']
                elif media == 'show':
                    info = res['show']
                year = info['year']
                if not year:
                    year = "none"
                ids = info['ids']
                tmdb = ids['tmdb']
                if not tmdb:
                    tmdb = "none"
                imdb = ids['imdb']
                if not imdb:
                    imdb = "none"
                trakt = ids['trakt']
                name = info['title']
                icon = ""
                fanart = ""
                try:
                    time.sleep(.2)            
                    tmdb_url = 'http://api.themoviedb.org/3/find/' +imdb+ '?api_key=' +tmdb_api_key+ '&external_source=imdb_id'
                    headers = {'User-Agent':User_Agent}
                    tmdbhtml = requests.get(tmdb_url,headers=headers,timeout=20).content
                    match = json.loads(tmdbhtml)
                    #koding.Show_Busy(status=True)
                    movie_results = match['movie_results']
                    tv_results = match['tv_results']
                    if movie_results:
                        media = "movie"
                        res = movie_results
                    elif tv_results:
                        media = "tv"
                        res = tv_results
                    for results in  res:
                        if media == 'movie':
                            icon = results['poster_path']
                            if not icon:
                                key = "thumbnail"
                                show_name = ""
                                missing_art(show_name,name,key,folder_name)
                            date = results['release_date']
                            year = date.split("-")[0]
                            fanart = results['backdrop_path']
                            if not fanart:
                                key = "fanart"
                                show_name = ""
                                missing_art(show_name,name,key,folder_name)
                            tmdb = results['id']
                        elif media == 'tv':
                            icon = results['poster_path']
                            date = results['first_air_date']
                            year = date.split("-")[0]
                            fanart = results['backdrop_path']
                            tmdb = results['id']
                            get_tv_seasons(tmdb,fanart,imdb,folder_name)                                   
                except:
                    icon = "none"
                    fanart = "none"
                print_movie_xml(list_name,media,name,year,imdb,tmdb,icon,fanart,folder_name)

        #koding.Show_Busy(status=False)                                     
    except:
        pass

@route(mode="imdb",args=["url"])
def imdb_info(url):
    try:
        folder_name = output_folder()    
        # folder_name = koding.Keyboard(heading='Output Folder Name')
        # folder_name = folder_name.replace(" ","_")
        #xml_folder = os.path.join(xml_path,folder_name)
        # os.mkdir( xml_folder, 0755 )
        list_number2 = koding.Keyboard(heading='IMDB List Number')
        list_number2 = list_number2.replace("ls","")
        url = "http://www.imdb.com/list/ls%s/" % int(list_number2)
        html = requests.get(url).content
        match2 = re.compile('<h1 class="header list-name">(.+?)</h1>',re.DOTALL).findall(html)       
        list_name = match2[0]
        list_name = clean_search(list_name)
        list_name = list_name.replace(" ", "_")
        #koding.Show_Busy(status=True)
        (url,html) = Pull_info(html,list_name,url,folder_name)
        print "pass1"
    except:
        pass
    try:
        match3 = re.compile('<a class="flat-button lister-page-next next-page" href="(.+?)"',re.DOTALL).findall(html)
        url = "http://www.imdb.com"+match3[0]
        html = requests.get(url).content
        (url,html) = Pull_info(html,list_name,url,folder_name)
        print "pass2"
    except:
        pass
    try:
        match3 = re.compile('<a class="flat-button lister-page-next next-page" href="(.+?)"',re.DOTALL).findall(html)
        url = "http://www.imdb.com"+match3[0]
        html = requests.get(url).content
        (url,html) = Pull_info(html,list_name,url,folder_name)
        print "pass3"
    except:
        pass
    try:
        match3 = re.compile('<a class="flat-button lister-page-next next-page" href="(.+?)"',re.DOTALL).findall(html)
        url = "http://www.imdb.com"+match3[0]
        html = requests.get(url).content
        (url,html) = Pull_info(html,list_name,url,folder_name)
        print "pass4"
    except:
        pass
    try:
        match3 = re.compile('<a class="flat-button lister-page-next next-page" href="(.+?)"',re.DOTALL).findall(html)
        url = "http://www.imdb.com"+match3[0]
        html = requests.get(url).content
        (url,html) = Pull_info(html,list_name,url,folder_name)
        print "pass5"
    except:
        pass
    try:
        match3 = re.compile('<a class="flat-button lister-page-next next-page" href="(.+?)"',re.DOTALL).findall(html)
        url = "http://www.imdb.com"+match3[0]
        html = requests.get(url).content
        (url,html) = Pull_info(html,list_name,url,folder_name)
        print "pass6"
    except:
        pass
    try:
        match3 = re.compile('<a class="flat-button lister-page-next next-page" href="(.+?)"',re.DOTALL).findall(html)
        url = "http://www.imdb.com"+match3[0]
        html = requests.get(url).content
        (url,html) = Pull_info(html,list_name,url,folder_name)
        print "pass7"
    except:
        pass
    try:
        match3 = re.compile('<a class="flat-button lister-page-next next-page" href="(.+?)"',re.DOTALL).findall(html)
        url = "http://www.imdb.com"+match3[0]
        html = requests.get(url).content
        (url,html) = Pull_info(html,list_name,url,folder_name)
        print "pass8"
    except:
        pass
    #koding.Show_Busy(status=False)

def Pull_info(html,list_name,url,folder_name):
    xml_folder = os.path.join(xml_path,folder_name)
    File = os.path.join(xml_folder,list_name)
    #File = File.replace(" ", "_")
    open('%s.xml'%(File),'a')   
    block = re.compile('<div class="lister-list">(.+?)<div class="row text-center lister-working hidden"></div>',re.DOTALL).findall(html)
    match = re.compile('<img alt="(.+?)".+?data-tconst="(.+?)".+?<span class="lister-item-year text-muted unbold">(.+?)</span>',re.DOTALL).findall(str(block))
    length = len(match)
    count = 0
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR ghostwhite]Writing XML's....  [/COLOR]")    
    for name, imdb, year in match:
        icon = ""
        fanart = ""
        count = count + 1
        progress(length,count,dp)        
        try:
            time.sleep(.2)           
            tmdb_url = 'http://api.themoviedb.org/3/find/' +imdb+ '?api_key=' +tmdb_api_key+ '&external_source=imdb_id'
            name = clean_search(name)
            name = remove_non_ascii(name)
            headers = {'User-Agent':User_Agent}
            tmdbhtml = requests.get(tmdb_url,headers=headers,timeout=20).content
            match = json.loads(tmdbhtml)
            movie_results = match['movie_results']
            tv_results = match['tv_results']
            if movie_results:
                media = "movie"
                res = movie_results
            elif tv_results:
                media = "tv"
                res = tv_results
            for results in  res:
                if media == 'movie':
                    icon = results['poster_path']
                    if not icon:
                        icon = ""
                        key = "thumbnail"
                        show_name = ""
                        missing_art(show_name,name,key,folder_name)
                    date = results['release_date']
                    year = date.split("-")[0]
                    fanart = results['backdrop_path']
                    if not fanart:
                        fanrt = ""
                        key = "fanart"
                        show_name = ""
                        missing_art(show_name,name,key,folder_name)
                    tmdb = results['id']
                    if not tmdb:
                        tmdb = "none"
                elif media == 'tv':
                    icon = results['poster_path']
                    if not icon:
                        icon = ""
                        key = "thumbnail"
                        show_name = ""
                        missing_art(show_name,name,key,folder_name)                    
                    date = results['first_air_date']
                    year = date.split("-")[0]
                    fanart = results['backdrop_path']
                    if not fanart:
                        fanart = ""
                        key = "fanart"
                        show_name = ""
                        missing_art(show_name,name,key,folder_name)                    
                    tmdb = results['id']
                    if not tmdb:
                        tmdb = "none"
                    get_tv_seasons(tmdb,fanart,imdb,folder_name)                                   
        except:
            icon = ""
            fanart = ""

        print_movie_xml(list_name,media,name,year,imdb,tmdb,icon,fanart,folder_name)

    return url,html

@route(mode="tmdb",args=["url"])
def Tmdb_info(url):
    folder_name = output_folder()
    xml_folder = os.path.join(xml_path,folder_name)
    list_number = koding.Keyboard(heading='TMDB List Number')
    start_url = "https://api.themoviedb.org/3/list/%s?api_key=%s&language=en-US"% (int(list_number) ,tmdb_api_key)
    html = requests.get(start_url).content
    match = json.loads(html)
    list_name = match['name']
    list_name = list_name.replace(" ", "_")
    list_name = clean_search(list_name)
    #koding.Show_Busy(status=True)
    if not list_name:
        list_name = match['description']
    res = match['items']
    if not res:
        res = match['results']
    xml_folder = os.path.join(xml_path,folder_name)       
    File = os.path.join(xml_folder,list_name)
    length = len(res)
    count = 0
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR ghostwhite]Writing XML's....  [/COLOR]")       
    open('%s.xml'%(File),'w')
    for results in res:
        count = count + 1
        progress(length,count,dp)         
        media = results['media_type']
        if media == 'movie':
            icon = results['poster_path']
            if not icon:
                icon = ""
                key = "thumbnail"
                show_name = ""
                missing_art(show_name,name,key,folder_name)
            name = results['title']
            date = results['release_date']
            year = date.split("-")[0]
            fanart = results['backdrop_path']
            if not fanart:
                fanart = ""
                key = "fanart"
                show_name = ""
                missing_art(show_name,name,key,folder_name)
            tmdb = results['id']
            url2 = "https://api.themoviedb.org/3/movie/%s/external_ids?api_key=%s"% (tmdb, tmdb_api_key)
            html2 = requests.get(url2).content
            match2 = json.loads(html2)
            try:                
                imdb = match2['imdb_id']
            except:
                imdb = "none"

        elif media == 'tv':
            icon = results['poster_path']
            if not icon:
                icon = ""
                key = "thumbnail"
                show_name = ""
                missing_art(show_name,name,key,folder_name)
            name = results['name']
            date = results['first_air_date']
            year = date.split("-")[0]
            fanart = results['backdrop_path']
            if not fanart:
                fanart = ""
                key = "fanart"
                show_name = ""
                missing_art(show_name,name,key,folder_name)
            tmdb = results['id']
            url2 = "https://api.themoviedb.org/3/movie/%s/external_ids?api_key=%s"% (tmdb, tmdb_api_key)
            html2 = requests.get(url2).content
            match2 = json.loads(html2)
            try:                
                imdb = match2['imdb_id']
            except:
                imdb = "none"       
            get_tv_seasons(tmdb,fanart,imdb,folder_name)
        print_movie_xml(list_name,media,name,year,imdb,tmdb,icon,fanart,folder_name)
    #koding.Show_Busy(status=False)
 
def print_movie_xml(list_name,media,name,year,imdb,tmdb,icon,fanart,folder_name):
    try:       
        if media == "movie":
            name = remove_non_ascii(name)
            xml_folder = os.path.join(xml_path,folder_name)
            File = os.path.join(xml_folder,list_name)
            #File = File.replace(" ","_")      
            f = open('%s.xml'%(File),'a')
            f.write('<item>\n')
            if bold_value == "true":
                f.write('\t<title>[B][COLOR=%s]%s[/COLOR][/B]</title>\n' % (Text_color,name))
            else:    
                f.write('\t<title>[COLOR=%s]%s[/COLOR]</title>\n' % (Text_color,name))
            f.write('\t<meta>\n')
            f.write('\t<imdb>%s</imdb>\n' % imdb)
            f.write('\t<content>%s</content>\n' % media)
            f.write('\t<title>%s</title>\n' % (name))
            f.write('\t<year>%s</year>\n' % year)
            f.write('\t</meta>\n')
            f.write('\t<link>\n')
            f.write('\t<sublink>%s</sublink>\n' % "search")
            f.write('\t<sublink>%s</sublink>\n' % "searchsd")
            f.write('\t</link>\n')
            f.write('\t<thumbnail>https://image.tmdb.org/t/p/w1280%s</thumbnail>\n' % icon)
            f.write('\t<fanart>https://image.tmdb.org/t/p/w1280%s</fanart>\n' % fanart)
            f.write('</item>\n')
            f.close()   
        elif media == "tv":
            name = remove_non_ascii(name)
            xml_folder = os.path.join(xml_path,folder_name)
            File = os.path.join(xml_folder,list_name)
            #File = File.replace(" ","_")
            f = open('%s.xml'%(File),'a')
            f.write('<dir>\n')
            if bold_value == "true":
                f.write('\t<title>[B][COLOR=%s]%s[/COLOR][/B]</title>\n' % (Text_color,name))
            else:
                f.write('\t<title>[COLOR=%s]%s[/COLOR]</title>\n' % (Text_color,name))
            f.write('\t<meta>\n')
            f.write('\t<imdb>%s</imdb>\n' % imdb)
            f.write('\t<content>%s</content>\n' % media)
            f.write('\t<title>%s</title>\n' % (name))
            f.write('\t<year>%s</year>\n' % year)
            f.write('\t</meta>\n')
            f.write('\t<link></link>\n')
            f.write('\t<thumbnail>https://image.tmdb.org/t/p/w1280%s</thumbnail>\n' % icon)
            f.write('\t<fanart>https://image.tmdb.org/t/p/w1280%s</fanart>\n' % fanart)
            f.write('</dir>\n')
            f.close()
    except:
        pass
    
def get_tv_seasons(tmdb,fanart,imdb,folder_name):
    try:      
        url = "https://api.themoviedb.org/3/tv/%s?api_key=%s&language=en-US"% (tmdb,tmdb_api_key)
        html = requests.get(url).content
        match = json.loads(html)
        seas = match['seasons']
        show_name = match['original_name']
        show_name = show_name.replace(":","")
        show_name = clean_search(show_name)
        xml_folder = os.path.join(xml_path,folder_name)
        File_show = os.path.join(xml_folder,show_name)
        #File_show = File_show.replace(" ","_")
        open('%s.xml'%(File_show),'w')
        for seasons in seas:   
            sea_name = seasons['name']
            date = seasons['air_date']
            if not date:
                year = ""            
            else:
                year = date.split("-")[0]
            icon = seasons['poster_path']
            if not 'poster_path':
                key = "thumbnail"
                missing_art(show_name,sea_name,key,folder_name)
                icon = ""
            sea_num = seasons['season_number']
            if not sea_num:
                sea_num = ""
            get_episodes(tmdb,sea_num,fanart,sea_name,show_name,imdb,folder_name)    
            print_seasons_xml(show_name,sea_name,year,fanart,icon,imdb,sea_num,folder_name)

    except:
        pass
    
def print_seasons_xml(show_name,sea_name,year,fanart,icon,imdb,sea_num,folder_name):
    try:
        xml_folder = os.path.join(xml_path,folder_name)
        File_show = os.path.join(xml_folder,show_name)
        #File_show = File_show.replace(" ","_")
        f = open('%s.xml'%(File_show),'a')
        f.write('<dir>\n')
        if bold_value == "true":
            f.write('\t<title>[B][COLOR=%s]%s[/COLOR][/B]</title>\n' % (Text_color,sea_name))
        else:
            f.write('\t<title>[COLOR=%s]%s[/COLOR]</title>\n' % (Text_color,sea_name))
        f.write('\t<meta>\n')
        f.write('\t<imdb>%s</imdb>\n' % imdb)
        f.write('\t<content>season</content>\n')
        f.write('\t<season>%s</season>\n' % (sea_num))
        f.write('\t<year>%s</year>\n' % year)
        f.write('\t</meta>\n')
        f.write('\t<link></link>\n')
        f.write('\t<thumbnail>https://image.tmdb.org/t/p/w1280%s</thumbnail>\n' % icon)
        f.write('\t<fanart>https://image.tmdb.org/t/p/w1280%s</fanart>\n' % fanart)
        f.write('</dir>\n')
        f.close()   
    except:
        pass
    
def get_episodes(tmdb,sea_num,fanart,sea_name,show_name,imdb,folder_name):
    try:
        
        url = "https://api.themoviedb.org/3/tv/%s/season/%s?api_key=%s&language=en-US"% (tmdb,sea_num, tmdb_api_key)
        html = requests.get(url).content
        match = json.loads(html)
        episodes = match['episodes']
        Episodes = show_name+"_"+sea_name
        xml_folder = os.path.join(xml_path,folder_name)
        File_episode = os.path.join(xml_folder,Episodes)
        #File_episode= File_episode.replace(" ","_")
        f = open('%s.xml'%(File_episode),'w')
        for epi in episodes:
            name = epi['name']
            episode_num = epi['episode_number']
            season_num = epi['season_number']
            icon = epi['still_path']
            if not icon:
                key = "thumbnail"
                missing_art(show_name,name,key,folder_name)
                icon = ""
            date = epi['air_date']
            if not date:
                year = ""            
            else:
                year = date.split("-")[0]
            print_episodes_xml(show_name,sea_name,fanart,name,season_num,episode_num,icon,year,imdb,folder_name)
    except:
        pass
    
def print_episodes_xml(show_name,sea_name,fanart,name,season_num,episode_num,icon,year,imdb,folder_name):
    try:        
        Episodes = show_name+"_"+sea_name
        xml_folder = os.path.join(xml_path,folder_name)
        File_episode = os.path.join(xml_folder,Episodes)
        #File_episode= File_episode.replace(" ","_")
        f = open('%s.xml'%(File_episode),'a')
        f.write('<item>\n')
        if bold_value == "true":
            f.write('\t<title>[B][COLOR=%s]%s[/COLOR][/B]</title>\n' % (Text_color,name))
        else:
            f.write('\t<title>[COLOR=%s]%s[/COLOR]</title>\n' % (Text_color,name))
        f.write('\t<meta>\n')
        f.write('\t<imdb>%s</imdb>\n' % imdb)
        f.write('\t<content>episode</content>\n')
        f.write('\t<tvshowtitle>%s</tvshowtitle>\n' % (show_name))
        f.write('\t<year>%s</year>\n' % year)
        f.write('\t<season>%s</season>\n' % (season_num))
        f.write('\t<episode>%s</episode>\n' % (episode_num))
        f.write('\t</meta>\n')
        f.write('\t<link>\n')
        f.write('\t<sublink>search</sublink>\n')
        f.write('\t<sublink>searchsd</sublink>\n')
        f.write('\t</link>\n')
        f.write('\t<thumbnail>https://image.tmdb.org/t/p/w1280%s</thumbnail>\n' % icon)
        f.write('\t<fanart>https://image.tmdb.org/t/p/w1280%s</fanart>\n' % fanart)
        f.write('</item>\n')
        f.close()
    except:
        pass
    
def clean_search(title):
    if title == None: return
    title = re.sub('&#(\d+);', '', title)
    title = re.sub('(&#[0-9]+)([^;^0-9]+)', '\\1;\\2', title)
    title = title.replace('&quot;', '\"').replace('&amp;', '&')
    title = re.sub('\\\|/|\(|\)|\[|\]|\{|\}|-|:|;|\*|\?|"|\'|<|>|\_|\.|\?', ' ', title)
    title = title.replace(":", "")
    title = title.replace("xc2","")
    title = title.replace("xb7","")
    title = title.replace("\\","")    
    title = ' '.join(title.split())
    return title    

def missing_art(show_name,name,key,folder_name):
    missing_art = 'missing_art'
    xml_folder = os.path.join(xml_path,folder_name)
    File_missing_art = os.path.join(xml_folder,missing_art)
    f = open('%s.txt'%(File_missing_art), 'a')
    if show_name == "":
        f.write('Movie : '+name+' - missing - '+key+'\n')
    else:
        f.write('TV Show : '+show_name+' : '+name+' - missing - '+key+'\n')
    f.close()

def remove_non_ascii(text):
    return unidecode(text)

def output_folder():
    folder_name = koding.Keyboard(heading='Output Folder Name')
    folder_name = folder_name.replace(" ","_")
    xml_folder = os.path.join(xml_path,folder_name)
    if os.path.exists(xml_folder):
         koding.Notify(title='Folder Already Exists', message='Choose a different folder', duration=5000)
         xml_folder = output_folder()
    else:
        os.mkdir( xml_folder, 0755 )
        return folder_name    

def progress(length,count,dp):
    try:
        percent = (count * 100) / length
        if dp.iscanceled():
            raise Exception("Cancelled")
            dp.close()
        else:
            dp.update(percent,"%s of %s written"% (count,length))
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled():
        raise Exception("Canceled")
        dp.close() 

if __name__ == "__main__":
    Run(default='main')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))