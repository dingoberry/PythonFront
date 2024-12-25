from requests.sessions import session

if __name__ == '__main__':
    s = session()
    s.headers.update({
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
    })
    resp = s.get('https://bck.hermes.com/product?locale=jp_ja&productsku=H010734CD4B')
    print(resp.status_code)
    print(resp.text)