from abc import abstractmethod, ABC

from app.models.pydantic import CoalesceResponseSchema


class Strategy(ABC):
    @abstractmethod
    async def request_input_list(self, member_id: int) -> CoalesceResponseSchema:
        pass


class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    async def get_input_list(self, member_id: int) -> CoalesceResponseSchema:
        return await self._strategy.request_input_list(member_id)
