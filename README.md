# RSS Feed Summarizer with Chat-GPT
![ailonag_an_info_graphic_of_an_AI_robot_taking_in_an_RSS_feed_an_152da832 7865 4f2f ae46 59cb840773eb](https://user-images.githubusercontent.com/81778135/227051825-e9a664c1-d4fb-4234-8430-84a78b270754.jpg)



### Are you tired of missing Microsoft announcements or too lazy to read the whole article? These scripts use the power of Chat-GPT to check a list of RSS feeds for new posts, generate a summary of the article along with five bullet points, and send them to either a Teams channel or email.


![image](https://user-images.githubusercontent.com/81778135/227434020-0e218e6e-79c9-498e-a759-b02b39c1d40f.png)

lternatively, you can run SendtoEmail.py to receive an email instead.
![image](https://user-images.githubusercontent.com/81778135/227434167-44d51c3a-5f94-4d56-96a6-b92dfe9eb6a5.png)



### Prerequisites
Before you can use this project, you will need to:

1. Clone the repository to your local machine.
2. Create an account on OpenAI and obtain an API key to access their services.
3. Create environment secrets to run the code in your own repository.

## Usage
To use this project, follow these steps:

1. Update the feeds.txt file with the RSS feed URLs you want to monitor.
2. Modify the scripts with your email server or the webhook URL via secret, and the feeds.txt file with the RSS feeds you want to monitor.
3. If you want to use Gmail as your SMTP server, follow the instructions here. Otherwise, specify your own SMTP server.
4. Go to the OpenAI website and sign up for an account if you don't already have one. You will need an API key to access their services.
5. In your OpenAI account dashboard, go to "API Keys" and click "Create an API key". Copy the secret key that starts with sk_ and keep it safe.
5. In your local repository, set the following secrets in "Settings" > "Secrets" > "Actions" > "New repository secret":
    - OPENAI_API_SECRET_KEY: Use the API key you obtained from OpenAI.
    - SMTP_SERVER: Use the SMTP server you want to use for email notifications.
    - SMTP_PORT: Use the SMTP port number for your email server.
    - SMTP_USERNAME: Use the username for your email server.
    - SMTP_PASSWORD: Use the password for your email server.
    - RECIPIENT_EMAIL: Use the email address where you want to receive the summaries.
6. Run the code in your own repository using Python.

**That's it! You can now sit back and let Chat-GPT summarize your favorite RSS feeds for you.

**If you want to subscribe to this as a service to receive summaries of Microsoft blogs via email, go to https://subscribe.ailonalab.com/ and follow the instructions.**
