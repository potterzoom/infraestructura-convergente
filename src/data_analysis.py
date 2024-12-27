import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def process_data(input_path, output_path):
    """
    Procesa los datos desde un archivo CSV de entrada y guarda los resultados procesados en un archivo CSV de salida.

    Args:
        input_path (str): Ruta al archivo CSV de entrada.
        output_path (str): Ruta al archivo CSV donde se guardarán los datos procesados.

    Returns:
        pd.DataFrame: DataFrame con los datos procesados.
    """
    print("Leyendo datos desde:", input_path)
    data = pd.read_csv(input_path)

    # Procesamiento de datos
    data['Impacto'] = data['Eficiencia'] * data['Seguridad']  # Ejemplo de cálculo
    
    # Guardar datos procesados
    data.to_csv(output_path, index=False)
    print("Datos procesados guardados en:", output_path)
    return data

def generate_plots(data, output_folder):
    """
    Genera gráficos a partir de un DataFrame y los guarda en una carpeta específica.

    Args:
        data (pd.DataFrame): DataFrame con los datos a graficar.
        output_folder (str): Ruta a la carpeta donde se guardarán los gráficos.
    """
    sns.set(style="whitegrid")

    # Gráfico de eficiencia operativa
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data, x="Departamento", y="Eficiencia")
    plt.title("Eficiencia Operativa por Departamento")
    plt.savefig(f"{output_folder}/eficiencia_operativa.png")
    print("Gráfico de eficiencia operativa guardado.")

    # Gráfico de seguridad cibernética
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x="Tiempo", y="Seguridad", marker="o")
    plt.title("Incremento de Seguridad Cibernética")
    plt.savefig(f"{output_folder}/seguridad_cibernetica.png")
    print("Gráfico de seguridad cibernética guardado.")

    # Gráfico de escalabilidad tecnológica
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x="Servicios", y="Escalabilidad", hue="Departamento")
    plt.title("Capacidad de Escalabilidad por Servicios")
    plt.savefig(f"{output_folder}/escalabilidad_tecnologica.png")
    print("Gráfico de escalabilidad tecnológica guardado.")