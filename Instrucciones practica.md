# Objetivo
Aplicar, en un repositorio real de GitHub, los comandos de Git que van más allá del flujo básico (add, commit, push, pull), reproduciendo escenarios de trabajo colaborativo donde surgen conflictos, historiales que deben limpiarse, errores que deben corregirse y versiones que deben publicarse formalmente.

## Objetivos específicos
* **Configurar y administrar** un repositorio compartido en GitHub trabajando en equipo.
* **Resolver un conflicto real** generado con `git stash`, sin perder el trabajo de ningún integrante.
* **Diferenciar en la práctica** el resultado de `git merge` y `git rebase` sobre un mismo historial.
* **Utilizar** `git rebase -i`, `git cherry-pick`, `git reset`, `git revert`, `git reflog`, `git bisect` y `git tag` en situaciones que justifican su uso.
* **Documentar** el proceso técnico y las decisiones tomadas por el equipo en un informe escrito.

## Instrucciones generales
* El trabajo se realiza en **grupos de 3 a 4 integrantes**, asignados por el docente o de forma libre según se indique en clase.
* **Todos los integrantes** deben tener commits propios (con su nombre y correo configurados) visibles en el historial del repositorio. No se aceptan repositorios donde una sola persona hizo todo el trabajo.
* Los escenarios están diseñados para ejecutarse en orden, ya que varios reutilizan las ramas y commits creados en el escenario anterior.
* Cada escenario indica qué capturas de pantalla o evidencia debe incluirse en el informe: no basta con ejecutar el comando, hay que **explicar qué ocurrió y por qué**.
* Si un comando destruye información (`reset --hard`, por ejemplo), practíquenlo solo después de comprender lo que hace: usen ramas de prueba si tienen dudas.

## Requisitos previos
* **Git instalado y configurado** (`git config --global user.name` / `user.email`) por cada integrante.
* **Cuenta activa en GitHub** y acceso de escritura (colaborador) al repositorio del equipo.
* **Editor de texto o IDE** de preferencia y una terminal (Git Bash, terminal de Linux/macOS o similar).
* Haber revisado la presentación de clase "Git: qué es y cómo usarlo", en especial la sección de comandos avanzados.

---

# Parte 1 · Preparación del repositorio
Antes de iniciar los escenarios, el equipo debe crear la base de trabajo. Un integrante crea el repositorio y agrega a los demás como colaboradores; todos deben clonarlo y poder publicar cambios.

### Tareas a realizar
1. Crear un repositorio nuevo en GitHub llamado `practicagit-avanzado` (público o privado, según indique el docente), inicializado con un `README.md`.
2. Agregar como colaboradores a los demás integrantes del equipo (Settings → Collaborators).
3. Cada integrante clona el repositorio en su máquina con `git clone` y configura su identidad si aún no lo ha hecho.
4. En el `README.md`, agregar una tabla con los nombres de los integrantes y el correo/usuario de GitHub que cada uno usó para sus commits.
5. Crear una estructura mínima de proyecto: puede ser un pequeño programa de consola (en cualquier lenguaje) o incluso archivos de texto que simulen código; lo importante es tener contenido versionable para los escenarios siguientes.
6. Hacer el primer commit conjunto ("commit inicial") y publicarlo en la rama `main`.

### Evidencia para el informe
Captura del repositorio en GitHub mostrando a los colaboradores agregados, y del primer commit en el historial.

---

# Parte 2 · Escenarios de práctica
A continuación se describen los escenarios que el equipo debe recrear dentro del repositorio. Cada escenario debe quedar reflejado en el historial real de commits, ramas y tags del repositorio: no es un ejercicio teórico, es evidencia que el docente revisará directamente en GitHub.

## Escenario 1 · Trabajo en ramas (branch / switch)
**Comando(s) protagonista(s):** `git branch` · `git switch`

Cada integrante del equipo va a desarrollar una pequeña funcionalidad distinta dentro del proyecto, de forma aislada, antes de integrarla a `main`.

### Comandos que necesitarás
```bash
git branch <nombre-rama>
git switch <nombre-rama>
git switch -c <nombre-rama>
git push -u origin <nombre-rama>
```

### Tareas a realizar
1. Cada integrante crea su propia rama a partir de `main`, con un nombre descriptivo (por ejemplo `feature-login`, `feature-reporte`).
2. En su rama, cada integrante agrega o modifica al menos un archivo y confirma el cambio con un commit propio.
3. Publican todas las ramas al repositorio remoto (`git push -u origin <rama>`).
4. Ejecutan `git branch -a` para listar todas las ramas locales y remotas, y capturan el resultado.

### Evidencia para el informe
Captura de `git branch -a` mostrando todas las ramas del equipo, y del repositorio en GitHub mostrando los commits de cada integrante en su propia rama.

## Escenario 2 · Conflicto real con git stash
**Comando(s) protagonista(s):** `git stash` · `git stash pop/apply` · `git stash list`

Uno de los integrantes (Persona A) está trabajando sobre `main` y tiene cambios sin confirmar en un archivo. Antes de terminar, otro integrante (Persona B) publica cambios a `main` que modifican esas mismas líneas. Persona A necesita obtener los cambios de Persona B sin perder su propio trabajo.

### Comandos que necesitarás
```bash
git stash
git stash list
git pull
git stash apply (o git stash pop)
# resolver el conflicto manualmente
git add <archivo>
git commit
```

### Tareas a realizar
1. Persona B modifica una línea específica de un archivo compartido (por ejemplo, una función o una constante) directamente en `main` y la publica.
2. Sin haber actualizado su copia, Persona A modifica esa misma línea de forma diferente, sin confirmar el cambio (working directory "sucio").
3. Persona A ejecuta `git stash` para guardar su cambio temporalmente y luego `git pull` para traer el cambio de Persona B.
4. Persona A ejecuta `git stash apply`: Git debe reportar un conflicto en el archivo.
5. Persona A resuelve el conflicto manualmente (elige, combina o reescribe el contenido final), y confirma el resultado con `git add` + `git commit`.
6. Ejecutan `git stash list` antes y después para verificar si el stash aplicado sigue almacenado o debe eliminarse con `git stash drop`.

### Evidencia para el informe
Captura del mensaje de conflicto que reporta Git, del archivo con las marcas `<<<<<<< / ======= / >>>>>>>`, y del commit final donde se resolvió. Expliquen en el informe qué decisión tomaron para resolver el conflicto y por qué.

## Escenario 3 · git merge vs. git rebase
**Comando(s) protagonista(s):** `git merge` · `git rebase`

El equipo va a integrar dos ramas de dos maneras distintas para comparar el resultado en el historial. Se recomienda hacerlo sobre ramas de práctica (por ejemplo copias temporales) para no afectar el trabajo ya integrado.

### Comandos que necesitarás
```bash
git switch main
git merge <rama-feature>
# --- en otra rama de prueba ---
git switch <otra-rama>
git rebase main
git log --oneline --graph --all
```

### Tareas a realizar
1. Creen dos ramas nuevas de práctica a partir de `main`, cada una con 2 o 3 commits propios.
2. Integren la primera rama a `main` usando `git merge` y observen el commit de fusión que se genera.
3. Integren la segunda rama usando `git rebase main` seguido de un merge fast-forward, y observen que no se genera un commit de fusión.
4. Ejecuten `git log --oneline --graph --all` antes y después de cada integración y comparen ambos historiales.

### Evidencia para el informe
Capturas del grafo (`git log --graph`) para el caso de merge y para el caso de rebase, con una breve explicación de al menos dos diferencias visibles entre ambos historiales.

## Escenario 4 · Limpieza de historial con rebase interactivo
**Comando(s) protagonista(s):** `git rebase -i`

Uno de los integrantes hizo varios commits pequeños de corrección ("arreglo typo", "otra corrección", "ahora sí") mientras desarrollaba su funcionalidad. Antes de integrarlos a `main`, el equipo decide limpiar ese historial.

### Comandos que necesitarás
```bash
git switch <rama-con-commits-desordenados>
git rebase -i HEAD~4
# en el editor: pick / squash / reword
```

### Tareas a realizar
1. En una rama de práctica, generen intencionalmente de 4 a 5 commits pequeños y con mensajes poco descriptivos.
2. Ejecuten `git rebase -i HEAD~4` (o el número de commits que corresponda).
3. Combinen (squash) al menos dos commits en uno solo.
4. Cambien (reword) el mensaje final para que sea claro y descriptivo.
5. Verifiquen con `git log --oneline` que el historial quedó limpio antes de integrarlo a `main`.

### Evidencia para el informe
Captura del historial antes (commits desordenados) y después (historial limpio) del rebase interactivo.

## Escenario 5 · Aplicar un hotfix puntual
**Comando(s) protagonista(s):** `git cherry-pick`

Se detecta un error urgente en producción (rama `main`). Uno de los integrantes crea una rama hotfix, corrige el problema con un solo commit, y ese commit debe aplicarse tanto a `main` como a una rama de desarrollo en curso, sin fusionar el resto del historial de ninguna de las dos.

### Comandos que necesitarás
```bash
git switch -c hotfix main
# corregir el error y confirmar
git switch main
git cherry-pick <hash-del-commit-hotfix>
git switch <rama-desarrollo>
git cherry-pick <hash-del-commit-hotfix>
```

### Tareas a realizar
1. Creen una rama hotfix desde `main` y hagan un único commit que corrija un "error" simulado.
2. Apliquen ese commit específico a `main` usando `git cherry-pick` con el hash correspondiente.
3. Apliquen el mismo commit a otra rama activa del equipo, también con cherry-pick.
4. Comparen los hashes del commit original y de las copias aplicadas con cherry-pick: deben ser distintos aunque el contenido sea igual.

### Evidencia para el informe
Captura de `git log` mostrando el mismo cambio con hashes diferentes en las dos ramas donde se aplicó el cherry-pick.

## Escenario 6 · git reset: soft, mixed y hard
**Comando(s) protagonista(s):** `git reset --soft/--mixed/--hard`

El equipo va a comprobar, en una rama de práctica que no afecte el trabajo ya integrado, qué le ocurre exactamente al área de preparación y al directorio de trabajo con cada variante de git reset.

### Comandos que necesitarás
```bash
git reset --soft HEAD~1
git status
git reset --mixed HEAD~1
git status
git reset --hard HEAD~1
git status
```

### Tareas a realizar
1. En una rama de prueba, hagan 3 commits simples y consecutivos.
2. Ejecuten `git reset --soft HEAD~1` y describan con `git status` qué pasó con el último commit y con los cambios.
3. Vuelvan a confirmar el commit y ahora prueben `git reset --mixed HEAD~1` (o solo `git reset HEAD~1`); comparen el resultado con el paso anterior.
4. Finalmente, con un commit de prueba que no les importe perder, ejecuten `git reset --hard HEAD~1` y confirmen con `git status` que no quedó ningún cambio pendiente.

### Evidencia para el informe
Tabla o capturas comparando la salida de `git status` después de cada tipo de reset, señalando qué se conservó y qué se perdió en cada caso.

## Escenario 7 · Deshacer un commit público con revert
**Comando(s) protagonista(s):** `git revert`

Un commit que ya fue publicado en `main` y compartido con el equipo resulta tener un error. Como ya es público, no debe eliminarse del historial con reset: debe deshacerse con un nuevo commit.

### Comandos que necesitarás
```bash
git log --oneline
git revert <hash-del-commit-a-deshacer>
```

### Tareas a realizar
1. Identifiquen (o generen) un commit ya publicado en `main` que "introduce un error" simulado.
2. Ejecuten `git revert` con el hash de ese commit.
3. Verifiquen que el commit original sigue existiendo en el historial y que se agregó un nuevo commit que deshace su efecto.
4. Publiquen el revert a `main`.

### Evidencia para el informe
Captura del historial mostrando ambos commits (el original y el revert), y una breve explicación de por qué en este caso no se usó `git reset`.

## Escenario 8 · Recuperar un commit "perdido"
**Comando(s) protagonista(s):** `git reflog`

Por accidente, un integrante ejecuta un `git reset --hard` a un punto anterior del historial y "pierde" un commit que ya había hecho con trabajo importante. El equipo debe recuperarlo sin rehacer el trabajo desde cero.

### Comandos que necesitarás
```bash
git reset --hard HEAD~2 # provocar la pérdida, a propósito
git reflog
git checkout <hash-recuperado>
git switch -c rama-recuperada <hash-recuperado>
```

### Tareas a realizar
1. En una rama de prueba, hagan un commit con contenido identificable (por ejemplo, un comentario con sus nombres).
2. Provoquen intencionalmente la "pérdida" de ese commit con un `git reset --hard` a un punto anterior.
3. Ejecuten `git reflog` y localicen la entrada correspondiente al commit perdido.
4. Recuperen el commit creando una nueva rama a partir de ese hash y verifiquen que el contenido perdido reaparece.

### Evidencia para el informe
Captura de la salida de `git reflog` señalando la entrada usada, y del contenido recuperado en la nueva rama.

## Escenario 9 · Encontrar el commit que introdujo un error
**Comando(s) protagonista(s):** `git bisect`

El equipo agrega intencionalmente, en algún punto intermedio de una secuencia de 8 a 10 commits, un cambio que "rompe" el proyecto (por ejemplo, un valor incorrecto en una función o una condición invertida). El resto del equipo, sin saber en cuál commit ocurrió, debe encontrarlo con búsqueda binaria.

### Comandos que necesitarás
```bash
git bisect start
git bisect bad
git bisect good <hash-de-un-commit-que-funcionaba>
# repetir hasta encontrarlo:
git bisect good # o
git bisect bad

git bisect reset
```

### Tareas a realizar
1. Un integrante prepara en secreto una rama con 8 a 10 commits, donde uno intermedio introduce el error.
2. Otro integrante, sin ver ese historial de antemano, ejecuta `git bisect start`, marca el estado actual como `bad` y un commit inicial conocido como `good`.
3. Sigue las instrucciones de Git, probando el proyecto en cada punto medio y marcándolo `good` o `bad`, hasta que Git señale el commit exacto que introdujo el error.
4. Finalicen con `git bisect reset` para volver al estado normal del repositorio.
5. Verifiquen manualmente que el commit señalado por Git es, en efecto, el que el equipo modificó a propósito.

### Evidencia para el informe
Captura de la secuencia de `git bisect` (los good/bad ejecutados) y del mensaje final donde Git identifica el commit responsable.

## Escenario 10 · Publicar una versión con tags
**Comando(s) protagonista(s):** `git tag`

El equipo considera que el proyecto llegó a un punto estable y quiere marcarlo formalmente como una versión (release), de forma que pueda identificarse y recuperarse fácilmente en el futuro.

### Comandos que necesitarás
```bash
git tag v1.0.0
git tag -a v1.1.0 -m "Primera versión estable"
git push origin v1.0.0
git push origin --tags
```

### Tareas a realizar
1. Creen un tag ligero (`v1.0.0`) sobre el commit actual de `main`.
2. Después de al menos un commit adicional, creen un tag anotado (`v1.1.0`) que incluya un mensaje describiendo qué cambió.
3. Publiquen ambos tags al repositorio remoto.
4. Verifiquen en la interfaz de GitHub (sección Releases o Tags) que ambos quedaron visibles.

### Evidencia para el informe
Captura de la sección de tags/releases del repositorio en GitHub mostrando ambas versiones publicadas.

---

# Parte 3 · Buenas prácticas de mantenimiento (bonus)
Estas tareas son opcionales y suman puntos adicionales. Aplican al mismo repositorio del equipo.

### .gitignore y git clean
* Agreguen un archivo `.gitignore` que excluya al menos tres tipos de archivo que no deberían versionarse en su proyecto (por ejemplo, archivos temporales, dependencias o configuraciones locales).
* Generen intencionalmente un archivo no rastreado, ejecuten `git clean -n` para previsualizar y luego `git clean -fd` para eliminarlo.

### Alias de Git
* Configuren al menos dos alias personalizados (por ejemplo `git config --global alias.st status`) y muestren su uso en una captura de terminal.

---

# Entregables

### 1. Repositorio en GitHub
* Enlace al repositorio compartido en la plataforma que indique el docente (o entregado por escrito en el informe).
* El historial de commits debe reflejar, de forma real y verificable, cada uno de los escenarios trabajados: ramas, merges, rebases, cherry-picks, resets, reverts y tags.
* Los commits deben estar distribuidos entre los integrantes del equipo (nombre y correo configurados correctamente en Git).
* El `README.md` debe incluir la tabla de integrantes y una breve descripción del proyecto usado como base para los ejercicios.

### 2. Informe técnico
Documento (PDF o Word) entregado por el equipo, con la siguiente estructura mínima:
* **Portada:** integrantes, carné, curso, sección y fecha.
* **Introducción y objetivo** del trabajo.
* **Desarrollo:** una sección por cada escenario, con el comando utilizado, una captura de pantalla como evidencia y una explicación en sus propias palabras de qué ocurrió internamente en Git.
* **Dificultades encontradas** y cómo las resolvieron como equipo.
* **Conclusiones:** una conclusión individual por integrante (mínimo tres líneas cada una).
* **Enlace al repositorio** de GitHub utilizado.

---

# Rúbrica de evaluación 

| Criterio | Descripción | Puntos |
| :--- | :--- | :---: |
| **Repositorio en GitHub** | El historial evidencia el uso correcto de ramas, merge, rebase, cherry-pick, reset, revert, reflog, bisect y tags descritos en los escenarios. | 35 |
| **Resolución de conflictos** | El conflicto generado con `git stash` es real, se documenta el mensaje de conflicto y la resolución manual es coherente. | 15 |
| **Trabajo en equipo** | Los commits están distribuidos entre los integrantes, cada uno con su propia identidad configurada en Git. | 15 |
| **Informe técnico** | Incluye evidencia (capturas) y explicación técnica correcta de cada escenario, no solo la ejecución del comando. | 20 |
| **Buenas prácticas (bonus)** | `.gitignore`, `git clean` y alias configurados y documentados. | 10 |
| **Conclusiones y presentación** | Conclusiones individuales, ortografía, orden y claridad general del documento. | 5 |
| **Total** | | **100** |

---

# Anexo · Referencia rápida de comandos

| Comando | Uso principal |
| :--- | :--- |
| `git stash` / `stash pop` / `stash list` | Guardar y recuperar cambios sin confirmar, de forma temporal. |
| `git branch` / `git switch` | Crear, listar y cambiar entre ramas. |
| `git merge` | Fusionar una rama en otra, conservando ambos historiales. |
| `git rebase` | Mover los commits de una rama sobre la punta de otra, dejando un historial lineal. |
| `git rebase -i` | Reescribir el historial reciente: combinar, reordenar o editar commits. |
| `git cherry-pick` | Copiar un commit específico de una rama a otra. |
| `git reset --soft/--mixed/--hard` | Mover el puntero de commit, con distinto efecto sobre el index y el directorio de trabajo. |
| `git revert` | Deshacer un commit ya publicado, creando uno nuevo que revierte su efecto. |
| `git reflog` | Ver el historial de movimientos de HEAD y recuperar commits "perdidos". |
| `git bisect` | Búsqueda binaria sobre el historial para encontrar el commit que introdujo un error. |
| `git tag` | Marcar un commit específico como una versión o release. |