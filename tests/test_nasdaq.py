from polars_datareader import data as web
from polars_datareader._testing import skip_on_exception
from polars_datareader._utils import RemoteDataError


class TestNasdaqSymbols(object):
    @skip_on_exception(RemoteDataError)
    def test_get_symbols(self):
        symbols = web.DataReader("symbols", "nasdaq")
        assert "IBM" in symbols.index
