

# Scrapping Aplicación Web Topdoctors.com.co 

:shipit: Scrapping information de doctores de topdoctors.com.co

## Empecemos!

Este repositorio captura información de la página web topdoctors.com.co/doctor, navegando por las páginas de la misma y entrando en cada perfil de doctor y substrayendo lo siguiente:
- name: Nombre del profesional
- id_profesional: N° de tarjeta profesional
- profession: Ej. `Pediatra`
- specialities: Especialidades. Ej. `Quimioterapia, Mieloma múltiple, Leucemia...`
- info: Ej. `Nefrología Pediátrica`
- about: Resumen del perfil del doctor(a)
- address: Dirección registrada 
- city: Ciudad registrada
- telephone: Teléfono registrado
- instagram: perfil de instagram registrado en el perfil de la página
- facebook: perfil de instagram registrado en el perfil de la página
- url: url del perfil del doctor

Finalmente genera un archivo .csv con toda la información anterior. En caso no tenga un telefono, o direccion o otro dato, dejará este campo vacío.

### Prerequisites

Pip y python instalados y configurados como variables de ambiente. Luego, instalar pipenv así:

```
pip install pipenv
```

### Instalando

Una vez instalado pipenv en el sistema operativo, sigue instalarlo en un ambiente aislado, así:

```
pipenv install -d
```

Con el comando anterior se instalarán las librerias usadas en el proyecto. Luego el paso siguiente es ejecutar el spider para que se genere el archivo csv con todos los datos antes mencionados. 
El comando a ejecutar es:

```
scrapy runspider topdoctors/topdoctors/spiders/topdoctors.py -o topdoctors.csv
```

Se generará el archivo doctors.csv con toda la información de los doctores. Esta tarea puede que demore unos minutos.

