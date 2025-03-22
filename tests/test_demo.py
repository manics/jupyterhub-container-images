# To run these tests with firefox:
#   python -mpytest --browser=firefox
# To investigate tests run this headed, and with a delay between actions
#   python -mpytest --browser=firefox --slowmo 2000 --headed

from playwright.sync_api import Page, expect


def test_simple(page: Page) -> None:
    page.goto("http://localhost:8000")
    # Login page
    expect(page.get_by_role("button", name="Sign in")).to_be_visible()
    page.get_by_role("textbox", name="Username:").fill("demo")
    page.get_by_role("textbox", name="Password:").fill("demo")
    page.get_by_role("button", name="Sign in").click()
    # JupyterLab
    page.wait_for_url("http://localhost:8000/user/demo/lab")
