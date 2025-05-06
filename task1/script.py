import requests
import logging

def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

def make_request(url: str, logger: logging.Logger) -> None:
    try:
        response = requests.get(url)
        
        if 100 <= response.status_code < 400:
            logger.info(f"Successful response from {url}")
            logger.info(f"Status code: {response.status_code}")
            if response.text:
                logger.info(f"Response body: {response.text}")
            else:
                logger.info("No response body")
        else:
            raise Exception(f"HTTP Error: {response.status_code} - {response.text}")
            
    except requests.RequestException as e:
        raise Exception(f"Request failed for {url}: {str(e)}")

def main() -> None:
    logger = setup_logger("HTTP-Client")
    urls = [
        "https://httpstat.us/101",
        "https://httpstat.us/200",
        "https://httpstat.us/301",
        "https://httpstat.us/404",
        "https://httpstat.us/500"
    ]
    
    for url in urls:
        try:
            logger.info(f"Making request to {url}")
            make_request(url, logger)
        except Exception as e:
            logger.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()