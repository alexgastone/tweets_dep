from tqdm import tqdm
import pickle
import pandas as pd
import twint

# Configure
c = twint.Config()

keywords = "depressed OR depression OR hopeless OR lonely OR suicide OR hopelessness OR antidepressants OR miserable OR sad"
limit = 1000
since = "2020-11-05"
l = "en"

dataframes = []

output = open(f'tweets_dep_test.pkl','wb')

## set up TWINT twitter search
c.Hide_output = True 
c.Search = keywords
c.Limit = limit 
c.Since = since
c.Lang = l
c.Count = True 
c.Pandas = True 
twint.run.Search(c) 

## create the dataframe
df = twint.storage.panda.Tweets_df
dataframes.append(df)
pickle.dump(dataframes,output)

print('Finished scraping') 