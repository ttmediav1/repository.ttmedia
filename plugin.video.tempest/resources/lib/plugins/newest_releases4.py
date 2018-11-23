"""
    releases.py 
    Copyright (C) 2018
    Version 3.0.1

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


    Returns the New Releases List-

    <dir>
    <title>Newest Releases3</title>
    <Airtable>Releases</Airtable>
    </dir>



    --------------------------------------------------------------

"""



from __future__ import absolute_import
import requests
import re
import os
import xbmc
import xbmcaddon
import json
import __builtin__
from koding import route
from ..plugin import Plugin
from resources.lib.external.airtable.airtable import Airtable
from resources.lib.util.context import get_context_items
from resources.lib.util.xml import JenItem, JenList, display_list
from requests.exceptions import HTTPError
import time
from unidecode import unidecode

CACHE_TIME = 3600  # change to wanted cache time in seconds

TMDB_api_key = __builtin__.tmdb_api_key
addon_fanart = xbmcaddon.Addon().getAddonInfo('fanart')
addon_icon = xbmcaddon.Addon().getAddonInfo('icon')
AddonName = xbmc.getInfoLabel('Container.PluginName')
AddonName = xbmcaddon.Addon(AddonName).getAddonInfo('id')


class NEWEST_RELEASES3(Plugin):
    name = "Releases"

    def process_item(self, item_xml):
        if "<Airtable>" in item_xml:
            item = JenItem(item_xml)
            if "Releases" in item.get("Airtable", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "Releasesv2",
                    'url': item.get("Airtable", ""),
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
                               

@route(mode='Releasesv2', args=["url"])
def Releases(url):
    xml = ""
    at = Airtable('appuNAD2qFkbCe4i8', 'Releases', api_key='keyZmzuBZ1XPQ0M1A')
    match = at.get_all(maxRecords=700, view='Grid view')
    url2 = "https://api.themoviedb.org/3/list/96428?api_key=20d53bcd9a2ee7d575badbc6f59446c6&language=en-US"
    html2 = requests.get(url2).content
    match2 = json.loads(html2)    
    for field in match:
        try:
            res = field['fields']
            title = res['title']
            tmdb = res['tmdb']
            year = res['year']
            link1 = res['link1']
            link2 = res['link2']
            link3 = res['link3']
            link4 = res['link4']
            link5 = res['link5']
            (thumbnail,fanart,summary) = tmdb_info(tmdb,match2)
            if "-*-" in link2:
                title = remove_non_ascii(title)
                summary = remove_non_ascii(summary)
                xml += "<item>"\
                        "<title>%s</title>"\
                        "<meta>"\
                        "<content>movie</content>"\
                        "<imdb></imdb>"\
                        "<title>%s</title>"\
                        "<year>%s</year>"\
                        "<thumbnail>%s</thumbnail>"\
                        "<fanart>%s</fanart>"\
                        "<summary>%s</summary>"\
                        "</meta>"\
                        "<link>"\
                        "<sublink>%s</sublink>"\
                        "<sublink>search</sublink>"\
                        "<sublink>searchsd</sublink>"\
                        "</link>"\
                        "</item>" % (title,title,year,thumbnail,fanart,summary,link1)   
            elif "-*-" in link3:
                title = remove_non_ascii(title)
                summary = remove_non_ascii(summary)
                xml += "<item>"\
                        "<title>%s</title>"\
                        "<meta>"\
                        "<content>movie</content>"\
                        "<imdb></imdb>"\
                        "<title>%s</title>"\
                        "<year>%s</year>"\
                        "<thumbnail>%s</thumbnail>"\
                        "<fanart>%s</fanart>"\
                        "<summary>%s</summary>"\
                        "</meta>"\
                        "<link>"\
                        "<sublink>%s</sublink>"\
                        "<sublink>%s</sublink>"\
                        "<sublink>search</sublink>"\
                        "<sublink>searchsd</sublink>"\
                        "</link>"\
                        "</item>" % (title,title,year,thumbnail,fanart,summary,link1,link2)
            elif "-*-" in link4:
                title = remove_non_ascii(title)
                summary = remove_non_ascii(summary)
                xml += "<item>"\
                        "<title>%s</title>"\
                        "<meta>"\
                        "<content>movie</content>"\
                        "<imdb></imdb>"\
                        "<title>%s</title>"\
                        "<year>%s</year>"\
                        "<thumbnail>%s</thumbnail>"\
                        "<fanart>%s</fanart>"\
                        "<summary>%s</summary>"\
                        "</meta>"\
                        "<link>"\
                        "<sublink>%s</sublink>"\
                        "<sublink>%s</sublink>"\
                        "<sublink>%s</sublink>"\
                        "<sublink>search</sublink>"\
                        "<sublink>searchsd</sublink>"\
                        "</link>"\
                        "</item>" % (title,title,year,thumbnail,fanart,summary,link1,link2,link3) 
            elif "-*-" in link5:
                title = remove_non_ascii(title)
                summary = remove_non_ascii(summary)
                xml += "<item>"\
                        "<title>%s</title>"\
                        "<meta>"\
                        "<content>movie</content>"\
                        "<imdb></imdb>"\
                        "<title>%s</title>"\
                        "<year>%s</year>"\
                        "<thumbnail>%s</thumbnail>"\
                        "<fanart>%s</fanart>"\
                        "<summary>%s</summary>"\
                        "</meta>"\
                        "<link>"\
                        "<sublink>%s</sublink>"\
                        "<sublink>%s</sublink>"\
                        "<sublink>%s</sublink>"\
                        "<sublink>%s</sublink>"\
                        "<sublink>search</sublink>"\
                        "<sublink>searchsd</sublink>"\
                        "</link>"\
                        "</item>" % (title,title,year,thumbnail,fanart,summary,link1,link2,link3,link4)
            else:
                title = remove_non_ascii(title)
                summary = remove_non_ascii(summary)
                xml += "<item>"\
                        "<title>%s</title>"\
                        "<meta>"\
                        "<content>movie</content>"\
                        "<imdb></imdb>"\
                        "<title>%s</title>"\
                        "<year>%s</year>"\
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
                        "<sublink>search</sublink>"\
                        "<sublink>searchsd</sublink>"\
                        "</link>"\
                        "</item>" % (title,title,year,thumbnail,fanart,summary,link1,link2,link3,link4,link5)
        except:
            pass                                                                               
    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())

def tmdb_info(tmdb,match2):
    try:
        tmdb_res = match2['items']
        for res in tmdb_res:
            movie_id = str(res['id'])
            if movie_id == tmdb:           
                thumbnail = res['poster_path']
                if not thumbnail:
                    thumbnail = ""
                summary = res['overview']
                fanart = res['backdrop_path']
                if not fanart:
                    fanart = ""
                thumbnail = "https://image.tmdb.org/t/p/original"+str(thumbnail)
                fanart = "https://image.tmdb.org/t/p/original"+str(fanart)
        return thumbnail,fanart,summary        
    except:
        return "","",""


def remove_non_ascii(text):
    return unidecode(text)

