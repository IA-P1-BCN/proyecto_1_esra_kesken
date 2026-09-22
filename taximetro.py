import time


TARIFA_MOVIMIENTO = 0.05
TARIFA_PARADO = 0.02

total = 0.0
estado = "parado"
marca_tiempo = None

while True:
    comando = input("Comando: ")
    if comando == "iniciar":
        marca_tiempo = time.time()
        print("Viaje iniciando. Estado: parado")
    elif comando == "movimiento":
        tiempo_transcurrido = time.time() - marca_tiempo
        if estado == "parado":
            total += tiempo_transcurrido * TARIFA_PARADO
        else:
            total += tiempo_transcurrido * TARIFA_MOVIMIENTO
        estado = "movimiento"
        marca_tiempo = time.time()
        print(f"Cambiado a movimiento. Total: {total:.2f}€")  
    elif comando == "parado":
        tiempo_transcurrido = time.time() - marca_tiempo
        if estado == "movimiento":
            total += tiempo_transcurrido * TARIFA_MOVIMIENTO
        else:
            total += tiempo_transcurrido * TARIFA_PARADO
        estado = "parado"
        marca_tiempo = time.time()
        print(f"Cambiado a parado. Total: {total:.2f}€")  
    elif comando == "finalizar":
        tiempo_transcurrido = time.time() - marca_tiempo
        if estado == "parado":
            total += tiempo_transcurrido * TARIFA_PARADO
        else:
            total += tiempo_transcurrido * TARIFA_MOVIMIENTO
        print(f"Viaje finalizando. Total a pagar: {total:.2f}€")
        total = 0.0
        estado = "parado"
        marca_tiempo = None
    elif comando == "salir":
        break
    else:
        print("Comando no reconocido")        

