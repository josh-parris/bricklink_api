import enum as _enum
import string as _string

from . import auth as _auth
from . import helper as _helper
from . import url as _url
from . import logger as _logger

import requests

class Method(_enum.Enum):
  GET = "GET"
  POST = "POST"
  PUT = "PUT"
  DELETE = "DELETE"


def request(
    request_method: Method,
    uri: str,
    *,
    auth=None,
    base_url=None,
    **kwargs
) -> requests.PreparedRequest:
  request_method = _helper.enumize(request_method, Method).value
  req = requests.Request(
      method = request_method,
      url = _url.get(uri=uri, base_url=base_url),
      auth = (auth or _auth.DefaultOAuth.get()),
      **kwargs
  )
  return req.prepare()


def method(
    request_method: Method,
    uri: str,
    **kwargs
) -> requests.Response:
  preq = request(request_method, uri, **kwargs)
  try:
    with requests.Session() as s:
      resp = s.send(preq)
    if _logger.fn:
      _logger.fn(preq, resp)
    return resp.json()
  except:
    return {}

