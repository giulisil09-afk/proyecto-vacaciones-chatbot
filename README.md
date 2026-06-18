# Sistema de Gestión de Vacaciones

**Tecnicatura Universitaria en Programación – Organización Empresarial**

**Autora:** Silva Lourdes

**Fecha:** Junio 2026

---

## Descripción del Proyecto

Este proyecto implementa un sistema de gestión de solicitudes de vacaciones desarrollado en Python.

El programa guía al usuario paso a paso mediante una conversación en consola, consulta una base de datos almacenada en Excel y determina si una solicitud de vacaciones puede ser aprobada o rechazada según la cantidad de días disponibles del empleado.

El trabajo integra los siguientes conceptos:

* Modelado de procesos BPMN 2.0
* Máquina de estados
* Gateway de decisión (aprobación/rechazo)
* Manejo de errores y caminos alternativos
* Persistencia de datos mediante Excel

---

## Características

✅ Máquina de estados para controlar la conversación

✅ Validación de legajo de empleado

✅ Validación de fechas ingresadas

✅ Cálculo automático de días solicitados

✅ Aprobación o rechazo de solicitudes

✅ Registro automático de solicitudes en Excel

✅ Actualización de días disponibles del empleado

✅ Cancelación del proceso por parte del usuario

✅ Manejo de errores y mensajes informativos

---

## Requisitos

| Requisito | Versión        |
| --------- | -------------- |
| Python    | 3.7 o superior |
| pandas    | Última versión |
| openpyxl  | Última versión |

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/giulisil09-afk/proyecto-vacaciones-chatbot.git
cd proyecto-vacaciones-chatbot
```

### 2. Instalar dependencias

```bash
pip install pandas openpyxl
```

### 3. Ejecutar el programa

```bash
python3 bot.py
```

---

## Base de Datos

La información de los empleados se almacena en el archivo:

```text
empleados.xlsx
```

El archivo contiene:

* Legajo
* Nombre
* Días disponibles de vacaciones

---

## ¿Cómo usar el sistema?

1. Ingresar el número de legajo.
2. Ingresar la fecha de inicio de vacaciones.
3. Ingresar la fecha de fin de vacaciones.
4. El sistema calcula automáticamente los días solicitados.
5. Se verifica la disponibilidad de días.
6. La solicitud es aprobada o rechazada.
7. Si corresponde, se actualizan los datos en el archivo Excel.

---

## Manejo de Errores

El sistema contempla los siguientes casos:

| Error                             | Respuesta                            |
| --------------------------------- | ------------------------------------ |
| Legajo inexistente                | Legajo no encontrado                 |
| Texto en lugar de número          | Debe ingresar un número válido       |
| Formato de fecha incorrecto       | Utilice DD/MM/AAAA                   |
| Fecha final anterior a la inicial | La fecha final no puede ser anterior |
| Días insuficientes                | Solicitud rechazada                  |

---

## Ejemplo de Uso

```text
Ingrese su número de legajo: 1001

Hola Juan Perez. Usted tiene 15 días disponibles.

Ingrese la fecha de inicio: 10/12/2026

Fecha de inicio registrada.

Ingrese la fecha de fin: 20/12/2026

Días solicitados: 11

SOLICITUD APROBADA
```

---

## Estado del Proyecto

El sistema se encuentra completamente funcional y permite:

* Consultar empleados desde una base de datos Excel.
* Solicitar vacaciones mediante una conversación guiada.
* Validar legajos y fechas.
* Calcular días solicitados.
* Aprobar o rechazar solicitudes.
* Registrar operaciones en la base de datos.
* Actualizar días disponibles de los empleados.

---

## Herramientas Utilizadas

* Python
* pandas
* openpyxl
* Excel
* BPMN 2.0
* Git y GitHub

---

## Uso de Inteligencia Artificial

Se utilizó ChatGPT como herramienta de apoyo para:

* Generación de ideas.
* Redacción técnica.
* Revisión de documentación.
* Ejemplos de código.

Todo el desarrollo, adaptación, validación y prueba del proyecto fue realizado por la autora.

---

## Archivos del Proyecto

* bot.py → Código principal
* empleados.xlsx → Base de datos de empleados
* README.md → Documentación del proyecto

---

## Repositorio

https://github.com/giulisil09-afk/proyecto-vacaciones-chatbot







