# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import base64
import pandas as pd
import os
import numpy as np
import flask

import handler

app = dash.Dash()
image_filename = '/Users/paulwright/Dropbox/UW/2018_s_DATA515/Project/UI_Testing/WC_Image.png' # replace with your own image
#encoded_image = base64.b64encode(open(image_filename, 'rb').read())
#encoded_image2 = base64.b64encode(open('img_test2.jpg', 'rb').read())
my_handler = handler.Handler()

#image_filename = static_image_route
encoded_image = base64.b64encode(open(image_filename,'rb').read())
#image_filename = 'WC_Image.png' # replace with your own image
#encoded_image = base64.b64encode(open(image_filename, 'rb').read())

static_image_route = '/Users/paulwright/Dropbox/UW/2018_s_DATA515/Project/UI_Testing/WC_Image.png'
app.layout = html.Div([
    
])

# Reusable
def make_dash_table(df):
    ''' Return a dash definition of an HTML table for a Pandas dataframe '''
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table

app.layout = html.Div([
    html.H2(["News Articles Analyzer"],
                    className="padded"),
    dcc.Textarea(value = "art photo picture performance theatre", #placeholder = "Enter text / article here...", 
        style = {'width': '100%'}, id='input-1-state'),#, type='text', value='Montréal'),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Div(id='output-state'),
    html.Div(id='output-state2'),
    #html.Img(src='data:image/png;base64,{}'.format(encoded_image)),
    #html.Img(src='data:image/png;base64,{}'.format(encoded_image)),
    html.Div([
        html.Div([
            html.H6(["Recommended Articles"],
                    className="gs-header gs-table-header padded"),
            html.Table(make_dash_table(
                            pd.DataFrame(np.asarray([['first article title','NYTimes'],
                                                    ['second article title','Breitbart'],
                                                    ['third article title','NY Post']]))
                                       ))
            ], id = "recommended_articles", className="six columns"),
        html.Div([
            
            html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
                     width='100%')
            #html.Img(src='https://www.w3schools.com/images/w3schools_green.jpg', 
            #     #height='142', 
            #     width='50%', 
            #     alt = "word cloud image?",
            #     id = "wc_image")
        ], id = "wc_image", className="six columns")
    ], className="row "),
    html.Div([
        html.Div([
            html.H6(["Article Sentiment"],
                    className="gs-header gs-table-header padded"),
            html.Table(make_dash_table(pd.DataFrame(np.asarray([['a','aa'],
                                                    ['b','aa'],
                                                    ['c','aa']]))))
            ], id = 'article_sentiment',className="six columns"),
        html.Div([
            html.H6(["Top Topics"],
                    className="gs-header gs-table-header padded"),
            html.Table(make_dash_table(pd.DataFrame(np.asarray([]))))
            ], id = 'top_topics',className="six columns")
    ], className="row ")
    #html.Div([
    #    html.Img(src='https://www.w3schools.com/images/w3schools_green.jpg', 
    #         height='142', 
    #         width='104', 
    #         alt = "test image")
    #], className="ten columns padded")

        
], className="page")

# WC_image.png
# img_test2.jpg


@app.callback(Output('output-state', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('input-1-state', 'value')])

def update_output(n_clicks, input1):
    return u'''
        The Button has been pressed {} times,
        Input 1 is "{}"
    '''.format(n_clicks, input1)

# Recommended Articles Data

@app.callback(Output('recommended_articles', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('input-1-state', 'value')])

def update_recommended_articles(n_clicks, query_article):
    recommended_articles = my_handler.get_recommended_articles(query_article)
    return [
            html.H5(["Recommended Articles"],
                    className="gs-header gs-table-header padded"),
            html.Table(make_dash_table(pd.DataFrame(recommended_articles)))
            ]

# Article Sentiment Data
@app.callback(Output('article_sentiment', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('input-1-state', 'value')])

def update_sentiment_information(n_clicks, query_article):
    sentiment_score = my_handler.get_sentiment(query_article)
    sentiment_df = pd.DataFrame(np.asarray([['Positive Sentences:',sentiment_score['Positive_Sentences']],
                            ['Neutral Sentences:',sentiment_score['Neutral_Sentences']],
                            ['Negative Sentences:',sentiment_score['Negative_Sentences']]]))
    return [
            html.H5(["Article Sentiment"],
                    className="gs-header gs-table-header padded"),
            html.Table(make_dash_table(sentiment_df))
            ]

# Top Topics
@app.callback(Output('top_topics', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('input-1-state', 'value')])

def update_top_topics(n_clicks, query_article):
    top_topics = pd.DataFrame(my_handler.get_topics(query_article)[0])
    return [
            html.H5(["Top Topics"],
                    className="gs-header gs-table-header padded"),
            html.Table(make_dash_table(top_topics))
            ]

# Word Cloud Image
@app.callback(Output('wc_image', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('input-1-state', 'value')])

def update_word_cloud_image(n_clicks, query_article):
    word_cloud_image = my_handler.get_word_cloud(query_article)#.to_image().convert('RGB')
    #.to_bytes(encoder_name='raw')
    print(type(word_cloud_image))
    print(type(encoded_image))
    #pd.DataFrame(my_handler.get_topics(query_article)[0])
    return [
            html.Img(src='data:image/png;base64,{}'.format(word_cloud_image.decode()),
                     width='100%')
            #html.Img(src='https://www.w3schools.com/images/w3schools_green.jpg', 
            #     #height='142', 
            #     width='50%', 
            #     alt = "word cloud image?",
            #     id = "wc_image")
        ]

external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://codepen.io/bcd/pen/KQrXdb.css",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

for css in external_css:
    app.css.append_css({"external_url": css})

external_js = ["https://code.jquery.com/jquery-3.2.1.min.js",
               "https://codepen.io/bcd/pen/YaXojL.js"]

for js in external_js:
    app.scripts.append_script({"external_url": js})

if __name__ == '__main__':
    app.run_server(debug=True)
    
    
    