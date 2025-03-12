import subprocess

#Lista de extensiones que deseas instalar
extensions = [
    "ms-python.python",  # Extensión de Python
    "formulahendry.auto-close-tag",  # Cierra automáticamente las etiquetas HTML/XML
    "formulahendry.auto-rename-tag",  # Renombra automáticamente las etiquetas HTML/XML
    "aaron-bond.better-comments",  # Mejora los comentarios en el código
    "adam-watters.vscode-color-pick",  # Selector de colores
    "anseki.vscode-color",  # Herramientas de color
    "kamikillerto.vscode-colorize",  # Visualización de colores en CSS
    "pucelle.vscode-css-navigation",  # Navegación en CSS
    "pranaygp.vscode-css-peek",  # Búsqueda de clases CSS
    "dbaeumer.vscode-eslint",  # Integración con ESLint
    "circlecodesolution.ccs-flutter-color",  # Colores para Flutter
    "ecmel.vscode-html-css",  # Soporte avanzado para HTML y CSS
    "kisstkondoros.vscode-gutter-preview",  # Vista previa de imágenes en el margen
    "sirtori.indenticator",  # Resalta la indentación
    "zignd.html-css-class-completion",  # Autocompletado de clases HTML/CSS
    "xabikos.javascriptsnippets",  # Snippets para JavaScript
    "ms-vscode.live-server",  # Servidor en vivo para desarrollo web
    "ritwickdey.liveserver",  # Servidor en vivo alternativo
    "pkief.material-icon-theme",  # Tema de iconos Material
    "esbenp.prettier-vscode",  # Formateador de código Prettier
    "ms-python.debugpy",  # Depuración de Python
    "mechatroner.rainbow-csv",  # Resaltado de CSV
    "viijay-kr.react-ts-css",  # Soporte para React, TypeScript y CSS
    "tonybaloney.vscode-pets",  # Mascotas en tu editor
    "ban.spellright",  # Corrector ortográfico
]
#Función para instalar una extensión
def install_extension(extension_id):
    try:
        # Usamos 'snap run code' para ejecutar VSCode y pasarle el comando de instalación
        subprocess.run(["snap", "run", "code", "--install-extension", extension_id], check=True)
        print(f"Extensión {extension_id} instalada correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar la extensión {extension_id}: {e}")

#Instalar todas las extensiones de la lista
for extension in extensions:
    install_extension(extension)

print("Todas las extensiones han sido procesadas.")