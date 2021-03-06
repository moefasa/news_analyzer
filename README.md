# News Articles Recommender and Analyzer

[![Build Status](https://travis-ci.org/heybaebae/news_analyzer.svg?branch=master)](https://travis-ci.org/heybaebae/news_analyzer)
[![Coverage Status](https://coveralls.io/repos/github/heybaebae/news_analyzer/badge.svg?branch=master)](https://coveralls.io/github/heybaebae/news_analyzer?branch=master)

## Background  
 
 Conventional news recommendation systems use a small set of keywords to identify the top recommended articles to users based on keywords frequency. We built upon this framework by enabling users to find recommended articles by providing an entire news article. The recommendation process uses article topics to evaluate which articles to recommended. 

Our system highlights topic insights through two different models: an unguided LDA for identifying topic recommended articles and a guided LDA with seed words from NYTimes to show interpretable topics. Our system also shows sentiment information and word cloud that summarize the query article for the user.


> #todo: Add screenshot of UI    
  
NARA does 3 things:
* Recommends news articles based on topic relevance
* Analyzes sentiment of news articles
* Visualizes news articles

How does it work?
* Takes user input query article or keyword/phrases from UI
* Recommends relevant articles from corpus using LDA
* Lists relevant topics for query article
* Presents sentiment analysis based on number of positive/negative/neutral sentences in input
* Visualizes query article using word cloud

*For more details, please see*: [FunctionalDesign.md](doc/FunctionalDesign.md)

## Examples  
> #todo: Need content  


## Data

The corpus comes from Kaggle dataset:
https://www.kaggle.com/snapcrack/all-the-news

It consists of over 140,000 articles from 15 US national publishers between 2015 - 2017. 

The New York Times API:
https://developer.nytimes.com

We used labelled article information from the New York Times to seed words for the guided LDA. We aggregated and analyzed the article titles, summaries and categories from a series of days to generate the list of seed words.


## Component Design  
![ComponentDesignFlowChart](doc/news-nlp-flowchart-2.png?raw=true)  
*For more details, please see*: [ComponentDesign.md](doc/ComponentDesign.md)

## Directory Structure
> #todo: Need content (run 'tree')

## Prerequistes and Setup  
> #todo: Need content  


## Team:WeReadTheNews
MS Data Science, University of Washington  
DATA 515 Software Design for Data Science (Spring 2018)  

Team members:  
 * [Ryan Bae](http://www.linkedin.com/in/ryanbae89)    
 * [Crystal Ding](https://www.linkedin.com/in/yumeng-crystal-ding)  
 * [Charles Duze](https://www.linkedin.com/in/charlesduze)    
 * [Mohammed Helal](https://www.linkedin.com/in/mohammed-helal-78969566)   
 * [Paul Wright](https://www.linkedin.com/in/paulcharleswright)     

 
