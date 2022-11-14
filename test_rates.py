import rates
import pytest
import requests


# test if Exception is raised when providing wrong environment
def test_env():
    with pytest.raises(Exception) as e:
        rates.fetch_rates("abc")


# get the real rates for comparison
def get_rates():
    url = "https://api.apilayer.com/exchangerates_data/latest"
    payload = {}
    headers = {
        "apikey": "ucTmfTVETT60Jb92G3NYRlgpaAIfDr5v"
    }
    return requests.request("GET", url, headers=headers, data=payload).json()


# test the fetch_rates func with the real rates
def test_rates():
    test_data = rates.fetch_rates("prod")
    real_data = get_rates()

    assert len(real_data['rates']) >= len(test_data)

    for curr in test_data:
        assert real_data['rates'][curr] < 10
