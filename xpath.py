from lxml import etree
import requests
import sys
import os
import string


def getHtml(url):
    data = requests.get(url)
    html = data.text
    return html

def getFilename(dir):
    re_text = ''
    tests = os.listdir(dir)
    #tests2 = os.walk(dir)
    if tests:
        for test in tests:
            if test.endswith('.php'):
                re_text = re_text+test + "\n"
    return re_text

def get_XPath(html,rule1):
    test = etree.HTML(html)
    items = test.xpath(rule1)
    tmp_list = []
    #/html/body/div/table[1]/tbody/tr/td[2]/nobr/text()
    #//span 敏感词较多
    if items:
        for n in items:
            try:
                if hasattr(n, "text") and n.text and n.text not in tmp_list:
                    if n.text.endswith('.php') == False:
                        tmp_list.append(n.text)
                        print(n.text.encode("utf-8", "ignore"))
            except UnicodeDecodeError:
                return get_XPath(html.decode("utf-8", "ignore"),rule1)
    else:
        print ('No matches!')  
    return tmp_list

def get_matches(file_name,rule):
    file_dir = dir+'\\'+ file_name
    f = open(file_dir,'rb')
    file_content = f.read()
    re_title_list = get_XPath(file_content,rule)
    for item in re_title_list:
        if item not in xpath_list:
            xpath_list.append(item)

if __name__ == '__main__':
    xpath_list = []
    key = 2
    dir = r'D:\Users\sangfor\Desktop\webshell-datum'
    rule = ['//b','//th','//tr','//table','//b','//title']
    if key == 0:
        html = getHtml('https://www.baidu.com')
    else:
        if key == 1:
            file_data = open(r'D:\Users\sangfor\Desktop\test.html','r')
            html = file_data.read().encode('utf-8')
            file_data.close()
            #print(get_XPath(html,rule1))
            #print(html)
        
        else:
            re_text = getFilename(dir)
            re_text_list = re_text.split('\n')
            for a in rule:    
                for item in re_text_list:
                    if item:
                        xpath_list = []
                        print(a)
                        get_matches(item,a)
                        f = open(r'D:\Users\sangfor\Desktop\results.txt','ab')
                        f.write(a.encode()+b'\n'+b"".join([e.encode("UTF-8", "ignore") for e in xpath_list])+b'\n'+b'----------------------------------------------------------------'+b'\n')
                        f.close()
                    #print('Current:'+str(re_text_list.index(item))+'/'+str(len(re_text_list))+'\n'+item+'\n--------------------------------------------------------\n')
            #print(re_text_list)
    print(xpath_list)
