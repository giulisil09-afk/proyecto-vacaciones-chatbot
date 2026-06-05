"""
Bot de Gestión de Vacaciones - Versión Consola
Técnicatura Universitaria en Programación - Organización Empresarial

Simula un chatbot para gestionar solicitudes de vacaciones.
Incluye máquina de estados, manejo de errores y gateway de decisión.
"""

import pandas as pd
from datetime import datetime

# ============================================
# ESTADOS DE LA MÁQUINA
# ============================================
ESTADO_ESPERANDO_LEGAJO = 1
ESTADO_ESPERANDO_FECHA_INICIO = 2
ESTADO_ESPERANDO_FECHA_FIN = 3
ESTADO_VALIDANDO = 4

# ============================================
# CARGAR BASE DE DATOS SIMULADA (EXCEL)
# ============================================
try:
    empleados = pd.read_excel("empleados.xlsx")
    print("✅ Base de datos cargada correctamente\n")
except Exception as e:
    print(f"❌ Error al cargar la base de datos: {e}")
    print("Asegurate de tener el archivo 'empleados.xlsx' en la misma carpeta")
    exit()

# ============================================
# VARIABLES GLOBALES
# ============================================
estado = ESTADO_ESPERANDO_LEGAJO
legajo = None
nombre = None
dias_disponibles = None
fecha_inicio = None
fecha_fin = None
dias_solicitados = None

# ============================================
# INICIO DEL PROGRAMA
# ============================================
print("=" * 55)
print("        SISTEMA DE GESTIÓN DE VACACIONES")
print("=" * 55)
print("Comando disponible: /cancelar (cancela la solicitud en cualquier momento)")
print("")

# ============================================
# BUCLE PRINCIPAL (MÁQUINA DE ESTADOS)
# ============================================
while True:
    
    # -------------------------------------------------
    # ESTADO 1: ESPERANDO LEGAJO
    # -------------------------------------------------
    if estado == ESTADO_ESPERANDO_LEGAJO:
        entrada = input("📌 Ingrese su número de LEGAJO: ")
        
        # Comando /cancelar
        if entrada == "/cancelar":
            print("❌ Proceso cancelado. Use /vacaciones para reiniciar.\n")
            estado = ESTADO_ESPERANDO_LEGAJO
            continue
        
        # Validar que sea número
        try:
            legajo = int(entrada)
        except ValueError:
            print("❌ ERROR: Debe ingresar un número válido.\n")
            continue
        
        # Buscar en la base de datos
        empleado = empleados[empleados["LEGAJO"] == legajo]
        
        if empleado.empty:
            print("❌ ERROR: Legajo no encontrado. Verifique e intente nuevamente.\n")
            continue
        
        # Guardar datos del empleado
        nombre = empleado["NOMBRE"].values[0]
        dias_disponibles = int(empleado["DIAS_DISPONIBLES"].values[0])
        
        print(f"✅ Hola {nombre}. Usted tiene {dias_disponibles} días disponibles.\n")
        estado = ESTADO_ESPERANDO_FECHA_INICIO
    

    # -------------------------------------------------
    # ESTADO 2: ESPERANDO FECHA DE INICIO
    # -------------------------------------------------
    elif estado == ESTADO_ESPERANDO_FECHA_INICIO:
        entrada = input("📌 Ingrese la FECHA DE INICIO (formato DD/MM/AAAA): ")
        
        # Comando /cancelar
        if entrada == "/cancelar":
            print("❌ Proceso cancelado. Use /vacaciones para reiniciar.\n")
            estado = ESTADO_ESPERANDO_LEGAJO
            continue
        
        # Validar formato de fecha
        try:
            fecha_inicio = datetime.strptime(entrada, "%d/%m/%Y")
        except ValueError:
            print("❌ ERROR: Formato incorrecto. Use DD/MM/AAAA (ejemplo: 10/12/2026)\n")
            continue
        
        # Validar que no sea fecha pasada
        if fecha_inicio.date() < datetime.now().date():
            print("❌ ERROR: No se pueden solicitar vacaciones con fecha pasada.\n")
            continue
        
        print("✅ Fecha de inicio registrada.\n")
        estado = ESTADO_ESPERANDO_FECHA_FIN
    

    # -------------------------------------------------
    # ESTADO 3: ESPERANDO FECHA DE FIN
    # -------------------------------------------------
    elif estado == ESTADO_ESPERANDO_FECHA_FIN:
        entrada = input("📌 Ingrese la FECHA DE FINALIZACIÓN (formato DD/MM/AAAA): ")
        
        # Comando /cancelar
        if entrada == "/cancelar":
            print("❌ Proceso cancelado. Use /vacaciones para reiniciar.\n")
            estado = ESTADO_ESPERANDO_LEGAJO
            continue
        
        # Validar formato de fecha
        try:
            fecha_fin = datetime.strptime(entrada, "%d/%m/%Y")
        except ValueError:
            print("❌ ERROR: Formato incorrecto. Use DD/MM/AAAA (ejemplo: 20/12/2026)\n")
            continue
        
        # Validar que fecha fin no sea anterior a fecha inicio
        if fecha_fin.date() < fecha_inicio.date():
            print("❌ ERROR: La fecha final no puede ser anterior a la fecha de inicio.\n")
            continue
        
        # Calcular días solicitados
        dias_solicitados = (fecha_fin - fecha_inicio).days + 1
        print(f"📆 Días solicitados: {dias_solicitados}\n")
        estado = ESTADO_VALIDANDO
    

    # -------------------------------------------------
    # ESTADO 4: VALIDANDO DISPONIBILIDAD (GATEWAY)
    # -------------------------------------------------
    elif estado == ESTADO_VALIDANDO:
        
        print("⏳ Validando disponibilidad...\n")
        
        # ============================================
        # GATEWAY: ¿Días disponibles suficientes?
        # ============================================
        if dias_disponibles >= dias_solicitados:
            # ========== RAMA DE APROBACIÓN ==========
            restantes = dias_disponibles - dias_solicitados
            
            print("=" * 55)
            print("✅✅✅ SOLICITUD APROBADA ✅✅✅")
            print("=" * 55)
            print(f"   👤 Empleado:   {nombre}")
            print(f"   🆔 Legajo:     {legajo}")
            print(f"   📅 Fecha inicio:  {fecha_inicio.strftime('%d/%m/%Y')}")
            print(f"   📅 Fecha fin:     {fecha_fin.strftime('%d/%m/%Y')}")
            print(f"   📊 Días solicitados: {dias_solicitados}")
            print(f"   📊 Días disponibles restantes: {restantes}")
            print("=" * 55)
            print("🎉 ¡Disfrute sus vacaciones! Operación registrada en el sistema.\n")
            
        else:
            # ========== RAMA DE RECHAZO ==========
            faltantes = dias_solicitados - dias_disponibles
            
            print("=" * 55)
            print("❌❌❌ SOLICITUD RECHAZADA ❌❌❌")
            print("=" * 55)
            print(f"   👤 Empleado:   {nombre}")
            print(f"   🆔 Legajo:     {legajo}")
            print(f"   📅 Fecha inicio:  {fecha_inicio.strftime('%d/%m/%Y')}")
            print(f"   📅 Fecha fin:     {fecha_fin.strftime('%d/%m/%Y')}")
            print(f"   📊 Días disponibles: {dias_disponibles}")
            print(f"   📊 Días solicitados: {dias_solicitados}")
            print(f"   ⚠️ Días faltantes:   {faltantes}")
            print("=" * 55)
            print("❌ Solicitud rechazada por falta de días disponibles.\n")
        
        # ============================================
        # PREGUNTAR SI QUIERE HACER OTRA SOLICITUD
        # ============================================
        respuesta = input("¿Desea realizar otra solicitud? (s/n): ")
        if respuesta.lower() == "s" or respuesta.lower() == "si":
            # Reiniciar variables
            estado = ESTADO_ESPERANDO_LEGAJO
            legajo = None
            nombre = None
            dias_disponibles = None
            fecha_inicio = None
            fecha_fin = None
            dias_solicitados = None
            print("\n" + "=" * 55)
            print("         NUEVA SOLICITUD DE VACACIONES")
            print("=" * 55 + "\n")
        else:
            print("\n" + "=" * 55)
            print("         GRACIAS POR USAR EL SISTEMA")
            print("=" * 55)
            break