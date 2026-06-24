from users.profile import update_profile

def handle_profile_update(request_body):
    # Also calls update_profile with a SINGLE argument
    return update_profile(request_body)
