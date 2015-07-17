import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def add_url():
    if sys.argv[1]==None:
        url = raw_input('Please input the download link\n')
    url = sys.argv[1]
    return url,'url' if url[:4]=='http' else 'magnet'

def add_header(dtype):
    if dtype=='url':
        headers = {
                'Host': 'dynamic.cloud.vip.xunlei.com',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
                'Accept': '*/*',
                'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate',
                'Referer': 'http://dynamic.cloud.vip.xunlei.com/user_task?userid=122159693&st=4',
                'Cookie': '',
                'Connection': 'keep-alive'
                    }
    else:
        headers = {
                'Host': 'dynamic.cloud.vip.xunlei.com',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
                'Accept': 'text/javascript, application/javascript, */*',
                'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate',
                'X-Requested-With': 'XMLHttpRequest',
                'Referer': 'http://dynamic.cloud.vip.xunlei.com/user_task?userid=122159693&st=4',
                'Cookie': '',
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
            'Cookie': '',
            'Connection': 'keep-alive',
            }
    return headers
            

def add_param(url,dtype):
    if dtype=='url':
        pa={
            'callback':'queryCid',
            'interfrom':'task',
            'random':'14364823095681746756.6432040562',
            'tcache':'1436482495896',
            'url':url
            }
    else:
        pa = {
            'callback':'queryUrl',
            'interfrom':'task',
            'random':'14371640487651572726.9114392987',
            'tcache':'1437164049947',
            'u':url
        }
    return pa

def urlparams(req,url):
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

def magnetparams(req,arg,sel):
    params = {
            'btname':req[2],
            'cid':req[0],
            'class_id':'0',
            'findex':'_'.join(sel)+'_',
            'goldbean':'0',
            'interfrom':'task',
            'o_page':'task',
            'o_taskid':'0',
            'silverbean':'0',
            'size':'_'.join([args[2][int(itm)] for itm in sel]) + '_',
            'tsize':req[1],
            'uid':'122159693',
            'verify_code':''
            }
    return params

def changename(filename):
    return '\.'.join('\ '.join(filename.split(' ')).split('.'))

if __name__ =='__main__':
    s = requests.Session()
#benzi
    downloadurl,dtype = add_url()
    import re 
    if dtype=='url':
        requrl = 'http://dynamic.cloud.vip.xunlei.com/interface/task_check?'
    else:
        requrl = 'http://dynamic.cloud.vip.xunlei.com/interface/url_query?'
    req = s.get(requrl,headers = add_header(dtype),params=add_param(downloadurl,dtype))
    if dtype=='url':
        reqstr = req.content[9:-1]
        lst = []
        for itm in reqstr.split(','):
            lst.append(itm.strip('\',\ '))
        upurl = 'http://dynamic.cloud.vip.xunlei.com/interface/task_commit?'
        up = s.get(upurl,headers = add_header(dtype),params = urlparams(lst,downloadurl))
        print urlparams(lst,downloadurl)
        print up.url
        print up.content
        html = s.get('http://dynamic.cloud.vip.xunlei.com/user_task?userid=122159693&st=4#',headers = page_header())
        taskid = re.findall(r'\'(\d*?)\'',up.content)
        url_pattern = re.compile(r'(http:\/\/gdl.lixian.vip.xunlei.com\/download\?fid.*?)\"')
        download = url_pattern.findall(html.content)
        file_name = lst[4]
        print 'aria2c -c -s10 -x10 --out ' + changename(file_name) +' --header \'Cookie: gdriveid=AF3954D510F91F8CFF1F534F7E1AAB8F;\' \'' + download[0] + '\''
    else:
        paPattern = re.compile(r'\'(.*?)\'')
        argPattern = re.compile(r'new\ Array\((.*?)\)')
        lst = paPattern.findall(req.content)
        args = argPattern.findall(req.content)
        num = 0
        for itm1,itm2 in zip(args[0].split(','),args[1].split(',')):
            print str(num) + ' . ' + itm1 + ' ' + itm2
            num += 1
        select = raw_input('select the files(default all):\n').split(',')
        upurl = 'http://dynamic.cloud.vip.xunlei.com/interface/bt_task_commit?'
        up = s.post(upurl,headers = add_header(dtype),data = magnetparams(lst,args,select))
        print urlparams(lst,downloadurl)
        print up.url
        print up.content
