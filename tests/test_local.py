import shutil

from kedroio.connectors.util.local import (
    local_file_exists,
    local_dir_exists,
    make_dir_if_not_exists
)


def test_local_file_exists():
    assert local_file_exists("tests/__init__.py")


def test_local_dir_exists():
    assert local_dir_exists("tests")


def test_make_dir_existing():
    assert local_dir_exists("tests")
    r = make_dir_if_not_exists("tests")
    assert not r


def test_make_dir_not_existing():
    dir_ = "fake"
    assert not local_dir_exists(dir_)
    r = make_dir_if_not_exists(dir_=dir_)
    assert r
    shutil.rmtree(dir_)
