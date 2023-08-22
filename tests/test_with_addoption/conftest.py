def pytest_addoption(parser):
    parser.addoption(
        '--url',
        default='https://ya.ru/sfhfhfhfhfhfhfhfh',
        help="This is request url"
    )
    parser.addoption(
        '--status_code',
        default=200,
        help='Default status code'
    )