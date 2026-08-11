def sanitize_account_number(account_number):

    cleaned_number = ""

    for character in account_number:
        if character.isdigit():
            cleaned_number += character

    if len(cleaned_number) == 10:
        return cleaned_number

    return None