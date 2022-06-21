from app.models.pydantic import CoalesceResponseSchema
from app.providers.data.context import Context
from app.providers.data.strategies.strategy_a import StrategyA
from app.providers.data.strategies.strategy_b import StrategyB
from app.providers.data.strategies.strategy_c import StrategyC


def get_provider_list() -> list:
    return [
        StrategyA,
        StrategyB,
        StrategyC,
    ]


async def get_member_data(member_id: int) -> list[CoalesceResponseSchema]:
    member_data = []
    for provider in get_provider_list():
        context = Context(provider())
        data = await context.get_input_list(member_id)
        if data:
            member_data.append(data)
    return member_data
