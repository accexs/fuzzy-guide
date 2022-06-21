from app.models.pydantic import CoalesceResponseSchema, valid_actions, valid_keys
from app.providers.data.data import get_member_data


async def coalesce(member_id: int, action: valid_actions, key: valid_keys):
    if action == "avg":
        return await calculate_avg(member_id)
    if action == "max_by":
        return await calculate_max(member_id, key)
    if action == "min_by":
        return await calculate_min(member_id, key)
    if action == "sum":
        return await sum_all(member_id)


async def calculate_avg(member_id: int) -> CoalesceResponseSchema:
    data_list = await get_member_data(member_id)
    data_list_len = len(data_list)
    deductible = sum(d["deductible"] for d in data_list) / data_list_len
    stop_loss = sum(d["stop_loss"] for d in data_list) / data_list_len
    oop_max = sum(d["oop_max"] for d in data_list) / data_list_len
    return CoalesceResponseSchema(
        deductible=deductible.__floor__(),
        stop_loss=stop_loss.__floor__(),
        oop_max=oop_max.__floor__(),
    )


async def calculate_max(member_id: int, key: valid_keys) -> CoalesceResponseSchema:
    data_list = await get_member_data(member_id)
    item = max(data_list, key=lambda x: x[key])
    return item


async def calculate_min(member_id: int, key: valid_keys) -> CoalesceResponseSchema:
    data_list = await get_member_data(member_id)
    item = min(data_list, key=lambda x: x[key])
    return item


async def sum_all(member_id: int) -> CoalesceResponseSchema:
    data_list = await get_member_data(member_id)
    deductible = sum(d["deductible"] for d in data_list)
    stop_loss = sum(d["stop_loss"] for d in data_list)
    oop_max = sum(d["oop_max"] for d in data_list)
    return CoalesceResponseSchema(
        deductible=deductible, stop_loss=stop_loss, oop_max=oop_max
    )
