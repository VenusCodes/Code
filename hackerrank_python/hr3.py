#https://www.hackerrank.com/challenges/html-parser-part-2/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#i don't know these stuff just took it from some online platform
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if data.count('\n') == 0:
            print('>>> Single-line Comment')
        else:
            print('>>> Multi-line Comment')
        print(data)
    def handle_data(self, data):
        if data.strip() != '':
            print('>>> Data')
            print(data)
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
parser = MyHTMLParser()
parser.feed(html)
parser.close()