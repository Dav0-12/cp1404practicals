"""
CP1404 Prac 10 - Wikipedia Prac
David Hunter
"""

import wikipedia

query = input("Search Wikipedia: ")
while query != "":
    result = wikipedia.page(query)
    print(result.title)
    print(result.url)
    print(result.summary)
    query = input("Search Wikipedia: ")
