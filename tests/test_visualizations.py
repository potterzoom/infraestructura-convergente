import unittest
import pandas as pd
import os
from src.data_analysis import generate_plots


class TestVisualizations(unittest.TestCase):
    def setUp(self):
        """Configuración inicial para las pruebas."""
        self.test_data_path = "src/data/test_processed_data.csv"
        self.plots_folder = "src/plots/test_plots/"

        # Crear carpeta para los gráficos de prueba
        os.makedirs(self.plots_folder, exist_ok=True)

        # Crear archivo de datos de prueba
        test_data = {
            "Departamento": ["TI", "Finanzas", "Marketing", "RRHH"],
            "Eficiencia": [0.6, 0.5, 0.4, 0.3],
            "Seguridad": [0.8, 0.7, 0.9, 0.6],
            "Impacto": [0.48, 0.35, 0.36, 0.18],
            "Tiempo": [1, 2, 3, 4],
            "Servicios": [5, 3, 4, 2],
            "Escalabilidad": [10, 8, 9, 7],  
        }

        self.test_df = pd.DataFrame(test_data)
        self.test_df.to_csv(self.test_data_path, index=False)

    def tearDown(self):
        """Limpieza después de las pruebas."""
        if os.path.exists(self.test_data_path):
            os.remove(self.test_data_path)
        if os.path.exists(self.plots_folder):
            for file in os.listdir(self.plots_folder):
                os.remove(os.path.join(self.plots_folder, file))
            os.rmdir(self.plots_folder)

    def test_generate_plots_creates_files(self):
        """Verifica que los gráficos son generados correctamente."""
        generate_plots(self.test_df, self.plots_folder)

        # Verificar la existencia de los archivos gráficos
        expected_files = [
            "eficiencia_operativa.png",
            "seguridad_cibernetica.png",
            "escalabilidad_tecnologica.png"
        ]
        for file in expected_files:
            self.assertTrue(os.path.exists(os.path.join(self.plots_folder, file)), f"Falta el archivo {file}")

    def test_generate_plots_visual_output(self):
        """Verifica que los gráficos tienen contenido visual no vacío."""
        generate_plots(self.test_df, self.plots_folder)

        for file in os.listdir(self.plots_folder):
            file_path = os.path.join(self.plots_folder, file)
            self.assertTrue(os.path.getsize(file_path) > 0, f"El archivo {file} está vacío.")

if __name__ == "__main__":
    unittest.main()