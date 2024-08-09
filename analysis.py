import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

df=pd.read_csv(r'Air India Review.csv')

df['Date']=pd.to_datetime(df['Date'], format='%Y-%m-%d')

# creating new column
df['Month'] = df['Date'].dt.month_name()

# Split the 'Detail.Route' column into 'Route Start' and 'Route End'
df[['Route Start','Route End']]=df['Detail.Route'].str.split(' to ',expand=True)

# Further split 'Route End' to extract the Final Destination and discard any 'via' part
df['Route End'] = df['Route End'].str.split(' via ', expand=True)[0]

df.to_csv('Air India Review.csv',index=False)