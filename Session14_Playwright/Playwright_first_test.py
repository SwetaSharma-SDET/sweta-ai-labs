import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.chatbot.com/")
    page.locator("iframe[name=\"chat-widget-minimized\"]").content_frame.get_by_role("textbox", name="Write a message…").click()
    page.locator("iframe[name=\"chat-widget-minimized\"]").content_frame.get_by_role("textbox", name="Write a message…").click()
    page.locator("iframe[name=\"chat-widget-minimized\"]").content_frame.get_by_role("textbox", name="Write a message…").fill("what is this website")
    page.locator("iframe[name=\"chat-widget-minimized\"]").content_frame.get_by_role("button", name="Send a message").click()
    page.locator("iframe[name=\"chat-widget\"]").content_frame.get_by_text("Absolutely! You’re currently").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
