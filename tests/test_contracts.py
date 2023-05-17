import random
from spaceship_rental.contracts import optimize_spaceship
import logging

logger = logging.getLogger(__name__)


def generate_contracts(num_contracts):
    contracts = []
    for i in range(num_contracts):
        contract = {
            'name': f'Contract{i + 1}',
            'start': random.randint(0, 100),
            'duration': random.randint(1, 10),
            'price': random.randint(1, 100)
        }
        contracts.append(contract)
    return contracts


def test_optimize_spaceship():
    contracts = [
        {"name": "Contract1", "start": 0, "duration": 5, "price": 10},
        {"name": "Contract2", "start": 3, "duration": 7, "price": 14},
        {"name": "Contract4", "start": 5, "duration": 9, "price": 7},
        {"name": "Contract3", "start": 5, "duration": 9, "price": 8},
    ]
    expected_result = {
        'income': 18,
        'path': ['Contract1', 'Contract3']
    }
    result = optimize_spaceship(contracts, logger)
    assert result == expected_result


def test_optimize_spaceship_2():
    contracts = [
        {"name": "Contract1", "start": 0, "duration": 5, "price": 10},
        {"name": "Contract2", "start": 3, "duration": 7, "price": 14},
        {"name": "Contract3", "start": 5, "duration": 9, "price": 8},
        {"name": "Contract4", "start": 5, "duration": 9, "price": 7},
        {"name": "Contract5", "start": 14, "duration": 4, "price": 12},
        {"name": "Contract6", "start": 9, "duration": 5, "price": 15},
    ]

    result = optimize_spaceship(contracts, logger)

    assert result['income'] == 37
    assert result['path'] == ['Contract1', 'Contract6', 'Contract5']


def test_optimize_spaceship_3():
    contracts = [
        {"name": "Contract1", "start": 0, "duration": 5, "price": 10},
        {"name": "Contract2", "start": 3, "duration": 7, "price": 20},
        {"name": "Contract3", "start": 5, "duration": 9, "price": 8},
        {"name": "Contract4", "start": 6, "duration": 9, "price": 8},
    ]
    expected_result = {
        'income': 20,
        'path': ['Contract2']
    }
    result = optimize_spaceship(contracts, logger)
    assert result == expected_result
