import feedparser
import time
import openai
import requests
import os

# OpenAI API key
openai.api_key = os.environ["Openai_SECRET"]

# Microsoft Teams webhook URL
webhook_url = "https://microsoft.webhook.office.com/webhookb2/c0432061-e985-4dc3-bfb9-0b04c8892c32@72f988bf-86f1-41af-91ab-2d7cd011db47/IncomingWebhook/6cbf6e172b1240c187097e924bd93575/ffe2077a-4d39-409d-8780-4ae313e5454f"

# List of RSS feed URLs
feeds = []

with open('feeds.txt', 'r') as f:
    for line in f:
        feed_url = line.strip()
        feeds.append(feed_url)
print(feeds)

# Load the list of processed articles from the log file
with open('teams_log.txt', 'r') as f:
    processed_urls = f.read().splitlines()

# Calculate the cutoff time as 24 hours ago
cutoff_time = time.time() - (1 * 24 * 60 * 60)

# Initialize a list to store the new article summaries
new_summaries = []

# Loop through each feed URL
for feed_url in feeds:
    # Parse the RSS feed using feedparser
    feed = feedparser.parse(feed_url)

    # Loop through each post in the feed
    for post in feed.entries:
        # Check if the post is new by comparing its published time to the cutoff time
        if time.mktime(post.published_parsed) > cutoff_time:
            # Check if the post has already been processed
            if post.link not in processed_urls:
                print(post.link)
                # Call the OpenAI API to generate a summary for the article
                summary = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"write a 200 character summary of the article below and include 5 highlight bullet points. please format your response in markdown syntax:\n{post.link}",
                temperature=0.7,
                max_tokens=420,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
                ).choices[0].text # type: ignore

                # Add the summary to the list of new article summaries
                new_summaries.append(f"^From the {feed.channel.title}^\n\n**{post.title}**\n{summary}\n\n{post.link}\n\n------\n\n")

                # Add the article URL to the list of processed articles
                processed_urls.append(post.link)
                #print(summary)

# Save the updated list of processed articles to the log file
with open('teams_log.txt', 'w') as f:
    f.write('\n'.join(processed_urls))

# Post a message to Microsoft Teams with the new article summaries
if new_summaries:
    message = {
        "text": "New Article Summaries\n\n" + '\n'.join(new_summaries) 
    }
    response = requests.post(webhook_url, json=message)
    response.raise_for_status()