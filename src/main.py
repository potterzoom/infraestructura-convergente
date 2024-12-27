from data_analysis import process_data, generate_plots

# Ruta de los archivos
RAW_DATA_PATH = "src/data/raw_data.csv"
PROCESSED_DATA_PATH = "src/data/processed_data.csv"
PLOTS_FOLDER = "src/plots/"

def main():
    """Función principal para ejecutar el flujo de procesamiento y análisis."""
    print("Iniciando procesamiento de datos...")
    
    # Procesar los datos
    try:
        data = process_data(RAW_DATA_PATH, PROCESSED_DATA_PATH)
        print("Datos procesados correctamente.")
    except Exception as e:
        print(f"Error durante el procesamiento de datos: {e}")
        return

    # Generar gráficos
    print("Generando gráficos...")
    try:
        generate_plots(data, PLOTS_FOLDER)
        print(f"Gráficos guardados en la carpeta: {PLOTS_FOLDER}")
    except Exception as e:
        print(f"Error al generar gráficos: {e}")
        return

    print("Proceso completado exitosamente.")

if __name__ == "__main__":
    main()