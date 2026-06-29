import requests
import json

def trigger_automation(webhook_url, payload_data):
    """
    Sends a payload of data to a Zapier or Make.com webhook.
    """
    # Set the headers to ensure the webhook reads the data as JSON
    headers = {
        'Content-Type': 'application/json'
    }

    try:
        # Send a POST request to the webhook URL
        response = requests.post(
            webhook_url, 
            data=json.dumps(payload_data), 
            headers=headers
        )

        # Check if the request was successful
        if response.status_code in [200, 201]:
            print(f"Success! Data sent to webhook. Status Code: {response.status_code}")
            return True
        else:
            print(f"Failed to send data. Status Code: {response.status_code}")
            print(f"Response: {response.text}")
            return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# ==========================================
# Testing the Script
# ==========================================
if __name__ == "__main__":
    # 1. Paste your Make.com or Zapier Webhook URL here
    MY_WEBHOOK_URL = "https://hook.eu1.make.com/6l25u44n17hmnywtrj76qpsb4j0rw0ie"

    # 2. Add the data you want to send to the automation platform
    my_data = {
        "event_type": "new_client_inquiry",
        "client_name": "John Doe",
        "email": "john.doe@example.com",
        "message": "I need help building an automated workflow.",
        "priority": "High"
    }

    # 3. Run the function
    print("Attempting to trigger automation...")
    trigger_automation(MY_WEBHOOK_URL, my_data)