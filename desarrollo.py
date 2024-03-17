import pandas as pd
import glob
import os
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        return archivo.readlines()[0]


def generar_lista_archivos(directorio):
    return glob.glob(os.path.join(directorio + '*.txt'))


def procesar_archivo(directorio):
    return [leer_archivo(archivo) for archivo in generar_lista_archivos(directorio)]



def generar_dataframe(train_or_test: str):
    diccionario = {"phrase": [], "sentiment": []}
    for nombre_sentimiento in ["negative", "neutral", "positive"]:
        lista_archivos = procesar_archivo(f"{train_or_test}/{nombre_sentimiento}/")
        diccionario["phrase"] += lista_archivos
        nueva_lista = [nombre_sentimiento] * len(lista_archivos)
        diccionario["sentiment"] += nueva_lista

    return (pd.DataFrame(diccionario), train_or_test)


def guardar_dataframe(df: pd.DataFrame, nombre):

    df.to_csv(nombre, sep = ",", index= False)

if __name__ == "__main__":
    df_test, test = generar_dataframe("test")
    df_train, train = generar_dataframe("train")

    guardar_dataframe(df_test, f"{test}_dataset.csv")
    guardar_dataframe(df_train, f"{train}_dataset.csv")







