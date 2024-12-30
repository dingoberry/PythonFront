from requests import session

if __name__ == '__main__':
    url = 'https://geo.captcha-delivery.com/captcha/?initialCid=AHrlqAAAAAMA2BRwEwozaTsAoVLs1A==&cid=z3mGgwyhzvDBRdt~QOqsQrnKqrPysCiXNLq5aNBCRFHxwT~Epp9q7NTT1vpSKbYwW4UDS2WVC8ITA5GSgiegOBOGsoRHssi82lV7g7xoyAm6VC7A7v1HgzIFvHaYREfg&referer=http%3A%2F%2Fbck.hermes.com%2Fcustomer-session%3Flocale%3Djp_ja%26withShippingMethods%3D0&hash=2211F522B61E269B869FA6EAFFB5E1&t=fe&s=8945&e=76079e1f171fbb059806eee44f3220287d756ff202d5c71934b479a1d63945e2'
    session = session()
    response = session.get(url)
    print(session.cookies)