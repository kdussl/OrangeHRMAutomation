import os

from dotenv import load_dotenv


load_dotenv(override=True)


BASE_URL = os.getenv(
    "BASE_URL",
    "https://opensource-demo.orangehrmlive.com/"
)

USERNAME = os.getenv(
    "USERNAME",
    "Admin"
)

PASSWORD = os.getenv(
    "PASSWORD",
    "admin123"
)

BROWSER = os.getenv(
    "BROWSER",
    "chromium"
)

HEADLESS = os.getenv(
    "HEADLESS",
    "false"
).lower() == "true"

SLOW_MO = int(
    os.getenv(
        "SLOW_MO",
        "0"
    )
)