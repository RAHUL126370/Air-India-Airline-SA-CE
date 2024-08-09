import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

data=[]

for i in range(1,137):
    url=f"https://www.airlinequality.com/airline-reviews/air-india/page/{i}/"

    # request
    html_text=requests.get(url).content
    soup=BeautifulSoup(html_text,'lxml')

    boxes=soup.find_all(name='article',attrs={'itemprop':'review'})
    for box in boxes:

        dictionary_review={}
        # Rating Value
        Rating=box.find(name='span',attrs={'itemprop':'ratingValue'})
        if Rating:
            Rating=Rating.get_text()
        else:
            Rating="N/A"

        # Customer Name    
        Customer_Name=box.find(name='span',attrs={'itemprop':'name'})
        if Customer_Name:
            Customer_Name=Customer_Name.get_text()
        else:
            Customer_Name="N/A"
            
        # Date
        Date=box.find(name='time',attrs={'itemprop':'datePublished'})['datetime']

        # Review
        Review=box.find(name='h2',attrs={'class':'text_header'})
        if Review:
            Review=Review.get_text()
        else:
            Review="N/A"
            
        # Review Body
        Review_Body=box.find(name='div',attrs={'class':'text_content'})   
        if Review_Body:
            Review_Body=Review_Body.get_text()
        else:
            Review_Body="N/A"
            
        # other Details
        d={}
        Table=box.find(name='table',attrs={'class':'review-ratings'})
        Table_Rows=box.find_all('tr')
        for table_row in Table_Rows:
            key=table_row.find_all('td')[0].get_text()
            value=table_row.find_all('td')[1]
            if value['class']==['review-rating-stars', 'stars']:
                value=len(value.find_all(name='span',attrs={'class':'star fill'}))
            else:
                value=value.get_text()
            d[key]=value    
            
            dictionary_review['Rating']=Rating
            dictionary_review['Customer_Name']=Customer_Name
            dictionary_review['Date']=Date
            dictionary_review['Review']=Review
            dictionary_review['Review_Body']=Review_Body
            dictionary_review['Detail']=d
        data.append(dictionary_review)    

df=pd.json_normalize(data)
df.to_csv('Air India Review.csv',index=False)   

     