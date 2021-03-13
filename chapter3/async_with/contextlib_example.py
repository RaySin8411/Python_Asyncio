from contextlib import contextmanager


def download_webpage(url: str):
    class Data:
        pass
    return Data()


def update_status(url: str):
    pass


def process(data):
    pass


@contextmanager
def web_page(url: str):
    data = download_webpage(url)
    yield data
    update_status(url)


def main():
    with web_page('google.com') as data:
        process(data)


if __name__ == '__main__':
    main()