import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
import re

df=pd.read_csv(r'Air India Review.csv')

# fill the missing values

df['Detail.Seat Comfort']=round(df['Detail.Seat Comfort'].fillna(df['Detail.Seat Comfort'].mean()))
df['Detail.Cabin Staff Service']=round(df['Detail.Cabin Staff Service'].fillna(df['Detail.Cabin Staff Service'].mean()))
df['Detail.Food & Beverages']=round(df['Detail.Food & Beverages'].fillna(df['Detail.Food & Beverages'].mean()))
df['Detail.Inflight Entertainment']=round(df['Detail.Inflight Entertainment'].fillna(df['Detail.Inflight Entertainment'].mean()))
df['Detail.Ground Service']=round(df['Detail.Ground Service'].fillna(df['Detail.Ground Service'].mean()))
df['Detail.Wifi & Connectivity']=round(df['Detail.Wifi & Connectivity'].fillna(df['Detail.Wifi & Connectivity'].mean()))

# correcting data from Review and Review body

df['Review']=df['Review'].replace({'“':'','”':''},regex=True)
df['Review_Body']=df['Review_Body'].replace({'✅ ':'','“':'','”':''},regex=True)

df['Detail.Aircraft']=df['Detail.Aircraft'].fillna('N/A')
df['Rating']=df['Rating'].fillna('N/A')

df.to_csv('Air India Review.csv',index=False)
df['Review']=df['Review'].str.replace('"','')

df.to_csv('Air India Review.csv',index=False)