def process_integerchoice(data):
    type = "integer"
    temp = {}
    for tuple in data:
        temp[tuple[0]] = tuple[1]
    return type, temp


def process_textchoice(data):
    type = "string"
    temp = {}
    for idx, tuple in enumerate(data):
        temp[idx + 1] = tuple[1]
    return type, temp
