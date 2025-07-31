import requests
from agents import function_tool

@function_tool
def post_complete_data_to_sheet(
    name: str,
    roll_no: str,
    department: str,
    year_of_admission: str,
    fee_status: str = "Unpaid",
):
    """
    Dynamically posts student data to Google Sheet using webhook (Google Apps Script).
    """
    url = "https://script.google.com/macros/s/AKfycbyfYuBRUd2ZgY7QjE7Thgr3nEiczx5sYmls6nOjnfr-AGGDFDz3QqSRemi3WlDnGXaL/exec"
    
    payload = {
        "name": name,
        "roll_no":roll_no,
        "department": department,
        "year_of_admission": year_of_admission,
        "fee_status": fee_status,
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return "✅ Student data successfully submitted!"
    else:
        return f"❌ Failed to submit data. Status: {response.status_code}"
