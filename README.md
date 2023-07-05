# Insights from team survey

Extract insights from the team survey data into a Slack message using OpenAI.

<p align="center">
  <img src=https://github.com/DidierRLopes/insights-from-team-survey/assets/25267873/62ae658e-6d4f-4fd1-88e8-241a36dd65ab alt="Example" width=600/>
</p>

## Example

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
  <img src="https://github.com/DidierRLopes/insights-from-team-survey/assets/25267873/62ae658e-6d4f-4fd1-88e8-241a36dd65ab" alt="Example"/>
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

