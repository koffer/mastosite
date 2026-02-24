![ultimospost](https://github.com/user-attachments/assets/4740f680-02ab-4e3b-8459-290d92ae20d3)
```markdown


# Generador de Web Estática desde Mastodon 🐘

Este proyecto es un script en Python que lee el feed RSS de cualquier cuenta pública de Mastodon y genera automáticamente un sitio web estático (archivos HTML). Es ideal para tener un respaldo de tus publicaciones o crear un blog personal ligero, rápido y sin necesidad de bases de datos.

## ✨ Características

- **Sitio Estático Rápido:** Genera un archivo `index.html` principal y páginas HTML individuales por cada publicación.
- **Soporte Multimedia:** Extrae automáticamente imágenes y videos adjuntos en Mastodon, incluyendo sus descripciones (textos `alt`) para mejorar la accesibilidad y el SEO.
- **Títulos Automáticos:** Como Mastodon no usa títulos tradicionales, el script extrae de forma inteligente las primeras palabras de tu publicación para nombrar cada página.
- **Menú Dinámico de Destacados:** Busca y ancla en el menú principal superior las últimas 5 publicaciones que contengan un hashtag específico (por defecto configurado para `#xalapa`), mostrando este menú en todas las páginas.
- **Diseño Separado:** Utiliza un archivo `style.css` externo para mantener el código HTML limpio y facilitar la personalización visual (incluyendo una retícula responsiva para el inicio).

## 🛠️ Requisitos Previos

Para ejecutar este proyecto necesitas tener instalado en tu computadora:
- [Python 3.6+](https://www.python.org/downloads/)

## 🚀 Instalación

1. **Clonar o descargar el proyecto:**
   Guarda los archivos del proyecto en una carpeta en tu computadora.

2. **Crear un entorno virtual (Recomendado):**
   Abre tu terminal, navega a la carpeta del proyecto y ejecuta:
   ```bash
   python -m venv venv

```

3. **Activar el entorno virtual:**
* En Windows:
```bash
venv\Scripts\activate

```


* En Mac / Linux:
```bash
source venv/bin/activate

```




4. **Instalar dependencias:**
El proyecto requiere la librería `feedparser` para leer el archivo RSS. Instálala con:
```bash
pip install feedparser

```



## ⚙️ Configuración

Antes de ejecutar el script, abre el archivo `generar_sitio.py` en tu editor de texto y modifica la sección de configuración con tus datos:

```python
# --- TU CONFIGURACIÓN ---
RSS_URL = "[https://tu-instancia.social/@tu_usuario.rss](https://tu-instancia.social/@tu_usuario.rss)" # Cambia esto por tu URL de RSS
CARPETA_SALIDA = "mi_blog_mastodon" # Nombre de la carpeta donde se guardará la web
# ------------------------

```

Si deseas cambiar el hashtag destacado del menú superior, busca la palabra `'xalapa'` (alrededor de la línea 70) en el script de Python y cámbiala por el término que prefieras.

## 🎨 El archivo de Estilos (CSS)

Asegúrate de tener un archivo llamado `style.css` dentro de la carpeta generada (`mi_blog_mastodon`). Este archivo controla la retícula responsiva del inicio y los colores del menú. Si no lo tienes, puedes crear uno con reglas básicas de CSS Grid para organizar la lista de posts (`ul.post-list`).

## ▶️ Uso

Una vez configurado, simplemente ejecuta el script desde tu terminal:

```bash
python generar_sitio.py

```

Verás un mensaje de éxito en la terminal indicando cuántas páginas se generaron. Abre la carpeta `mi_blog_mastodon` y haz doble clic en el archivo `index.html` para ver tu nuevo blog funcionando en tu navegador web.

## 📂 Estructura del Resultado

Después de la ejecución, tu carpeta se verá así:

```text
mi_blog_mastodon/
│
├── style.css           # Tu archivo de estilos (debes crearlo/editarlo)
├── index.html          # Página principal con la retícula de posts
├── post_123456.html    # Página individual del post
├── post_789012.html    # Página individual del post
└── ...

```

```

***

### ¿Cómo usar este texto?
Simplemente crea un archivo nuevo en tu editor de código, pégale todo el texto del bloque anterior (empezando desde el `# Generador de Web...`), y guárdalo con el nombre exacto de **`README.md`** en la misma carpeta donde tienes tu archivo `generar_sitio.py`. 

Si subes esto a GitHub o GitLab en el futuro, la plataforma detectará automáticamente este archivo y lo mostrará como la portada de tu proyecto.

```
