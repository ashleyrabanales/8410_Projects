#%%
#!pip install beautifulsoup4 requests
import requests
import json
from bs4 import BeautifulSoup
# %%
if __name__ == "__main__":
    soup = BeautifulSoup(requests.get("http://app.ddot.dc.gov/").text, "html.parser")
    imageObj = (soup.find_all("script")[2])
    print(imageObj.text[27:100]) # looking for only one bracket not ()
    #27 is the beginning bc we are looking for a json 
    jsondict = json.loads(imageObj.text[27:-8])
    print(type(jsondict)) #convert a string to json object that is a stucture object to a jsondict 

    for a in jsondict:
        print(a["name"]) # or we can print the long, lat, name, etc
     
     #save as jsondict into a json file 
     #TODO: if file exists, do not get data again
    with open("locations.json", "w") as fp:
        json.dump(jsondict, fp)

# %%
