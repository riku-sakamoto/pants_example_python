import pathlib

from settings import UserSetting


def showing():
    name = "foo"
    path = pathlib.Path("path/to/somewhere")

    setting = UserSetting(name=name, home_directory=path)

    print(setting)


if __name__ == "__main__":
    showing()
