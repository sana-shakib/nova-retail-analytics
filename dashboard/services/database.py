import pandas as pd


def load_from_database(query, connection):

    """
    Execute SQL query
    """

    df = pd.read_sql(
        query,
        connection
    )

    return df