import shutil

from codegen.core.params import PACKAGE_DIR


def test_remove_git_folder():
    git_path = PACKAGE_DIR.joinpath("hello").joinpath(".git")
    # os.chmod(git_path, stat.S_IWUSR)
    shutil.rmtree(git_path)