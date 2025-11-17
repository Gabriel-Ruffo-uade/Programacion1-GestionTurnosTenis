# 🎾 Reserva de Turnos – Clases de Tenis

Trabajo Práctico – Programación 1
Universidad Argentina de la Empresa (UADE)

---

## 📖 Idea del Proyecto

Aplicación por consola para gestionar la reserva de turnos de clases de tenis. Permite:

* Registrar y administrar **profesores**
* Registrar y administrar **clientes**
* Gestionar **turnos** (alta, baja, modificación)
* Validar datos de entrada y evitar inconsistencias
* Guardar la información en archivos **JSON locales**

---

## 👥 Roles

* **Project leader**: Amorrortu Belèn 
* **Desarrollador**: Mottura Diana
* **QA tester**: Oven Santiago
* **Analista funcional**: Citoler Martìn
* **Documentación**: Ruffo Eduardo Gabriel

---

## 🎯 Objetivos

* Crear una aplicación de consola para gestionar turnos.
* Mantener gestión local en JSON (clientes, profesores, turnos).
* Implementar validaciones en entradas de usuarios y turnos.
* Sentar bases para futura implementación con interfaz gráfica.

---

## 📝 Boceto del Menú Principal

```
--- MENÚ PRINCIPAL ---
1. Gestionar clientes
2. Gestionar profesores
3. Gestionar turnos
0. Salir
```

Cada submenú permite **listar, agregar, modificar o eliminar** registros.

---

## 📌 Ejemplos de Uso

* **Agregar Profesor**

  * Entrada: `Nombre, Turno`
  * Salida: Profesor agregado al archivo `Profesores.json` y mensaje en consola.

* **Eliminar Profesor**

  * Entrada: `ID`
  * Salida: Profesor eliminado de `Profesores.json` con confirmación en consola.

* **Agregar Cliente**

  * Entrada: `Nombre, Numero`
  * Salida: Cliente agregado a `Clientes.json`.

---

## ⚙️ Estructura del Proyecto

```
Programacion1-GestionTurnosTenis/
│
├── Programacion1-GestionTurnosTenis-main/
│   ├── data/
│   │   ├── clientes.json
│   │   ├── profesores.json
│   │   ├── turnos.json
│   ├── clientes.py
│   ├── main.py
│   ├── menu.py
│   ├── profesores.py
│   ├── storage.py
│   ├── turnos.py
│   ├── utils.py
│   ├── validaciones.py
```

* `utils.py` y `validaciones.py`: centraliza funciones de validación (ej. validar nombre no vacío, edad > 0, turno válido, fecha/hora).
* Cada módulo (`clientes`, `profesores`, `turnos`) implementa sus funciones CRUD apoyándose en `utils` y `validaciones.py`.

---

## 📚 Documentación Técnica

### 👨‍🏫 Profesores

#### Alta (Agregar Profesor)

* **Input**:

  * `nombre` (string, obligatorio, no vacío)
  * `turno` (string: `"Mañana"`, `"Tarde"`, `"Noche"`)
* **Validaciones (`utils` y `validaciones.py`)**:

  * Nombre no vacío (`validar_nombre`)
  * Turno debe ser uno de los valores válidos (`validar_turno`)
* **Ejemplo**:

  * Entrada: `"Juan Pérez", "Mañana"`
  * Salida: Profesor agregado a `Profesores.json`

#### Modificación

* **Input**: `id`, nuevos valores de `nombre` y/o `turno`
* **Validaciones**: ID existente, turno válido
* **Ejemplo**:

  * Entrada: `id=2, nombre="Carlos López", turno="Tarde"`
  * Salida: Profesor actualizado correctamente

#### Lectura

* Lista todos los profesores en consola.

#### Baja

* **Input**: `id`
* **Validación**: ID debe existir
* **Salida**: eliminación del registro

---

### 👤 Clientes

#### Alta

* **Input**:

  * `nombre` (string, obligatorio)
  * `edad` (int > 0)
* **Validaciones (`utils` y `validaciones.py`)**:

  * Nombre no vacío
  * Edad mayor a 0
* **Ejemplo**:

  * Entrada: `"Ana García", 25`
  * Salida: Cliente agregado a `Clientes.json`

#### Modificación, Lectura y Baja

* Misma lógica que Profesores.

---

### 📅 Turnos

#### Alta (Reservar Turno)

* **Input**:

  * `id_cliente`
  * `id_profesor`
  * `fecha y hora` (`dd/mm/yyyy hh:mm`)
* **Validaciones (`utils` y `validaciones.py`)**:

  * Los JSON de clientes y profesores deben tener por lo menos una entrada
  * Cliente y profesor deben existir
  * Fecha y hora con formato correcto y existencia real
  * Teléfono válido (solo números, 10 dígitos en formato argentino)
  * Validación horaria por rango de turno (mañana/tarde/noche)
  * La fecha y hora del turno deben coincidir con los horarios disponibles del profesor
  * Se valida que el ID exista utilizando un conjunto (set), el cual permite verificar de forma eficiente si el ID está presente y devolver un valor booleano, optimizando el uso de los recursos del sistema
* **Ejemplo**:

  * Entrada: `id_cliente=1, id_profesor=2, fecha_hora="2025-10-15 18:00`
  * Salida: turno agregado a `Turnos.json`

#### Modificación

* Se selecciona por `id_turno` y se cambia fecha/hora.

#### Lectura

* Lista turnos por mes, cliente o profesor.

#### Baja

* Elimina turno por `id`.

#### Matriz turnos

* Lista los `turnos` junto con su respectivo `cliente` y `profesor`.

#### Estadisticas de turnos

* Muestra la cantidad de turnos tomados y libres de cada mes

---

## ✅ Validaciones Generales

- ✔ **Texto válido:** solo letras y espacios  
- ✔ **Fecha y hora válida:** formato `YYYY-MM-DD HH:MM`, existencia real 
- ✔ **Teléfono válido:** 10 dígitos numéricos  
- ✔ **ID existente:** validado mediante `set` para búsqueda eficiente  
- ✔ **Turnos válidos:** `Mañana / Tarde / Noche`  
- ✔ **Horario coincide con el turno:** validación de rango horario  
- ✔ **Nombre no vacío:** evita entradas en blanco o solo espacios  
- ✔ **IDs únicos e incrementales:** controlados desde los archivos JSON  
- ✔ **Archivos JSON creados automáticamente** si no existen

---

## 📖 Bibliografía

* Material de Programación 1 – UADE
* Documentación de Python y JSON
