import requests, json, re, time,logging,sys,xbmcgui,xbmc,os


import subprocess
import xbmcaddon
Addon = xbmcaddon.Addon()
resuaddon=xbmcaddon.Addon('script.module.resolveurl')
def copy2clip(txt):
    platform = sys.platform

    if platform == 'win32':
        try:
            cmd = 'echo ' + txt.strip() + '|clip'
            return subprocess.check_call(cmd, shell=True)
            pass
        except:
            pass
    elif platform == 'linux2':
        try:
            from subprocess import Popen, PIPE

            p = Popen(['xsel', '-pi'], stdin=PIPE)
            p.communicate(input=txt)
        except:
            pass
    else:
        pass
    pass
def colorString(text, color=None):
    try:
        text = text.encode('utf-8')
    except:
        try:
            text = bytes(text).decode('utf-8')
            text = str(text)
        except:
            pass
        pass

    if color is 'default' or color is '' or color is None:
        color = ''
        if color is '':
            color = 'deepskyblue'

    try:
        return '[COLOR ' + str(color) + ']' + text + '[/COLOR]'
    except:
        return '[COLOR ' + str(color) + ']' + text   + '[/COLOR]'
class RealDebrid:

    def __init__(self):
        self.ClientID = Addon.getSetting('rd.client_id')
        if self.ClientID == '':
            self.ClientID = 'X245A4XAIBGVM'
        self.OauthUrl = 'https://api.real-debrid.com/oauth/v2/'
        self.DeviceCodeUrl = "device/code?%s"
        self.DeviceCredUrl = "device/credentials?%s"
        self.TokenUrl = "token"
        self.token = Addon.getSetting('rd.auth')
        self.refresh = Addon.getSetting('rd.refresh')
        self.DeviceCode = ''
        self.ClientSecret = Addon.getSetting('rd.secret')
        self.OauthTimeout = 0
        self.OauthTimeStep = 0
        self.BaseUrl = "https://api.real-debrid.com/rest/1.0/"

    def auth_loop(self,dp):
        
        if dp.iscanceled():
            dp.close()
            return
        time.sleep(self.OauthTimeStep)
        url = "client_id=%s&code=%s" % (self.ClientID, self.DeviceCode)
        url = self.OauthUrl + self.DeviceCredUrl % url
        response = json.loads(requests.get(url).text)
        if 'error' in response:
            return
        else:
            dp.close()
            Addon.setSetting('rd.client_id', response['client_id'])
            Addon.setSetting('rd.secret', response['client_secret'])
            resuaddon.setSetting('RealDebridResolver_client_id', response['client_id'])
            resuaddon.setSetting('RealDebridResolver_client_secret', response['client_secret'])
            self.ClientSecret = response['client_secret']
            self.ClientID = response['client_id']
            return

    def auth(self):
        self.ClientSecret = ''
        self.ClientID = 'X245A4XAIBGVM'
        url = ("client_id=%s&new_credentials=yes" % self.ClientID)
        url = self.OauthUrl + self.DeviceCodeUrl % url
        response = json.loads(requests.get(url).text)
        copy2clip(response['user_code'])
        dp = xbmcgui . DialogProgress ( )
        dp.create("Real Debrid Auth","Open this link in a browser: " + ' %s' % colorString('https://real-debrid.com/device'), "Enter the code: " + ' %s' % colorString(response['user_code']), 'This code has been copied to your clipboard')
        dp.update(-1, "Open this link in a browser: " + ' %s' % colorString('https://real-debrid.com/device'), "Enter the code: " + ' %s' % colorString(response['user_code']), 'This code has been copied to your clipboard')
            
        
        self.OauthTimeout = int(response['expires_in'])
        self.OauthTimeStep = int(response['interval'])
        self.DeviceCode = response['device_code']
        while self.ClientSecret == '':
            self.auth_loop(dp)
            if dp.iscanceled():
              dp.close()
              return 0
        self.token_request()

    def token_request(self):
        import time
        if self.ClientSecret is '':
            return

        postData = {'client_id': self.ClientID,
                    'client_secret': self.ClientSecret,
                    'code': self.DeviceCode,
                    'grant_type': 'http://oauth.net/grant_type/device/1.0'}

        url = self.OauthUrl + self.TokenUrl
        response = requests.post(url, data=postData).text
        response = json.loads(response)
        Addon.setSetting('rd.auth', response['access_token'])
        Addon.setSetting('rd.refresh', response['refresh_token'])
        resuaddon.setSetting('RealDebridResolver_token', response['access_token'])
        resuaddon.setSetting('RealDebridResolver_refresh', response['refresh_token'])
        self.token = response['access_token']
        self.refresh = response['refresh_token']
        Addon.setSetting('rd.expiry', str(time.time() + int(response['expires_in'])))
        username = self.get_url('user')['username']
        Addon.setSetting('rd.username', username)
        xbmcgui.Dialog().ok('', 'Real Debrid ' + "Authentication is completed")
        logging.warning('Authorised Real Debrid successfully', 'info')

    def refreshToken(self):
        import time
        postData = {'grant_type': 'http://oauth.net/grant_type/device/1.0',
                    'code': self.refresh,
                    'client_secret': self.ClientSecret,
                    'client_id': self.ClientID
                    }
        url = self.OauthUrl + 'token'
        response = requests.post(url, data=postData)
      
        response = json.loads(response.text)
        self.token = response['access_token']
        self.refresh = response['refresh_token']
        Addon.setSetting('rd.auth', self.token)
        Addon.setSetting('rd.refresh', self.refresh)
        Addon.setSetting('rd.expiry', str(time.time() + int(response['expires_in'])))
        logging.warning('Real Debrid Token Refreshed')
        ###############################################
        # To be FINISHED FINISH ME
        ###############################################
    def check_link(self,media_id):
        
        unrestrict_link_path = 'unrestrict/check'
        url =  ( unrestrict_link_path)
        postData = {'link': media_id}
        result = self.post_url(url, postData)
        return result
    def get_link(self,media_id):
        
        unrestrict_link_path = 'unrestrict/link'
        url =  ( unrestrict_link_path)
        postData = {'link': media_id}
        result = self.post_url(url, postData)
        return result
    def post_url(self, url, postData, fail_check=False):
        original_url = url
        url = self.BaseUrl + url
        if not fail_check:
            if '?' not in url:
                url += "?auth_token=%s" % self.token
            else:
                url += "&auth_token=%s" % self.token

        response = requests.post(url, data=postData).text
       
        if 'bad_token' in response or 'Bad Request' in response:
            if not fail_check:
                self.refreshToken()
                response = self.post_url(original_url,postData, fail_check=False)
        try:
            return json.loads(response)
        except:
            return response
    def get_url_new1(self, url,data, fail_check=False):
        original_url = url
        url = self.BaseUrl + url
        url += "?auth_token=%s" % self.token
        logging.warning(url)
        response = requests.get(url,data=data).text
    
     
        try:
           return json.loads(response)
        except:
            return response
    def get_url_new(self, url,data, fail_check=False):
        original_url = url
        url = self.BaseUrl + url
        url += "?auth_token=%s" % self.token
        logging.warning(url)
        response = requests.put(url,data=data).text
    
     
        try:
           return json.loads(response)
        except:
            return response
    def get_url(self, url, fail_check=False):
        original_url = url
        url = self.BaseUrl + url
        if not fail_check:
            if '?' not in url:
                url += "?auth_token=%s" % self.token
            else:
                url += "&auth_token=%s" % self.token

        response = requests.get(url).text
    
        if 'bad_token' in response or 'Bad Request' in response:
            logging.warning('Refreshing RD Token')
            if not fail_check:
                self.refreshToken()
                response = self.get_url(original_url, fail_check=False)
        try:
           return json.loads(response)
        except:
            return response

    def checkHash(self, hashList):
        hashString = ''
        if isinstance(hashList, list):
            for i in hashList:
                hashString += '/%s' % i
        else:
            hashString = "/" + hashList

        return self.get_url("torrents/instantAvailability" + hashString)

    def addMagnet(self, magnet):
        postData = {'magnet': magnet}
        url = 'torrents/addMagnet'
        response = self.post_url(url, postData)
        return response

    def list_torrents(self):
        url = "torrents"
        response = self.get_url(url)
        return response

    def torrentInfo(self, id):
        url = "torrents/info/%s" % id
        return self.get_url(url)

    def torrentSelect(self, torrentID, fileID):
        url = "torrents/selectFiles/%s" % torrentID
        postData = {'files': fileID}
        return self.post_url(url, postData)

    def unrestrict_link(self, link):
        url = 'unrestrict/link'
        postData = {'link': link}
        response = self.post_url(url, postData)
        try:
            return response['download']
        except:
            return None
    def select_torrent_files(self,torrent_id, file_ids):
        uri = 'torrents/selectFiles/' + torrent_id
        if type(file_ids) is list:
            files = ','.join(file_ids)
        else:
            files = file_ids
        #RD.request(uri, data={"files": str(files)}, auth=True, encode_data=False)
        logging.warning(files)
        return self.post_url(uri, {"files": str(files['id'])})
       
    def deleteTorrent(self, id):
        url = "torrents/delete/%s&auth_token=%s" % (id, self.token)
        response = requests.delete(self.BaseUrl + url)
    def addtorrent(self,url):
        uri = 'torrents/addTorrent'
        file = open(url, 'rb') 
        dp = xbmcgui . DialogProgress ( )
        dp.create("Real Debrid Magnet","Starting", "", '')
        
    
        torrent=(self.get_url_new(uri,file))
        logging.warning(torrent)
       
        
        if 'id' in torrent:#try:
            res = self.torrentInfo(torrent['id'])
     
            if res['status']=='waiting_files_selection':
                   
                    fileIDString = ''
                    
                
                    if len(res['files'])>0:
                        max_size=0
                        for items in res['files']:
                            if items['bytes']>max_size:
                                max_size=items['bytes']
                                f_id=items['id']
                        start_file=f_id
                        
                       
                        self.torrentSelect(torrent['id'], start_file)#go
            f_size=0
            size=0
            status=''
            while status!='downloaded':
               
                status=res['status']
                size=res['bytes']
                unit=''
                unit2=''
                f_size=0
                f_size2=0
                if size>1024:
                    f_size=float(size)/1024
                    unit='Kb'
                if size>(1024*1024):
                    f_size=float(size)/(1024*1024)
                    unit='Mb'
                if size>(1024*1024*1024):
                    f_size=float(size)/(1024*1024*1024)
                    unit='Gb'
                size2=res['original_bytes']
                if size2>1024:
                    f_size2=float(size2)/1024
                    unit2='Kb'
                if size2>(1024*1024):
                    f_size2=float(size2)/(1024*1024)
                    unit2='Mb'
                if size2>(1024*1024*1024):
                    f_size2=float(size2)/(1024*1024*1024)
                    unit2='Gb'
                seed=''
                if 'seeders' in res:
                
                    seed='S-'+str(res['seeders'])
                if 'speed' in res:
                    unit3='b/s'
                    f_size3=res['speed']
                    if res['speed']>1024:
                        f_size3=float(res['speed'])/1024
                        unit3='Kb/s'
                    if res['speed']>(1024*1024):
                        f_size3=float(res['speed'])/(1024*1024)
                        unit3='Mb/s'
                    if res['speed']>(1024*1024*1024):
                        f_size3=float(res['speed'])/(1024*1024*1024)
                        unit3='Gb/s'
                    
                    speed=str(round(f_size3,2))+unit3
                else:
                    speed=''
                prog=0
                if 'progress' in res:
                    prog=res['progress']
                dp.update(prog, res['status']+' [COLOR yellow]'+seed+' '+speed+'[/COLOR]', res['original_filename'], str(round(f_size,2))+' '+unit+'/'+str(round(f_size2,2))+' '+unit2)
                xbmc.sleep(1000)
                res= requests.get(torrent['uri']+ "?auth_token=%s" % self.token).json()
                if dp.iscanceled():
                    self.deleteTorrent(torrent['id'])
                    dp.close()
                    return
            link = self.torrentInfo(torrent['id'])
            
            logging.warning(link)
            link = self.unrestrict_link(link['links'][0])
            
            
            self.deleteTorrent(torrent['id'])
            dp.close()
       
        
        #except:
        #    self.deleteTorrent(torrent['id'])
        #    return None
        
        return link
    def singleMagnetToLink(self, magnet):
        logging.warning('singleMagnetToLink')
        rd_sources=Addon.getSetting("rdsource")
        allow_debrid = rd_sources == "true" 
        if allow_debrid:
            maget_pre_reso= Addon.getSetting("magnet_rd_reso")
        else:
            maget_pre_reso='0'
        logging.warning(maget_pre_reso)
        if maget_pre_reso=='1':
            from run import resolve_rd
            rdlink=resolve_rd(magnet)
            logging.warning('rd link:'+rdlink)
            return rdlink
        try:
            dp = xbmcgui . DialogProgress ( )
            dp.create("Real Debrid Magnet","Starting", "", '')
            
            
            if self.ClientSecret == '':
                self.auth()
            hash = str(re.findall(r'btih:(.*?)&', magnet)[0].lower())
            hashCheck = self.checkHash(hash)
            fileIDString = ''
            logging.warning('hshhhhhhhh11111')
            if hash in hashCheck:
                
                if 'rd' in hashCheck[hash]:
                    if len(hashCheck[hash]['rd'])>0:
                        for key in hashCheck[hash]['rd'][0]:
                            fileIDString += ',' + key
          
            torrent = self.addMagnet(magnet)
          
  
            res= requests.get(torrent['uri']+ "?auth_token=%s" % self.token).json()
            f_size=0
            size=0
            status=''
            while status!='downloaded':
               
                status=res['status']
                size=res['bytes']
                unit=''
                unit2=''
                f_size=0
                f_size2=0
                if size>1024:
                    f_size=float(size)/1024
                    unit='Kb'
                if size>(1024*1024):
                    f_size=float(size)/(1024*1024)
                    unit='Mb'
                if size>(1024*1024*1024):
                    f_size=float(size)/(1024*1024*1024)
                    unit='Gb'
                size2=res['original_bytes']
                if size2>1024:
                    f_size2=float(size2)/1024
                    unit2='Kb'
                if size2>(1024*1024):
                    f_size2=float(size2)/(1024*1024)
                    unit2='Mb'
                if size2>(1024*1024*1024):
                    f_size2=float(size2)/(1024*1024*1024)
                    unit2='Gb'
                seed=''
                if 'seeders' in res:
                
                    seed='S-'+str(res['seeders'])
                if 'speed' in res:
                    unit3='b/s'
                    f_size3=res['speed']
                    if res['speed']>1024:
                        f_size3=float(res['speed'])/1024
                        unit3='Kb/s'
                    if res['speed']>(1024*1024):
                        f_size3=float(res['speed'])/(1024*1024)
                        unit3='Mb/s'
                    if res['speed']>(1024*1024*1024):
                        f_size3=float(res['speed'])/(1024*1024*1024)
                        unit3='Gb/s'
                    
                    speed=str(round(f_size3,2))+unit3
                else:
                    speed=''
                prog=0
                if 'progress' in res:
                    prog=res['progress']
                dp.update(prog, res['status']+' [COLOR yellow]'+seed+' '+speed+'[/COLOR]', res['original_filename'], str(round(f_size,2))+' '+unit+'/'+str(round(f_size2,2))+' '+unit2)
                xbmc.sleep(1000)
                res= requests.get(torrent['uri']+ "?auth_token=%s" % self.token).json()
               
                if res['status']=='waiting_files_selection':
                   
                    fileIDString = ''
                    
                    f_id=''
                    if len(res['files'])>0:
                        max_size=0
                        for items in res['files']:
                            if items['bytes']>max_size:
                                max_size=items['bytes']
                                if 'id' in items:
                                    f_id=items['id']
                        start_file=f_id
                        
                        if f_id=='':
                          xbmc.executebuiltin((u'Notification(%s,%s)' % ('', 'Rd Failed in torrent')).encode('utf-8'))
                        if 'id' in torrent:
                        
                            self.torrentSelect(torrent['id'], start_file)#go
                        else:
                            xbmc.executebuiltin((u'Notification(%s,%s)' % ('', 'Rd Failed in torrent')).encode('utf-8'))
                            return
                if dp.iscanceled():
                    if 'id' in torrent:
                        self.deleteTorrent(torrent['id'])
                    dp.close()
                    return
         
            dp.close()
            try:
                link = self.torrentSelect(torrent['id'], fileIDString[1:])
                link = self.torrentInfo(torrent['id'])
                link = self.unrestrict_link(link['links'][0])
                
                self.deleteTorrent(torrent['id'])
            except:
                xbmc.executebuiltin((u'Notification(%s,%s)' % ('', 'Rd Failed in torrent')).encode('utf-8'))
                if 'id' in torrent:
                    self.deleteTorrent(torrent['id'])
                return None
          
            return link
      
        except Exception as e:
            if 'id' in torrent:
                self.deleteTorrent(torrent['id'])
            import linecache
            exc_type, exc_obj, tb = sys.exc_info()
            f = tb.tb_frame
            lineno = tb.tb_lineno
            filename = f.f_code.co_filename
            linecache.checkcache(filename)
            line = linecache.getline(filename, lineno, f.f_globals)
            xbmc.executebuiltin((u'Notification(%s,%s)' % ('', 'Line:'+str(lineno)+' E:'+str(e))).encode('utf-8'))
            logging.warning('ERROR IN RD torrent :'+str(lineno))
            logging.warning('inline:'+line)
            logging.warning(e)
            logging.warning('BAD RD torrent')
    '''
    def magnetToLink(self, torrent, args):
        try:
            logging.warning('Magnet to link')
            if torrent['package'] == 'single':
                return self.singleMagnetToLink(torrent['magnet'])

            hash = str(re.findall(r'btih:(.*?)&', torrent['magnet'])[0].lower())
            hashCheck = self.checkHash(hash)
            torrent = self.addMagnet(torrent['magnet'])
            episodeStrings, seasonStrings = source_utils.torrentCacheStrings(args)
            file_key = None
            logging.warning('Magnet to link1111')
            for storage_variant in hashCheck[hash]['rd']:
                if len(storage_variant) > 1:
                    continue
                else:
                    key = list(storage_variant.keys())[0]
                    filename = storage_variant[key]['filename']

                    if any(source_utils.cleanTitle(episodeString) in source_utils.cleanTitle(filename) for episodeString in episodeStrings):
                        if any(filename.lower().endswith(extension) for extension in
                               source_utils.COMMON_VIDEO_EXTENSIONS):
                            file_key = key
                            break
            if file_key == None:
                logging.warning('Magnet to link2222')
                self.deleteTorrent(torrent['id'])
                return None
            logging.warning('Magnet to link3333')
            self.torrentSelect(torrent['id'], file_key)
            logging.warning("torrent['id']")
            logging.warning(torrent['id'])
            link = self.torrentInfo(torrent['id'])
            logging.warning(link)
            
            link = self.unrestrict_link(link['links'][0])
            logging.warning(link)
            if link.endswith('rar'):
                link = None

            if Addon.getSetting('rd.autodelete') == 'true':
                self.deleteTorrent(torrent['id'])
            return link
        except:
            import traceback
            traceback.print_exc()
            self.deleteTorrent(torrent['id'])
            return None
    '''
    def getRelevantHosters(self):
        
        try:
            host_list = self.get_url('hosts/status')
            valid_hosts = []
            for domain, status in host_list.iteritems():
                if status['supported'] == 1 and status['status'] == 'up':
                    valid_hosts.append(domain)
            return valid_hosts
        except:
            
            return []
