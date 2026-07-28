import tomllib
import urllib.parse
import webbrowser
import tomli_w
import os
from colorama import init, Fore, Back, Style
import webview

init(autoreset=True)

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

with open("Data/profile.toml", "rb") as f:
    profile = tomllib.load(f)
with open("Data/Data.toml", "rb") as f:
    data = tomllib.load(f)

while True:
    
    # Main menu
    
    clear_console()
    print("========================================================")
    print(Style.BRIGHT + Fore.RED + "          Search Assistant v0.2")
    print("========================================================")
    print("1. Continue to search")
    print("2. Settings")
    print("3. About")
    print("4. Exit")
    print("========================================================")
    print("Webview is currently set to: " + str(profile["User"]["Webview"]))
    choice = input("Enter your choice (1-4): ")
    
    # Search functionality
    
    if choice == "1":
        clear_console()
        search_query = input("Enter your search query: ")
        search_engine = profile["User"]["SearchEngine"]
        browser = profile["User"]["Browser"]
        
        browser_config = data["Browsers"].get(browser)
        search_engine_config = data["SearchEngines"].get(search_engine)
        
        browser_path = browser_config["path"] if browser_config else None
        search_url_template = search_engine_config["url"] if search_engine_config else None
        Webview_enabled = profile["User"]["Webview"]
        
        if Webview_enabled:
            webview.create_window("Search Assistant", search_url_template.format(query=urllib.parse.quote(search_query)), width=800, height=600)
            webview.start()
        else:
            webbrowser.register(browser, None, webbrowser.BackgroundBrowser(browser_path))
            webbrowser.get(browser).open(search_url_template.format(query=urllib.parse.quote(search_query)))
        
    # Settings menu    
    
    elif choice == "2":
        clear_console()
        print(Style.BRIGHT + Fore.GREEN + "Settings Menu")
        print("========================================================")
        print("1. Change search engine (Default: Google), now: " + profile["User"]["SearchEngine"])
        print("2. Change browser, now: " + profile["User"]["Browser"])
        print("3. Toggle webview (Default: True), now: " + str(profile["User"]["Webview"]))
        print("========================================================")
        settings_choice = input("Enter your choice (1-3): ")
        
        # Search engine
        if settings_choice == "1":
            print("Change search engine(1. Google, 2. Brave, 3. DuckDuckGo, 4. Bing, 5. Yahoo, 6. Yandex, 7. PerplexityAI, 8. Baidu)")
            search_engine_choice = input("Enter your choice (1-8): ")
            search_engine_mapping = {
                "1": "Google",
                "2": "BraveSearch",
                "3": "DuckDuckGo",
                "4": "Bing",
                "5": "Yahoo",
                "6": "Yandex",
                "7": "PerplexityAI",
                "8": "Baidu"
            }
            if search_engine_choice in search_engine_mapping:
                profile["User"]["SearchEngine"] = search_engine_mapping[search_engine_choice]
        
        # Browser
        elif settings_choice == "2":
            print("Change browser (1. Chrome, 2. Brave, 3. Firefox, 4. Edge, 5. Yandex, 6. Opera)")
            browser_choice = input("Enter your choice (1-6): ")
            browser_mapping = {
                "1": "Chrome",
                "2": "Brave",
                "3": "Firefox",
                "4": "Edge",
                "5": "Yandex",
                "6": "Opera"
            }
            if browser_choice in browser_mapping:
                profile["User"]["Browser"] = browser_mapping[browser_choice]
                
        # Webview
        elif settings_choice == "3":
            profile["User"]["Webview"] = not profile["User"]["Webview"]
            print("Webview is now set to: " + str(profile["User"]["Webview"]))
        
        # Save changes to profile.toml
        with open("profile.toml", "wb") as f:
            tomli_w.dump(profile, f)
            
    # About menu
    
    elif choice == "3":
        clear_console()
        print(Style.BRIGHT + Fore.YELLOW + "About Search Assistant")
        print("========================================================")
        print(Style.BRIGHT + Fore.CYAN + "Version: 0.2")
        print("Author: Justness23")
        print("Github: https://github.com/Justness23/Search-Assistance")
        print("YouTube: https://www.youtube.com/@Justness32")
        print("Discord: Soon")
        print("License: MIT License")
        print("This application allows you to search the web using your preferred search engine and browser.")
        print("========================================================")
        input("Press Enter to return to the main menu...")
    
    # Exit the program
    
    elif choice == "4":
        clear_console()
        print(Style.BRIGHT + Fore.MAGENTA + "Bye! Thank you for using Search Assistant.")
        break
