# Jira Bot
Is a bot assistant GPT like bot that performs updates in a Jira instance.

## Setup

```bash
./setup.sh
source activate.sh
```

## Jupyter notebooks
```
source activate.sh
cd notebooks
jupyter notebook JiraToolkitTest.ipynb 
```

## JiraBot
```
source activate
cd jirabot
```

### Slack

1. Start ngrok and check traffic at http://127.0.0.1:4040
```
ngrok
```  

2. Start slackbot server
```
python slackbot.py
```

3. Talk to bot
on slack

### CLI
1. Run bot CLI
```
python cli.py
```

## Env

### Vars
Env vars saved in `jirabot/.env` and `notebooks/.env`

### OpenAI
APi Key: https://platform.openai.com/api-keys

### Slack config
Signing secret: https://api.slack.com/apps/A06ECDVGMGR/general  
API Token: https://api.slack.com/apps/A06ECDVGMGR/oauth  
App config: https://app.slack.com/app-settings/T06DUT7DE67/A06ECDVGMGR/app-manifest  
Manifest also comitted to `jirabot/slack/manifest.yml`  

### Ngrok

https://dashboard.ngrok.com/cloud-edge/endpoints 

