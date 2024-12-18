import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

import openai
openai.api_key=api_key
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system", "content": "You are an analyst and historian tasked with analyzing daily news headlines and matching them with relevant quotes from ancient history. Provide a bold and insightful quote and a 1-2 sentence analysis that strongly connects the quote to the headline, making a decisive statement about the implications of the headline. The purpose is to create a 'quote of the day' social media post where the quote is the centerpiece and the analysis serves as a striking caption. For example: Headline: 'Supreme court overturns Roe v Wade.' Quote: 'The closer the collapse of the Empire, the crazier its laws are.' - Marcus Tullius Cicero. Explanation: We are witness to the fall of women's rights, despite vast support from the American public. The failure of our laws to protect citizens foretells the fall of the American nation."},
        {"role":"user", "content":"Congress fails to pass climate change bill despite increasing natural disasters."}
    ],
    max_tokens= 100
)
print(response['choices'][0]['message']['content'])