from typing import Literal

from alphax.dataset import DATASET_DIR

CandleTimeframe = Literal['1m', '3m', '5m', '10m', '1h', '2d', '1d', '5d', '10d']

DATASET_CANDLE_DIR = f"{DATASET_DIR}/candle"

