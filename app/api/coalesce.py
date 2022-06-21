from typing import Optional

from fastapi import APIRouter, Path, Query

from app.models.pydantic import CoalesceResponseSchema, valid_keys, valid_actions
from app.services.coalesce import coalesce

router = APIRouter()


@router.get("/{member_id}", response_model=CoalesceResponseSchema)
async def get_coalesced_value(
    member_id: int = Path(..., gt=0),
    key: Optional[valid_keys] = Query(default=None),
    action: valid_actions = Query(...),
) -> CoalesceResponseSchema:
    # TODO: should validate action and key further and raise HTTPException(status_code=422, detail="Validation error")
    return await coalesce(member_id, action, key)
