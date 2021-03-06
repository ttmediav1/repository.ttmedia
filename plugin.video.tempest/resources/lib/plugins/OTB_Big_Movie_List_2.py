
# -*- coding: utf-8 -*-
"""
    OTB Big Movie List.py
    Copyright (C) 2018, Team OTB
    Version 2.0.0

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

    -------------------------------------------------------------

    Usage Examples:

    Search the OTB Big Movie List

    <dir>
    <title>Search OTB Big Movie List Movies</title>
    <bml>search</bml>
    </dir>

    Returns the OTB Big Movie list

    <dir>
    <title>OTB Big Movie List</title>
    <bml>open</bml>
    </dir>


    Returns the OTB Big Movie list with metadata

    <dir>
    <title>OTB Big Movie List</title>
    <bml>movie_meta</bml>
    </dir>

    ---------------------

    Possible Genre's are:
    Action
    Adventure
    Comedy
    Documentary
    Drama
    Family
    Horror
    Kids
    Romance
    SciFi
    Standup Comedy
    Thriller
    War
    Western

    -----------------------

    Genre tag examples

    <dir>
    <title>OTB Action Movies</title>
    <bml>genre/Action</bml>
    </dir>

    <dir>
    <title>OTB Comedy Movies</title>
    <bml>genre/Comedy</bml>
    </dir>    


    Gener tag with metadata

    <dir>
    <title>OTB Action Movies</title>
    <bml>genre_meta/Action</bml>
    </dir>
    --------------------------------------------------------------

"""


import requests,re,os,xbmc,xbmcaddon
import base64,pickle,koding,time,sqlite3
from koding import route
from ..plugin import Plugin
from resources.lib.util.context import get_context_items
from resources.lib.util.xml import JenItem, JenList, display_list, display_data, clean_url
from resources.lib.external.airtable.airtable import Airtable
from unidecode import unidecode

CACHE_TIME = 86400  # change to wanted cache time in seconds

addon_id = xbmcaddon.Addon().getAddonInfo('id')
addon_fanart = xbmcaddon.Addon().getAddonInfo('fanart')
addon_icon = xbmcaddon.Addon().getAddonInfo('icon')
AddonName = xbmc.getInfoLabel('Container.PluginName')
home_folder = xbmc.translatePath('special://home/')
user_data_folder = os.path.join(home_folder, 'userdata')
addon_data_folder = os.path.join(user_data_folder, 'addon_data')
database_path = os.path.join(addon_data_folder, addon_id)
database_loc = os.path.join(database_path, 'database.db')


class OTB_Big_Movie_List(Plugin):
    name = "OTB_big_movie_list"  

    def process_item(self, item_xml):
        if "<bml>" in item_xml:
            item = JenItem(item_xml)
            if "open" in item.get("bml", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "open_bml_movies2",
                    'url': item.get("bml", ""),
                    'folder': True,
                    'imdb': "0",
                    'season': "0",
                    'episode': "0",
                    'info': {},
                    'year': "0",
                    'context': get_context_items(item),
                    "summary": item.get("summary", None)
                }
                result_item["properties"] = {
                    'fanart_image': result_item["fanart"]
                }
                result_item['fanart_small'] = result_item["fanart"]
                return result_item              
            elif "genre" in item.get("bml", ""):    
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "open_action_movies2",
                    'url': item.get("bml", ""),
                    'folder': True,
                    'imdb': "0",
                    'season': "0",
                    'episode': "0",
                    'info': {},
                    'year': "0",
                    'context': get_context_items(item),
                    "summary": item.get("summary", None)
                }
                result_item["properties"] = {
                    'fanart_image': result_item["fanart"]
                }
                result_item['fanart_small'] = result_item["fanart"]
                return result_item 
            elif "movie_meta" in item.get("bml", ""):   
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "open_movie_meta_movies2",
                    'url': item.get("bml", ""),
                    'folder': True,
                    'imdb': "0",
                    'season': "0",
                    'episode': "0",
                    'info': {},
                    'year': "0",
                    'context': get_context_items(item),
                    "summary": item.get("summary", None)
                }
                result_item["properties"] = {
                    'fanart_image': result_item["fanart"]
                }
                result_item['fanart_small'] = result_item["fanart"]
                return result_item 
            elif "genre_meta" in item.get("bml", ""):    
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "open_genre_meta_movies2",
                    'url': item.get("bml", ""),
                    'folder': True,
                    'imdb': "0",
                    'season': "0",
                    'episode': "0",
                    'info': {},
                    'year': "0",
                    'context': get_context_items(item),
                    "summary": item.get("summary", None)
                }
                result_item["properties"] = {
                    'fanart_image': result_item["fanart"]
                }
                result_item['fanart_small'] = result_item["fanart"]
                return result_item 
            elif "search" in item.get("bml", ""):   
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "open_bml_search",
                    'url': item.get("bml", ""),
                    'folder': True,
                    'imdb': "0",
                    'season': "0",
                    'episode': "0",
                    'info': {},
                    'year': "0",
                    'context': get_context_items(item),
                    "summary": item.get("summary", None)
                }
                result_item["properties"] = {
                    'fanart_image': result_item["fanart"]
                }
                result_item['fanart_small'] = result_item["fanart"]
                return result_item                                 

def display_xml(name,trailer,summary,thumbnail,fanart,link_a,link_b,link_c,link_d,link_e):
    xml = ""
    if link_b == "-":
        xml += "<item>"\
             "<title>%s</title>"\
             "<meta>"\
             "<content>movie</content>"\
             "<imdb></imdb>"\
             "<title></title>"\
             "<year></year>"\
             "<thumbnail>%s</thumbnail>"\
             "<fanart>%s</fanart>"\
             "<summary>%s</summary>"\
             "</meta>"\
             "<link>"\
             "<sublink>%s</sublink>"\
             "<sublink>%s(Trailer)</sublink>"\
             "</link>"\
             "</item>" % (name,thumbnail,fanart,summary,link_a,trailer)
    elif link_c == "-":
        xml += "<item>"\
             "<title>%s</title>"\
             "<meta>"\
             "<content>movie</content>"\
             "<imdb></imdb>"\
             "<title></title>"\
             "<year></year>"\
             "<thumbnail>%s</thumbnail>"\
             "<fanart>%s</fanart>"\
             "<summary>%s</summary>"\
             "</meta>"\
             "<link>"\
             "<sublink>%s</sublink>"\
             "<sublink>%s</sublink>"\
             "<sublink>%s(Trailer)</sublink>"\
             "</link>"\
             "</item>" % (name,thumbnail,fanart,summary,link_a,link_b,trailer) 
    elif link_d == "-":
        xml += "<item>"\
             "<title>%s</title>"\
             "<meta>"\
             "<content>movie</content>"\
             "<imdb></imdb>"\
             "<title></title>"\
             "<year></year>"\
             "<thumbnail>%s</thumbnail>"\
             "<fanart>%s</fanart>"\
             "<summary>%s</summary>"\
             "</meta>"\
             "<link>"\
             "<sublink>%s</sublink>"\
             "<sublink>%s</sublink>"\
             "<sublink>%s</sublink>"\
             "<sublink>%s(Trailer)</sublink>"\
             "</link>"\
             "</item>" % (name,thumbnail,fanart,summary,link_a,link_b,link_c,trailer)
    elif link_e == "-":
        xml += "<item>"\
             "<title>%s</title>"\
             "<meta>"\
             "<content>movie</content>"\
             "<imdb></imdb>"\
             "<title></title>"\
             "<year></year>"\
             "<thumbnail>%s</thumbnail>"\
             "<fanart>%s</fanart>"\
             "<summary>%s</summary>"\
             "</meta>"\
             "<link>"\
             "<sublink>%s</sublink>"\
             "<sublink>%s</sublink>"\
             "<sublink>%s</sublink>"\
             "<sublink>%s</sublink>"\
             "<sublink>%s(Trailer)</sublink>"\
             "</link>"\
             "</item>" % (name,thumbnail,fanart,summary,link_a,link_b,link_c,link_d,trailer)
    else:
        xml += "<item>"\
             "<title>%s</title>"\
             "<meta>"\
             "<content>movie</content>"\
             "<imdb></imdb>"\
             "<title></title>"\
             "<year></year>"\
             "<thumbnail>%s</thumbnail>"\
             "<fanart>%s</fanart>"\
             "<summary>%s</summary>"\
             "</meta>"\
             "<link>"\
             "<sublink>%s</sublink>"\
             "<sublink>%s</sublink>"\
             "<sublink>%s</sublink>"\
             "<sublink>%s</sublink>"\
             "<sublink>%s</sublink>"\
             "<sublink>%s(Trailer)</sublink>"\
             "</link>"\
             "</item>" % (name,thumbnail,fanart,summary,link_a,link_b,link_c,link_d,link_e,trailer)
    return (xml)

@route(mode='open_bml_movies2')
def open_movies():
    xml = ""
    pins = "PLuginbmlopen"
    Items = fetch_from_db2(pins)
    if Items:
        display_data(Items)  
    else:    
        at = Airtable('app1aK3wfaR0xDxSK', 'OTB Big Movie List', api_key='keyikW1exArRfNAWj')
        match = at.get_all(maxRecords=1200, sort=['name'])
        for field in match:
            try:
                res = field['fields']   
                name = res['name']
                name = remove_non_ascii(name)
                trailer = res['trailer']
                summary = res['summary']
                summary = remove_non_ascii(summary)
                thumbnail = res['thumbnail']
                fanart = res['fanart']
                link_a = res['link_a']
                link_b = res['link_b']
                link_c = res['link_c']
                link_d = res['link_d']  
                link_e = res['link_e']
                xml += display_xml(name,trailer,summary,thumbnail,fanart,link_a,link_b,link_c,link_d,link_e)                    
            except:
                pass    
        at2 = Airtable('appaVv9EN3EJnvUz4', 'OTB Big Movie List 2', api_key='keyikW1exArRfNAWj')
        match2 = at2.get_all(maxRecords=1200, sort=['name'])      
        for field2 in match2:
            try:
                res = field2['fields']   
                name = res['name']
                name = remove_non_ascii(name)
                trailer = res['trailer']
                summary = res['summary']
                summary = remove_non_ascii(summary)
                thumbnail = res['thumbnail']
                fanart = res['fanart']
                link_a = res['link_a']
                link_b = res['link_b']
                link_c = res['link_c']
                link_d = res['link_d']
                link_e = res['link_e']
                xml += display_xml(name,trailer,summary,thumbnail,fanart,link_a,link_b,link_c,link_d,link_e)      
            except:
                pass                                                                                 
        jenlist = JenList(xml)
        display_list(jenlist.get_list(), jenlist.get_content_type(), pins)

        

@route(mode='open_action_movies2',args=["url"])
def open_action_movies(url):
    xml = ""
    pins = "PLuginbml"+url
    Items = fetch_from_db2(pins)
    if Items: 
        display_data(Items) 
    else:       
        genre = url.split("/")[-1]
        at = Airtable('app1aK3wfaR0xDxSK', 'OTB Big Movie List', api_key='keyikW1exArRfNAWj')
        try:
            match = at.search('type', genre, sort=['name'])
            for field in match:
                res = field['fields']   
                name = res['name']
                name = remove_non_ascii(name)
                trailer = res['trailer']
                summary = res['summary']
                summary = remove_non_ascii(summary)
                thumbnail = res['thumbnail']
                fanart = res['fanart']
                link_a = res['link_a']
                link_b = res['link_b']
                link_c = res['link_c']
                link_d = res['link_d']
                link_e = res['link_e']
                xml += display_xml(name,trailer,summary,thumbnail,fanart,link_a,link_b,link_c,link_d,link_e)                   
        except:
            pass 
        at2 = Airtable('appaVv9EN3EJnvUz4', 'OTB Big Movie List 2', api_key='keyikW1exArRfNAWj')
        try:
            match2 = at2.search('type', genre, sort=['name'])
            for field2 in match2:
                res = field2['fields']   
                name = res['name']
                name = remove_non_ascii(name)
                trailer = res['trailer']
                summary = res['summary']
                summary = remove_non_ascii(summary)
                thumbnail = res['thumbnail']
                fanart = res['fanart']
                link_a = res['link_a']
                link_b = res['link_b']
                link_c = res['link_c']
                link_d = res['link_d']
                link_e = res['link_e']
                xml += display_xml(name,trailer,summary,thumbnail,fanart,link_a,link_b,link_c,link_d,link_e)                  
        except:
            pass                                 
        jenlist = JenList(xml)
        display_list(jenlist.get_list(), jenlist.get_content_type(), pins)

@route(mode='open_movie_meta_movies2',args=["url"])
def open_movie_meta_movies(url):
    xml = ""
    pins = "PLuginbmlopenmeta"
    Items = fetch_from_db2(pins)
    if Items: 
        display_data(Items) 
    else:                               
        at = Airtable('app1aK3wfaR0xDxSK', 'OTB Big Movie List', api_key='keyikW1exArRfNAWj')
        match = at.get_all(maxRecords=1200, sort=['name'])  
        for field in match:
            try:
                res = field['fields']   
                name = res['name']
                name = remove_non_ascii(name)
                trailer = res['trailer']
                summary = res['summary']
                summary = remove_non_ascii(summary)
                thumbnail = res['thumbnail']
                fanart = res['fanart']
                link_a = res['link_a']
                link_b = res['link_b']
                link_c = res['link_c']
                link_d = res['link_d']
                link_e = res['link_e']
                xml += display_xml(name,trailer,summary,thumbnail,fanart,link_a,link_b,link_c,link_d,link_e)
            except:
                pass
        at2 = Airtable('appaVv9EN3EJnvUz4', 'OTB Big Movie List 2', api_key='keyikW1exArRfNAWj')
        match2 = at2.get_all(maxRecords=1200, sort=['name'])  
        for field2 in match2:
            try:
                res = field2['fields']   
                name = res['name']
                name = remove_non_ascii(name)
                trailer = res['trailer']
                summary = res['summary']
                summary = remove_non_ascii(summary)
                thumbnail = res['thumbnail']
                fanart = res['fanart']
                link_a = res['link_a']
                link_b = res['link_b']
                link_c = res['link_c']
                link_d = res['link_d']
                link_e = res['link_e']
                xml += display_xml(name,trailer,summary,thumbnail,fanart,link_a,link_b,link_c,link_d,link_e)
            except:
                pass                       
        jenlist = JenList(xml)
        display_list(jenlist.get_list(), jenlist.get_content_type(), pins)

@route(mode='open_genre_meta_movies2',args=["url"])
def open_genre_meta_movies(url):
    xml = ""
    pins = "PLuginbmlmeta"+url
    Items = fetch_from_db2(pins)
    if Items: 
        display_data(Items) 
    else:     
        genre = url.split("/")[-1]
        at = Airtable('app1aK3wfaR0xDxSK', 'OTB Big Movie List', api_key='keyikW1exArRfNAWj')
        try:
            match = at.search('type', genre)
            for field in match:
                res = field['fields']   
                name = res['name']
                name = remove_non_ascii(name)
                trailer = res['trailer']
                summary = res['summary']
                summary = remove_non_ascii(summary)
                thumbnail = res['thumbnail']
                fanart = res['fanart']
                link_a = res['link_a']
                link_b = res['link_b']
                link_c = res['link_c']
                link_d = res['link_d']
                link_e = res['link_e']
                xml += display_xml(name,trailer,summary,thumbnail,fanart,link_a,link_b,link_c,link_d,link_e)                  
        except:
            pass
        at2 = Airtable('appaVv9EN3EJnvUz4', 'OTB Big Movie List 2', api_key='keyikW1exArRfNAWj')
        try:
            match2 = at2.search('type', genre)
            for field2 in match2:
                res = field2['fields']   
                name = res['name']
                name = remove_non_ascii(name)
                trailer = res['trailer']
                summary = res['summary']
                summary = remove_non_ascii(summary)
                thumbnail = res['thumbnail']
                fanart = res['fanart']
                link_a = res['link_a']
                link_b = res['link_b']
                link_c = res['link_c']
                link_d = res['link_d']
                link_e = res['link_e']
                xml += display_xml(name,trailer,summary,thumbnail,fanart,link_a,link_b,link_c,link_d,link_e)                   
        except:
            pass                          
        jenlist = JenList(xml)
        display_list(jenlist.get_list(), jenlist.get_content_type(), pins)

@route(mode='open_bml_search',args=["url"])
def open_bml_search(url):
    pins = ""
    xml = ""
    show = koding.Keyboard(heading='Movie Name')
    movie_list = []
    at = Airtable('app1aK3wfaR0xDxSK', 'OTB Big Movie List', api_key='keyikW1exArRfNAWj')
    match = at.get_all(maxRecords=1200, sort=['name'])
    for field in match:
        res = field['fields']        
        name = res['name']
        movie_list.append(name)
    at3 = Airtable('appaVv9EN3EJnvUz4', 'OTB Big Movie List 2', api_key='keyikW1exArRfNAWj')
    match3 = at3.get_all(maxRecords=1200, sort=['name'])  
    for field3 in match3:       
        res3 = field3['fields']        
        name3 = res3['name']
        movie_list.append(name3)                         
    search_result = koding.Fuzzy_Search(show, movie_list)
    if not search_result:
        xbmc.log("--------no results--------",level=xbmc.LOGNOTICE)
        xml += "<item>"\
            "<title>[COLOR=orange][B]Movie was not found[/B][/COLOR]</title>"\
            "</item>"
        jenlist = JenList(xml)
        display_list(jenlist.get_list(), jenlist.get_content_type(), pins)    
    for item in search_result:
        item2 = str(item)
        item2 = remove_non_ascii(item2)           
        try:
            match2 = at.search('name', item2)
            for field2 in match2:
                res2 = field2['fields']        
                name = res2['name']
                name = remove_non_ascii(name)
                fanart = res2['fanart']
                thumbnail = res2['thumbnail']
                summary = res2['summary']
                summary = remove_non_ascii(summary)
                link_a = res2['link_a']
                link_b = res2['link_b']
                link_c = res2['link_c']
                link_d = res2['link_d']
                link_e = res2['link_e']
                trailer = res2['trailer']
                xml += display_xml(name,trailer,summary,thumbnail,fanart,link_a,link_b,link_c,link_d,link_e)
        except:
            pass        
        try:
            match2 = at3.search('name', item2)
            for field2 in match2:
                res2 = field2['fields']        
                name = res2['name']
                name = remove_non_ascii(name)
                fanart = res2['fanart']
                thumbnail = res2['thumbnail']
                summary = res2['summary']
                summary = remove_non_ascii(summary)
                link_a = res2['link_a']
                link_b = res2['link_b']
                link_c = res2['link_c']
                link_d = res2['link_d']
                link_e = res2['link_e']
                trailer = res2['trailer']
                xml += display_xml(name,trailer,summary,thumbnail,fanart,link_a,link_b,link_c,link_d,link_e)                   
        except:
            pass
    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type(), pins)        

def fetch_from_db2(url):
    koding.reset_db()
    url2 = clean_url(url)
    match = koding.Get_All_From_Table(url2)
    if match:
        match = match[0]
        if not match["value"]:
            return None   
        match_item = match["value"]
        try:
                result = pickle.loads(base64.b64decode(match_item))
        except:
                return None
        created_time = match["created"]
        if float(created_time) + CACHE_TIME <= time.time():
            koding.Remove_Table(url2)
            db = sqlite3.connect('%s' % (database_loc))        
            cursor = db.cursor()
            db.execute("vacuum")
            db.commit()
            db.close()
            return result
        else:
            pass                     
        return result
    else:
        return []               


def remove_non_ascii(text):
    return unidecode(text)
