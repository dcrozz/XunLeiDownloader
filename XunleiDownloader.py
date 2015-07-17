import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def add_header():
    headers = {
        'Host': 'dynamic.cloud.vip.xunlei.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://dynamic.cloud.vip.xunlei.com/user_task?userid=122159693&st=4',
        'Cookie': ''
        'Connection': 'keep-alive'
        }
    return headers
def page_header():
    headers = {
        'Host': 'dynamic.cloud.vip.xunlei.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
        'Accept': 'text/javascript, application/javascript, */*',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://dynamic.cloud.vip.xunlei.com/user_task?userid=122159693&st=4',
        'Cookie': '_x_a_=1E6549CAE778712544456E9F73671DA6D2CFD7226E65B41FAE0C3F9977A295DE963AD0EA205B1F152F014908EB58B93288B443F7E3D8430E7F6403C3358334B7; gdriveid=AF3954D510F91F8CFF1F534F7E1AAB8F; _xltj=34a1437060291610b52c; default_version=1.0; pagenum=30; kuaichuanid=EAD4E241D4FD0E4AEF77C553510474B3; _x_t_=3_1; active=1; downbyte=1442982102419; downfile=4070; isspwd=0; isvip=6; jumpkey=1DAF5839AE8C7EC92521B34BC810878B3C6C271970298D2386C9488E972C680471524F7461C7EE8ABA4BC0D1652BC0DE56B103854C2170D017774CD4432BC3EE15332EA294FE199912D37D2CA42ED30F6F5684A740B530FA2453098D8F1AA4F8; logintype=1; nickname=%BC%DF%C3%F0%CC%EC%CA%B9; onlinetime=15383225; order=1682644; safe=0; score=37212; sessionid=1E6549CAE778712544456E9F73671DA6D2CFD7226E65B41FAE0C3F9977A295DE963AD0EA205B1F152F014908EB58B93288B443F7E3D8430E7F6403C3358334B7; sex=m; upgrade=0; userid=122159693; usernewno=142104318; usernick=%E6%AD%BC%E7%81%AD%E5%A4%A9%E4%BD%BF; usertype=0; usrname=; bg_opentime=; vip_isvip=1; vip_level=6; vip_paytype=5; user_type=1; vip_expiredate=2015-11-18; dl_enable=1; dl_size=3145738; dl_num=150; dl_expire=365; user_task_time=0.40057897567749; check_e=AQAB; check_n=vWVMmBTnPum5MaERT%2blNq%2fcwrJYpj85EOfqKBAD8YJUnBOTGojoAHRk8lMuTTd3GNhYs8jGwCO0NgIr3ugfgEHZbJav3akZy2E%2f%2frBetgpe8iWNfgDFGg3Y9tRJvqjubdSwMU5KZ02Drn5qr6qsByhArhGB5dt86%2fkMEwpYuYn0%3d; verify_type=SEA; VERIFY_KEY=; lx_nf_all=page_check_all%3Dcommtask%26class_check%3D0%26page_check%3Dcommtask%26fl_page_id%3D0%26class_check_new%3D0%26set_tab_status%3D4; task_nowclick=1009388986242048; rw_list_open=1; queryTime=1; __xltjbr=1437089094952; _s34=1437531815934b1437060291610b2bhttp%3A//dynamic.cloud.vip.xunlei.com/user_task%3Fuserid%3D122159693%26st%3D4; moretasknum=0',
        'Connection': 'keep-alive'
}
    return headers

            
def add_url():
    return raw_input('please input the download url:\n')
def add_param(url):
    pa={
        'callback':'queryCid',
        'interfrom':'task',
        'random':'14364823095681746756.6432040562',
        'tcache':'1436482495896',
        'url':url
    }
    return pa
def upload(req,url):
    pa = {
        'callback':'ret_task',
        'cid':req[0],
        'class_id':'0',
        'database':'undefined',
        'gcid':req[1],
        'goldbean':'0',
        'interfrom':'task',
        'noCacheIE':'1436482924125',
        'o_page':'history',
        'o_taskid':'0',
        'silverbean':'0',
        'size':req[2],
        't':req[4],
        'time':'Thu Jul 09 2015 23:02:04 GMT 0000 (UTC)',
        'type':'0',
        'uid':'122159693',
        'url':url,
        'verify_code':''
    }
    return pa
def changename(filename):
    return '\.'.join('\ '.join(filename.split(' ')).split('.'))
if __name__ =='__main__':
    s = requests.Session()
#benzi
    requrl = 'http://dynamic.cloud.vip.xunlei.com/interface/task_check?'
    downloadurl = add_url()
    req = s.get(requrl,headers = add_header(),params = add_param(downloadurl))
    reqstr = req.content[9:-1]
    lst = []
    for itm in reqstr.split(','):
        lst.append(itm.strip('\',\ '))
    upurl = 'http://dynamic.cloud.vip.xunlei.com/interface/task_commit?'
    up = s.get(upurl,headers = add_header(),params = upload(lst,downloadurl))
    print upload(lst,downloadurl)
    print up.url
    print up.content
    html = s.get('http://dynamic.cloud.vip.xunlei.com/user_task?userid=122159693&st=4#',headers = page_header())
    import re 
    taskid = re.findall(r'\'(\d*?)\'',up.content)
    url_pattern = re.compile(r'(http:\/\/gdl.lixian.vip.xunlei.com\/download\?fid.*?)\"')
    download = url_pattern.findall(html.content)
    with open('downloadurl','w') as f:
        f.write(download[0])
    file_name = lst[4]
    print 'aria2c -c -s10 -x10 --out ' + changename(file_name) +' --header \'Cookie: gdriveid=AF3954D510F91F8CFF1F534F7E1AAB8F;\' \'' + download[0] + '\''
