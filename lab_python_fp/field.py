def field(items, *args):
    assert len(args) > 0
    res = []

    for item in items:
        tmp_res = {}

        if len(args) > 1:
            for arg in args:
                tmp_res[arg] = item[arg]
            res.append(tmp_res)
        else:
            res.append(item[args[0]])

    return res
