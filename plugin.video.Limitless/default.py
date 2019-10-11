#############################################################
#################### START ADDON IMPORTS ####################
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

import os
import re
import sys
import Live
import Movies

import pyxbmct.addonwindow as pyxbmct
from addon.common.addon import Addon

#############################################################
#################### SET ADDON ID ###########################
_addon_id_	= 'plugin.video.Limitless'
_self_		= xbmcaddon.Addon(id=_addon_id_)
addon		= Addon(_addon_id_, sys.argv)
Dialog		= xbmcgui.Dialog()

def clearup():

    cachePath     = xbmc.translatePath(os.path.join('special://home/cache'))
    thumbPath     = xbmc.translatePath(os.path.join('special://profile/Thumbnails'))
    packcagesPath = xbmc.translatePath(os.path.join('special://home/addons/packages'))
    
    i =[(cachePath,'Cache'),(thumbPath,'Thumbnails'),(packcagesPath,'Packages')]
    for r in i:
        for root,dirs,files in os.walk(r[0]):
            for f in files:
                if (f.endswith('.log')): continue
                try: os.unlink(os.path.join(root, f))
                except: pass
clearup()
def START():

	try:
		if not _self_.getSetting('Username') or not _self_.getSetting('Password'):
			Dialog.ok('[COLOR blue]Limitless[/COLOR]','There Seems To Be Some Information Missing From Your Account Settings Please Double Check You Have Entered Everything.')
			_self_.openSettings()
		else:
			if _self_.getSetting('Mode') == 'Live':
				Live.LiveWindow()
			else:
				Movies.MoviesWindow()
	except (RuntimeError, SystemError):
		pass

START()
