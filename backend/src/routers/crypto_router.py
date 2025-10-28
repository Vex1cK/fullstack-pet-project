from fastapi import APIRouter

from src.http_client import cmc_client


crypto_router = APIRouter(
    prefix="/cryptocurrencies"
)


@crypto_router.get("")
async def get_cryptocurrencies():
    return await cmc_client.get_listings()


@crypto_router.get("/{currency_id}")
async def get_cryptocurrency(currency_id: int):
    return await cmc_client.get_currency(currency_id)