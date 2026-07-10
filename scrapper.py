import requests
from bs4 import BeautifulSoup
headers = {'User-agent' : ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36')}

def search_incruit(keyword, page=1):

    jobs=[]

    for i in range(page):
        page = 30 * i

        url = f'https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno={page}'
        r = requests.get(url, headers = headers)
        # print(r.status_code)
        # print(r.text)
        soup = BeautifulSoup(r.text, "html.parser")
        lis = soup.find_all("li", class_='c_col')

        for li in lis:
            company = li.find('a', class_='cpname').text 
            title = li.find('div', class_= 'cell_mid').find('div', class_='cl_top').find('a').text
            location = li.find('div', class_='cl_md').find_all('span')[0].text
            link = li.find('div', class_='cell_mid').find('div', class_='cl_top').find('a').get('href')

            job_data = {
                'company' : company,
                'title' : title,
                'location': location,
                'link': link
            }
            jobs.append(job_data)
    return jobs

if __name__ == '__main__':
    result = search_incruit('간호사',2)
    print(result)
    print(len(result))

def search_saramin(keyword):
    url = f'https://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword={keyword}'
    r = requests.get(url, headers = headers)
    print(r.status_code)
    print(r.url)
    print(r.history)
    print(r.text[:1000])
    soup = BeautifulSoup(r.text, 'html.parser')
    sarams = soup.find_all('div', class_='item_recruit')

    jobs_saramin = []

    for saram in sarams:
        company = saram.find('strong' , class_='corp_name').text
        title = saram.find('div', class_ = 'area_job').find('h2', class_ = 'job_tit').find('a').text
        location = saram.find('div', class_ = 'job_condition').find_all('span')[0].text
        link = saram.find('div', class_ = 'area_job').find('h2', class_='job_tit').find('a').get('href')

        job_data2 = {
            'company' : company,
            'title' : title,
            'location' : location,
            'link' : link
        }
        jobs_saramin.append(job_data2)
    return jobs_saramin

    
