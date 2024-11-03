from datetime import date
from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import outdated_products


@pytest.fixture()
def products() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160,
        },
    ]


@pytest.mark.parametrize(
    "today_date, expected",
    [
        pytest.param(
            date(2022, 2, 5),
            ["duck"],
            id="only one product is outdated"
        ),
        pytest.param(
            date(2022, 2, 12),
            ["salmon", "chicken", "duck"],
            id="all products are outdated"
        ),
        pytest.param(
            date(2022, 2, 1),
            [],
            id="no products are outdated"
        ),

        pytest.param(
            date(2022, 2, 6),
            ["chicken", "duck"],
            id="some products are outdated and some are not"
        ),
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(
        mocked_date: MagicMock,
        products: list[dict],
        today_date: str,
        expected: list
) -> None:
    mocked_date.date.today.return_value = today_date
    result = outdated_products(products)
    assert result == expected
