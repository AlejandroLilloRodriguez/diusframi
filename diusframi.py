class Tarjeta:
    """
    Clase que maneja una variable interna con métodos para leer y escribir.
    """
    def __init__(self):
        self._saldo = 0.0 
        self.pin = 1234
         # Saldo inicial de la tarjeta

    def set_pin(self,pin):
        self.pin = pin
       
        
    
    def escribir(self, monto):
        """
        Método para añadir un monto al saldo.
        """
        self._saldo += monto
        print(f"Saldo actualizado: {self._saldo:.2f}")

    def cod_clave(self,monto):
        clave = monto*2
        return clave
    
    def identificar(self,pin):
        if pin == self.pin:
            return True
        else:
            return False
    
    def leer(self):
        """
        Método para leer el saldo actual de la tarjeta.
        """
        print(f"Saldo actual: {self._saldo:.2f}")
        return self._saldo


class Cajero:
    """
    Clase maestra que interactúa con la clase Tarjeta.
    """
    def __init__(self):
        self.tarjeta = Tarjeta()  # Instancia de la clase Tarjeta
    
    def ejecutar(self):
        """
        Método principal para interactuar con la clase Tarjeta.
        """

        while True:
            
            print("\n1. Depositar dinero")
            print("2. Consultar saldo")
            print("3. Cambiar pin")
            print("4. Salir")
            opcion = input("Elige una opción: ")
            
            if opcion == "1":
                try:
                    monto = float(input("Ingresa el monto a depositar: "))
                    clave = self.tarjeta.cod_clave(monto)
                    monto_cod = clave//2
                    if monto < 0 and monto_cod != monto:
                        print("El monto no puede ser negativo. O la clave no es correcta")
                    elif monto > 50:
                        print("\n Ingresa tu pin")
                        pin = int(input())
                        if self.tarjeta.pin == pin:
                            print("Operation exitosa")
                            self.tarjeta.escribir(monto)
                        else:
                            print("Pin incorrecto")
                            break
                    else:
                        self.tarjeta.escribir(monto)
                        
                except ValueError:
                    print("Por favor, ingresa un número válido.")
            elif opcion == "2":
                self.tarjeta.leer()
            elif opcion == "3":
                pin = int(input("Ingrese el pin actual: "))
                if self.tarjeta.identificar(pin):
                    pin = int(input("Ingrese el nuevo pin: "))
                    self.tarjeta.set_pin(pin)
                else:
                    print("Pin incorrecto")
                
            elif opcion == "4":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")


# Ejecución del programa
if __name__ == "__main__":
    cajero = Cajero()
    cajero.ejecutar()