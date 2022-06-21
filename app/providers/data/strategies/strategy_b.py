from app.models.pydantic import CoalesceResponseSchema
from app.providers.data.context import Strategy


class StrategyB(Strategy):
    async def request_input_list(self, member_id: int) -> CoalesceResponseSchema:
        return CoalesceResponseSchema(deductible=1200, stop_loss=13000, oop_max=6000)
