import requests


def resource_parser(contentType="Posts"):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'ru-UA,ru;q=0.9,en-US;q=0.8,en;q=0.7,ru-RU;q=0.6',
    }
    link = "https://jsonplaceholder.typicode.com/"

    if contentType == "Posts":
        link += "posts"
    elif contentType == "Comments":
        link += "comments"
    elif contentType == "Albums":
        link += "albums"
    elif contentType == "Photos":
        link += "photos"
    elif contentType == "To Do":
        link += "todos"
    elif contentType == "Users":
        link += "users"
    else:
        return ""

    data = requests.get(link).json()
    return data
