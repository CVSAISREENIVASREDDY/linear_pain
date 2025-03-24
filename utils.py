from transformers import pipeline

classify = pipeline('sentiment-analysis') 

def classify_sentiment(news):
    for article in news :
        content = article['title'] + article['content'] 
        article['sentiment'] = classify(content)[0]['label']  
    return news 

def sentiment_count(news):
    count = {'POSITIVE':0 , 'NEGATIVE':0} 
    for article in news:
        count[article['sentiment']] += 1 
    return count 

ner = pipeline("ner", grouped_entities=True) 

def keywords(news):
    for article in news :
        content = article['title'] + article['content'] 
        keywords = set()
        key_set = ner(content) 
        for set in key_set :
            keywords.add(set['word'])  
        article['keywords'] = keywords 
    return news 

def overall_content(news):
    content = ""
    for article in news :
        content += article['title'] 
        content += article['content'] 
    return content 
