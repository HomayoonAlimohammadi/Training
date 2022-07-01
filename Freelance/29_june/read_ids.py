from data import data
import random
from copy import deepcopy

# import SapModel


def get_column_data_and_ids(data):
    id_list = []
    new_data = deepcopy(data)
    idx = 0
    while idx < len(new_data):
        record = new_data[idx]
        if record["frame_type"] == "Beam":
            del new_data[idx]
        else:
            section_area = record["width"] * record["height"]
            record["section_area"] = section_area
            del record["width"], record["height"]
            id_list.append(record["id"])
            idx += 1

    return new_data, id_list


def get_width_height(data, id_list):
    result = {}
    for idx in id_list:
        for record in data:
            if record["id"] == idx:
                height, width = record["height"], record["width"]
                break
        result[idx] = {"height": height, "width": width}
    return result


def get_max_pmm(id_list):
    pmm_list = []
    for id in id_list:
        pmm_list.append(SapModel.DesignConcrete.GetSummaryResultsColumn(id))
    return max(pmm_list)


def test(data):
    def test_column_data_and_ids():
        new_data, id_list = get_column_data_and_ids(data)
        for idx, record in zip(id_list, new_data):
            if (
                idx != record["id"]
                or "height" in record
                or "width" in record
                or "section_area" not in record
            ):
                print("Invalid record:", f"{id=}", record)
                break
        else:
            print("All the record were valid.")

    def test_width_height():
        _, id_list = get_column_data_and_ids(data)
        sample_ids = random.sample(id_list, 20)
        result = get_width_height(data, sample_ids)
        flag = True
        for idx, res_dict in result.items():
            for record in data:
                if record["id"] == idx:
                    if (
                        record["width"] != res_dict["width"]
                        or record["height"] != res_dict["height"]
                    ):
                        flag = False
                    break
            if not flag:
                break
        else:
            print("Result contained valid width and height.")

    test_column_data_and_ids()
    test_width_height()


if __name__ == "__main__":
    test(data)
