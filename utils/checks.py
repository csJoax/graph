
def check_dict(obj):
    """
    check if obj is a dict
    if true, return obj
    if false, return {}
    :param obj:
    :return:
    """
    if obj is None:
        return {}
    elif isinstance(obj, dict):
        return obj
    else:
        raise TypeError('Dict type needed.', obj)
