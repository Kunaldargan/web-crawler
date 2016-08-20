def get_next_target(source):
    start_link = source.find('<a href=')
    start_quote = source.find('"',start_link)
    end_quote = source.find('"',start_quote+1)
    url = source[start_quote+1:end_quote]
    return url
    
    
    
