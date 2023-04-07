from bs4 import BeautifulSoup
import requests
import time

print('Print some skill you are not familiar with:')
unfamiliar_skill = input(">")
print(f'Filtering out : {unfamiliar_skill}')
print(' ')
print(' ')
print(' ')
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index , job in enumerate(jobs):
        published_dates =  job.find('span', class_ = 'sim-posted').span.text
        if 'few' in published_dates:
            company_name = job.find('h3', class_ ='joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'path/output.txt','w') as f:
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f"More Info: {more_info.strip()}\n")  
                print(f'File Saved: output')
                
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 2
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)