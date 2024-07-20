from emailer import email_list, email_sender, email_body, email_subject
from quote_generator import new_quote_generator, random_quote_generator
from datetime import datetime, date
from history_scraper import history_scraper
from weather_scraper import weather_scraper

if __name__ == "__main__":
    today = date.today()

    list = email_list()

    print(f"\nAI Quote:")
    while True:
        new_quote = new_quote_generator()

        print(f"\n{new_quote}")
        response = input("Is this AI quote solid? (y/n)")

        if response.lower() == "y":
            break
        elif response.lower() == "n":
            continue
        else:
            print("Invalid response, please enter 'y' or 'n'.")
            continue
    
    print(f"\nRandom Quote:")
    while True:
        quote, author = random_quote_generator()

        print(f"\n{quote}")
        response = input("Is this real quote solid? (y/n)")

        if response.lower() == "y":
            break
        elif response.lower() == "n":
            continue
        else:
            print("Invalid response, please enter 'y' or 'n'.")
            continue

    hist_title, hist_body = history_scraper()

    for index, rec in list.iterrows():
        print(f"{index + 1}: {rec['FIRST_NAME']} {rec['LAST_NAME']}\n")
        
        weather_conditions = weather_scraper(rec['WEATHER_URL'])

        email_sender(email_receiver = rec["EMAIL"], 
                     body = email_body(rec["FIRST_NAME"], quote, author, new_quote, rec['CITY'], weather_conditions, hist_title, hist_body), 
                     subject = email_subject(today))