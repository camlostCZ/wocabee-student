import sys

from selenium.common.exceptions import SessionNotCreatedException, WebDriverException
from student import Student

try:
    app = Student()
    app.run()
except FileNotFoundError:
    print("Error: Vocabulary not found.", file=sys.stderr)
except (SessionNotCreatedException, WebDriverException) as e:
    print(f"Error: Web browser driver not found.\n {e}",
        file=sys.stderr)
