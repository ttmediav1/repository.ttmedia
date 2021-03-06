import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'TTMedia Wizard'
EXCLUDES       = [ADDON_ID]
# Text File with build info in it.
BUILDFILE      = 'http://ttmedia.live/wizard/autobuilds.txt'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.  Leave as 'http://' to ignore
APKFILE        = 'http://ttmedia.live/wizard/apk.txt'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = ''
YOUTUBEFILE    = 'http://'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'http://'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://'
# Text file for roms and emus
ROMPACK        = 'https://ttmedia.live/wizard/roms.txt'
EMUAPKS        = 'https://ttmedia.live/wizard/emu.txt'

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'https://ttmedia.live/wizard/builds.png'
ICONMAINT      = 'https://ttmedia.live/wizard/maint.png'
ICONSPEED      = 'https://ttmedia.live/wizard/tools.png'
ICONAPK        = 'https://ttmedia.live/wizard/apks.png'
ICONRETRO      = 'https://ttmedia.live/wizard/retro.png'
ICONADDONS     = 'http://ttmedia.live/wizard/icon.png'
ICONYOUTUBE    = 'http://ttmedia.live/wizard/icon.png'
ICONSAVE       = 'https://ttmedia.live/wizard/data.png'
ICONTRAKT      = 'http://ttmedia.live/wizard/icon.png'
ICONREAL       = 'http://ttmedia.live/wizard/icon.png'
ICONLOGIN      = 'http://ttmedia.live/wizard/icon.png'
ICONCONTACT    = 'http://ttmedia.live/wizard/icon.png'
ICONSETTINGS   = 'https://ttmedia.live/wizard/settings.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '*'

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'dodgerblue'
COLOR2         = 'deepskyblue'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+'][B]Current Build:[/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+'][B]Current Theme:[/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'yes'
# You can add \n to do line breaks
CONTACT        = ''
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'http://ttmedia.live/wizard/icon.png'
CONTACTFANART  = 'http://ttmedia.live/wizard/fanart.jpg'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'Yes'
# Url to wizard version
WIZARDFILE     = 'http://ttmedia.live/wizard/autobuilds.txt'
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'
# Addon ID for the repository
REPOID         = ''
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'http://'
# Url to folder zip is located in
REPOZIPURL     = 'http://'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'http://ttmedia.live/wizard/notify.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Image'
HEADERMESSAGE  = ''
# url to image if using Image 500x50(Width can vary but height of image needs to be 50px)
HEADERIMAGE    = 'http://ttmedia.live/wizard/icon.png'
# Background for Notification Window
BACKGROUND     = ''
#########################################################