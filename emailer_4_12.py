import os
from email.message import EmailMessage
import ssl
import smtplib
from datetime import datetime, date
import pandas as pd

# Read in email list
def email_list():
    df = pd.read_csv(r'C:\Users\harke\OneDrive\Desktop\Python\quotes\input\email_list_test.csv')
    return df

# Email Body
def email_body(first_name, quote, author, new_quote, city, conditions, current_temp, hist_title, hist_body):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Am I HTML already?</title>
    </head>
    <body>
    <h1>Conrad Quotes!</h1>
    <p>Good morning, {first_name}!
    <p>Welcome to Conrad Quotes. Below are two quotes, one real, one artificially generated through text and sentiment analysis. <br>
    The text and sentiment analysis was performed on over five thousand quotes, which were all scraped from the web!</p>
    <p>The current weather condition in {city} is {conditions} and {current_temp} farhenheit.

    <h3>Quote of the day:</h3>
    <p>"{quote}"<br>
    <strong> - {author}</strong>

    <h3>AI quote of the day:</h3>
    <p>"{new_quote}"<br>
    <strong> - Artificial Intelligence</strong>

    <h2>Today in History</h2>
    <h4>{hist_title}</h4>
    <p>{hist_body}</p>
    <p></p>
    <h3>Development notes</h3>
    <ul>
        <li>Added temperature and weather conditions</li>
        <li>Added 'Today in History' which pulls events that happened this day in the past</li>
    </ul>        
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