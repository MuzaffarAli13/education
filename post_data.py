import requests
from agents import function_tool

@function_tool
def post_complete_data_to_sheet(
    full_name: str,
    roll_no: str,
    cnic_b_form_number: str,
    phone_number: str,
    department: str,
    gender: str,
    year_of_admission: str,
    address: str,
    email: str,
    fee_status: str = "Unpaid",
    remarks: str = ""
):
    """
    Dynamically posts student data to Google Sheet using webhook (Google Apps Script).
    """
    url = "https://script.google.com/macros/s/AKfycbzxrDoqlENFDM7jwnS24MyRrHWcQ5j47ODQgqY3CPDYNkok87kFUTvd-Gaj7OOFb-gw/exec"
    
    payload = {
        "full_name": full_name,
        "roll_no":roll_no,
        "cnic_b_form_number": cnic_b_form_number,
        "phone_number": phone_number,
        "department": department,
        "gender":gender,
        "year_of_admission": year_of_admission,
        "address": address,
        "email": email,
        "fee_status": fee_status,
        "remarks": remarks
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return "✅ Student data successfully submitted!"
    else:
        return f"❌ Failed to submit data. Status: {response.status_code}"
