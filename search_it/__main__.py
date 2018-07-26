import webbrowser, sys, pyperclip

SEARCH_ENGINES = [
    'google.com/search?q=',
    'bing.com?q=',
    'search.yahoo.com/search?q=',
    'ask.com/web?q=',
    'duckduckgo.com?q=',
    'youtube.com/results?search_query=',
]

if __name__ == '__main__':
    search_term = ''

    if len(sys.argv) > 1:
        search_term = ' '.join(sys.argv[1:])
    else:
        search_term = pyperclip.paste()

    for engine in SEARCH_ENGINES:
        webbrowser.open('https://{0}{1}'.format(engine, search_term))

