import webbrowser

def searchGoogle(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")

def searchYoutube(query):
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

def searchWikipedia(query):
    webbrowser.open(f"https://en.wikipedia.org/wiki/{query}")
