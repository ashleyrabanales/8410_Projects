#%%
#import natural language toolkit
import nltk 

nltk.download('stopwords')
nltk.download('punkt')

# %%
import pandas as pd
df =pd.read_csv('/Users/ashleyrabanales/8410_Projects/Lessons/emotions.csv')
df.head()
# %%
text = df.iloc[0] #gets all the rows
print(text)
print(text.split(" "))
# %%
#stopwords = ["so", "not"]
stopwords = nltk.corpus.stopwords # syntax of stoping case 

stopwords.append("rather")
#%%
text = " ".join ([w for w in text.split(" ") if w not in stopwords])
print(text)
# %%


df["text"] = df["text"].apply(lambda x: " ".join ([w for w in x.split(" ") if w not in stopwords]))
df.head()
# %%
#important
#importabtly
#the most important
#important matters
#cows
#cow
text = df.iloc[0]["text"]
print(text)

nltk.stem.PorterStemmer()
for w in text.split():
    print(w, porter.stem(w))
# %%
df["stemmed_text"] = df["text"].apply(lambda x: " ".join ([porter.stem(w) for w in x.split(" ") if w not in stopwords]))
df.head()
#%%
from transformers import BertModel, TFBertModel
# %%
model = transformers.pipline("sentiment-analysis")
model(["Today is a beautiful day", 
"I'm not feeling good.",
"Today is not terrible but it's to "])
# %%
#Q: how to perform sentiment analysis on datset
df =pd.read_csv('/Users/ashleyrabanales/8410_Projects/Lessons/emotions.csv')
df.head()

