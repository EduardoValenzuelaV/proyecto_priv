import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from fastapi import HTTPException

import Dallana_main as api


class ValidacionFotosTests(unittest.TestCase):
    def test_acepta_firmas_de_formatos_permitidos(self):
        muestras = {
            "image/png": b"\x89PNG\r\n\x1a\nresto",
            "image/jpeg": b"\xff\xd8\xffresto",
            "image/webp": b"RIFF\x00\x00\x00\x00WEBPrest",
            "image/gif": b"GIF89arest",
        }
        for tipo, datos in muestras.items():
            with self.subTest(tipo=tipo):
                self.assertTrue(api.firma_imagen_valida(tipo, datos))

    def test_rechaza_archivo_vacio_tipo_falso_y_formato_no_permitido(self):
        self.assertFalse(api.firma_imagen_valida("image/png", b""))
        self.assertFalse(api.firma_imagen_valida("image/png", b"texto que finge ser PNG"))
        self.assertFalse(api.firma_imagen_valida("image/svg+xml", b"<svg></svg>"))


class PersistenciaTests(unittest.TestCase):
    def test_guardar_conserva_la_version_anterior_como_respaldo(self):
        with tempfile.TemporaryDirectory() as carpeta:
            datos = Path(carpeta) / "contenido.json"
            datos.write_text('{"carta":"anterior"}', encoding="utf-8")
            with patch.object(api, "DATOS", datos):
                api.guardar_datos({"carta": "nuevo"})
            respaldo = datos.with_suffix(".json.bak")
            self.assertEqual(json.loads(respaldo.read_text(encoding="utf-8")), {"carta": "anterior"})
            self.assertEqual(json.loads(datos.read_text(encoding="utf-8")), {"carta": "nuevo"})

    def test_json_danado_no_se_reemplaza_silenciosamente(self):
        with tempfile.TemporaryDirectory() as carpeta:
            datos = Path(carpeta) / "contenido.json"
            original = b"{json roto"
            datos.write_bytes(original)
            with patch.object(api, "DATOS", datos):
                with self.assertRaisesRegex(RuntimeError, "se conservó el archivo"):
                    api.leer_datos()
            self.assertEqual(datos.read_bytes(), original)


class AutenticacionTests(unittest.TestCase):
    def test_token_requiere_configuracion_y_comparacion_correcta(self):
        with patch.dict(os.environ, {"DALLANA_ADMIN_TOKEN": ""}):
            with self.assertRaises(HTTPException) as sin_configurar:
                api.exigir_admin(None)
            self.assertEqual(sin_configurar.exception.status_code, 503)
        with patch.dict(os.environ, {"DALLANA_ADMIN_TOKEN": "secreto-largo"}):
            with self.assertRaises(HTTPException) as incorrecto:
                api.exigir_admin("no-es")
            self.assertEqual(incorrecto.exception.status_code, 401)
            self.assertIsNone(api.exigir_admin("secreto-largo"))


if __name__ == "__main__":
    unittest.main()
