from google import genai
GOOGLE_API_KEY = 'AIzaSyDrvOU7IPnOwGxKuBfAlLGc-cicgGad6Wc'
client = genai.Client(api_key=GOOGLE_API_KEY)

def summarise(content):
    model = "gemini-2.0-flash"
    prompt = f'''
        perform the compartive sentiment analysis and give me the summarised text 
        the text should describe the positives and negatives of total content 
        The given text is {content} '''  