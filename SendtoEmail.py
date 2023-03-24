import feedparser
import time
import openai
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# OpenAI credentials
openai.api_key = os.environ["Openai_SECRET"]
# Email credentials
email_address = "erichgellert@gmail.com"
email_password = os.environ["Gmail_SECRET"]
email_toaddress = "erichgellert@gmail.com"

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = email_address
SMTP_PASSWORD = email_password
EMAIL_FROM = email_address
EMAIL_TO = 'ailona@ailona.com; erichgellert@gmail.com; erich.gellert@microsoft.com; russ.rimmerman@microsoft.com'

# List of RSS feed URLs
feeds = []

with open('feeds.txt', 'r') as f:
    for line in f:
        feed_url = line.strip()
        feeds.append(feed_url)
print(feeds)

# Load the list of processed articles from the log file
with open('email_log.txt', 'r') as f:
    processed_urls = f.read().splitlines()

# Calculate the cutoff time as 24 hours ago
cutoff_time = time.time() - (10 * 24 * 60 * 60)

# Initialize a list to store the new article summaries
new_summaries = []

# Loop through each feed URL
for feed_url in feeds:
    # Parse the RSS feed using feedparser
    feed = feedparser.parse(feed_url)
    
    # Loop through each post in the feed
    for post in feed.entries:
        print(feed.channel.title)
        # Check if the post is new by comparing its published time to the cutoff time
        if time.mktime(post.published_parsed) > cutoff_time:
            # Check if the post has already been processed
            
            if post.link not in processed_urls:
                print(post.link)
                # Call the OpenAI API to generate a summary for the article
                summary = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"write a 120 character summary of the article below and include 5 bullet points:\n{post.link}",
                temperature=0.7,
                max_tokens=120,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
                ).choices[0].text # type: ignore

                # Add the summary to the list of new article summaries
                new_summaries.append(f"From the {feed.channel.title}\n{post.title}\n{summary}\n{post.link}\n")

                # Add the article URL to the list of processed articles
                processed_urls.append(post.link)

# Save the updated list of processed articles to the log file
with open('email_log.txt', 'w') as f:
    f.write('\n'.join(processed_urls))

# Send an email with the new article summaries
if new_summaries:
    # Create the email message
    message = MIMEMultipart()
    message['Subject'] = 'New MSFT Blog Articles Summaries from last days'
    message['From'] = EMAIL_FROM
    message['To'] = EMAIL_TO
    message.attach(MIMEText('\n'.join(new_summaries), 'plain'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
        smtp.sendmail(EMAIL_FROM, EMAIL_TO, message.as_string())
