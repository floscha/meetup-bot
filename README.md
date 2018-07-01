![meetup-bot logo](logo.png)

# Meetup Bot

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7a0bdd2c2c9140cc9c8d5d22128a4628)](https://www.codacy.com/app/floscha/meetup-bot?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=floscha/meetup-bot&amp;utm_campaign=Badge_Grade)

## Feature Roadmap

- [x] Query [Meetup API](https://www.meetup.com/meetup_api) from Python.
- [x] Access above functionality using a [Slack chatbot](https://api.slack.com/bot-users).
- [x] Make interactions more natural by integrating [Dialogflow](https://dialogflow.com/).

## Setup

1. Set the environmental variable `MEETUP_API_KEY` to [your key](https://secure.meetup.com/meetup_api/key/) (requires being logged in):
```
export MEETUP_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

2. Set the environmental variable `SLACK_BOT_TOKEN` to your `Bot User OAuth Access Token` from [Slack API](https://api.slack.com/):
```
export SLACK_BOT_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
3. Install all dependencies:
```
pip install -r requirements.txt
```

## Supported commands

- `find <text> group in <country>`
  - Find meetup groups in an (optional) country
- `find <text> meetups in <country>`
  - Find meetup events in an (optional) country
