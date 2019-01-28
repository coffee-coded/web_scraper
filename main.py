import requests
from bs4 import BeautifulSoup

search = input("Enter the search term : ")


params = {"q":search}
s = requests.Session()
r = s.get("https://www.bing.com/search",params=params)

soup = BeautifulSoup(r.text,"html.parser")

results = soup.find("ol",{"id":"b_results"})
links = results.findAll("li",{"class":"b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)

        if item.find("a").parent.parent.find("p"):
            print("Summary : ",item.find("a").parent.parent.find("p").text)
        else:
            print("No Description!")
        print("\n\n")


