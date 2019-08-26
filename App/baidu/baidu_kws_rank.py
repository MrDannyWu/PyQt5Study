import requests
from bs4 import BeautifulSoup
# from lxml import etree


def get_html(url, header):
    try:
        resp = requests.get(url, headers=header)
        resp.encoding = 'utf-8'
        return resp.text, resp.url
    except:
        try:
            resp = requests.get(url, headers=header)
            resp.encoding = 'utf-8'
            return resp.text, resp.url
        except:
            # print(requests.get(url, headers=header))
            print('Connection Error!')
            return '', ''


def parse(kw, response):
    # html = etree.HTML(response)
    soup = BeautifulSoup(response, 'lxml')
    items = soup.select('#content_left .c-container h3 a')
    for item in items:
        title = item.text
        baidu_url = item.get('href')
        print(title, baidu_url)
        # resp = requests.get()
        response = get_html(baidu_url, '')
        # resp = requests.get(baidu_url)
        # article_url = resp.url
        print(kw, title, baidu_url, response[1])
        with open('baidu_search_results.csv', 'a')as f:
            f.write(kw.replace(',', '') + ',' + title.strip().replace(',' , '') + ',' + baidu_url.strip() + ',' + response[1].strip() + '\n')


def main():
    # page为0 10 20
    with open('baidu_search_results.csv', 'w')as f:
        f.write('kw,title,baidu_url,article_url' + '\n')
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'BIDUPSID=873B1CF1320F20F15C87A2F2B1EC5A6F; PSTM=1564986934; BD_UPN=12314753; BAIDUID=026A2884882CF38C5E121381F2F8691A:FG=1; BDUSS=NRS3FBVjdUamhmcnJsZS04LXc0Vm9RYUZueE94TlJSTTV3OVRGTTZhcDFXMjlkSVFBQUFBJCQAAAAAAAAAAAEAAAB-vqpjztLP687Ssru5u7rDYW4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHXOR111zkddZV; H_PS_PSSID=29493_1457_21098_29522_29521_29099_29568_29221_26350_29459; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BD_CK_SAM=1; PSINO=7; sug=3; sugstore=0; ORIGIN=0; bdime=0; COOKIE_SESSION=1316_0_6_3_0_4_0_0_4_3_0_0_0_0_0_0_0_0_1566789077%7C6%230_0_1566782230%7C1; H_PS_645EC=d0bbERl3iVeyBGan7bn8rzdW2Va1vxXlmJbBPKIJNLPpMVRynAzzOO5yZuM',
        'Host': 'www.baidu.com',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    base_url = 'https://www.baidu.com/s?wd={}&pn={}'
    with open('kws.txt', 'r', encoding='utf-8')as rea:
        results = rea.readlines()
        rea.close()
    for kw in results:
        for i in range(3):
            url = base_url.format(kw.strip(), i*10)
            print(url)
            response = get_html(url, header)
            # print(response)
            parse(kw.strip(), response[0])


if __name__ == '__main__':
    main()
