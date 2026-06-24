def update_profile(profile):
    """Update a user's profile. Returns the saved profile."""
    if not profile.get("first_name"):
        raise ValueError("first_name is required")
    saved = {**profile, "updated": True}
    return saved
