"""
    m3u.py --- Jen Plugin for accessing m3u data
    Copyright (C) 2018, Mister-X
    version 1.0.2

    7-8-19 - Added cache function and modified regex - TH
    6-9-19 - Modified regex and added User Agent - TH

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


    Usage Examples:
    <dir>
    <title>M3U NAME</title>
    <thumbnail></thumbnail>
    <m3u>M3U LINK</m3u>
    <fanart></fanart>
    <info> </info>
    </dir>
"""

import urllib2
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
UserAgent = "|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"

class M3U(Plugin):
    name = "m3u"

    def process_item(self, item_xml):
        if "<m3u>" in item_xml:
            item = JenItem(item_xml)
            result_item = {
                'label': item["title"],
                'icon': item.get("thumbnail", addon_icon),
                'fanart': item.get("fanart", addon_fanart),
                'mode': "m3u",
                'url': item.get("m3u", ""),
                'folder': True,
                'imdb': "0",
                'content': "files",
                'season': "0",
                'episode': "0",
                'info': {},
                'year': "0",
                'context': get_context_items(item),
                "summary": item.get("summary", None)
            }
            result_item["properties"] = {'fanart_image': result_item["fanart"]}
            result_item['fanart_small'] = result_item["fanart"]
            return result_item


@route(mode='m3u', args=["url"])
def m3u(url):
    xml = ""
    pins = "PLuginm3u"
    Items = fetch_from_db2(pins)
    if Items: 
        display_data(Items) 
    else:
        if not xml:
            xml = ""
            if '.m3u' in url:
                listhtml = getHtml(url)
                #match = re.compile('#EXTINF:.+?,(.+?)\n([^"]+)\s+\n',
                #                   re.IGNORECASE | re.DOTALL).findall(listhtml)
                match = re.compile('#EXTINF:.+?,(.+?)\n(.+?).m3u8',re.DOTALL).findall(listhtml)
                for name, url in match:
                    name = name
                    url = url + ".m3u8"
                    url = url + UserAgent
                    xml += "<item>"\
                           "<title>%s</title>"\
                           "<link>%s</link>"\
                           "<thumbnail></thumbnail>"\
                           "</item>" % (name, url)
    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type(), pins)


def getHtml(url, referer=None, hdr=None, data=None):
    """GRAB HTML FROM THE LINK"""
    USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
    headers = {
        'User-Agent': USER_AGENT,
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
    if not hdr:
        req = urllib2.Request(url, data, headers)
    else:
        req = urllib2.Request(url, data, hdr)
    if referer:
        req.add_header('Referer', referer)
    response = urllib2.urlopen(req, timeout=60)
    data = response.read()
    response.close()
    return data

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
        print created_time + "created"
        print time.time() 
        print CACHE_TIME
        test_time = float(created_time) + CACHE_TIME 
        print test_time
        if float(created_time) + CACHE_TIME <= time.time():
            koding.Remove_Table(url2)
            db = sqlite3.connect('%s' % (database_loc))        
            cursor = db.cursor()
            db.execute("vacuum")
            db.commit()
            db.close()
            display_list2(result, "video", url2)
        else:
            pass                     
        return result
    else:
        return []     
