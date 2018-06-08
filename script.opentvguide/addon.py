# -*- coding: utf-8 -*-
#
#      Copyright (C) 2012 Tommy Winther
#      http://tommy.winther.nu
#
#      Modified for FTV Guide (09/2014 onwards)
#      by Thomas Geppert [bluezed] - bluezed.apps@gmail.com
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this Program; see the file LICENSE.txt.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#
import gui
from utils import reset_playing
import xbmc
import os
import xbmcgui
import download
import urllib
import urllib2
import zipfile
import sfile
import utils
import time
from shutil import copyfile
import webbrowser
import xbmcaddon


__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')


# After a restart the proc file should be wiped!
reset_playing()

update = xbmcgui.Dialog().yesno("[COLOR gold]TV Guide Helper[/COLOR]","[COLOR yellow][/COLOR]","Update Once A Day" ,"Or if you have stream issues.","Open Guide","Update InI File")
#download(LOCATION,file2) 
if update:
    try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.opentvguide/vistatv.xml"))
    except: pass
    utils.DeleteFile(xbmc.translatePath("special://userdata/addon_data/script.opentvguide/vistatv.xml"))
    xbmc.executebuiltin('RunAddon("plugin.video.opentvguide.ini.creator")')
else:
    try:
        w = gui.TVGuide()
        w.doModal()
        del w

    except:
        import sys
        import traceback as tb
        (etype, value, traceback) = sys.exc_info()
        tb.print_exception(etype, value, traceback)

