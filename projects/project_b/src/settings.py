import pathlib

import pydantic.dataclasses as dc
from pydantic import ConfigDict


@dc.dataclass(frozen=True, config=ConfigDict(extra="forbid"))
class UserSetting:
    name: str
    home_directory: pathlib.Path
