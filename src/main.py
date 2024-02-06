import argparse
from src.core.params import pyproject_toml_params
parser = argparse.ArgumentParser(description=pyproject_toml_params.description)


def start():
    """
    项目开始入口
    :return: None
    """
    print("hello world")