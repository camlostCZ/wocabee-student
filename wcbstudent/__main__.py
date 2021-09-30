import sys

from selenium.common.exceptions import SessionNotCreatedException
from student import Student

try:
    app = Student()
    app.run()
except FileNotFoundError:
    print("Error: Vocabulary not found.", file=sys.stderr)
except SessionNotCreatedException:
    print("Error: Web browser driver not found. Download correct version:\n"
        "https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/",
        file=sys.stderr)
