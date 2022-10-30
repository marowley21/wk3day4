import requests,json
from colorama import Fore, Style
import os
import time


class Bored():
    def __init__(self):
        self.min_price = 0
        self.max_price = 0

    def find_activity():
        while True:
            os.system('cls')
            min_price = input("What is you minimum price? Number between 0 and 1, 'q' to Quit: ")
            if min_price == 'q':
                os.system('cls')
                break
            os.system('cls')
            max_price = input("What is you maximum price? Number between 0 and 1, 'q' to Quit: ")
            if max_price == 'q':
                os.system('cls')
                break
            url= f"http://www.boredapi.com/api/activity?minprice={min_price}&maxprice={max_price}"
            response = requests.get(url)
            data = response.json()
            os.system('cls')
            print(Fore.BLUE + f'Activity: {data["activity"]}')
            print(Fore.RED + f'Type: {data["type"]}')
            print(Fore.YELLOW + f'Participants: {data["participants"]}')
            print(Fore.GREEN + f'Price: ${data["price"]}')
            print(Style.RESET_ALL)
            while True:
                answer = input("'q' to Quit: ")
                if answer.lower().strip() == 'q':
                    break
                else:
                    print("Invalid input, please try again")
            break

    def main():
        os.system('cls')
        while True:
            os.system('cls')
            answer = input("Would you like to find an activity or quit? 'f' to find activity 'q' to quit: ")
            if answer.lower().strip() == 'q':
                os.system('cls')
                print("Goodbye")
                break
            elif answer.lower().strip() == 'f':
                Bored.find_activity()
Bored.main()