import os
import shutil
import stat

from oliver_codegen.core.params import PROJECT_ROOT_PATH



def test_remove_git_folder():
    git_path = PROJECT_ROOT_PATH.joinpath("hello").joinpath(".git")
    # os.chmod(git_path, stat.S_IWUSR)
    shutil.rmtree(git_path)