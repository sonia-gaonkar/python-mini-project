from users.profile import update_profile

def deactivate_account(profile):
    # Calls update_profile with a SINGLE argument
    result = update_profile(profile)
    result["active"] = False
    return result
