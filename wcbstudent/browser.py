"""
Common browser functions
"""

from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions


def init_browser(driver_path: str, headless: bool = True) -> webdriver:
    """Initialize MS Edge browser.

    Args:
        driver_path (str): Path to MS Edge driver
        headless (bool, optional): Whether to run the browser in the headless 
            mode. Defaults to True.

    Returns:
        webdriver: Initialized driver instance
    """
    options = EdgeOptions()
    options.use_chromium = True  # Use the Chromium-based browser, not MSIE
    options.add_argument("user-data-dir=C:\\Temp")
    options.add_argument("profile-directory=Profile 1")
    if headless:
        options.add_argument('headless')
        options.add_argument('disable-gpu')
    return Edge(executable_path=driver_path, options=options)
