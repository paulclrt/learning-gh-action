import requests

def test_important():
    """
    THis is a shit test to learn workflows
    """
    assert 1+1 == 2

def test_win():
    """
    THis is a shit test to learn workflows
    """
    assert 1+1 == 2

def test_works():
    """
    THis is a shit test to learn workflows
    """
    assert 1+1 == 2

def test_fine():
    """
    THis is a shit test to learn workflows
    """
    assert 1+1 == 2


def test_ohhhh_nooooo_this_fails():
    """
    What a shitty repo this is
    """
    assert 2+1 == 3


def test_request_fails():
    """
    What a shitty repo this is
    """
    req = requests.get("http://paul-claret.pro/zaduazhdaz")
    assert req.status_code == 404
