from user_profile.profile import update_profile

def handle_profile_update(body):
    return update_profile(body)        # one arg — will break after the PR
