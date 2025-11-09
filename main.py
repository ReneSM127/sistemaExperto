# =======================================================
# SISTEMA EXPERTO: Diagnóstico de fallas en red local
# =======================================================

def preguntar(pregunta):
    respuesta = input(pregunta + " (si/no): ").strip().lower()
    return respuesta == "si"

def diagnosticar():
    print("=" * 50)
    print("SISTEMA EXPERTO - Diagnóstico de Red (Mayan Tours)")
    print("=" * 50)
    # print("===========================================")

    print("Hola soy tu asistente, te haré unas preguntas y responde con si o no")

    # =======================
    # REGLA 1
    # =======================
    acceso_internet = preguntar("¿Tu equipo tiene acceso a Internet?")
    if not acceso_internet:
        otros_si_tienen = preguntar("¿Los demás equipos de la oficina sí tienen acceso a Internet?")
        if otros_si_tienen:
            print("➡ R1 activada:")
            print("Diagnóstico: Problema en la configuración IP local (gateway o DNS incorrecto).")
            return

    # =======================
    # REGLA 2
    # =======================
    tiene_ip = preguntar("¿El equipo obtiene dirección IP?")
    if not tiene_ip:
        print("➡ R2 activada:")
        print("Diagnóstico: Falla en el servidor DHCP o comunicación con él.")
        return

    # =======================
    # REGLA 3
    # =======================
    cable_desconectado = preguntar("¿Aparece el mensaje 'Cable de red desconectado'?")
    if cable_desconectado:
        print("➡ R3 activada:")
        print("Diagnóstico: Cable dañado o puerto físico del switch/PC defectuoso.")
        return

    # =======================
    # REGLA 4
    # =======================
    conexion_interm = preguntar("¿La conexión es intermitente?")
    navegacion_lenta = preguntar("¿La navegación es muy lenta?")
    if conexion_interm or navegacion_lenta:
        print("➡ R4 activada:")
        print("Diagnóstico: Interferencia Wi-Fi o cableado defectuoso.")
        return

    # =======================
    # REGLA 5
    # =======================
    detecta_wifi = preguntar("¿Tu equipo detecta la red Wi-Fi?")
    if not detecta_wifi:
        print("➡ R5 activada:")
        print("Diagnóstico: Adaptador Wi-Fi deshabilitado o punto de acceso fuera de servicio.")
        return

    # =======================
    # REGLA 6
    # =======================
    puede_imprimir = preguntar("¿Puedes imprimir en la impresora de red?")
    if not puede_imprimir:
        if acceso_internet:
            print("➡ R6 activada:")
            print("Diagnóstico: Error en la impresora de red (IP cambiada o servicio detenido).")
            return

    # =======================
    # REGLA 7
    # =======================
    acceso_carpetas = preguntar("¿Puedes acceder a carpetas compartidas?")
    if not acceso_carpetas and acceso_internet:
        print("➡ R7 activada:")
        print("Diagnóstico: Problema de permisos o rutas de carpetas compartidas.")
        return

    # =======================
    # REGLA 8
    # =======================
    conflicto_ip = preguntar("¿El sistema muestra conflicto de dirección IP?")
    if conflicto_ip:
        print("➡ R8 activada:")
        print("Diagnóstico: Dirección IP duplicada en la red.")
        return

    # Si ninguna regla se cumple
    print("No se encontró una coincidencia directa con las reglas.")
    print("Recomendación: Revisar conectividad general o contactar al soporte técnico.")
    print("Gracias por usar el Sistema Experto de Mayan Tours.")


if __name__ == "__main__":
    diagnosticar()
