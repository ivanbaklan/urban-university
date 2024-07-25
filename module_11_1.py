"""
Requests
url: https://requests.readthedocs.io/en/latest/index.html
Данная библиотека упрощает работ с запросами к HTTP/HTTPS ресурсам
Пример использования:
    import requests
    r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    >>> r.status_code
    200
    >>> r.headers['content-type']
    'application/json; charset=utf8'
    >>> r.encoding
    'utf-8'
    >>> r.text
    '{"type":"User"...'
    >>> r.json()
    {'private_gists': 419, 'total_private_repos': 77, ...}
"""

"""
NumPy
url: https://numpy.org/doc/stable/user/absolute_beginners.html
Данная библиотека упрощает и ускоряет работу с массивами чисел и операциями над ними.
Пример использования:
    import numpy as np
    >>> a = np.array([[1, 2, 3],
    ...               [4, 5, 6]])
    >>> a.shape
    (2, 3)
"""