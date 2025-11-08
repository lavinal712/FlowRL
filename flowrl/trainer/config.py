import os
from dataclasses import asdict, dataclass, field, fields, is_dataclass
from typing import Optional, Tuple


@dataclass
class ModelConfig:
    pretrained_model_name_or_path: str = "black-forest-labs/FLUX.1-dev"


@dataclass
class RewardConfig:
    pass


@dataclass
class AlgorithmConfig:
    pass


@dataclass
class DataConfig:
    data_path: str = "prompts.txt"


@dataclass
class TrainerConfig:
    train_batch_size: int = 1
    learning_rate: float = 1.0e-4
