import urllib
import urllib.request
from bs4 import BeautifulSoup
import os


def soup(url):
    thepage=urllib.request.urlopen(url)
    soupdata=BeautifulSoup(thepage,"html.parser")
    thepage.close()
    return soupdata

edatas=""
edata1=""

surl="https://www.flipkart.com/search?q=machine+learning+books&sid=bks&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_na&as-pos=1&as-type=RECENT&suggestionId=machine+learning+books%7CBooks&requestId=6c0f8314-2c02-42af-baa0-d6aad0a5c945&as-searchtext=machine%20learning%20books"
soup1=soup(surl)
# print(soup1)

count=soup1.findAll("a",{"class":"s1Q9rs"})
print(len(count))

for record in soup1.findAll("div",{"class":"_1YokD2 _3Mn1Gg"}):
    for record2 in record.findAll("div",{"class":"_4ddWXP"}):
        for record3 in record2.findAll("a",{"class":"s1Q9rs"}):
            title=record3.text.replace(',',"..")

        for record4 in record2.findAll("div",{"class":"_30jeq3"}):
            price=record4.text.replace(',','')
            data=title+","+price
        edatas=edatas+"\n"+data

print(edatas)

# header="book name,price"
# file=open(os.path.expanduser("out1.csv"),"wb")
# file.write(bytes(header, encoding="ascii",errors="ignore"))
# file.write(bytes(edatas,encoding="ascii",errors="ignore"))
