import feedparser
import os
import re  # Importamos 're' para limpiar etiquetas HTML y extraer el texto puro

# --- TU CONFIGURACIÓN ---
RSS_URL = "https://mastodon.social/@username.rss" # Cambia esto por tu feed
CARPETA_SALIDA = "mi_blog_mastodon"
# ------------------------

if not os.path.exists(CARPETA_SALIDA):
    os.makedirs(CARPETA_SALIDA)

print("Descargando el feed...")
feed = feedparser.parse(RSS_URL)

posts_data = []
posts_destacados_xalapa = []

# --- PASO 1: RECOPILAR TODOS LOS POSTS ---
for entrada in feed.entries:
    post_id = entrada.link.split('/')[-1]
    nombre_archivo = f"post_{post_id}.html"
    
    contenido = entrada.summary
    fecha = entrada.published
    
    # --- NUEVA LÓGICA PARA EL TÍTULO ---
    # Extraemos el texto puro sin etiquetas HTML (como <p>, <br>, etc.)
    texto_plano = re.sub(r'<[^>]+>', ' ', contenido).strip()
    
    # Si Mastodon envía un título en el RSS, lo usamos. 
    # Si no, usamos los primeros 60 caracteres del texto como título.
    if 'title' in entrada and entrada.title:
        titulo = entrada.title
    elif texto_plano:
        titulo = texto_plano[:60] + "..." if len(texto_plano) > 60 else texto_plano
    else:
        titulo = "Publicación multimedia" # Por si es solo una foto sin texto
    # -----------------------------------

    # Extraer multimedia
    html_multimedia = ""
    if 'media_content' in entrada:
        for media in entrada.media_content:
            url_media = media.get('url')
            tipo_media = media.get('type', '')
            texto_alt = media.get('description', 'Imagen adjunta de Mastodon')
            
            if url_media and tipo_media.startswith('image/'):
                html_multimedia += f'<div class="media-container">\n'
                html_multimedia += f'  <img src="{url_media}" alt="{texto_alt}" class="media-content">\n'
                html_multimedia += f'</div>\n'
            elif url_media and tipo_media.startswith('video/'):
                html_multimedia += f'<div class="media-container">\n'
                html_multimedia += f'  <video src="{url_media}" controls aria-label="{texto_alt}" class="media-content"></video>\n'
                html_multimedia += f'</div>\n'
                
    contenido_completo = contenido + html_multimedia

    # Guardar toda la información
    datos_del_post = {
        "archivo": nombre_archivo,
        "titulo": titulo,
        "fecha": fecha,
        "contenido": contenido_completo,
        "link_original": entrada.link
    }
    posts_data.append(datos_del_post)

    # Buscar si tiene el hashtag xalapa (máximo 5)
    if len(posts_destacados_xalapa) < 5:
        es_xalapa = False
        
        # Revisar en las etiquetas nativas
        if 'tags' in entrada:
            for tag in entrada.tags:
                if 'xalapa' in tag.get('term', '').lower():
                    es_xalapa = True
                    break
        
        # Revisar en el texto
        if not es_xalapa and '#xalapa' in contenido.lower():
            es_xalapa = True

        if es_xalapa:
            posts_destacados_xalapa.append(datos_del_post)

# --- PASO 2: CONSTRUIR EL MENÚ GENERAL HTML ---
html_enlaces_menu = ""
# Usamos enumerate para tener un contador (i) que empiece en 1
for i, post_xalapa in enumerate(posts_destacados_xalapa, start=1):
    html_enlaces_menu += f'<li><a href="{post_xalapa["archivo"]}">Menú {i}</a></li>\n'

html_menu = f"""
    <nav class="menu-general">
        <ul>
            <li><a href="index.html" class="enlace-inicio">Inicio</a></li>
            {html_enlaces_menu}
        </ul>
    </nav>
"""

# --- PASO 3: CREAR LOS ARCHIVOS HTML INDIVIDUALES ---
for post in posts_data:
    ruta_archivo = os.path.join(CARPETA_SALIDA, post["archivo"])
    
    html_post = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{post["titulo"]}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    {html_menu}
    <div class="post-container">
        <div style="margin-top: 20px;">
            {post["contenido"]}
        </div>
        <div class="meta">
            <p><a href="{post["link_original"]}" target="_blank">Ver original en Mastodon</a></p>
        </div>
    </div>
</body>
</html>"""

    with open(ruta_archivo, "w", encoding="utf-8") as f:
        f.write(html_post)

# --- PASO 4: CREAR LA PÁGINA PRINCIPAL (INDEX) ---
html_enlaces_index = ""
for post in posts_data:
    html_enlaces_index += f'<li class="post-item">\n'
    html_enlaces_index += f'  <a href="{post["archivo"]}" class="post-title">{post["titulo"]}</a>\n'
    html_enlaces_index += f'</li>\n'

html_index = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Feed de Mastodon</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    {html_menu}
    <div class="main-container" style="max-width: 1000px; margin: 0 auto;">
        <h1>Mis Últimos Posts</h1>
        <ul class="post-list">
            {html_enlaces_index}
        </ul>
    </div>
</body>
</html>"""

with open(os.path.join(CARPETA_SALIDA, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_index)

print(f"¡Éxito! Títulos actualizados. Menú con {len(posts_destacados_xalapa)} posts destacados de Xalapa.")