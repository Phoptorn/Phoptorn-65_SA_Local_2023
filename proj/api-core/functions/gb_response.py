def res(gb_status_code, data):

    code = gb_status_code[0]
    detail = gb_status_code[1]

    status = {"status_code": code, "detail": detail}

    res = {"status": status, "data": data}

    return dict(res)
