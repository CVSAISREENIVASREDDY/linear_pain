from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
}

def  fetch_links(company):
    url = f"https://www.google.com/search?q={company}&sca_esv=2dacf5db398f8a2d&biw=1536&bih=782&sxsrf=AHTn8zoBy6bFT4hAd1N5cxY6uZi_ar3ORQ:1742230580293&tbm=nws&source=lnms&fbs=ABzOT_Cen_XDZtKf_vBGcVfGecI24gcwiADvKL7ToV_4ZQb8U_wgDs7rj_aj9b2OrTsMajW4EB-7xvfwVsepmiE30SqNVIEG246GCe0jBU3KIfAD-Se5QmOlQKxn85pIRV4GgCfAJ_F2ofdKvE-LMWPFq1gtwgSQLyTXmwjMJ0aaiIh_zsX5cQoEo-GvhmOnYa5SvDhJtaXfio3OZy0jHO_zb9bi_X086sb_cjaVBa747Tf3X3LKfeA&sa=X&ved=2ahUKEwi1uOvWypGMAxUkVmwGHdsFO4MQ0pQJegQIERAB"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser') 
    news = soup.select(".WlydOe")
    return [(new.attrs.get('href'), new.select_one(".OSrXXb.rbYSKb.LfVVr").text) for new in news]


def fetch_news(company):
    links = fetch_links(company)
    articles = []
    for link, date_posted in links:
        try:
            response = requests.get(link, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            page_title = soup.title.string
            page_description = soup.find('meta', attrs={'name': 'description'}).attrs['content']
            source = link.split('/')[2] 
            
            articles.append({
                'title': page_title,
                'description': page_description,
                'source': source,
                'date_posted': date_posted,
            })

        except Exception as e:
            continue
        if len(articles) == 15:
            break
    return articles 