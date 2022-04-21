from typing import List

import requests
from fastapi import Response

from app.config.nasdaq import settings
from app.services.market.schemas import Quote
from app.services.market.schemas.summary import Summary

_local_session = requests.Session()


class NASDAQClient:
    """NASDAQ data provider internal client


    Returns:
        __instance: NASDAQ
    """

    __instance = None
    url = ""
    session: requests.Session
    username = None
    password = None
    symbols: List[str]

    def __new__(cls):
        if NASDAQClient.__instance is None:
            NASDAQClient.__instance = object.__new__(cls)
            NASDAQClient.__instance.url = settings.nasdaq_url or ""
            NASDAQClient.__instance.session = _local_session
            NASDAQClient.__instance.symbols = (
                NASDAQClient.__instance.get_symbols()
            )

        return NASDAQClient.__instance

    def _make_request(
        self,
        method: str,
        endpoint: str,
        query_params: dict = None,
        body: dict = None,
        **kwargs,
    ) -> Response:
        """Generic method to retrieve HTTP call to API

        Args:
            method (str): Methods for the request.
                          Options are GET, OPTIONS,
                          HEAD, POST, PUT, PATCH, or DELETE.
            endpoint (str): URL for the request
        """
        url = self.url + endpoint

        headers = {
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
        }
        additional_headers = kwargs.pop("headers", dict())
        headers.update(additional_headers or dict())

        try:
            response = self.session.request(
                method,
                url,
                headers=headers,
                params=query_params,
                json=body,
                allow_redirects=True,
            )
        except Exception as error:
            raise error

        return response

    def get_quote(self, symbol: str) -> Quote:
        endpoint = f"/quote/{symbol}/info"
        params = {"assetclass": "stocks"}

        raw_response = self._make_request("GET", endpoint, params)

        try:
            json_response = raw_response.json()

            return Quote(**json_response["data"])

        except ValueError as err:
            raise err

    def get_summary(self, symbol: str) -> Summary:
        endpoint = f"/quote/{symbol}/summary"
        params = {"assetclass": "stocks"}

        raw_response = self._make_request("GET", endpoint, params)

        try:
            json_response = raw_response.json()

            return Summary(**json_response["data"])

        except ValueError as err:
            raise err

    def get_symbols(self) -> List[str]:
        """Get NASDAQ Symbols

        Returns:
            List[str]: array of listed nasdaq symbols
        """
        endpoint = "/screener/stocks"
        params = {"tableonly": "true", "limit": "400", "offset": "0"}

        raw_response = self._make_request("GET", endpoint, params)

        try:
            json_response = raw_response.json()

            rows = json_response["data"]["table"]["rows"]

            return [e["symbol"] for e in rows]

        except ValueError as err:
            raise err
