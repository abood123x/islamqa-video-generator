# IslamQA Video Generator

A Python-based tool that extracts Islamic questions and answers from IslamQA and automatically generates videos using MoviePy.

## Features

* Extracts questions and answers from IslamQA pages.
* Parses HTML using BeautifulSoup.
* Converts extracted text into video overlays.
* Uses a background video.
* Automatically generates an MP4 video.

## Technologies

* Python
* Requests
* BeautifulSoup
* lxml
* MoviePy

## Project Structure

```text
islamqa-video-generator/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository and install the required packages:

```bash
pip install -r requirements.txt
```

You also need ImageMagick installed and configured for MoviePy.

## Usage

Place a suitable background video in the project directory and name it:

```text
background.mp4
```

Then run:

```bash
python main.py
```

The generated video will be saved as:

```text
output.mp4
```

## How It Works

1. Sends a request to an IslamQA page.
2. Extracts the question and answer from the HTML.
3. Processes the extracted text.
4. Creates text clips using MoviePy.
5. Combines the text with a background video.
6. Exports the final video as an MP4 file.

## Learning Goals

This project was created as a practical Python project to learn:

* Web scraping
* HTML parsing
* HTTP requests
* Text processing
* Video automation
* Working with external Python libraries
