from fastapi import Depends, HTTPException

from app.core.auth import get_current_user
from app.models.user import User


def require_admin(
    current_user: User = Depends(get_current_user),
):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required",
        )

    return current_user


def require_employee(
    current_user: User = Depends(get_current_user),
):
    return current_user