# Today's movies in Atlanta 

#pip install bs4
import requests
import bs4


if __name__ == "__main__":
    url ="https://www.imdb.com/showtimes/locatiom?ref_=sh_lc"
    res = requests.get(url)
  #  print(res.content)


soup_result = bs4.BeautifulSoup(res.content, "html.parser")
print(soup_result.title)

movies = soup_result.findALL("div", {"class:" "titles"})
for m in movies:
    print("---")
    movie_name = m.find("a")
    print(movie_name.text)


# %%
