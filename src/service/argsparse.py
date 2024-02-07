import argparse
from src.core.params import pyproject_toml_params


class ArgumentParser:
    """
    解析命令行参数主逻辑
    """

    def __init__(self):
        self.parser = argparse.ArgumentParser(description=pyproject_toml_params.description)
        self.add_argument()

    def add_argument(self):
        self.parser.add_argument("--version", "-v", action="version", help="版本信息",
                                 version=pyproject_toml_params.version)

    def parse(self) -> argparse.Namespace:
        return self.parser.parse_args()