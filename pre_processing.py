'''
    En este archivo se encontraran diferentes funciones para preparar los datos para ser estudiados.
'''

#imports
import pandas as pd
import json, bz2, utils, time

def download_images(res_json, path):
    ''' Funcion para descargar todas las imagenes indicadas como respuesta en un json '''
    #partial path to the working directory
    sys_path = ""
    path = f'{sys_path}/{path}/q_hits'
    res_json = f'{sys_path}/{res_json}'
    q_res = None
    with open(res_json, 'rb') as f:
        data = f.read()
        data = bz2.decompress(data)
        data = json.loads(data)
        q_res = data["products"]
    if q_res:
        for item in q_res:
            f_name = f"{path}/res1.png"
            utils.download_img(item["product_image_url"], f_name)
            #delay para no colapsar la pagina
            time.sleep(0.2)
    return len(q_res)

def download_query_results(query_csv):
    ''' Funcion para procesar un csv de busquedas visuales y descargar las respuestas entregadas a cada query por el motor de busqueda '''
    q_df = pd.read_csv(query_csv)
    for i,row in q_df.iterrows():
        #path_to_json = f"{row["sse_server_path"]}/{row["sse_hits_filename"]}"
        path_to_json = "{}/{}".format(row["sse_server_path"], row["sse_hits_filename"])
        path_to_imgs = row["sse_server_path"]
        download_images(path_to_json, path_to_imgs)
    