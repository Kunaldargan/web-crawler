def get_next_target(source):
    start_link = source.find('<a href=')
    if start_link == -1:
        return None,0
    start_quote = source.find('"',start_link)
    end_quote = source.find('"',start_quote+1)
    url = source[start_quote+1:end_quote]
    return url,end_quote

 
def get_all_links(source):
    list_of_links=[]
    while True:
        url, endpos=get_next_target(source)
        if url:
            list_of_links.append(url)
            source = source[endpos:]
        else:
            break
    return list_of_links  

