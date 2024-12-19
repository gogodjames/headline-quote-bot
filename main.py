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

import praw #reddit API init, sets up u/politics-quote-bot as a personal use script (therefore, no need for OAuth, just the password authentification)
redditbot = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD
)
subreddit = redditbot.subreddit("politics")
for submission in subreddit.rising(limit=1): #finds the most popular rising post on r/politics at time of request
    headline = submission.title #saves its title as the headline
    rising_post = submission #saves the post itself to be used for comment later

import openai #ChatGPT API init
openai.api_key=gpt_api_key
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        #system content gives a prompt asking GPT to analyze a headline and spit out a quote related to it and some explanation
        {"role":"system", "content": "You are an analyst and historian tasked with analyzing daily news headlines and matching them with bold, radical, and historically significant quotes from less mainstream figures. Provide a direct quote (no paraphrasing or made-up content) from thinkers such as Karl Marx, al-Farabi, or similarly radical or underrepresented voices. Follow the quote with a sharp, insightful, and provocative 1-2 sentence analysis that connects the quote to the headline. For personal dynamics or ego-driven headlines (e.g., conflicts between public figures or power struggles), focus on dramatic, psychological, or interpersonal interpretations, emphasizing motivations and character. For systemic or ideological issues (e.g., economic policies, societal shifts), provide broader philosophical or historical commentary, highlighting structural implications and ideological stakes. Avoid quoting overly familiar figures like Plato or MLK unless absolutely necessary, and ensure the quote is the centerpiece of the response."},
        #user content feeds the headline we got from the reddit API
        {"role":"user", "content":headline}
    ],
    max_tokens= 500 #token number needs to be fine tuned (must consider accuracy of GPT's response against the maitenence cost of the API)
)
comment = response['choices'][0]['message']['content'] 
rising_post.reply(comment)


