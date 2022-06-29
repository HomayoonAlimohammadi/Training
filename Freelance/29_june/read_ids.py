from data import data


def read_column_ids(data):
    return [record["id"] for record in data if record["frame_type"] == "Column"]


if __name__ == "__main__":
    ids = read_column_ids(data)
    print(ids)
