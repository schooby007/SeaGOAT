"""
This type stub file was generated by pyright.
"""

from typing import AnyStr, Optional, Union, overload

"""utilities to help provide compatibility with python 3"""
is_win: bool = ...
is_posix = ...
is_darwin = ...
defenc = ...

@overload
def safe_decode(s: None) -> None: ...
@overload
def safe_decode(s: AnyStr) -> str: ...
def safe_decode(s: Union[AnyStr, None]) -> Optional[str]:
    """Safely decodes a binary string to unicode"""
    ...

@overload
def safe_encode(s: None) -> None: ...
@overload
def safe_encode(s: AnyStr) -> bytes: ...
def safe_encode(s: Optional[AnyStr]) -> Optional[bytes]:
    """Safely encodes a binary string to unicode"""
    ...

@overload
def win_encode(s: None) -> None: ...
@overload
def win_encode(s: AnyStr) -> bytes: ...
def win_encode(s: Optional[AnyStr]) -> Optional[bytes]:
    """Encode unicodes for process arguments on Windows."""
    ...
