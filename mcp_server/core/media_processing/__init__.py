from .tools import register_tools
from ...config import config


def load(cfg: config.Config):
    register_tools(cfg)


__all__ = [
    "load",
]
