from typing import NewType, Literal

from pydantic import BaseModel

valid_keys = NewType("valid_keys", Literal["deductible", "stop_loss", "oop_max"])
valid_actions = NewType("valid_actions", Literal["avg", "max_by", "min_by", "sum"])


class CoalesceResponseSchema(BaseModel):
    deductible: int
    stop_loss: int
    oop_max: int

    def __getitem__(self, item):
        return getattr(self, item)
