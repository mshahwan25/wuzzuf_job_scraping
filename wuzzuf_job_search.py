import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame(columns=['Job','Company','Requirements'])

kword = input ('Enter Keyword: ')
num = int (input('Enter number of pages to seach in: '))

for i in range (num):
    url = 'https://wuzzuf.net/search/jobs/?a=hpb&q='+kword+'&start='+""+str(i)+""
    cont = requests.get(url).content
    soup = BeautifulSoup(cont, 'lxml')
    jobs = soup.find_all('div', class_='css-9hlx6w')
    for job in jobs:
        jobname = job.find('h2',class_='css-m604qf').text
        jobcomp = job.find('a',class_='css-17s97q8').text
        jobrequ = job.find('div', class_='css-y4udm8').text
        df = df.append({'Job':jobname, 'Company':jobcomp,'Requirements':jobrequ},ignore_index=True)
    print ('Page switched.')

df.to_csv('Refined_jobs.csv', index=False)
print ('Successful export!, you can check the jobs in Refined_jobs.csv')