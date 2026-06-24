from user_profile.profile import update_profile

def deactivate_account(profile):
    result = update_profile(profile)   # one arg — will break after the PR
    result["active"] = False
    return result
