from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages=set()
random.seed(datetime.datetime.now())

#内链
def getInternalLinks(bsObj,includeUrl):
    internalLinks=[]
    for link in bsObj.findAll('a',href=re.compile("^(/|.*'+includeUrl+')")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href']);
    return internalLinks

#外链
def getExternalLinks(bsObj,excludeUrl):
    excludeLinks=[]
    for link in bsObj.findAll('a',href=re.compile("^(http|www)(?!'+excludeUrl+'.)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in excludeLinks:
                excludeLinks.append(link.attrs['href'])
    return excludeLinks

def splitAddress(address):
    addresspart=address.replace("http://","").split('/')
    return addresspart

def getRandomExternalLink(startingPage):
    html=urlopen(startingPage)
    bsObj=BeautifulSoup(html)
    externalLinks=getExternalLinks(bsObj,splitAddress(startingPage)[0])
    if len(externalLinks)==0:
        internalLinks=getInternalLinks(bsObj,splitAddress(startingPage)[0])
        return internalLinks[random.randint(0,len(internalLinks)-1)]
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink=getRandomExternalLink("http://oreilly.com")
    print("随机外链是："+externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")

    
                
        
            
