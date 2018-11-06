import requests
from lxml import etree

def getUri(page):
    if 0 < page <= 64:
        uri = 'http://www.anquan.us/search?keywords=&&content_search_by=by_drops&&search_by_html=False&&page='
        #print(uri+str(page))
        html = requests.get(uri+str(page))
        html_data = html.text
        #print(html_data)
        return html_data
    else:
        return("out of range!")

def xpath_func(html_data):
    xpath_html = etree.HTML(html_data)
    uri_list = xpath_html.xpath('//tr[position()<22]/td[2]/a/@href')
    title_list = xpath_html.xpath('//tr[position()<22]/td[2]/a')
    for n in range(len(uri_list)):
        result_list.append(str(title_list[n].text)+"||"+"http://www.anquan.us/"+str(uri_list[n]))
    #print(result_list)

def getContent(result_list):
    print('start get content!')
    for item in result_list:
        name = item.split('||')[0]
        uri = item.split('||')[1]
        html = requests.get(uri)
        html_data = html.text
        name = name.replace('"','')
        with open('D:\\Users\\sangfor\\Desktop\\test'+'\\'+name.strip()+'.html',mode='w+b') as file:
            print('current saving file:'+ name.strip())
            file.write(bytes(html_data,encoding='utf-8'))
        

if __name__ == '__main__':
    result_list = []
    for page in range(2):
        html_data = getUri(page)
        xpath_func(html_data)
        print('got no.'+str(page)+' page!')
    print('got all item!')
    getContent(result_list)
