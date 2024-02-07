from src.service.argsparse import ArgumentParser


def start():
    """
    项目开始入口
    :return: None
    """
    args_parser = ArgumentParser()
    arg = args_parser.parse()
