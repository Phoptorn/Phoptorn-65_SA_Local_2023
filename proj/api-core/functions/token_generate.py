from .gb_timestamp import timestamp

def token_gen(id):

    timestr = timestamp()

    # hash(device_id + timestr)
    token = hash(id + timestr)  # type token int
    
    return str(token)

# print(create_token("1234567890"))
