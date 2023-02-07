def is_int(x):
    return x.isdigit() or (x[0] in ["-","+"] and x[1:].isdigit())