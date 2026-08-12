def validate_kyc(user_data):

    required_fields = ["bvn", "nin", "full_name", "dob"]

    for field in required_fields:

        if field not in user_data:
            return False

        if not isinstance(user_data[field], str):
            return False

        if user_data[field].strip() == "":
            return False

    # BVN must contain exactly 11 digits
    if len(user_data["bvn"]) != 11 or not user_data["bvn"].isdigit():
        return False

    # NIN must contain exactly 11 digits
    if len(user_data["nin"]) != 11 or not user_data["nin"].isdigit():
        return False

    return True