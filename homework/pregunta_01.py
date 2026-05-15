"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import os

import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt
import pandas as pd


def pregunta_01():
    # ------------------------------------------------------------
    # Configuración de colores, orden de pintado y grosores de línea
    # ------------------------------------------------------------
    colores_por_medio = {
        "Television": "dimgrey",
        "Newspaper": "grey",
        "Internet": "tab:blue",
        "Radio": "lightgrey",
    }

    orden_por_medio = {
        "Television": 1,
        "Newspaper": 1,
        "Internet": 2,
        "Radio": 1,
    }

    ancho_por_medio = {
        "Television": 2,
        "Newspaper": 2,
        "Internet": 3,
        "Radio": 2,
    }

    # ------------------------------------------------------------
    # Cargar datos
    # ------------------------------------------------------------
    ruta_entrada_datos = "files/input/news.csv"
    datos_medios = pd.read_csv(ruta_entrada_datos, index_col=0)

    # ------------------------------------------------------------
    # Preparar carpeta de salida
    # ------------------------------------------------------------
    directorio_salida = "files/plots"
    os.makedirs(directorio_salida, exist_ok=True)

    # ------------------------------------------------------------
    # Crear figura
    # ------------------------------------------------------------
    plt.figure()

    # ------------------------------------------------------------
    # Líneas principales
    # ------------------------------------------------------------
    for medio_comunicacion in datos_medios.columns:
        plt.plot(
            datos_medios[medio_comunicacion],
            label=medio_comunicacion,
            color=colores_por_medio[medio_comunicacion],
            zorder=orden_por_medio[medio_comunicacion],
            linewidth=ancho_por_medio[medio_comunicacion],
        )

    # ------------------------------------------------------------
    # Título del gráfico
    # ------------------------------------------------------------
    plt.title("How people get their news", fontsize=16)

    # ------------------------------------------------------------
    # Personalizar ejes
    # ------------------------------------------------------------
    ejes = plt.gca()
    ejes.spines["top"].set_visible(False)
    ejes.spines["left"].set_visible(False)
    ejes.spines["right"].set_visible(False)
    ejes.get_yaxis().set_visible(False)

    # ------------------------------------------------------------
    # Obtener primer y último año
    # ------------------------------------------------------------
    anio_inicial = datos_medios.index[0]
    anio_final = datos_medios.index[-1]

    # ------------------------------------------------------------
    # Puntos y etiquetas en el año inicial
    # ------------------------------------------------------------
    for medio_comunicacion in datos_medios.columns:
        valor_inicial_medio = datos_medios.loc[anio_inicial, medio_comunicacion]

        plt.scatter(
            x=anio_inicial,
            y=valor_inicial_medio,
            color=colores_por_medio[medio_comunicacion],
            zorder=orden_por_medio[medio_comunicacion],
        )

        plt.text(
            anio_inicial - 0.2,
            valor_inicial_medio,
            f"{medio_comunicacion} {valor_inicial_medio}%",
            ha="right",
            va="center",
            color=colores_por_medio[medio_comunicacion],
        )

    # ------------------------------------------------------------
    # Puntos en el año final
    # ------------------------------------------------------------
    for medio_comunicacion in datos_medios.columns:
        valor_final_medio = datos_medios.loc[anio_final, medio_comunicacion]
        plt.scatter(
            x=anio_final,
            y=valor_final_medio,
            color=colores_por_medio[medio_comunicacion],
        )

    # ------------------------------------------------------------
    # Guardar imagen
    # ------------------------------------------------------------
    ruta_salida_imagen = os.path.join(directorio_salida, "news.png")
    plt.savefig(ruta_salida_imagen, bbox_inches="tight")
    plt.close()

    return ruta_salida_imagen


if __name__ == "__main__":
    pregunta_01()