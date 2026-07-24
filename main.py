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
        
        browser_path = ""
        if browser == "Chrome":
            browser_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        elif browser == "Brave":
            browser_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
        
        search_url = ""
        if search_engine == "Google":
            search_url = f"https://www.google.com/search?q={urllib.parse.quote(search_query)}"
        elif search_engine == "Brave":
            search_url = f"https://search.brave.com/search?q={urllib.parse.quote(search_query)}"
        elif search_engine == "DuckDuckGo":
            search_url = f"https://duckduckgo.com/?q={urllib.parse.quote(search_query)}"
            
        webbrowser.register(browser, None, webbrowser.BackgroundBrowser(browser_path))
        webbrowser.get(browser).open(search_url)
        
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
            print("Change search engine(1. Google, 2. Brave, 3. DuckDuckGo)")
            search_engine_choice = input("Enter your choice (1-3): ")
            if search_engine_choice == "1":
                profile["User"]["SearchEngine"] = "Google"
            elif search_engine_choice == "2":
                profile["User"]["SearchEngine"] = "Brave"
            elif search_engine_choice == "3":
                profile["User"]["SearchEngine"] = "DuckDuckGo"
        
        elif settings_choice == "2":
            print("Change browser (1. Chrome, 2. Brave)")
            browser_choice = input("Enter your choice (1-2): ")
            if browser_choice == "1":
                profile["User"]["Browser"] = "Chrome"
            elif browser_choice == "2":
                profile["User"]["Browser"] = "Brave"
        
        with open("profile.toml", "wb") as f:
            tomli_w.dump(profile, f)
    
    # Exit the program
    
    elif choice == "3":
        clear_console()
        break
