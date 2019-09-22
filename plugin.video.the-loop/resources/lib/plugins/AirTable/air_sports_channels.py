"""
    air_channels_script.py --- writes a sports channel xml
    Copyright (C) 2017, TonyH

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


    Directory to run the script, put this in your main xml.
    Replace "---YOUR ADDON---" with the name of your addon.

    <dir>
    <title>Update Channel List</title>
    <link>plugin://plugin.video."---YOUR ADDON---"/?mode=RunScript&url=special://home/addons/plugin.video."---YOUR ADDON---"/resources/lib/plugins/AirTable/air_sports_channels.py</link>
    <summary>Updates the Nan tv channels list</summary>
    </dir>


    Directory to display the generated xml, put this in your main xml

    <dir>
    <name>Nan Tv Channels</name>
    <link>file://nan_sports.xml</link>
    <summary></summary>
    </dir>

    The nan_sports.xml that is generated is located in the kodi/addons/plugin.video."YOUR ADDON"/xml folder

    --------------------------------------------------------------
"""




import requests,re,xbmc,xbmcaddon
import airtable
from airtable.airtable import Airtable
from airtable import airtable

AddonName = xbmc.getInfoLabel('Container.PluginName')
AddonName = xbmcaddon.Addon(AddonName).getAddonInfo('id')
xml_file = xbmc.translatePath('special://home/addons/'+AddonName+'/xml/nan_sports.xml')
open(xml_file,'w')

def Pull_info():
    try:
        at = Airtable('apppx7NENxSaqMkM5', 'Nan_sports_channels', api_key='keyOHaxsTGzHU9EEh')
        match = at.get_all(maxRecords=700, sort=['channel'])
        print match
        results = re.compile("fanart': u'(.+?)'.+?link': u'(.+?)'.+?thumbnail': u'(.+?)'.+?channel': u'(.+?)'.+?summary': u'(.+?)'",re.DOTALL).findall(str(match))
        for fanart,link,thumbnail,channel,summary in results:
            print_xml(fanart,link,thumbnail,channel,summary)

    except:pass    


def print_xml(fanart,link,thumbnail,channel,summary):
    try:
        if 'plugin://plugin' in link:
            f = open(xml_file,'a')
            f.write('<plugin>\n')
            f.write('\t<title>%s</title>\n' % channel)
            f.write('\t<link>\n')
            f.write('\t<sublink>%s</sublink>\n' % link)
            f.write('\t</link>\n')
            f.write('\t<thumbnail>%s</thumbnail>\n' % thumbnail)
            f.write('\t<fanart>%s</fanart>\n' % fanart)
            f.write('\t<summary>%s</summary>\n' % summary)
            f.write('</plugin>\n')
            f.close()
        else:

            f = open(xml_file,'a')
            f.write('<item>\n')
            f.write('\t<title>%s</title>\n' % channel)
            f.write('\t<link>\n')
            f.write('\t<sublink>%s</sublink>\n' % link)
            f.write('\t</link>\n')
            f.write('\t<thumbnail>%s</thumbnail>\n' % thumbnail)
            f.write('\t<fanart>%s</fanart>\n' % fanart)
            f.write('\t<summary>%s</summary>\n' % summary)
            f.write('</item>\n')
            f.close()
          
    except:pass     

Pull_info()


