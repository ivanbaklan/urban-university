"""
Requests
url: https://requests.readthedocs.io/en/latest/index.html
Данная библиотека упрощает работ с запросами к HTTP/HTTPS ресурсам
Пример использования:

    GET method
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

    POST method
    import requests
    payload = {'key1': 'value1', 'key2': 'value2'}
    >>> r = requests.post('https://httpbin.org/post', data=payload)
    >>> print(r.text)
    {
      ...
      "form": {
        "key2": "value2",
        "key1": "value1"
      },
      ...
    }

    POST a Multipart-Encoded File
    import requests
    url = 'https://httpbin.org/post'
    >>> files = {'file': open('report.xls', 'rb')}

    >>> r = requests.post(url, files=files)
    >>> r.text
    {
      ...
      "files": {
        "file": "<censored...binary...data>"
      },
      ...
    }
"""

"""
NumPy
url: https://numpy.org/doc/stable/user/absolute_beginners.html
Данная библиотека упрощает и ускоряет работу с массивами чисел и операциями над ними.
Пример использования:
    
    Create array
    import numpy as np
    >>> a = np.array([1, 2, 3, 4, 5, 6])
    >>> a
    array([1, 2, 3, 4, 5, 6])

    Применение метода shape к массиву
    import numpy as np
    >>> a = np.array([[1, 2, 3],
    ...               [4, 5, 6]])
    >>> a.shape
    (2, 3)
    
    Пример сортировки массива
    >>> arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
    >>> np.sort(arr)
    array([1, 2, 3, 4, 5, 6, 7, 8])
"""