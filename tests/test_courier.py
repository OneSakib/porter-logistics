import pytest
from porter.api import courier


def test_get_couriers(requests_mock):
    mock_response = {
        "couriers": [
            {"id": "dhl", "name": "DHL"},
            {"id": "fedex", "name": "FedEx"}
        ]
    }
    requests_mock.get(
        "https://api.yourshippingprovider.com/v1/couriers", json=mock_response)

    result = courier.Courier()
    assert isinstance(result, dict)
    assert "couriers" in result
    assert len(result["couriers"]) == 2
    assert result["couriers"][0]["name"] == "DHL"
