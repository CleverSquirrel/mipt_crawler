FROM python:3.10.2-bullseye

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN python -m pip install -r requirements.txt
COPY . /app

WORKDIR /app/DOCrawler
ENTRYPOINT scrapy crawl post
