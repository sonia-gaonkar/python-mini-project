from fastapi import APIRouter, HTTPException
import re

router = APIRouter()


@router.put("/profile")
def update_profile(profile):

    if not profile.get("firstName"):
        raise HTTPException(
            status_code=400,
            detail="First Name is required"
        )

    if not profile.get("lastName"):
        raise HTTPException(
            status_code=400,
            detail="Last Name is required"
        )

    phone = profile.get("phone", "")

    if phone and not re.fullmatch(r"\d{10}", phone):
        raise HTTPException(
            status_code=400,
            detail="Phone number must contain exactly 10 digits"
        )

    return {
        "status": "success",
        "message": "Profile Updated",
        "data": profile
    }
