# Libs
import os
import tomllib
import tomli_w
from pathlib import Path

# Scripts
import command_processing

# Load Data
base_dir = Path(__file__).parent.parent
data_dir = base_dir / "Data"
        
with open(data_dir / "Data.toml", "rb") as f:
    data = tomllib.load(f)


with open(data_dir / "profile.toml", "rb") as f:
    profile = tomllib.load(f)

os.system('')
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

# Colors
green = "\033[92m" # Green
red = "\033[91m" # Red

# Banner & Menus

banner3 = r"""
 .----..----.  .--.  .---. .----..-. .-.      .--.   .----. .----..-. .----..-----. .--.  .-. .-..-----. 
{ {__-`} |__} / {} \ } }}_}| }`-'{ {_} |     / {} \ { {__-`{ {__-`{ |{ {__-``-' '-'/ {} \ |  \{ |`-' '-' 
.-._} }} '__}/  /\  \| } \ | },-.| { } }    /  /\  \.-._} }.-._} }| }.-._} }  } { /  /\  \| }\  {  } {   
`----' `----'`-'  `-'`-'-' `----'`-' `-'    `-'  `-'`----' `----' `-'`----'   `-' `-'  `-'`-' `-'  `-'                                                                                             
"""

help_menu = r"""
            
    Avaliable commands:
            
    [1] help - Shows this help message.
    [2] search/s query - to search.
    [3] settings - show settings menu
    [4] about - show about menu
    [5] fastsearchhelp/fsh - show fast commands
    [6] clear - clear console
            
            """

fast_help_menu = r"""
                        
        Avaliable commands:
                        
        [1] g - google search.      [7] pai - perplexity AI(need login to your account)
        [2] br - brave search.      [8] ba - baidu
        [3] ddg - duckduckgo        [9] wiki - wikipedia
        [4] b - bing                [10] yt - youtube
        [5] y - yahoo               [11] gh - github
        [6] ya - yandex             [12] tw - twitch
                        
            """

settings_menu = r"""

        Choose option:
        
        [1] Search engine
        [2] Webview
        
"""

current_search_engine = profile["User"]["SearchEngine"]

settings_search_engine = r"""

        Choose search engine(current: {current_search_engine}):
        
        [1] Google                 
        [2] Brave
        [3] DuckDuckGo
        [4] Bing
        [5] Yahoo
        [6] Yandex
        [7] PerplexityAI
        [8] Baidu
        
"""

about_menu = r"""

        About Search Assistant v 1.0.0
        
        Author: Justness23
        Github: https://github.com/Justness23/Search-Assistance
        YouTube: https://www.youtube.com/@Justness32
        Discord: Soon
        License: MIT License
        
"""

print(green + banner3)
print("Type 'help' to see the list of commands.")

# Main
def main_menu():
    while True:
        print()
        command = input(green + "SA>")
        result = command_processing.process_command(command)
        if result == "help":
            print(help_menu)
            
        elif result == "settings":
            print(settings_menu)
            settings_choice = input("SA> ")
            
            if settings_choice == "1":
                print(settings_search_engine)
                search_engine_choice = input("SA> ")
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
                print("Soon")
                
            else:
                print("Error: Unknown command, type 'help' to see a list of available commands")
                
        elif result == "about":
            print(about_menu)
            
        elif result == "fastsearchhelp":
            print(fast_help_menu)
            
        elif result == "clear":
            clear_console()
            print(green + banner3)
            print("Type 'help' to see the list of commands.")
            
        elif result == "Success":
            print(green + "Success")
            
        elif result == "error":
            print(red + "Error: Unknown command, type 'help' to see a list of available commands")
            
        else:
            print(red + "Error: Unknown command, type 'help' to see a list of available commands")
        
if __name__ == "__main__":
    main_menu()