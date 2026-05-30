#!/usr/bin/env python3
import sys
import lightkurve as lk
import matplotlib.pyplot as plt

def procesar_exoplaneta(nombre_estrella, archivo_grafico):
    print(f"Buscando datos públicos en la NASA para {nombre_estrella}...")
    
    # 1. Buscar y descargar la curva de luz desde el archivo MAST de la NASA
    search_result = lk.search_lightcurve(nombre_estrella, mission='TESS', author='SPOC')
    
    # Descargamos solo el primer sector disponible para que sea rápido
    lc = search_result[0].download()
    
    # 2. Limpiar los datos (eliminar valores nulos y ruido de fondo del telescopio)
    lc_limpia = lc.remove_nans().flatten(window_length=401)
    
    # 3. Dibujar la curva de luz donde se aprecian los tránsitos
    plt.figure(figsize=(10, 5))
    lc_limpia.scatter(color='black', s=1)
    plt.title(f"Curva de Luz de {nombre_estrella} (Datos Públicos del Telescopio TESS de la NASA)")
    plt.xlabel("Tiempo (Días Barycentric JD)")
    plt.ylabel("Brillo Relativo Normalizado")
    
    # Hacer un pequeño zoom en una ventana de tiempo para ver un tránsito claro
    # WASP-19 tiene tránsitos constantes, limitamos el eje X para ver un par de ellos
    plt.xlim(lc_limpia.time[0].value + 1, lc_limpia.time[0].value + 5)
    
    # Guardar el gráfico resultante
    plt.savefig(archivo_grafico, dpi=150)
    print(f"¡Gráfico guardado con éxito en {archivo_grafico}!")

if __name__ == '__main__':
    estrella = sys.argv[1] if len(sys.argv) > 1 else "Wasp-19"
    salida = sys.argv[2] if len(sys.argv) > 2 else "transito_exoplaneta.png"
    procesar_exoplaneta(estrella, salida)
