import argparse
from src.core.params import pyproject_toml_params
parser = argparse.ArgumentParser(description=pyproject_toml_params.description)
parser.add_argument("--version", "-v", action="version", help="版本信息", version=pyproject_toml_params.version)

args = parser.parse_args()

print(args)
def start():
    """
    项目开始入口
    :return: None
    """
    print("hello world")