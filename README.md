# Insights from team survey

Extract insights from the team survey data into a Slack message using OpenAI.

<p align="center">
  <img src="https://github.com/DidierRLopes/insights-from-team-survey/assets/25267873/7a867401-27b7-4228-867d-4d13fba792a8" alt="Example" width=600/>
</p>


## Example

This is what [OpenBB](http://openbb.co)'s team survey data looks like:

<p align="center">
  <img width="1351" alt="Screenshot 2023-07-04 at 7 43 09 PM" src="https://github.com/DidierRLopes/insights-from-team-survey/assets/25267873/57aeca64-88ee-4fa3-8ab7-76f05c0222a8">
</p>

```
$ python extract_insights_from_last_team_survey.py 
```

This is what you can expect for output in case of the script running successfully.
```
Loading environment variables...

Loading team survey data from Airtable...

Processing data from Airtable...

Extracting insights from team survey data...

Sending insights to Slack through a message...

SUCCESS: Message posted to Didier Lopes
```

<p align="center">
  <img src="https://github.com/DidierRLopes/insights-from-team-survey/assets/25267873/7a867401-27b7-4228-867d-4d13fba792a8" alt="Example" width=600/>
</p>

## Installation

1. Create new environment:
```
conda create --name insights
```

2. Activate new environment:
```
conda activate insights
```

3. Install python and poetry
```
conda install python poetry
```

4. Let poetry install all dependencies
```
poetry install
```

## Set your variables

Create an `.env` file and copy-paste:

```
SLACK_WEBHOOK_URL='REPLACEME'
SLACK_CHANNEL_NAME='REPLACEME'
AIRTABLE_API_KEY = 'REPLACEME'
AIRTABLE_BASE_ID = 'REPLACEME'
AIRTABLE_TABLE_NAME = 'REPLACEME'
OPENAI_API_KEY = "REPLACEME"
```

with `REPLACEME` being replaced by your own keys and tokens extracted from [Slack](https://api.slack.com/apps), [Airtable](https://airtable.com/create/tokens) and [OpenAI](https://platform.openai.com/account/api-keys), respectively. Note that for Airtable you will need details from the table you are trying to access information from.

