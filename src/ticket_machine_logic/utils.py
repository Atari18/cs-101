def _check_user_input(user_input, range_list):
    try:
        if int(user_input) in range_list:
            return True
        else:
            return False
    except ValueError:
        return False

