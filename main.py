import os
from dotenv import load_dotenv
load_dotenv()
gpt_api_key = os.getenv("OPENAI_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT')
REDDIT_USERNAME = os.getenv('REDDIT_USERNAME')
REDDIT_PASSWORD = os.getenv('REDDIT_PASSWORD')

import praw
redditbot = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD
)
subreddit = redditbot.subreddit("politics")
for submission in subreddit.hot(limit=10):
    print(submission.title)

'''from newsdataapi import NewsDataApiClient
newsapi = NewsDataApiClient(apikey="pub_62754921c21b1816fa80ae62f8c39337f2a15")
response = newsapi.latest_api(country='us',language='en', category='sports')
for article in response['results']:
    print(f"Title: {article['title']}")
    print(f"Categories: {article['category']}")
    print("---")'''

'''from newsapi import NewsApiClient

newsapi = NewsApiClient(news_api_key)
headlines=newsapi.get_top_headlines(country='us',sortBy='popularity',page_size=1,category='general')
for article in headlines['articles']:
    print(article['title'])'''

'''import openai
openai.api_key=gpt_api_key
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system", "content": "You are an analyst and historian tasked with analyzing daily news headlines and matching them with relevant quotes from ancient history. Provide a bold and insightful quote and a 1-2 sentence analysis that strongly connects the quote to the headline, making a decisive statement about the implications of the headline. The purpose is to create a 'quote of the day' social media post where the quote is the centerpiece and the analysis serves as a striking caption. For example: Headline: 'Supreme court overturns Roe v Wade.' Quote: 'The closer the collapse of the Empire, the crazier its laws are.' - Marcus Tullius Cicero. Explanation: We are witness to the fall of women's rights, despite vast support from the American public. The failure of our laws to protect citizens foretells the fall of the American nation."},
        {"role":"user", "content":"Congress fails to pass climate change bill despite increasing natural disasters."}
    ],
    max_tokens= 100
)
print(response['choices'][0]['message']['content'])'''
