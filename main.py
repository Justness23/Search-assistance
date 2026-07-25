import tomllib
import urllib.parse
import webbrowser
import tomli_w
import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

with open("profile.toml", "rb") as f:
    profile = tomllib.load(f)
with open("Data.toml", "rb") as f:
    data = tomllib.load(f)

while True:
    
    # Main menu
    
    clear_console()
    print("========================================================")
    print("Welcome to search assistant! v0.1")
    print("1. Continue to search")
    print("2. Settings")
    print("3. Exit")
    print("========================================================")
    choice = input("Enter your choice (1-3): ")
    
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
         
        webbrowser.register(browser, None, webbrowser.BackgroundBrowser(browser_path))
        webbrowser.get(browser).open(search_url_template.format(query=urllib.parse.quote(search_query)))
        
    # Settings menu    
    
    elif choice == "2":
        clear_console()
        print("========================================================")
        print("Settings Menu")
        print("1. Change search engine (Default: Google)")
        print("2. Change browser (Default: Chrome)")
        print("3. Back to main menu")
        print("========================================================")
        settings_choice = input("Enter your choice (1-3): ")
        
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
        
        with open("profile.toml", "wb") as f:
            tomli_w.dump(profile, f)
    
    # Exit the program
    
    elif choice == "3":
        clear_console()
        break
