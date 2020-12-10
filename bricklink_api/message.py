import enum as _enum

from .method import method as _method


class Direction(_enum.Enum):
  OUT = "out"
  IN = "in"
  DEFAULT = "in"


def get_message_list(
    *,
    direction: Direction = None,
    **kwargs
) -> dict:
  return _method("GET", "/messages",
      **kwargs
  )


def get_message(
    message_id: int,
    **kwargs
) -> dict:
  return _method("GET", f'/messages/{message_id}',
      **kwargs
  )


def reply_message(
    message_id: int,
    message_resource: dict,
    **kwargs
) -> dict:
  return _method("POST", f'/messages/{message_id}/reply',
      json = message_resource,
      **kwargs
  )
