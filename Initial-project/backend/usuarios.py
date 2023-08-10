import os
import json
import pprint

# Ruta de la carpeta que contiene los archivos JSON
folder = "pruebatecnica"

# Ruta completa del directorio de la carpeta y ruta completa donde guardar el archivo resultado
folder_path = os.path.join(os.getcwd(), folder)

# Crear un diccionario para almacenar los módulos y los usuarios correspondientes
# module_users = {}
module_users = {
    "auth_module": {},
    "content_module": {}
}

# Leer los archivos JSON y procesar los datos
for file in os.listdir(folder_path):
    if file.endswith(".json"):
        file_path = os.path.join(folder_path, file)

        with open(file_path) as f:
            data = json.load(f)
            provider = data.get("provider", {})
            content_module = provider.get("content_module")
            auth_module = provider.get("auth_module")

            if content_module:
                if content_module not in module_users["content_module"]:
                    module_users["content_module"][content_module] = []
                module_users["content_module"][content_module].append(file)

            if auth_module:
                if auth_module not in module_users["auth_module"]:
                    module_users["auth_module"][auth_module] = []
                module_users["auth_module"][auth_module].append(file)

# Ruta del archivo JSON a guardar en la misma ruta que el archivo usuarios.py
result_file_path = os.path.join(os.path.dirname(__file__), "resultado.json")
print(result_file_path)

# Guardar la información en el archivo JSON
with open(result_file_path, "w") as json_file:
    json.dump(module_users, json_file)

print("Archivo JSON guardado exitosamente:", result_file_path)

