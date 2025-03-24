from fetch import fetch_news 
from filter import filter 
import utils
import streamlit as st
from summarise import summarise 

company = st.text_input('company name') 
news = fetch_news(company) 

filtered_news = filter(news) 
sentimented_news = utils.classify_sentiment(filtered_news) 

content = utils.overall_content(sentimented_news) 
summary = summarise(content) 

