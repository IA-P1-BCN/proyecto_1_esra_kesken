import time
import json
import datetime

with open("config/tarifas.json") as f:
    tarifas = json.load(f)


TARIFA_MOVIMIENTO = tarifas["tarifa_movimiento"]
TARIFA_PARADO = tarifas["tarifa_parado"]

def calcular_importe(estado, tiempo_transcurrido):
    if estado == "parado":
        return tiempo_transcurrido * TARIFA_PARADO
    else:
        return tiempo_transcurrido * TARIFA_MOVIMIENTO


total = 0.0
estado = "parado"
marca_tiempo = None

if __name__ == "__main__":
    
    while True:
        comando = input("Comando: ")
        if comando == "iniciar":
            marca_tiempo = time.time()
            print("Viaje iniciando. Estado: parado")
        elif comando == "movimiento":
            if marca_tiempo is None:
                print("Error: primero debes iniciar un viaje con 'iniciar'.")
                continue
            tiempo_transcurrido = time.time() - marca_tiempo
            total += calcular_importe(estado, tiempo_transcurrido)
            estado = "movimiento"
            marca_tiempo = time.time()
            print(f"Cambiado a movimiento. Total: {total:.2f}€")  
        elif comando == "parado":
            if marca_tiempo is None:
                print("Error: primero debes iniciar un viaje con 'iniciar'.")
                continue
            tiempo_transcurrido = time.time() - marca_tiempo
            total += calcular_importe(estado, tiempo_transcurrido)
            estado = "parado"
            marca_tiempo = time.time()
            print(f"Cambiado a parado. Total: {total:.2f}€")  
        elif comando == "finalizar":
            if marca_tiempo is None:
                print("Error: primero debes iniciar un viaje con 'iniciar'.")
                continue
            tiempo_transcurrido = time.time() - marca_tiempo
            total += calcular_importe(estado, tiempo_transcurrido)
            print(f"Viaje finalizando. Total a pagar: {total:.2f}€")
            with open("logs/historial.txt", "a") as log:
                log.write(f"{datetime.datetime.now()} - Total: {total:.2f}€\n")
            total = 0.0
            estado = "parado"
            marca_tiempo = None
        elif comando == "salir":
            break
        else:
            print("Comando no reconocido")        

