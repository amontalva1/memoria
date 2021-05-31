import requests


def download_img(url, img_path):
    '''Funcion para descargar y guardar imagenes de una url'''
    if 'http' not in url:
        url = 'http://' + url
    res = requests.get(url)
    with open(img_path, 'wb') as f:
        f.write(res.content)
