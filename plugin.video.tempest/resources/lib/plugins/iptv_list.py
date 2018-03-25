import requests,re

User_Agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4'
start_url = 'https://raw.githubusercontent.com/jassa007/IPTV/master/28092017.txt'
open('iptv_list.xml','w')

def iptv_list(start_url):
    try:
        headers = {'User_Agent':User_Agent}
        html = requests.get(start_url,headers=headers).content
        match = re.compile('title="(.+?)".+?logo="(.+?)",(.+?)#EXTINF',re.DOTALL).findall(html)
        for region,logo,combi in match:
            if logo == "":
                logo = 'need logo'
            combi = combi.split('\r\n')
            name = combi[0]
            link = combi[1]
            print_xml(name,logo,link)

                

    except:
        pass

def print_xml(name,logo,link):
    try:
        f = open('iptv_list.xml','a')
        f.write('<item>\n')
        f.write('\t<title>%s</title>\n' % name)
        f.write('\t<link>%s</link>\n' %link)
        f.write('\t<thumbnail>%s</thumbnail>\n' %logo)
        f.write('</item>\n')
        f.close()
          
    except:pass

iptv_list(start_url)    
