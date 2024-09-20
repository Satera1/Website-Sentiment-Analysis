# Website Sentiment Analysis
## Motivation and Idea
Due to the need and curiosity for investments, I decided to create this script to carry out web scrapping of financial news sites and use an AI (in this case, Google's Gemini AI) to carry out a sentiment analysis of the news to find out whether it is generally positive or negative.
Obviously the code isn't limited to financial news, so you can use it to carry out a sentiment analysis of any site. The code will generate a note on the sentiment of the news on a floating scale from 0.00 to 1.00, where 0.00 is very negative and 1.00 is very positive, and will provide a justification and summarise its analysis of the news.

# Attention
The code makes use of the Gemini AI chatbot to predict and analyse the sentiment of the text taken from the site, because so far, it's the only good one with a free API KEY. That said, you'll need to create a google account and create an API KEY to use this tool.
You can create this via the website ‘https://aistudio.google.com/app/apikey’.

**THIS ANALYSIS IS DONE USING A CHATBOT, SO ITS RESULTS MAY BE DIFFERENT FOR THE SAME NEWS ITEM EACH TIME IT IS RUN.**

# Downloads
 - [Python](https://www.python.org/downloads/)
 - We highly recommend using an [IDE](https://code.visualstudio.com/download) to run the code
 - [Code](https://github.com/Satera1/Website-Sentiment-Analysis.git’)

# How to use
 1. Download the zip code and extract it or clone it using the link ‘https://github.com/Satera1/Website-Sentiment-Analysis.git’.
 2. Change the link to the news site in quotes to `‘HTTPS_WEBSITE_LINK_HERE’` in the file `Web_Scrapping.py`.
 3. Create a Google Gemini AI API KEY via ‘https://aistudio.google.com/app/apikey’ and copy and paste the key in quotes into `"YOUR_GEMINI_API_KEY_HERE"` and change the name of the model you'll be using to `"gemini-pro"` if necessary (‘gemini-pro’ is used by default) in the file `Sentiment_Analysis.py`.
 4. Run the file `Sentiment_Analysis.py` and see the result in the terminal.
