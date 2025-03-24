from google import genai
from google.genai import types 
import json 

GOOGLE_API_KEY = 'AIzaSyDrvOU7IPnOwGxKuBfAlLGc-cicgGad6Wc'
client = genai.Client(api_key=GOOGLE_API_KEY)

response_schema = {  
    "type": "ARRAY",
    "description": "A list of extracted items from the input content.",
    "items": {
        "type": "OBJECT", 
        "required": ["title", "content", "source", "time"],
        "properties": {
            "title": {
                "type": "STRING",
                "description": "Short headline for the content",
            },
            "content": {
                "type": "STRING",
                "description": "2–3 sentence summary of the content",
            },
            "source": {
                "type": "STRING",
                "description": "Source of the content or 'unknown'",
            },
            "time": {
                "type": "STRING",
                "description": "Timestamp or 'unknown'",
            },
        },
    },
}

def filter(news): 
    model = "gemini-2.0-flash"
    config = types.GenerateContentConfig(
        response_mime_type='application/json',
        response_schema = response_schema) 
    prompt = f'''
      I will give you a list of dictionaries containing the news information of certain company as
      title , description , source and date
      summarise the all content in your own words for each of the dictionary in list
      Give it a title and return the list of dictionaries with the same keys but change the content
      Don't give me the code , just give me the list and nothing else 
      if there are terms like access denied or captcha, then don't include that dictionary in my list
      The given input for you is {news}
        '''
    response = client.models.generate_content(
        model=model,
        contents=[prompt],
        config=config
    ).text 
    return json.loads(response)

