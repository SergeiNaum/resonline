from pydantic import BaseModel


class CreateValuesRequest(BaseModel):

    values: list[int]


class CalculatedValueEntity(BaseModel):

    value: int
    prime_factors: list[int]
