from bs4 import BeautifulSoup
import requests
import pandas as pd
from locale import atof

html = requests.get("https://en.wikipedia.org/wiki/Transistor_count").text
#html.encoding = 'utf-8'
soup = BeautifulSoup(html,'lxml')

#print(soup)

h2s = soup.find_all('h2')
i = 0


h2 = h2s[1+3]

def find_table(tag, name):
    for sibling in h2.next_siblings:
        if sibling.name == name:
            return sibling

table = find_table(h2, 'table')

tbody = table.find_all("tbody")

trs=table.find_all('tr')

i = 0

datas = []

for tr in trs:
    i += 1
    #print("HHHA:0===>%d\n%s"% (i,tr))
    tds = tr.find_all(['th',"td"])
    row = []
    j = 0;
    for td in tds:
        for s in td.find_all('sup',class_='reference'):#移除引用
            print("移除引用：",s)
            s.clear()
        j += 1
        if i != 1 and j==2:
            row.append(atof(td.text))
        elif i != 1 and j==3:
            row.append(td.text.split()[0])
        else:
            
            row.append(td.text.split('[')[0].strip().replace("\xa0"," "))
        if j == 4:
            break;
    datas.append(row)

print("HHHB:0====>")
for data in datas:
    print(data)

print(len(datas))

df = pd.DataFrame(datas[1:],columns=datas[0])

df.to_csv("gpu_transcount.csv",index=False)




    


    
