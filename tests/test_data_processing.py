import unittest
import pandas as pd
from src.data_analysis import process_data
import os


class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        """Configuración inicial para las pruebas."""
        self.raw_data_path = "src/data/test_raw_data.csv"
        self.processed_data_path = "src/data/test_processed_data.csv"

        # Crear archivo de datos de prueba
        test_data = {
            "Departamento": ["TI", "Finanzas", "Marketing", "RRHH"],
            "Eficiencia": [0.6, 0.5, 0.4, 0.3],
            "Seguridad": [0.8, 0.7, 0.9, 0.6],
        }
        self.test_df = pd.DataFrame(test_data)
        self.test_df.to_csv(self.raw_data_path, index=False)

    def tearDown(self):
        """Limpieza después de las pruebas."""
        if os.path.exists(self.raw_data_path):
            os.remove(self.raw_data_path)
        if os.path.exists(self.processed_data_path):
            os.remove(self.processed_data_path)

    def test_process_data_creates_impact_column(self):
        """Verifica que process_data crea correctamente la columna 'Impacto'."""
        processed_df = process_data(self.raw_data_path, self.processed_data_path)

        # Comprobar que el archivo procesado existe
        self.assertTrue(os.path.exists(self.processed_data_path))

        # Verificar la columna 'Impacto'
        self.assertIn("Impacto", processed_df.columns)
        expected_impact = self.test_df["Eficiencia"] * self.test_df["Seguridad"]
        self.assertTrue(all(processed_df["Impacto"] == expected_impact))

    def test_process_data_output_structure(self):
        """Verifica que el archivo procesado tenga la estructura esperada."""
        processed_df = process_data(self.raw_data_path, self.processed_data_path)
        expected_columns = ["Departamento", "Eficiencia", "Seguridad", "Impacto"]
        self.assertListEqual(list(processed_df.columns), expected_columns)

if __name__ == "__main__":
    unittest.main()
