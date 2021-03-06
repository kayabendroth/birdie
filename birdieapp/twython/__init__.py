#     ______                  __   __
#    /_  __/_      __ __  __ / /_ / /_   ____   ____
#     / /  | | /| / // / / // __// __ \ / __ \ / __ \
#    / /   | |/ |/ // /_/ // /_ / / / // /_/ // / / /
#   /_/    |__/|__/ \__, / \__//_/ /_/ \____//_/ /_/
#                  /____/

"""
Twython
-------

Twython is a library for Python that wraps the Twitter API.

It aims to abstract away all the API endpoints, so that additions to the library
and/or the Twitter API won't cause any overall problems.

Questions, comments? ryan@venodesigns.net
"""

__author__ = 'Ryan McGrath <ryan@venodesigns.net>'
__version__ = '3.1.2'

from birdieapp.twython.api import Twython
from birdieapp.twython.streaming import TwythonStreamer
from birdieapp.twython.exceptions import (
    TwythonError, TwythonRateLimitError, TwythonAuthError,
    TwythonStreamError
)
