import os
from email.message import EmailMessage
import ssl
import smtplib
from datetime import datetime, date
import pandas as pd

# Read in email list
def email_list():
    df = pd.read_csv(r'C:\Users\harke\OneDrive\Desktop\Python\quotes\input\email_list_macy.csv')
    return df

# Email Body
def email_body(first_name, quote, author, new_quote, city, weather_conditions, hist_title, hist_body):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Am I HTML already?</title>
        </head>
        <body>
            <div style="background-color:rgb(255,255,255); padding:10px 20px; width:65%; margin-left:auto; margin-right:auto; border-radius: 6px;">
                <h1 style="text-align: center; font-family:sans-serif; color:rgb(145, 76, 76);"><strong>Conrad Quotes!</strong></h1>
            </div>
            <div style="padding:10px 20px; width:75%; margin-left:auto; margin-right:auto;">
                <table style="border-collapse: separate; border-radius: 6px; letter-spacing: 1px; font-size: 0.8rem; margin-left: auto; margin-right: auto; table-layout: fixed; width: 65%;">
                    <caption style="border: 1px solid rgb(190,190,190);  background-color: rgb(145, 76, 76); font-size: 1.0rem; padding: 10px 16px; border-collapse: separate; border-radius: 6px; color: rgb(245,245,245)"><strong>{city} Weather Report</strong></caption>
                        <tr style="background-color: rgb(119, 104, 104);">
                            <th style="border: 1px solid rgb(190,190,190); padding: 8px 16px; border-collapse: separate; border-radius: 6px; color: rgb(245,245,245)">Temperature</th>
                            <th style="border: 1px solid rgb(190,190,190); padding: 8px 16px; border-collapse: separate; border-radius: 6px; color: rgb(245,245,245)">Condition</th>
                            <th style="border: 1px solid rgb(190,190,190); padding: 8px 16px; border-collapse: separate; border-radius: 6px; color: rgb(245,245,245)">High</th>
                            <th style="border: 1px solid rgb(190,190,190); padding: 8px 16px; border-collapse: separate; border-radius: 6px; color: rgb(245,245,245)">Low</th>
                            <th style="border: 1px solid rgb(190,190,190); padding: 8px 16px; border-collapse: separate; border-radius: 6px; color: rgb(245,245,245)">Humidity</th>
                            <th style="border: 1px solid rgb(190,190,190); padding: 8px 16px; border-collapse: separate; border-radius: 6px; color: rgb(245,245,245)">UV Index</th>
                        </tr>
                        <tr style = "background-color:rgb(212, 201, 201)">
                            <td style="border: 1px solid rgb(190,190,190); padding: 10px 16px; border-collapse: separate; border-radius: 6px; text-align: center;"><strong>{weather_conditions[0]}</strong></td>
                            <td style="border: 1px solid rgb(190,190,190); padding: 10px 16px; border-collapse: separate; border-radius: 6px; text-align: center;"><strong>{weather_conditions[1]}</strong></td>
                            <td style="border: 1px solid rgb(190,190,190); padding: 10px 16px; border-collapse: separate; border-radius: 6px; text-align: center;"><strong>{weather_conditions[2]}</strong></td>
                            <td style="border: 1px solid rgb(190,190,190); padding: 10px 16px; border-collapse: separate; border-radius: 6px; text-align: center;"><strong>{weather_conditions[3]}</strong></td>
                            <td style="border: 1px solid rgb(190,190,190); padding: 10px 16px; border-collapse: separate; border-radius: 6px; text-align: center;"><strong>{weather_conditions[4]}</strong></td>
                            <td style="border: 1px solid rgb(190,190,190); padding: 10px 16px; border-collapse: separate; border-radius: 6px; text-align: center;"><strong>{weather_conditions[5]}</strong></td>
                        </tr>
                </table>
            </div>
            <br>
            <!-- CONRADS QUOTES SECTION -->
            <div style="background-color:rgb(238, 231, 231); padding:10px 20px; width:55%; margin-left:auto; margin-right:auto;">
                <div>
                    <p>Good morning, {first_name}!</p>
                    <p>Welcome to Conrad Quotes. Below are two quotes, one real, one artificially generated through text and sentiment analysis. The text and sentiment analysis was performed on over five thousand quotes, which were all scraped from the web!</p>
                </div>
                <br>
                <div style="text-align: center; padding:10px 20px; width:45%; margin-left:auto; margin-right:auto; border-radius: 6px;">
                    <div>
                        <h3>Quote of the day:</h3>
                            <p>"{quote}"<br>
                        <strong> - {author}</strong></p>
                    </div>
                    <br>
                    <br>
                    <div>
                        <h3>AI quote of the day:</h3>
                            <p>"{new_quote}"<br>
                        <strong> - Artificial Intelligence</strong></p>
                    </div>
                </div>
            </div>
            <br>
            <!-- TODAY IN HISTORY -->
            <div style="background-color: rgb(238, 231, 231); padding:10px 20px; width:55%;  margin-left:auto; margin-right:auto;">
            <h2>Today in History</h2>
            <h4>{hist_title}</h4>
            <p>{hist_body}</p>
            </div>
            <!-- DEVELOPMENT NOTES -->
            <br>
            <div style = " width:55%;  margin-left:auto; margin-right:auto;">
                <h3>Development notes</h3>
                    <ul>
                        <li>Pushed 'inline' html formatting as much as I could</li>
                        <li>Added temperature and weather conditions</li>
                        <li>Added 'Today in History' which pulls events that happened this day in the past</li>
                </ul>  
            </div>      
        </body>
    </html>
    """

# Email Subject
def email_subject(today):
    return f'Conrad Quotes {today}'

# Send emails
def email_sender(email_receiver, body, subject):
    today = date.today()

    email_sender = 'conradquotes@gmail.com'
    email_password = 'dnidbvnvasftbium'

    em = EmailMessage()

    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body, subtype='html')

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', port = 465, context = context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(em)