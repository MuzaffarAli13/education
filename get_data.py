import pandas as pd
import requests
from io import StringIO
from agents import function_tool
from dotenv import load_dotenv
import os
load_dotenv()

@function_tool
def get_all_students_data_from_sheet() -> list:
    """
    Retrieves all complaints from the Google Sheet and returns them as a list of dictionaries.
    Each dictionary contains: name, complaint_type, complaint_detail.
    """
    sheet_url = "https://docs.google.com/spreadsheets/d/1tHXDBKJZJzY2fdSaZ3ysPH1ChumrgOmKtdizrcr8kHA/export?format=csv&gid=0"
    
    # if admin_pin != os.getenv("PIN"):
    #     return [{"error": "Access Denied. Valid admin PIN required."}]
    
    response = requests.get(sheet_url)
    
    if response.status_code != 200:
        return [{"error": "Failed to fetch data from Google Sheet"}]
    
    df = pd.read_csv(StringIO(response.text))
    
    return df.to_dict(orient="records")




