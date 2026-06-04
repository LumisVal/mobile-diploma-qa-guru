import os

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene.support.shared import browser

from config.settings import settings
from utils import attachments


def is_bstack():
    return os.getenv("CONTEXT") == "bstack"


def create_bstack_options():
    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.app = settings.android_app

    options.set_capability(
        "bstack:options",
        {
            "userName": settings.browserstack_user,
            "accessKey": settings.browserstack_key,
            "deviceName": settings.android_device,
            "osVersion": settings.android_os_version,
            "projectName": settings.project_name,
            "buildName": settings.build_name,
            "sessionName": settings.session_name,
        },
    )

    return options


def create_local_options():
    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.device_name = settings.device_name
    options.platform_version = settings.platform_version
    options.app = os.path.abspath(settings.app)

    return options


@pytest.fixture(scope="function", autouse=True)
def mobile_management():
    if is_bstack():
        driver = webdriver.Remote(
            command_executor="https://hub.browserstack.com/wd/hub",
            options=create_bstack_options(),
        )
    else:
        driver = webdriver.Remote(
            command_executor="http://127.0.0.1:4723",
            options=create_local_options(),
        )

    browser.config.driver = driver
    browser.config.timeout = 10

    yield

    session_id = driver.session_id

    attachments.add_screenshot("Screenshot after test")
    attachments.add_page_source()

    browser.quit()

    if is_bstack():
        attachments.add_browserstack_session_link(session_id)
        attachments.add_browserstack_video(session_id)