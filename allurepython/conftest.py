import pytest


def pytest_collection_modifyitems(session,config,items:list):
    for item in items:
        if "add" in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif "div" in item.nodeid:
            item.add_marker(pytest.mark.div)
        elif "mul" in item.nodeid:
            item.add_marker(pytest.mark.mul)
        elif "sub" in item.nodeid:
            item.add_marker(pytest.mark.sub)
    # print(items)
    # print(type(items))