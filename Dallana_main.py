import json
import os
import random
import secrets
import shutil
import uuid
from datetime import datetime
from pathlib import Path
from typing import Optional
from zoneinfo import ZoneInfo

from fastapi import FastAPI, File, Header, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

app = FastAPI(title="La API del amor 💌")

origins = [item.strip() for item in os.getenv(
    "DALLANA_ALLOWED_ORIGINS",
    "http://localhost:5500,http://127.0.0.1:5500"
).split(",") if item.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "X-Admin-Token"],
)

DATOS = Path(os.getenv("DALLANA_DATA_FILE", "cumplidos.json"))
FOTOS = Path(os.getenv("DALLANA_MEDIA_DIR", str(DATOS.parent / "fotos")))
FOTOS.mkdir(parents=True, exist_ok=True)
app.mount("/media", StaticFiles(directory=FOTOS), name="media")

INICIALES = [
    {"mensaje": "Me encanta tu sonrisa, ilumina cualquier día.", "foto": ""},
    {"mensaje": "Conocerte en ese curso de la universidad ha sido mi parte favorita del semestre.", "foto": ""},
    {"mensaje": "Caminar contigo por Paicaví siempre es un buen plan si voy de tu mano.", "foto": ""},
    {"mensaje": "Eres increíblemente inteligente y admiro tu dedicación en tu carrera.", "foto": ""},
    {"mensaje": "No puedo esperar para celebrar este 17 de noviembre contigo, Dallana.", "foto": ""},
    {"mensaje": "Haces que hasta un día pesado valga totalmente la pena.", "foto": ""},
    {"mensaje": "Vale por una invitación a comer tu sushi favorito. 🍣", "foto": ""},
    {"mensaje": "Vale por un helado en Sweet Cream, yo invito. 🍦", "foto": ""},
    {"mensaje": "Me encanta cómo empezamos a hablar, es mi recuerdo favorito.", "foto": ""},
    {"mensaje": "Tu risa es mi sonido favorito en el mundo.", "foto": ""},
    {"mensaje": "Contigo hasta esperar la micro se siente como una aventura.", "foto": ""},
    {"mensaje": "Eres la razón por la que reviso mi celular con una sonrisa.", "foto": ""},
    {"mensaje": "Me gusta lo tranquilo que se siente todo cuando estoy contigo.", "foto": ""},
    {"mensaje": "Gracias por ser tú, tal cual eres. Eso es lo que más me gusta.", "foto": ""},
    {"mensaje": "Vale por un abrazo largo, de esos que arreglan el día. 🤗", "foto": ""},
    {"mensaje": "Admiro lo fuerte y valiente que eres, aunque a veces no lo notes.", "foto": ""},
    {"mensaje": "Me encanta cómo te brillan los ojos cuando hablas de lo que te apasiona.", "foto": ""},
    {"mensaje": "Vale por una tarde de película y manta, tú eliges la película. 🎬", "foto": ""},
    {"mensaje": "En este primer mes aprendí que mi lugar favorito es a tu lado.", "foto": ""},
    {"mensaje": "Si pudiera repetir un día, elegiría cualquiera de los que pasé contigo.", "foto": ""},
    {"mensaje": "Eres mi persona favorita para contarle todo.", "foto": ""},
    {"mensaje": "Me haces querer ser una mejor versión de mí.", "foto": ""},
    {"mensaje": "Vale por un paseo sin apuro y sin destino. 🌅", "foto": ""},
    {"mensaje": "Tus mensajes son la mejor parte de mis días.", "foto": ""},
    {"mensaje": "Me encanta que contigo hasta el silencio sea cómodo.", "foto": ""},
    {"mensaje": "Gracias por hacerme tan feliz en tan poco tiempo.", "foto": ""},
    {"mensaje": "Vale por un 'te quiero' extra hoy, y mañana otro. 💕", "foto": ""},
    {"mensaje": "Eres de esas casualidades bonitas que uno agradece toda la vida.", "foto": ""},
    {"mensaje": "Un mes juntos y ya no me imagino los días sin ti.", "foto": ""},
    {"mensaje": "Te elegiría otra vez, y otra vez, y otra vez. ❤️", "foto": ""},
]

CARTA_INICIAL = "Dallana, gracias por cada paseo, cada conversación y cada risa. Me haces muy feliz. Te elegiría una y mil veces. Con todo mi cariño, siempre."
SALUDOS_INICIALES = {
    "manana": "Buenos días, amor. Ojalá hoy encuentres un motivo nuevo para sonreír. Yo ya tengo el mío: tú. ☀️",
    "noche": "Buenas noches, mi vida. Que descanses bonito y sueñes con todo lo que todavía nos queda por vivir. 🌙",
}

CONTENIDO_INICIAL = {
    "autoestima": [
        {"categoria": "Su personalidad", "icono": "✿", "mensaje": "Tu forma de ser tiene algo que te hace única."},
        {"categoria": "Su personalidad", "icono": "♡", "mensaje": "No necesitas cambiar tu esencia para ser suficiente."},
        {"categoria": "Su personalidad", "icono": "❀", "mensaje": "Tu manera de ver el mundo es algo muy bonito."},
        {"categoria": "Su personalidad", "icono": "☼", "mensaje": "Tienes una forma especial de hacer sentir bien a quienes te rodean."},
        {"categoria": "Su belleza", "icono": "✧", "mensaje": "Ojalá pudieras verte con los ojos de quienes te admiran."},
        {"categoria": "Su belleza", "icono": "❀", "mensaje": "No necesitas cumplir ningún estándar para ser hermosa."},
        {"categoria": "Su belleza", "icono": "♡", "mensaje": "Hay belleza en tu sonrisa, pero también en tu manera de ser."},
        {"categoria": "Su belleza", "icono": "✿", "mensaje": "Eres mucho más que lo que ves frente al espejo."},
        {"categoria": "Su inteligencia", "icono": "✦", "mensaje": "Tienes una mente que merece ser valorada."},
        {"categoria": "Su inteligencia", "icono": "☼", "mensaje": "No saber algo todavía no significa que no seas capaz."},
        {"categoria": "Su inteligencia", "icono": "✧", "mensaje": "Tu curiosidad y tus ideas también son parte de lo maravillosa que eres."},
        {"categoria": "Su inteligencia", "icono": "❀", "mensaje": "Nunca minimices lo que puedes lograr."},
        {"categoria": "Su valentía", "icono": "♡", "mensaje": "Has superado días que quizá nadie conoce."},
        {"categoria": "Su valentía", "icono": "✿", "mensaje": "Seguir intentándolo también es una forma de valentía."},
        {"categoria": "Su valentía", "icono": "☼", "mensaje": "Está bien descansar, no tienes que poder con todo."},
        {"categoria": "Su valentía", "icono": "✦", "mensaje": "No eres menos fuerte por tener días difíciles."},
        {"categoria": "Su valor personal", "icono": "❀", "mensaje": "No tienes que demostrar nada para merecer cariño."},
        {"categoria": "Su valor personal", "icono": "♡", "mensaje": "Tu valor no depende de la opinión de otras personas."},
        {"categoria": "Su valor personal", "icono": "✧", "mensaje": "Mereces cosas bonitas, incluso en tus días más complicados."},
        {"categoria": "Su valor personal", "icono": "✿", "mensaje": "Eres suficiente, incluso cuando tú misma lo dudas."},
    ],
    "cartas": [
        {"titulo": "Ábreme cuando estés triste", "mensaje": "No tienes que arreglarlo todo ahora. Si puedes, respira despacio y date permiso para sentir. Este momento difícil no cuenta toda tu historia; también hay días más amables esperándote."},
        {"titulo": "Ábreme cuando no te sientas bonita", "mensaje": "No hay una sola forma correcta de ser bonita. Tu cuerpo no tiene que cumplir ninguna medida para merecer respeto y ternura. Ojalá hoy puedas hablarte con un poquito de la paciencia que tendrías con alguien que quieres."},
        {"titulo": "Ábreme cuando dudes de ti misma", "mensaje": "No necesitas tener todas las respuestas para seguir siendo capaz. Puedes aprender, cambiar de idea y avanzar a tu ritmo. Lo que todavía no sabes no reduce todo lo que ya eres."},
        {"titulo": "Ábreme cuando tengas un mal día", "mensaje": "Un día pesado no convierte tu vida en una vida pesada. Haz lo que puedas, deja lo demás para después y recuerda que descansar también cuenta como cuidarte."},
        {"titulo": "Ábreme cuando sientas que no puedes más", "mensaje": "No tienes que resolver todo de una vez. Busca un paso pequeño, una pausa o a alguien de confianza con quien compartir el peso. Pedir compañía también es una forma de cuidarte."},
        {"titulo": "Ábreme cuando estés orgullosa de ti", "mensaje": "Detente un momento y reconoce lo que hiciste. No hace falta que sea algo enorme para que importe. Tu esfuerzo merece ser celebrado, sobre todo por ti."},
        {"titulo": "Ábreme cuando necesites recordar cuánto vales", "mensaje": "Tu valor no se gana con logros, aprobación ni días perfectos. Estás aquí, siendo tú, y eso basta para merecer cuidado, respeto y cosas buenas."},
        {"titulo": "Ábreme cuando simplemente quieras sonreír", "mensaje": "Ojalá encuentres una canción que te guste, algo rico para comer y un ratito sin apuro. No necesitas una razón grande para regalarte un momento bonito."},
    ],
    "frasco": [
        "No tienes que ganarte el descanso.", "Tu voz y tus ideas merecen espacio.",
        "Un paso pequeño también es avanzar.", "Puedes sentir mucho y seguir siendo capaz.",
        "Hoy mereces tratarte con cariño.", "Tu valor no depende de cómo salió el día.",
        "Está bien pedir apoyo cuando lo necesitas.", "Ojalá notes una cosa bonita de ti hoy.",
    ],
    "museo": [
        {"titulo": "Tu vocación", "descripcion": "Tu curiosidad por la geología y la dedicación que pones en tu carrera me inspiran.", "mensaje": "Mi geóloga favorita.", "foto": ""},
        {"titulo": "Tu sonrisa", "descripcion": "Me encanta tu sonrisa; puede hacer más amable hasta un día común.", "mensaje": "Una de mis cosas favoritas de ti.", "foto": ""},
        {"titulo": "Tus gustos", "descripcion": "Sushi, un helado en Sweet Cream y esos momentos simples que disfrutamos juntos.", "mensaje": "Me gusta aprender qué cosas te hacen feliz.", "foto": ""},
        {"titulo": "Nuestros paseos", "descripcion": "Caminar contigo por Paicaví siempre es un buen plan.", "mensaje": "A tu lado, cualquier camino se vuelve mi favorito.", "foto": ""},
    ],
    "suenos": [
        {"id": "sueno-1", "titulo": "Conocer un lugar nuevo", "descripcion": "", "hecho": False},
        {"id": "sueno-2", "titulo": "Ver una película juntos", "descripcion": "", "hecho": False},
        {"id": "sueno-3", "titulo": "Salir a caminar sin apuro", "descripcion": "", "hecho": False},
        {"id": "sueno-4", "titulo": "Compartir una comida rica", "descripcion": "", "hecho": False},
        {"id": "sueno-5", "titulo": "Tomarnos fotografías", "descripcion": "", "hecho": False},
        {"id": "sueno-6", "titulo": "Vivir una pequeña aventura", "descripcion": "", "hecho": False},
    ],
}

_cache_mtime: Optional[float] = None
_cache_data: Optional[dict] = None

def leer_datos() -> dict:
    global _cache_mtime, _cache_data
    if DATOS.exists():
        mtime = DATOS.stat().st_mtime
        if _cache_data is not None and _cache_mtime == mtime:
            return json.loads(json.dumps(_cache_data))
        try:
            _cache_data = json.loads(DATOS.read_text(encoding="utf-8"))
            _cache_mtime = mtime
        except (OSError, json.JSONDecodeError) as error:
            respaldo = DATOS.with_suffix(DATOS.suffix + ".bak")
            detalle = f" Revisa el respaldo {respaldo}." if respaldo.exists() else ""
            raise RuntimeError(f"No se pudo leer {DATOS}; se conservó el archivo para recuperación.{detalle}") from error
        datos = json.loads(json.dumps(_cache_data))
    else:
        datos = {}

    cumplidos = datos.get("cumplidos") or [dict(item, id=str(i)) for i, item in enumerate(INICIALES)]
    for i, item in enumerate(cumplidos):
        item.setdefault("id", str(i))
        item.setdefault("foto", "")
    datos["cumplidos"] = cumplidos
    datos.setdefault("carta", CARTA_INICIAL)
    datos.setdefault("saludos", dict(SALUDOS_INICIALES))
    for clave, valor in SALUDOS_INICIALES.items():
        datos["saludos"].setdefault(clave, valor)
    datos.setdefault("contenido", json.loads(json.dumps(CONTENIDO_INICIAL, ensure_ascii=False)))
    for clave, valor in CONTENIDO_INICIAL.items():
        datos["contenido"].setdefault(clave, json.loads(json.dumps(valor, ensure_ascii=False)))
    return datos


def guardar_datos(datos: dict) -> None:
    global _cache_mtime, _cache_data
    DATOS.parent.mkdir(parents=True, exist_ok=True)
    temporal = DATOS.with_suffix(DATOS.suffix + ".tmp")
    respaldo = DATOS.with_suffix(DATOS.suffix + ".bak")
    respaldo_temporal = DATOS.with_suffix(DATOS.suffix + ".bak.tmp")
    temporal.write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8")
    if DATOS.exists():
        shutil.copy2(DATOS, respaldo_temporal)
        respaldo_temporal.replace(respaldo)
    temporal.replace(DATOS)
    _cache_data = json.loads(json.dumps(datos))
    _cache_mtime = DATOS.stat().st_mtime


def exigir_admin(token: Optional[str]) -> None:
    esperado = os.getenv("DALLANA_ADMIN_TOKEN", "")
    if not esperado:
        raise HTTPException(503, "Configura DALLANA_ADMIN_TOKEN en el servidor.")
    if not token or not secrets.compare_digest(token, esperado):
        raise HTTPException(401, "Clave incorrecta.")


def firma_imagen_valida(tipo: str, contenido: bytes) -> bool:
    firmas = {
        "image/png": lambda data: data.startswith(b"\x89PNG\r\n\x1a\n"),
        "image/jpeg": lambda data: data.startswith(b"\xff\xd8\xff"),
        "image/webp": lambda data: len(data) >= 12 and data.startswith(b"RIFF") and data[8:12] == b"WEBP",
        "image/gif": lambda data: data.startswith((b"GIF87a", b"GIF89a")),
    }
    validar = firmas.get(tipo)
    return bool(contenido and validar and validar(contenido))


def encontrar(datos: dict, mensaje_id: str) -> dict:
    item = next((item for item in datos["cumplidos"] if str(item["id"]) == mensaje_id), None)
    if item is None:
        raise HTTPException(404, "No encontré ese recuerdo.")
    return item


class Cumplido(BaseModel):
    mensaje: str = Field(min_length=1, max_length=500)
    foto: str = Field(default="", max_length=2000)


class Carta(BaseModel):
    carta: str = Field(min_length=1, max_length=10000)


class Saludos(BaseModel):
    manana: str = Field(min_length=1, max_length=500)
    noche: str = Field(min_length=1, max_length=500)


class Contenido(BaseModel):
    autoestima: list[dict]
    cartas: list[dict]
    frasco: list[str]
    museo: list[dict]
    suenos: list[dict]


@app.get("/")
def raiz():
    return {"estado": "La API del amor está funcionando 💌", "cumplidos": len(leer_datos()["cumplidos"])}


@app.get("/health")
def health():
    try:
        datos = leer_datos()
        return {"ok": True, "cumplidos": len(datos["cumplidos"])}
    except Exception as e:
        return {"ok": False, "error": str(e)}


@app.get("/api/cumplido")
def obtener_cumplido(ultimo: Optional[str] = None):
    cumplidos = leer_datos()["cumplidos"]
    opciones = [item for item in cumplidos if str(item["id"]) != str(ultimo)] or cumplidos
    if not opciones:
        raise HTTPException(503, "Todavía no hay recuerdos guardados.")
    item = random.choice(opciones)
    return {**item, "total": len(cumplidos)}


@app.get("/api/del-dia")
def mensaje_del_dia():
    datos = leer_datos()
    cumplidos = datos["cumplidos"]
    if not cumplidos:
        raise HTTPException(503, "Todavía no hay recuerdos guardados.")
    hoy = datetime.now(ZoneInfo("America/Santiago")).date()
    item = cumplidos[hoy.toordinal() % len(cumplidos)]
    return {**item, "fecha": hoy.isoformat()}


@app.get("/api/momento")
def mensaje_del_momento():
    datos = leer_datos()
    ahora = datetime.now(ZoneInfo("America/Santiago"))
    if ahora.hour < 12:
        return {"id": "saludo-manana", "mensaje": datos["saludos"]["manana"], "foto": "", "tipo": "Buenos días"}
    if ahora.hour >= 21:
        return {"id": "saludo-noche", "mensaje": datos["saludos"]["noche"], "foto": "", "tipo": "Buenas noches"}
    cumplidos = datos["cumplidos"]
    if not cumplidos:
        raise HTTPException(503, "Todavía no hay recuerdos guardados.")
    item = random.choice(cumplidos)
    return {**item, "tipo": "Un mensaje para ti"}


@app.get("/api/carta")
def obtener_carta():
    return {"carta": leer_datos()["carta"]}


@app.get("/api/contenido")
def obtener_contenido():
    return leer_datos()["contenido"]


@app.get("/api/administracion")
def listar_admin(x_admin_token: Optional[str] = Header(default=None)):
    exigir_admin(x_admin_token)
    return leer_datos()


@app.post("/api/administracion/cumplidos")
def agregar_cumplido(nuevo: Cumplido, x_admin_token: Optional[str] = Header(default=None)):
    exigir_admin(x_admin_token)
    datos = leer_datos()
    datos["cumplidos"].append({"id": uuid.uuid4().hex, **nuevo.dict()})
    guardar_datos(datos)
    return {"total": len(datos["cumplidos"])}


@app.put("/api/administracion/cumplidos/{mensaje_id}")
def editar_cumplido(mensaje_id: str, cambio: Cumplido, x_admin_token: Optional[str] = Header(default=None)):
    exigir_admin(x_admin_token)
    datos = leer_datos()
    item = encontrar(datos, mensaje_id)
    item.update(cambio.dict())
    guardar_datos(datos)
    return item


@app.delete("/api/administracion/cumplidos/{mensaje_id}")
def eliminar_cumplido(mensaje_id: str, x_admin_token: Optional[str] = Header(default=None)):
    exigir_admin(x_admin_token)
    datos = leer_datos()
    encontrar(datos, mensaje_id)
    if len(datos["cumplidos"]) <= 1:
        raise HTTPException(409, "Debes conservar al menos un recuerdo.")
    datos["cumplidos"] = [item for item in datos["cumplidos"] if str(item["id"]) != mensaje_id]
    guardar_datos(datos)
    return {"total": len(datos["cumplidos"])}


@app.post("/api/administracion/fotos")
async def subir_foto(foto: UploadFile = File(...), x_admin_token: Optional[str] = Header(default=None)):
    exigir_admin(x_admin_token)
    extensiones = {"image/png": ".png", "image/jpeg": ".jpg", "image/webp": ".webp", "image/gif": ".gif"}
    if foto.content_type not in extensiones:
        raise HTTPException(415, "El archivo debe ser una imagen.")
    extension = extensiones[foto.content_type]
    contenido = await foto.read(8 * 1024 * 1024 + 1)
    if len(contenido) > 8 * 1024 * 1024:
        raise HTTPException(413, "La imagen debe pesar menos de 8 MB.")
    if not firma_imagen_valida(foto.content_type, contenido):
        raise HTTPException(415, "El archivo no coincide con el formato de imagen declarado.")
    nombre = f"{uuid.uuid4().hex}{extension}"
    (FOTOS / nombre).write_bytes(contenido)
    return {"foto": f"/media/{nombre}"}


@app.put("/api/administracion/carta")
def actualizar_carta(nueva: Carta, x_admin_token: Optional[str] = Header(default=None)):
    exigir_admin(x_admin_token)
    datos = leer_datos()
    datos["carta"] = nueva.carta
    guardar_datos(datos)
    return {"guardado": True}


@app.put("/api/administracion/saludos")
def actualizar_saludos(nuevos: Saludos, x_admin_token: Optional[str] = Header(default=None)):
    exigir_admin(x_admin_token)
    datos = leer_datos()
    datos["saludos"] = nuevos.dict()
    guardar_datos(datos)
    return {"guardado": True}


@app.put("/api/administracion/contenido")
def actualizar_contenido(nuevo: Contenido, x_admin_token: Optional[str] = Header(default=None)):
    exigir_admin(x_admin_token)
    contenido = nuevo.dict()
    for clave in ("autoestima", "cartas", "frasco", "museo", "suenos"):
        if not contenido[clave]:
            raise HTTPException(422, f"La colección {clave} debe contener al menos un elemento.")
    for item in contenido["cartas"]:
        if not isinstance(item, dict) or not item.get("titulo") or not item.get("mensaje"):
            raise HTTPException(422, "Cada carta debe tener 'titulo' y 'mensaje'.")
    for item in contenido["museo"]:
        if not isinstance(item, dict) or not item.get("titulo"):
            raise HTTPException(422, "Cada vitrina del museo debe tener 'titulo'.")
    datos = leer_datos()
    datos["contenido"] = contenido
    guardar_datos(datos)
    return {"guardado": True, "contenido": contenido}