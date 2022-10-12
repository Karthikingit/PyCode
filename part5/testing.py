def any_name(num):
    try:
        return int(num) + 15
    except TypeError as err:
        return err

    