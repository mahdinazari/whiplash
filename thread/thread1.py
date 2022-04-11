from datetime import datetime
import requests
import threading
from concurrent import futures


local_thread = threading.local()


def get_session():
    if not hasattr(local_thread, 'session'):
        local_thread.session = requests.Session()

    return local_thread.session

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

def download_all(sites):
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)


if __name__ == '__main__':
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80

    start_time = datetime.now()
    download_site(sites)
    duration = datetime.now() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")

