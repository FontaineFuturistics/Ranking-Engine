def lst_to_str(lst):
    """
    Convert a list to a string representation.
    """
    output = "["

    for item in lst:
        # If item is a list, recursively convert it to a string
        if isinstance(item, list):
            output += lst_to_str(item) + ", "
        # If item is a dictionary, convert it to a string
        elif isinstance(item, dict):
            output += dct_to_str(item) + ", "
        # Otherwise, just convert it to a string
        else:
            output += str(item) + ", "

    # Remove the last comma and space
    if len(output) > 1:
        output = output[:-2]

    output += "]"

    return output

def dct_to_str(dct):
    """
    Convert a dictionary to a string representation.
    """
    output = "{"

    for key, value in dct.items():
        # If value is a list,  convert it to a string
        if isinstance(value, list):
            output += f"{key}: {lst_to_str(value)}, "
        # If value is a dictionary, recursively convert it to a string
        elif isinstance(value, dict):
            output += f"{key}: {dct_to_str(value)}, "
        else:
            output += f"{key}: {value}, "

    # Remove the last comma and space
    if len(output) > 1:
        output = output[:-2]

    output += "}"
    return output

def print_dict(dct):
    """
    Print a dictionary in a readable format.
    """
    print(dct_to_str(dct))

def print_list(lst):
    """
    Print a list in a readable format.
    """
    print(lst_to_str(lst))