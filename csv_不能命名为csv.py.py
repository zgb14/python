import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bsObj=BeautifulSoup(html)
#主对比表格是当前页面第一个表格
table=bsObj.findAll('table',{'class':'wikitable'})[0]
rows=table.findAll('tr')

csvfile=open('../python_result/edtiors.csv','wt',newline='',encoding='utf8')
writer=csv.writer(csvfile)
try:
    for row in rows:
        csvrow=[]
        for cell in row.findAll(['td','th']):
            csvrow.append(cell.get_text())
            print(cell.get_text())
            writer.writerow(csvrow)
finally:
    csvfile.close()
    
                
            

