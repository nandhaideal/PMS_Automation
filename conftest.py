from logging import config

import pytest
from config.config import Config


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default=input("Enter Website URL: "),
        help="Application URL"
    )

    parser.addoption(
        "--username",
        action="store",
        default=input("Enter Username: "),
        help="Username"
    )

    parser.addoption(
        "--password",
        action="store",
        default=input("Enter Password: "),
        help="Password"
    )


    parser.addoption(
        "--project",
        action="store",
        default=input("Enter Project Name: "),
        help="Project Name"
    )

@pytest.fixture(scope="session", autouse=True)
def load_config(request):
    Config.BASE_URL = request.config.getoption("--url")
    Config.USERNAME = request.config.getoption("--username")
    Config.PASSWORD = request.config.getoption("--password")
    Config.PROJECT = request.config.getoption("--project")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        if report.passed:
            print(f"\n✅ {item.name} - Passed")
        elif report.failed:
            print(f"\n❌ {item.name} - Failed")