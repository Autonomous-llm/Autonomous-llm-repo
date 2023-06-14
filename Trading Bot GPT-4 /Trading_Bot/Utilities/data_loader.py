# Contains functions for loading data from external sources
import requests
import pandas as pd


def load_data_from_api(url: str, params: dict) -> pd.DataFrame:
    """
    Loads data from an API and returns it as a pandas DataFrame.

    Args:
        url (str): The API endpoint URL to request data from.
        params (dict): A dictionary containing any parameters to include in the API request.

    Returns:
        pd.DataFrame: The data returned by the API, formatted as a pandas DataFrame.
    """

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"API returned status code {response.status_code}")

    data = response.json()

    if not data:
        raise Exception("API returned empty response")

    df = pd.DataFrame.from_records(data)

    return df
