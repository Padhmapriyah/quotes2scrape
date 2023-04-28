# Quotes2Scrape Challenge
## Summary:

As per the requirement, we have to scrape the below given fields from http://quotes.toscrape.com/js/ using Scrapy and Splash because it requires JS execution.

quote

author

tags

### Pre-Requisite

Please install the pre-requisites modules.

Scrapy Framework: [scrapy](https://pypi.org/project/Scrapy)

Scrapy-Splash module to execute JS: [scrapy_splash](https://pypi.org/project/scrapy-splash/)

```
pip install scrapy

pip install scrapy-splash
```
You need to make sure that you have docker installed, and an instance of docker is running before starting the spider.

Use the below command to start the docker instance.

```
sudo docker run -it -p 8050:8050 scrapinghub/splash
```

### Steps:

You can create your own scrapy project:

```commandline
scrapy startproject quotes2scrape_challenge
scrapy genspider quotes2scrape http://quotes.toscrape.com
```

OR

You can clone this project as well

```
git clone https://github.com/Padhmapriyah/quotes2scrape.git
```
Once the spider is created or cloned the project, you can run the spider using the below command

```
scrapy crawl quotes2scrape -o quotes100.csv
```
Reference Documents:

https://splash.readthedocs.io/en/stable/

https://github.com/scrapy-plugins/scrapy-splash

https://docs.scrapy.org/en/latest/intro/tutorial.html

Screenshot for reference:

Starting.

![start_quotes](https://user-images.githubusercontent.com/132034355/235143824-6d043ac8-0cc0-479b-9261-9f334a0a5cbc.png)

Ending.
![end_quotes](https://user-images.githubusercontent.com/132034355/235143830-fedc7182-85ef-4b06-9285-3c0a1c83a066.png)
