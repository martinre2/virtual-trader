""" NASDAQ Summary Schema """

from pydantic import BaseModel

from app.utils import str_to_float


class SummaryData(BaseModel):
    """Summary[Data] Schema"""

    Exchange: str
    Sector: str
    Industry: str
    OneYrTarget: str
    TodayHighLow: str
    TodayHigh: str
    TodayLow: str
    TodayAvg: str
    ShareVolume: str
    AverageVolume: str
    PreviousClose: str
    FiftTwoWeekHighLow: str
    MarketCap: str
    PERatio: str
    ForwardPE1Yr: str
    EarningsPerShare: str
    AnnualizedDividend: str
    ExDividendDate: str
    DividendPaymentDate: str
    Yield: str
    Beta: str

    def __init__(self, **data):

        keys = data.keys()
        values = [data[e]["value"] for e in data]

        data_t = dict(zip(keys, values))

        low, high = data_t["TodayHighLow"].split("/")

        data_t["TodayHigh"] = high.replace("$", "")
        data_t["TodayLow"] = low.replace("$", "")
        data_t["TodayAvg"] = (
            str_to_float(data_t["TodayHigh"]) + str_to_float(data_t["TodayLow"])
        ) / 2

        super().__init__(**data_t)


class Summary(BaseModel):
    """Summary Schema"""

    symbol: str
    summaryData: SummaryData
    assetClass: str
