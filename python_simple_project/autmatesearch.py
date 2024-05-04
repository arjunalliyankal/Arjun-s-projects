import webbrowser
import sys

websites_needed=[
    'stackoverflow.com'
]
url="https://www.google.com"

chrome_path='open -a/ C:\Program Files\Google\Chrome\Application\chrome.exe %s'
webbrowser.get(chrome_path).open(url)

def create_filter():
    filter='('
    for index,website in enumerate(websites_needed):
        filter +='site:'+website
        if index==len(websites_needed)-1:
            filter += ')'
        else:
           filter +='OR'
    return filter     


def create_query():
    query=sys.argv[1:]
    return ' '.join(query)

def create_url():
    if len(sys.argv[1:])==0:
        print("error")
    else:
        final_url = url + create_query() + create_filter()
        webbrowser.get(chrome_path).open(final_url)    