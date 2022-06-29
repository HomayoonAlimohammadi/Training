from data import data

# import SapModel


def read_column_ids(data):
    id_list = []
    for record in data:
        if record["frame_type"] == "Column":
            id_list.append(record["id"])

    return id_list


def get_max_pmm(id_list):
    pmm_list = []
    for id in id_list:
        pmm_list.append(SapModel.DesignConcrete.GetSummaryResultsColumn(id))
    return max(pmm_list)


id_list = read_column_ids(data)
max_pmm = get_max_pmm(id_list)
