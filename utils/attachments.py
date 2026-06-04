from selene.support.shared import browser
import allure
from allure_commons.types import AttachmentType


def add_screenshot(name="Screenshot"):
    allure.attach(
        browser.config.driver.get_screenshot_as_png(),
        name=name,
        attachment_type=AttachmentType.PNG,
    )


def add_page_source():
    allure.attach(
        browser.config.driver.page_source,
        name="Page Source",
        attachment_type=AttachmentType.XML,
    )


def add_browserstack_session_link(session_id):
    allure.attach(
        f"https://app-automate.browserstack.com/dashboard/v2/sessions/{session_id}",
        name="BrowserStack Session",
        attachment_type=AttachmentType.TEXT,
    )


def add_browserstack_video(session_id):
    allure.attach(
        f"https://app-automate.browserstack.com/dashboard/v2/sessions/{session_id}",
        name="BrowserStack Video",
        attachment_type=AttachmentType.TEXT,
    )