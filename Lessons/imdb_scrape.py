# from https://www.imdb.com/showtimes/location?ref_=sh_lc
# A dataframe with two columns:
#   Title (string)
#   Rank  (int)

# pip install requests bs4
import requests
import bs4
import pandas as pd

if __name__ == "__main__":
    res = requests.get("https://www.imdb.com/showtimes/location?ref_=sh_lc")
    #print(res.content)
    soup_res = bs4.BeautifulSoup(res.content, "html.parser")
    movies = soup_res.findAll("div", {"class":"title"})

    titles = []
    for m in movies:
        titles.append(m.find("a").text)
    #print(titles)

    df = pd.DataFrame(titles, columns=["Title"])
    print(df)
