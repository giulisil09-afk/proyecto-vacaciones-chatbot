# Chatbot de Gestión de Vacaciones

**Tecnicatura Universitaria en Programación - Organización Empresarial**

**Autora:** Silva Lourdes

**Fecha:** Junio 2026

---

## 📌 Descripción del Proyecto

Este proyecto implementa un chatbot en Python para automatizar el proceso de solicitud de vacaciones en una organización. El sistema guía al usuario paso a paso, consulta una base de datos simulada en Excel y determina si la solicitud puede ser aprobada o rechazada según los días disponibles.

El trabajo integra conceptos de:
- Modelado de procesos BPMN 2.0
- Máquina de estados
- Gateway de decisión (aprobación/rechazo)
- Manejo de errores (camino infeliz)

---

## 🚀 Características

- ✅ Máquina de estados para manejar la conversación
- ✅ Validación de entradas (legajo, fechas)
- ✅ Gateway de decisión (aprobación/rechazo)
- ✅ Comando `/cancelar` para interrumpir el proceso
- ✅ Base de datos simulada en Excel
- ✅ Manejo de errores (legajo inexistente, fechas incorrectas, etc.)

---

## 📋 Requisitos

| Requisito | Versión |
|-----------|---------|
| Python | 3.7 o superior |
| pandas | última versión |
| openpyxl | última versión |

---

## 🔧 Instalación

### 1. Clonar o descargar el repositorio

```bash
git clone https://github.com/giulisil09-afk/proyecto-vacaciones-chatbot.git
cd proyecto-vacaciones-chatbot

¿Cómo ejecutar?
python3 bot.py


Base de datos (empleados.xlsx)

LEGAJO	NOMBRE	    DIAS_DISPONIBLES
1001	Juan Perez	15
1002	Ana Gomez	5
1003	Carlos Ruiz	20
1004	Lucia Fernandez	10


¿Cómo usar?

Ingresar legajo (ej: 1001)
Ingresar fecha de inicio (formato DD/MM/AAAA)
Ingresar fecha de fin (formato DD/MM/AAAA)
El sistema aprueba o rechaza automáticamente
Comando especial: /cancelar (cancela la solicitud en cualquier momento)

Manejo de errores

Error	                        Respuesta
Legajo inexistente	        "ERROR: Legajo no encontrado"
Texto en lugar de número	"ERROR: Debe ingresar un número válido"
Formato fecha incorrecto	"ERROR: Formato incorrecto. Use DD/MM/AAAA"
Fecha final anterior a inicio	"ERROR: La fecha final no puede ser anterior"
Días insuficientes	        "❌ SOLICITUD RECHAZADA"

Ejemplo de uso:

📌 Ingrese su número de LEGAJO: 1001
✅ Hola Juan Perez. Usted tiene 15 días disponibles.
📌 Ingrese la FECHA DE INICIO: 10/12/2026
✅ Fecha de inicio registrada.
📌 Ingrese la FECHA DE FIN: 20/12/2026
📆 Días solicitados: 11
✅✅✅ SOLICITUD APROBADA ✅✅✅

Herramientas IA

Se utilizó ChatGPT para: generación de ideas, redacción técnica y ejemplos de código.

Archivos del proyecto

bot.py - Código principal
empleados.xlsx - Base de datos
README.md - Este archivo
Repositorio: https://github.com/giulisil09-afk/proyecto-vacaciones-chatbot





