# ChatGPT Plugin - Data Analysis Assistant

This plugin is a data analysis assistant for ChatGPT. It allows you to easily analyze your data and get insights about it.

## Setup

1. Preparation environment
```bash
pip install -r requirements.txt
```

2. Link your database
update your database information in `.env.example` and rename it to `.env`


3. run the plugin
```bash
python main.py
```

## Usage

1. Navigate to https://chat.openai.com.
2. Select "Develop your own plugin"
3. Enter in `localhost:1163`, then select "Find manifest file".

You can start with a question like "Get all Table Structure about the dataset." or "Write an SQL: XXXX and execute it" 

