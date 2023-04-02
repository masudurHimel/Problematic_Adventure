parent_map = {
    "cluster": None,
    "region": "cluster",
    "zone": "region",
    "area": "zone",
    "territory": "area"
}


def get_parent(c_p):
    res = []
    p = parent_map[c_p]
    while p:
        res.append(p)
        p = parent_map[p]
    return res


print(get_parent("tk"))
