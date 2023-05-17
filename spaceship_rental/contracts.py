import numpy as np
import pandas as pd


def optimize_spaceship(contracts, logger):
    """
    Optimize the result for a spaceship rental company

    :param contracts: list of dict
                    - name (str)
                    - start (int)
                    - duration (int)
                    - price (int)
    :param logger: logger
    :return: dict: contain the result
             - income (int): total income achieved by optimization contracts
             - path (list): list of contracts in order
    """
    logger.info("Start optimization")

    df = pd.DataFrame(contracts)

    # sort contracts by start hour in ascending order
    df = df.sort_values('start').reset_index(drop=True)

    starts = df['start'].values
    durations = df['duration'].values
    prices = df['price'].values

    n = len(df)

    # initialize the best prices array to store the max income at each position
    bp = np.zeros(n, dtype=int)
    # initialize the path array to store the selected contracts
    path = [[] for _ in range(n)]

    # the max income at the first position is the price of the first contract
    bp[0] = prices[0]
    path[0] = [df.loc[0, 'name']]

    for i in range(1, n):
        # get list of contracts that do not overlap the current contract
        candidates = [prices[i] + bp[j] for j in range(i) if starts[i] >= starts[j] + durations[j]]
        if candidates:
            # if candidates, select the one with the max income
            bp[i] = max(candidates)
            j = np.argmax(candidates)
            path[i] = path[j] + [df.loc[i, 'name']]
        else:
            # if no candidates, select the current contract only
            bp[i] = prices[i]
            path[i] = [df.loc[i, 'name']]

    # find the index of the max income and get the value of income and path
    max_income_idx = np.argmax(bp)
    max_income = int(bp[max_income_idx])
    selected_path = path[max_income_idx]

    # create result dictionary
    result = {
        'income': max_income,
        'path': selected_path
    }

    logger.info("Optimization completed.")

    return result
