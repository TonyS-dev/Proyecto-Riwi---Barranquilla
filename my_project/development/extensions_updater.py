import subprocess
import sys
import time

# Lista de extensiones que deseas instalar
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
    "cstrap.python-snippets", #Python snippets
    "usernamehw.errorlens", #Errores
    "mathematic.vscode-pdf", #Pdf-viewer
    "frhtylcn.pythonsnippets" #Python snippets
    "tomoki1207.pdf" #Pdf viewer
    "mhutchie.git-graph"
    "donjayamanne.githistory"
    "eamodio.gitlens"
]

# Función para instalar una extensión con mejor formato
def install_extension(extension_id, index, total):
    progress = f"[{index}/{total}]"
    try:
        print(f"\n{'-' * 60}")
        print(f"{progress} Instalando: {extension_id}")
        
        # Capture the output
        result = subprocess.run(
            ["code", "--install-extension", extension_id],
            capture_output=True,
            text=True,
            check=False
        )
        
        if result.returncode == 0:
            print(f"{progress} ✅ Éxito: {extension_id}")
        else:
            print(f"{progress} ❌ Error: {extension_id}")
            print(f"Detalles: {result.stderr.strip()}")
            
        return result.returncode == 0
            
    except Exception as e:
        print(f"{progress} ❌ Error: {extension_id}")
        print(f"Excepción: {str(e)}")
        return False

# Contador de éxitos y fallos
success_count = 0
failure_count = 0

# Instalar todas las extensiones de la lista
total = len(extensions)
print(f"\n{'=' * 60}")
print(f"INSTALANDO {total} EXTENSIONES")
print(f"{'=' * 60}")

start_time = time.time()

for idx, extension in enumerate(extensions, 1):
    if install_extension(extension, idx, total):
        success_count += 1
    else:
        failure_count += 1

end_time = time.time()
duration = end_time - start_time

print(f"\n{'=' * 60}")
print(f"RESUMEN DE INSTALACIÓN")
print(f"{'=' * 60}")
print(f"Total de extensiones: {total}")
print(f"✅ Instaladas correctamente: {success_count}")
print(f"❌ Fallos: {failure_count}")
print(f"⏱️ Tiempo total: {duration:.2f} segundos")
print(f"{'=' * 60}\n")
