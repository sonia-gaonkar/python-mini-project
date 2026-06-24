from fastapi import APIRouter, HTTPException
import re

router = APIRouter()

# In-memory store for the demo
_profiles = {}

PHONE_RE = re.compile(r"^\+?[0-9]{7,15}$")


@router.put("/profile")
def update_profile(profile: dict):
    """
    Update a user's profile (first name, last name, phone number).

    Note: email is intentionally not updatable here.
    """
    errors = {}

    # AC-2: mandatory fields must be present -> validation messages
    for field in ("first_name", "last_name", "phone"):
        if not str(profile.get(field, "")).strip():
            errors[field] = f"{field.replace('_', ' ').title()} is required."

    # AC-3: invalid phone number is rejected
    phone = str(profile.get("phone", "")).strip()
    if phone and not PHONE_RE.match(phone):
        errors["phone"] = "Phone number is invalid."

    # AC-7: return an error response for invalid data
    if errors:
        raise HTTPException(status_code=400, detail={"validation_errors": errors})

    # AC-4: email is never modified, even if supplied in the payload
    existing = _profiles.get("current_user", {})
    updated = {
        "first_name": profile["first_name"].strip(),
        "last_name": profile["last_name"].strip(),
        "phone": phone,
        "email": existing.get("email", ""),  # email stays disabled/unchanged
    }
    _profiles["current_user"] = updated

    # AC-6: return success for a valid update
    return {"status": "success", "profile": updated}

# NOTE for testing: AC-5 (audit logging on success) and
# AC-8 (rejecting unauthenticated users) are intentionally NOT implemented,
# so the requirement-alignment check should mark those two as "Not Met".
