# Manual de Git

Git es un sistema de control de versiones distribuido que permite rastrear cambios en archivos y coordinar el trabajo entre multiples personas.

## Comandos Basicos

### git status

Muestra el estado actual del repositorio, indicando los archivos modificados, los que estan en el area de preparacion (staging area) y la rama en la que trabajamos.

```bash
git status
```

### git log

Muestra el historial de cambios del repositorio, incluyendo el autor, la fecha y el mensaje de cada commit.

```bash
git log
```

### git diff

Compara los cambios entre el directorio de trabajo y el area de preparacion.

```bash
git diff
```

### git show

Muestra detalles de un commit especifico, incluyendo los archivos modificados y su contenido.

```bash
git show <commit_hash>
```

### git config

Permite configurar opciones globales de Git, como el nombre de usuario y el correo electronico.

```bash
git config --global user.name "nombre_de_usuario"
git config --global user.email "correo_electronico"
git config --list
```

### git fetch

Trae la ultima version de la rama desde el repositorio remoto (origin) sin fusionarla automaticamente con la rama actual.

```bash
git fetch origin <nombre-de-la-rama>
```

### git merge

Combina los cambios de una rama con otra. Integra el historial de dos ramas

```bash
git merge <nombre-de-la-rama>
```

### git reset

Permite deshacer cambios en el area de preparacion o en el historial de commits.

```bash
git reset
```

### git revert

Crea un nuevo commit que revierte los cambios de un commit anterior, sin alterar el historial.

```bash
git revert <commit_hash>
```

### Gestion de un Repositorio

### Inicializar un Repositorio

```bash
# Inicializa un nuevo repositorio local Git en el directorio actual. Esto crea una carpeta oculta llamada .git donde Git almacena toda la informacion del repositorio.
git init

# Agrega todos los archivos modificados y nuevos al area de preparacion (staging area).
git add .

# Crea un commit con los cambios preparados y un mensaje descriptivo.
git commit -m "mensaje del commit"
```

### Subir un Repositorio a GitHub

```bash
# Conecta el repositorio local con un repositorio remoto en la URL especificada.
git remote add origin <url_del_repositorio_remoto>

# Renombra la rama predeterminada a main.
git branch -M main

# Sube los cambios al repositorio remoto y establece la rama main como la rama predeterminada para futuros push. La opcion -u asocia la rama local con la rama remota.
git push -u origin main
```

### Crear y Trabajar con Ramas

```bash
# Crea una nueva rama llamada develop.
git branch develop

# Cambia a la rama develop para comenzar a trabajar en ella.
git checkout develop

# Sube la rama develop al repositorio remoto.
git push origin develop
```

### Trabajar en la Rama `develop`

```bash
# Hacer cambios en los archivos del proyecto.

# Agregar todos los cambios al area de preparacion.
git add .

# Crea un commit con los cambios preparados y un mensaje descriptivo.
git commit -m "mensaje del commit"

# Sube los cambios de la rama develop al repositorio remoto.
git push origin develop
```

### Crear un Release

```bash
# Cambia a la rama "develop" para asegurarno de trabajar desde la ultima version del codigo.
git checkout develop

#  Crea una nueva rama llamada release-1.0.0 desde "develop".
git branch release-1.0.0

# Cambia a la rama de release para comenzar a trabajar en ella.
git checkout release-1.0.0

# Trae los ultimos cambios de "develop" a la rama de "release".
git pull origin develop

# Sube la rama de release al repositorio remoto.
git push origin release-1.0.0
```

### Fusionar Cambios

```bash
# Cambiarse a la rama principal (main).
git checkout main

# Traer y fusionar los cambios de la rama remota.
git pull origin release-1.0.0

# Subir los cambios fusionados al repositorio remoto.
git push origin main
```