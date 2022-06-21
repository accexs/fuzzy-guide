from typing import Optional

from app.models.pydantic import CoalesceResponseSchema
from app.providers.data.context import Strategy


class StrategyA(Strategy):
    async def request_input_list(
        self, member_id: int
    ) -> Optional[CoalesceResponseSchema]:
        return CoalesceResponseSchema(deductible=1000, stop_loss=10000, oop_max=5000)
