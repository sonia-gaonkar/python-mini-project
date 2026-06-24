def update_profile(profile, audit_log):           # ← new REQUIRED param
    """Update a user's profile and record an audit entry."""
    if not profile.get("first_name"):
        raise ValueError("first_name is required")
    saved = {**profile, "updated": True}
    audit_log.record("profile_updated", profile)  # uses the new param
    return saved
