"""NimbusPost Python SDK - A comprehensive package for NimbusPost shipping APIs"""

from nimbuspost.__version__ import __version__, __author__, __email__
from nimbuspost.client import NimbusPost
from nimbuspost.exceptions import (
    EShopBoxException,
    AuthenticationError,
    APIError,
    ValidationError,
    RateLimitError,
    NotFoundError
)

__all__ = [
    'NimbusPost',
    'EShopBoxException',
    'AuthenticationError',
    'APIError',
    'ValidationError',
    'RateLimitError',
    'NotFoundError',
    '__version__'
]