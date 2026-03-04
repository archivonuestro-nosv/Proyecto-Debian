# Conclusiones del Taller 1: Introducción a Git y manejo de ramas

## Leonardo Morales
## Desarrollo de Software

### Fecha: marzo 2026

---

## ¿Qué aprendí en este taller?

En este taller aprendí a trabajar con **ramas en Git**, una herramienta fundamental para el desarrollo de software moderno. A continuación, resumo los principales aprendizajes:

### 1. Creación y manejo de ramas
- Aprendí a crear ramas con `git branch <nombre>`.
- Descubrí cómo cambiar entre ramas usando `git switch <nombre>`.
- Comprendí que cada rama es un "espacio de trabajo independiente" que puede tener sus propios archivos y commits sin afectar a las demás.

### 2. Flujo básico de Git
- Practiqué el ciclo básico: `git add` para preparar archivos, `git commit -m "mensaje"` para guardar los cambios en el historial.
- Aprendí a ver el estado del repositorio con `git status`.
- Utilicé `git log` y el alias `git tree` para visualizar el historial de commits de forma gráfica.

### 3. Archivos desarrollados en cada rama

#### Rama `main`
- `README.md` (archivo inicial del repositorio)

#### Rama `programador`
- `fecha.py`
- `bisiesto.py`

#### Rama `analista`
- `palindromo.py` (verifica si un número es capicúa)
- `calculadorainicial.py` (menú de operaciones aritméticas, inicialmente sin ciclo)
- `fibonacci.py` (genera la serie de Fibonacci)

### 4. Modificaciones importantes
En la rama `analista`, modifiqué `calculadorainicial.py` para agregarle un **ciclo `while`**, lo que permite que el menú se repita hasta que el usuario elija la opción de salir. Esto mejora la experiencia de usuario y muestra cómo se puede iterar sobre el código.

### 5. Comparación entre ramas
Al listar los archivos de cada rama (`ls -l`) y ver sus historiales (`git tree`), confirmé que:
- Cada rama mantiene **sus propios archivos**.
- Los commits de una rama **no afectan a las otras** hasta que se fusionan (tema que veremos más adelante).
- La rama `main` se mantuvo limpia, solo con el archivo inicial, mientras que las ramas de trabajo (`programador` y `analista`) contienen los desarrollos específicos.

---

## Conclusión final

Este taller me permitió comprender la importancia de las **ramas en Git** para organizar el trabajo de desarrollo. Ahora entiendo por qué es útil tener ramas separadas para diferentes funcionalidades: permite trabajar de forma aislada, experimentar sin miedo a dañar la rama principal, y mantener un historial ordenado.

Además, practiqué comandos esenciales de Git que usaré durante todo el curso y en mi futura vida profesional como ingeniero de sistemas.

---

## Comandos utilizados en el taller

| Comando | Descripción |
|---------|-------------|
| `git init` | Inicializar un repositorio |
| `git branch <nombre>` | Crear una nueva rama |
| `git switch <rama>` | Cambiar a otra rama |
| `git add <archivo>` | Agregar archivo al staging area |
| `git commit -m "mensaje"` | Hacer un commit |
| `git status` | Ver el estado del repositorio |
| `git log` | Ver el historial de commits |
| `git tree` (alias) | Ver historial gráfico |
| `ls -l` | Listar archivos (comando de Linux) |
| `nano <archivo>` | Editar archivos en la terminal |
| `python3 <archivo>` | Ejecutar un programa Python |

---

¡Fin del informe!
