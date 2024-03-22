import re
import sys

from codegen.util.file_folder_util import modify_poetry_file


def test_modify_toml_file():
    location = "pyproject.toml"
    project_name = "test2"
    description = "ddd"
    version = "fff"
    package_name = 'kkk'
    modify_poetry_file(location, package_name, project_name, description, version)

