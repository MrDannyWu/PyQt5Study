import requests


def get_orignal_url(url):
    try:
        resp = requests.get(url)
        return url, resp.url
    except:
        try:
            resp = requests.get(url)
            return url, resp.url
        except:
            return url, ''
            pass

def main():
    with open('o_url.txt', 'r')as f:
        results = f.readlines()
        f.close()

    for i in results:
        url = i.strip()
        result_url = get_orignal_url(url)
        print(result_url)
        with open('url_list.csv', 'a')as w:
            w.write(result_url[0] + "," + result_url[1] + '\n')
    w.close()


if __name__ == '__main__':
    main()
