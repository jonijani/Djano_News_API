import requests 
from bs4 import BeautifulSoup
import json



BASE_URL = 'https://www.dailymail.co.uk/news/'
def get_res(url):
    res = requests.get(url)
    if res.status_code == 200:
        print(url)
        return res
    else:
        print(res)
        raise Exception('URL is not successfull')
    
'''def user_input_format(user_input):
    formated_user_input = user_input.replace(' ','%20')
    return formated_user_input'''

def create_dic_from_card(a_tag):
    d = {}
    title_ = a_tag.find('div',class_='articleListRowHeadline')
    title = title_.text

    link = a_tag.get('href')

    d['title'] = title
    d['link'] = link

    return d

def get_news_in_json_format(url):
    result = get_res(url)

    soup = BeautifulSoup(result.text,'html.parser')
    div_ = soup.find('div',class_='articleListRow')
    a_tags = div_.find_all('a',class_='articleListRowItem')

    l = []
    for a_tag in a_tags:
        d = create_dic_from_card(a_tag)
        l.append(d)
    return l
    # json_data = json.dumps(l)
    # return json_data


def get_url_link(keyword,page):
    #keyword = input('Enter city name in UK :')
    res_url = '/index.html'
    if page :
        page_no = f'?page={page}'
    else:
        page_no = ''

    url = url = f"{BASE_URL}{keyword}{res_url}{page_no}"
    print(url)
    return url

def get_search_result(keyword):
    count = 1
    pre_page_data = ''
    current_page_data = ''
    json_data_list = []
    while True:
        url = get_url_link(keyword,count)
        current_page_data = get_news_in_json_format(url)
        print(pre_page_data)
        print(current_page_data)
        if current_page_data == pre_page_data:
            break
        json_data_list.extend(current_page_data)
        count += 1
        pre_page_data = current_page_data




    return json_data_list





if __name__ == '__main__':
    # user_input = input('Enter word :')
    # res_url = '/index.html'
    # test = 'russia'
    # #url = f"{BASE_URL}{user_input_format(user_input)}{res_url}"
    # url = f"{BASE_URL}{user_input}{res_url}"

    # print(get_news_in_json_format(url))

    print(get_search_result('london'))




