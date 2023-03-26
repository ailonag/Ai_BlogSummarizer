# Ai Blog Summarizers
![ailonag_an_info_graphic_of_an_AI_robot_taking_in_an_RSS_feed_an_152da832 7865 4f2f ae46 59cb840773eb](https://user-images.githubusercontent.com/81778135/227051825-e9a664c1-d4fb-4234-8430-84a78b270754.jpg)

Tired of always missing Microsoft annoucements or too lazy to actually read the whole article. I was :).  Leveraging the power of Chat-GPT, these scipts will check a list of RSS Feeds for new posts and send them to ChatGPT to generate a summary of the article along with 5 bullet points then sends them to either Teams channel or Email.  

![image](https://user-images.githubusercontent.com/81778135/227434020-0e218e6e-79c9-498e-a759-b02b39c1d40f.png)

or run the SendtoEmail.py and get an email 
![image](https://user-images.githubusercontent.com/81778135/227434167-44d51c3a-5f94-4d56-96a6-b92dfe9eb6a5.png)


To use clone this repo and create your own open ai account and enviroment secrets so this can run in their own repro, please follow these steps:

1. Clone the repro and update the feeds.txt with your RSS Feed URLS
2. Modify the scripts with your email server  or the webhook url via secret,  and the Feeds.txt file with the RSS Feeds you would like. 
3. if you want to use gmail as your smtp follow the instructions here https://support.google.com/mail/answer/7126229 otherwise specify your own smtp server 
4. Go to https://openai.com/ and sign up for an account if you don't have one already. You will need an API key to access the OpenAI services.
5. In your OpenAI account dashboard, go to API Keys and click Create an API key. Copy the secret key that starts with sk_ and keep it safe.
6. In your local repo, Set secrets in Settings/Secrets/Actions -> 'New repository secret'. Use the same secret name inside the atction .yml and *.py
7. You have successfully cloned the repo and created your own environment secrets. You can now run the code in your own repro using Python 


If you want to scribe to this as a service to have the summaries emailed to you, Subscribe here https://subscribe.ailonalab.com/
