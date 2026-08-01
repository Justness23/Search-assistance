# Libs
from pathlib import Path
import tomllib
import webview

# Load Data
base_dir = Path(__file__).parent.parent
data_dir = base_dir / "Data"
        
with open(data_dir / "Data.toml", "rb") as f:
    data = tomllib.load(f)
    
with open(data_dir / "profile.toml", "rb") as f:
    profile = tomllib.load(f)

fast_search_keywords = data["FastSearhKeywords"].keys()

# Main
def process_command(command):
    FastSearchKeyword = command.partition(" ")[0]
    if command == "help":
        return "help"
    elif command == "search" or command == "s":
        query = command.partition(" ")[2]
        current_search_engine = profile["User"]["SearchEngine"]
        webview.create_window("Search Assistant", data["SearchEngines"][current_search_engine]["url"].format(query=query), width=800, height=600)
        webview.start()
        return "Success"
    elif command == "settings":
        return "settings"
    elif command == "about":
        return "about"
    elif command == "fastsearchhelp" or command == "fsh":
        return "fastsearchhelp"
    elif FastSearchKeyword in fast_search_keywords:
        query = command.partition(" ")[2]
        webview.create_window("Search Assistant", data["FastSearhKeywords"][FastSearchKeyword]["url"].format(query=query), width=800, height=600)
        webview.start()
        return "Success"
    elif command == "clear":
        return "clear"
    else:
        return "error"