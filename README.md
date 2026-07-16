# Blog Content Generator with Cohere AI

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blogmobileapp3.streamlit.app/)
[![GitHub](https://img.shields.io/badge/View%20on-GitHub-181717?logo=github&style=flat-square)](https://github.com/gituserc1140/BlogMobileApp3)
[![Sponsor me on GitHub](https://img.shields.io/badge/Sponsor%20me%20on-GitHub-EA4AAA?logo=githubsponsors&style=flat-square)](https://github.com/sponsors/gituserc1140)

A Streamlit web app that generates blog posts on any topic using the [Cohere](https://cohere.com) AI API. Enter a topic, pick a model, and get a ready-to-download Markdown blog post in seconds.

## Features

- API key entered securely in the sidebar settings panel
- Choose from multiple [Cohere](https://cohere.com) command models
- Enter any blog topic and set your desired length
- Generate polished blog content with one click
- Download the result as a Markdown file

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`

## Usage

1. Open the **Settings** sidebar and enter your [Cohere API key](https://cohere.com)
2. Select a compatible Cohere model
3. Enter a blog topic in the main area
4. Adjust the token length if needed
5. Click **Generate Blog** to see your post

## Notes

- You need a valid [Cohere](https://cohere.com) API key — sign up for free at cohere.com
- The app uses the Cohere Chat API with the selected command model
