import os
import numpy as np
import pandas as pd
from wall import data


def get_bottom_records(data):
    raw_data = np.array(data).T
    raw_data = list(filter(lambda row: row[3].lower() != "top", raw_data))

    # Create DataFrame
    df = pd.DataFrame(
        raw_data,
        columns=[
            "Story",
            "Pier",
            "Output Case",
            "Location",
            "V1",
            "V2",
            "V3",
            "V4",
            "V5",
            "V6",
        ],
    )

    # Drop unwanted Columns
    df = df.drop(["V1", "V4", "V5", "V6"], axis=1)

    # Change type for better use of the data
    df = df.astype(
        {
            "Story": "string",
            "Pier": "string",
            "Output Case": "string",
            "Location": "string",
            "V2": "float64",
            "V3": "float64",
        }
    )

    # Convert V2 and V3 values
    df["V2"] = df["V2"] / 1000
    df["V3"] = df["V3"] / 1000

    # Output an excel file
    absolute_path = os.path.join(os.getcwd(), os.path.dirname(__file__))
    df.to_excel(os.path.join(absolute_path, "appr_wall.xlsx"))

    return df


df = get_bottom_records(data)
