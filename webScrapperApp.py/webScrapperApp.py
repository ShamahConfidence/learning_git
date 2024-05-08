import requests
from bs4 import BeautifulSoup

# Send a request to the website
url ="https://www.alibaba.com/?src=sem_ggl&field=UG&from=sem_ggl&cmpgn=9922923274&adgrp=97780323582&fditm=&tgt=kwd-303543537278&locintrst=&locphyscl=9073670&mtchtyp=e&ntwrk=g&device=c&dvcmdl=&creative=598857653490&plcmnt=&plcmntcat=&aceid=&position=&gad_source=1&gclid=CjwKCAiAi6uvBhADEiwAWiyRdvbarkBBAz-mmdUKLu-5Ash9HJ2ex8dkIjd_KlNRdgAVCvnLhGXgsRoCInsQAvD_BwE'"
response = requests.get(url)


#Parse the HTML content
soup = BeautifulSoup(response.content,"html.parser")

#Extract the desired data
#For example, let's extract all the link on the page
links = soup.find_all("a")
for link in links:
    print(link.get("href"))
