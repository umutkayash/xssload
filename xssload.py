import argparse
from lib.helper.helper import *
from lib.helper.Log import *
from lib.core import *
from random import randint
from lib.crawler.crawler import *

epilog = """
Github: x
"""

logo = """
                          _..._      .-'''-.                                     .-'''-.                           _..._                     
                       .-'_..._''.  '   _    \_______                           '   _    \                      .-'_..._''.            .---. 
                     .' .'      './   /` '.   \  ___ `'.        __.....__     /   /` '.   \              .--. .' .'      '..--.        |   | 
                    / .'         .   |     \  '' |--.\  \   .-''         '.  .   |     \  '  _.._    _.._|__|/ .'          |__|        |   | 
                   . '           |   '      |  | |    \  ' /     .-''"'-.  `.|   '      |  .' .._| .' .._.--. '            .--.        |   | 
                   | |           \    \     / /| |     |  /     /________\   \    \     / /| '     | '   |  | |            |  |   __   |   | 
.--------..--------| |            `.   ` ..' / | |     |  |                  |`.   ` ..' __| |__ __| |__ |  | |            |  |.:--.'. |   | 
|____    ||____    . '               '-...-'`  | |     ' .\    .-------------'   '-...-'|__   __|__   __||  . '            |  / |   \ ||   | 
    /   /     /   / \ '.          .            | |___.' /' \    '-.____...---.             | |     | |   |  |\ '.          |  `" __ | ||   | 
  .'   /    .'   /   '. `._____.-'/           /_______.'/   `.             .'              | |     | |   |__| '. `._____.-'|__|.'.''| ||   | 
 /    /___ /    /___   `-.______ /            \_______|/      `''-...... -'                | |     | |          `-.______ /   / /   | |'---' 
|         |         |           `                                                          | |     | |                   `    \ \._,\ '/     
|_________|_________|   
"""

def check(getopt):
    payload = int(getopt.payload_level)
    if payload > 6 and getopt.payload is None:
        Log.info("Do you want use custom payload (Y/n)?")
        answer = input("> ")
        if answer.lower().strip() == "y":
            Log.info("Write the XSS payload below")
            payload = input("> ")
        else:
            payload = core.generate(randint(1, 6))
    else:
        payload = core.generate(payload)
    return payload if getopt.payload is None else getopt.payload

def interactive_menu():
    print(logo)
    print("Welcome to XSSLoad")
    print("What would you like to do?")
    options = [
        "1. Target a URL for scanning (-u)",
        "2. Single URL scan (--single)",
        "3. Set custom payload (--payload)",
        "4. Set payload level (--payload-level)",
        "5. Set depth for web crawling (--depth)",
        "7. Exit"
    ]
    for option in options:
        print(option)
    choice = input("\nEnter the number of your choice: ").strip()
    return choice

def handle_choice(choice):
    if choice == "1":
        url = input("Enter the target URL (e.g., http://testphp.vulnweb.com): ").strip()
        depth = input("Enter depth for crawling (default is 2): ").strip() or "2"
        return {"u": url, "depth": int(depth)}
    elif choice == "2":
        single = input("Enter the single URL for scanning: ").strip()
        return {"single": single}
    elif choice == "3":
        payload = input("Enter your custom payload (e.g., <script>alert(2005)</script>): ").strip()
        return {"payload": payload}
    elif choice == "4":
        level = input("Enter payload level (1-6, 7 for custom): ").strip()
        return {"payload_level": int(level)}
    elif choice == "5":
        depth = input("Enter depth for web crawling: ").strip()
        return {"depth": int(depth)}
    elif choice == "7":
        print("\nThis is the XSSLoad tool.\n" + epilog)
        return None
    elif choice == "6":
        print("Exiting. Goodbye!")
        exit()
    else:
        print("Invalid choice, please try again.")
        return None

def start():
    while True:
        choice = interactive_menu()
        args = handle_choice(choice)
        if args:
            Log.info("Starting with the selected options...")
            # Replace this with logic to process `args` as needed
            print(f"Options selected: {args}")
        else:
            continue

if __name__ == "__main__":
    start()