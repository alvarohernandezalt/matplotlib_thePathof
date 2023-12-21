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


