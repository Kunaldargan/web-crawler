import requests
import urllib.request
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
req=Request('https://www.udacity.com/cs101x/index.html')
response=urlopen(req)
html=response.read()
def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)
    return p
            

def get_next_target(page):
    start_link = page.find(b'<a href=')
    if start_link == -1:
        return None,0
    start_quote = page.find(b'"',start_link)
    end_quote = page.find(b'"',start_quote+1)
    url = page[start_quote+1:end_quote]
    return url,end_quote

 
def get_all_links(page):
    list_of_links=[]
    while True:
        url, endpos=get_next_target(page)
        if url:
            list_of_links.append(url)
            page = page[endpos:]
        else:
            break
    return list_of_links
print(get_all_links(html))
#print(html)

def crawl_web(seed):
    to_crawl=[seed]
    crawled=[]
    index=[]
    while to_crawl:
        page=to_crawl.pop()
        if page not in crawled:
            content=get_page(page)
            add_page_to_index(index,page,content)
            union(to_crawl,get_all_links(content))
            crawled.append(page)
    return index
            
def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0]==keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def lookup(index,keyword):
    for entry in index:
        if entry[0]==keyword:
            return entry[1]
    return []

def add_page_to_index(index,url,content):
    words=content.split()
    for word in words:
        add_to_index(index,word,url)
