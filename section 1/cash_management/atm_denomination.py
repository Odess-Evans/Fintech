def calculate_notes(amount):

    denominations = [1000, 500, 200]

    notes = {}

    for denomination in denominations:

        count = amount // denomination

        notes[denomination] = count

        amount = amount % denomination

    if amount != 0:
        return None

    return notes