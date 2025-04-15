import logging
import sys
import time
import requests
h = [
    logging.FileHandler("./logs/log.log"),
    logging.StreamHandler(stream=sys.stdout)
]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=h,
)
logger = logging.getLogger(__name__)


def main():
    r = requests.get("https://www.google.com")
    logger.info("Hello World")
    logger.info("Starting a complex calculation")
    time.sleep(5)
    logger.info(r.text)
    logger.info("37")
    logger.info("Completing a complex calculation")


if __name__ == "__main__":
    main()
