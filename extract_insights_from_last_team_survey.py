import os
import json
import pandas as pd
import requests
import openai
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from dotenv import load_dotenv
from datetime import datetime, timedelta


def main():
    # ------- Environment Variables -------

    print("\nLoading environment variables...\n")
    load_dotenv()

    ## Slack API
    SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL') or "REPLACE-ME"
    SLACK_CHANNEL_NAME = os.getenv('SLACK_CHANNEL_NAME') or "REPLACE-ME"
    ## Airtable API
    AIRTABLE_API_KEY = os.getenv('AIRTABLE_API_KEY') or "REPLACE-ME"
    AIRTABLE_BASE_ID = os.getenv('AIRTABLE_BASE_ID') or "REPLACE-ME"
    AIRTABLE_TABLE_NAME = os.getenv('AIRTABLE_TABLE_NAME') or "REPLACE-ME"
    ## OpenAI API
    OPENAI_API_KEY= os.getenv('OPENAI_API_KEY') or "REPLACE-ME"

    # ------- Team survey data from Airtable -------

    print("Loading team survey data from Airtable...\n")

    response = requests.get(
        url=f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}',
        headers={'Authorization': f'Bearer {AIRTABLE_API_KEY}'}
    )

    # Check if the data has been loaded correctly
    if response.status_code == 200:
        data = response.json()["records"]
    else:
        print(f"Error: {response.status_code}")
        return 0

    print("Processing data from Airtable...\n")

    # Processing data from Airtable
    survey = [d["fields"] for d in data]
    df = pd.DataFrame(survey)

    df.drop(['Note'], axis=1, inplace=True)
    df['Current date'] = df['Current date'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d").strftime("%Y-%m"))
    df = df.sort_values("Current date")

    # ------- OpenAI to extract insights from this data -------

    print("Extracting insights from team survey data...\n")

    # Obtain most recent team survey and the month before
    # Current datetime 
    now = datetime.now()
    # We need to go back 2 weeks to get the last feedback we have which assume it was last month since we are assessing it one month after
    current_month = (now - timedelta(days=15)).strftime("%Y-%m")
    # We need to go back 2 weeks to get the last feedback we have which assume it was last month since we are assessing it one month after
    last_month = (now - timedelta(days=30+15)).strftime("%Y-%m")

    # Set OpenAI API key
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
            {"role": "system", "content": "You are a Chief of Staff with a MSc. in Data analysis and are trying to improve the culture of the company."},
            {"role": "user", 
            "content": 
                f"""
        This table represents the company survey for the previous month: {str(df[df["Current date"] == current_month])}

        This table represents the company survey for this month: {str(df[df["Current date"] == last_month])}.

        Based on this data, can you do 3 things:
        
        1. Summarize main differences since last month
        2. Summarize main highlights for current month
        3. Create suggestions for what could be done to improve those areas
        
        Please use the following format for the output:
            As the title use the following: Insights from team survey in {current_month}.
            Follow the title by 2 line breaks.
            Use bullet points within each of the points mentioned above.
            Between the 3 points, use 1 line breaks, a line with ----------------------- and another line break.
            Use `` when referring to a component like `Reward` or `Growth`.
            Do not use asterisks '*' or '**'.
            When referring to to Engineering or Product, Marketing, Design, Finance wrap them around asterisk, e.g. _Engineering_.
                """
            },
        ]
    )

    insight = response.choices[0].message.content

    # ------- Send insights to Slack -------

    print("Sending insights to Slack through a message...\n")

    payload = {
        'text': insight,
        'channel': SLACK_CHANNEL_NAME,
    }

    req = Request(SLACK_WEBHOOK_URL, json.dumps(payload).encode('utf-8'))
    try:
        response = urlopen(req)
        response.read()
        
        print(f"SUCCESS: Message posted to {payload['channel']}\n")
        return 1
    except HTTPError as e:
        print(f"Request failed: {e.code} {e.reason}\n")
        return 0
    except URLError as e:
        print(f"Server connection failed: {e.reason}\n")
        return 0


if __name__ == '__main__':
    main()