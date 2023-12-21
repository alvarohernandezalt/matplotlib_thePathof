from pyairtable import Api
import pandas as pd

def create_dataframe(api_key, base_id, table_name):
    # Create an API instance
    api = Api(api_key)

    # Get the base and table
    base = api.base(base_id)
    table = base.table(table_name)

    # Fetch all records
    records = table.all()

    # Convert records to DataFrame
    df= pd.DataFrame([record['fields'] for record in records])

    return df

df = create_dataframe(api_key, base_id, table_name)

df['Pais'] = ['Spain','Spain', 'Spain']

import requests
import json

# Define the URL and headers
url = f"https://api.airtable.com/v0/{base_id}/{table_name}"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Define the data
data = {
    "description": "Number of goals.",
    "name": "Goles",
    "options": {
      "color": "greenBright",
      "icon": "check"
    },
    "type": "checkbox"
}

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check the response
if response.status_code == 200:
    print("Field created successfully.")
else:
    print("Failed to create field. Response:", response.content)