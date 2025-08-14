from porter.client import Client
from dotenv import load_dotenv
import os
load_dotenv()
if __name__ == '__main__':    
    client = Client(api_key=os.getenv('PORTER_API_KEY'))
    PAYLOAD={
    "pickup_details": {
        "lat": 30.7126095,
        "lng": 76.7076925
    },
    "drop_details": {
        "lat": 30.762283,
            "lng": 76.725151
        },
        "customer": {
            "name": "Sakib Malik",
            "mobile": {
                "country_code": "+91",
                "number": "8954664647"
            }
        }
    }
    print("Fetch all", client.courier.get_quote(PAYLOAD))
