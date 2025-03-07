'''
1) ingresar el saldo disponible 
2) lo quiero en soles no en dolares 
3) no pued retirar saldos mayores a 8000 ni menores a 50
4) opcion para aumentar el saldo

'''
def saludar():
     print("hola como estas")
     
saludar()


def simularCajeroAutomatico():
    saldo = float(input("Ingrese saldo disponible: S/."))
    while True:
        print("\n🏦 Cajero Automático")
        print(f"Saldo disponible: S/.{saldo}")
        print("1. Retirar dinero")
        print("2. deposito de dinero")
        print("3. Salir")
            
        opcion = input("Seleccione una opción: ")
        #monto = input(float("INGRESAR SALDO:"))
            
        if opcion == "1":
            monto = float(input("Ingrese el monto a retirar: S/."))
            '''
            if monto <= 0:
                print("⛔ Monto inválido. Debe ser mayor que 0.")
            
            '''  
            if monto > saldo:
                print("❌ Saldo insuficiente. Intente un monto menor.")
    
            elif monto < 50 or monto > 8000 : 
                 print("⛔ Monto inválido. Intente un monto entre S/.50 y S/.8000")
            
            else:
                saldo -= monto # saldo = saldo - monto 
                print(f"✅ Retiro exitoso. Nuevo saldo: S/.{saldo}")
                    
            if saldo == 0:
                print("⚠️ Saldo agotado. Operaciones finalizadas.")
                break  # Termina el bucle si no hay saldo
    
        elif opcion == "2":
                monto = 0
                while monto <= 0:
                    monto = float(input("Ingrese el monto a depositar: S/."))
                saldo += monto
                print(f"✅ Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
             
                    
        elif opcion == "3":
                print("👋 Gracias por usar el cajero. ¡Hasta pronto!")
                break  # Sale del bucle y termina el programa
            
        else:
            print("❌ Opción inválida. Intente nuevamente.")



def sumardosnumeros(numero1,numero2):
    resultado = numero1 + numero2
    print("el resultado es",resultado) 
    return resultado




def pagar_deuda(deuda, pago_mensual, interes_anual):
    meses = 0
    while deuda > 0:
        intereses = deuda * (interes_anual / 12 / 100)
        deuda += intereses - pago_mensual
        meses += 1

        if deuda < 0:
            deuda = 0

        print(f"Mes {meses}: Deuda restante: ${deuda:.2f}")
    
    print(f"\nDeuda pagada en {meses} meses.")            


sumardosnumeros(5,6)


def sumartresnumeros(numero1,numero2,numero3):
    resultadodelasumadedos = sumardosnumeros(numero1,numero2)
    resultado = resultadodelasumadedos + numero3
    print("el resultado total es",resultado) 


sumartresnumeros(5,6,9)    