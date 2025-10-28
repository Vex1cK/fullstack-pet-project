from aiohttp import ClientSession
from async_lru import alru_cache

from src.config import settings


class HTTPClient:
    def __init__(self, base_url: str, api_key_header: str, api_key: str):
        self._session = ClientSession(
            base_url=base_url,
            headers={
                api_key_header: api_key
            }
        )


class CMCHTTOSClient(HTTPClient):
    api_key_header="X-CMC_PRO_API_KEY"
    base_url="https://pro-api.coinmarketcap.com"

    def __init__(self, api_key: str):
        super().__init__(
            base_url=CMCHTTOSClient.base_url,
            api_key_header=CMCHTTOSClient.api_key_header,
            api_key=api_key
        )

    @alru_cache
    async def get_listings(self):
        async with self._session.get("/v1/cryptocurrency/listings/latest") as response:
            result = await response.json()
            return result["data"]
    
    @alru_cache
    async def get_currency(self, currency_id: int):
        async with self._session.get(
            "/v2/cryptocurrency/quotes/latest",
            params={"id": currency_id}
        ) as resp:
            result = await resp.json()
            return result["data"][str(currency_id)]



cmc_client = CMCHTTOSClient(
    api_key=settings.CMC_API_KEY
)