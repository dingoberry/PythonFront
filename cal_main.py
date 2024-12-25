from execjs import *

if __name__ == '__main__':
    with open('cal.js', encoding='utf-8') as f:
        print(compile(f.read()).call('execute'))