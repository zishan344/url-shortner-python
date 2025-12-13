from utils import generate_code
from storage import load_data, save_data

def shorten_url(long_url):
    data = load_data()

    code = generate_code()
    while code in data:
        code = generate_code()

    data[code] = long_url
    save_data(data)
    return code

def expand_url(code):
    data = load_data()
    return data.get(code)
