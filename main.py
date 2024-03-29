#configuraciones
from colorama import init, Fore, Style
import time
import os
from tabulate import tabulate
#agregar
import Agregar.addActivos as addAc
import Agregar.addPersonal as addPer
import Agregar.addZonas as addZon
#buscar
import Buscar.getActivos as getAc
import Buscar.getPersonal as getPer
import Buscar.getZonas as getZon
#editar
import Editar.updateActivos as upAc
import Editar.updatePersonal as upPer
import Editar.updateZonas as upZon
#eliminar
import Eliminar.deleteActivos as delAc
import Eliminar.deletePersonal as delPer
import Eliminar.deleteZonas as delZon 
#reportes
import Reportes.getReportes as getRep
#movimiento de activos
import MenuMovimientoDeActivos.configMovActivos as MovAc

init(autoreset=True)

def clear_screen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

def animate_text(text):
    for char in text:
        print(Fore.WHITE + char, end="", flush=True)
        time.sleep(0.000001) 
    print(Style.RESET_ALL) 

def animateTextDeLosMenus(text):
    for char in text:
        print(Fore.BLUE + char, end="", flush=True)
        time.sleep(0.001) 
    print(Style.RESET_ALL) 


def menuZonas():
    while True:
        clear_screen()
        animateTextDeLosMenus('''

 
  __  __  ______  _   _  _    _         ______ ____   _   _             _____ 
 |  \/  ||  ____|| \ | || |  | |       |___  // __ \ | \ | |    /\     / ____|
 | \  / || |__   |  \| || |  | |          / /| |  | ||  \| |   /  \   | (___  
 | |\/| ||  __|  | . ` || |  | |         / / | |  | || . ` |  / /\ \   \___ \ 
 | |  | || |____ | |\  || |__| |        / /__| |__| || |\  | / ____ \  ____) |
 |_|  |_||______||_| \_| \____/        /_____|\____/ |_| \_|/_/    \_\|_____/ 
                                                                              
                                                                                                                                                      
              1. AGREGAR
              2. EDITAR
              3. ELIMINAR
              4. BUSCAR
              5. REGRESAR AL MENU PRINCIPAL
              ''')
        try:
            OPCIONES= int(input("Ingrese el número de la seleccion deceada: "))
            if OPCIONES == 1: 
                print(tabulate(addZon.AddZona(), headers="keys", tablefmt="double_outline"))
                input(f"""
                                         OPRIMA UNA TECLA PARA CONTINUAR... """)
               
                
            elif OPCIONES == 2:
                idZonas = input("Ingrese el id de la zona : ")
                print(tabulate(upZon.updateZonas(idZonas), headers="keys", tablefmt="rounded_grid"))
                input(f"""
                                         OPRIMA UNA TECLA PARA CONTINUAR... """)
            elif OPCIONES == 3:
                idZonas = input("Ingrese el id de la zona : ")
                print(tabulate(delZon.DeletePersonal(idZonas), headers="keys", tablefmt="rounded_grid"))
                input(f"""
                
                      ZONA ELIMINA
                                         OPRIMA UNA TECLA PARA CONTINUAR... """)

                
            elif OPCIONES == 4:
                idZonas = input("Ingrese el id de la zona : ")
                print(tabulate(getZon.BuscarZonas(idZonas), headers="keys", tablefmt="rounded_grid"))
                input(f"""
                                         OPRIMA UNA TECLA PARA CONTINUAR... """)
            elif OPCIONES == 5:
                break
        except ValueError as error:
            print(error)
            input("Oprima enter para volver a cargar el programa")
        except KeyboardInterrupt as error:
              print(error)
              input("Oprima alguna tecla para continuar con el programa")

def menuPersonal():
    while True:
        clear_screen()
        animateTextDeLosMenus('''

  __  __  ______  _   _  _    _         _____   ______  _____    _____   ____   _   _            _      
 |  \/  ||  ____|| \ | || |  | |       |  __ \ |  ____||  __ \  / ____| / __ \ | \ | |    /\    | |     
 | \  / || |__   |  \| || |  | |       | |__) || |__   | |__) || (___  | |  | ||  \| |   /  \   | |     
 | |\/| ||  __|  | . ` || |  | |       |  ___/ |  __|  |  _  /  \___ \ | |  | || . ` |  / /\ \  | |     
 | |  | || |____ | |\  || |__| |       | |     | |____ | | \ \  ____) || |__| || |\  | / ____ \ | |____ 
 |_|  |_||______||_| \_| \____/        |_|     |______||_|  \_\|_____/  \____/ |_| \_|/_/    \_\|______|
                                                                                                        
              1. AGREGAR
              2. EDITAR
              3. ELIMINAR
              4. BUSCAR
              5. REGRESAR AL MENU PRINCIPAL
              ''')
        try:
            OPCIONES= int(input("Ingrese el número de la seleccion deceada: "))
            if OPCIONES == 1:
                print()
            elif OPCIONES == 2:
                idPersonal = input("Ingrese el id de la persona a editar: ")
                print(tabulate( upPer.updatePersonal(idPersonal), headers="keys", tablefmt="rounded_grid"))
                input(f"""
                                         OPRIMA UNA TECLA PARA CONTINUAR... """)
                
            elif OPCIONES == 3:
                idPersonal = input("Ingrese el id del personal : ")
                print(tabulate(delPer.DeletePersonal(idPersonal), headers="keys", tablefmt="rounded_grid"))
                input(f"""
                      
                      PERSONAL ELIMINADO

                                         OPRIMA UNA TECLA PARA CONTINUAR... """)
                
            elif OPCIONES == 4:
                idPersonal = input("Ingrese el id del activo : ")
                print(tabulate( getPer.BuscarPersonal(idPersonal), headers="keys", tablefmt="rounded_grid"))
                input(f"""
                                         OPRIMA UNA TECLA PARA CONTINUAR... """)
                
            elif OPCIONES == 5:
                break
        except ValueError as error:
            print(error)
            input("Oprima enter para volver a cargar el programa")
        except KeyboardInterrupt as error:
              print(error)
              input("Oprima alguna tecla para continuar con el programa")

def menuActivos():
    while True:
        clear_screen()
        animateTextDeLosMenus('''


  __  __  ______  _   _  _    _                   _____  _______  _____ __      __ ____    _____ 
 |  \/  ||  ____|| \ | || |  | |           /\    / ____||__   __||_   _|\ \    / // __ \  / ____|
 | \  / || |__   |  \| || |  | |          /  \  | |        | |     | |   \ \  / /| |  | || (___  
 | |\/| ||  __|  | . ` || |  | |         / /\ \ | |        | |     | |    \ \/ / | |  | | \___ \ 
 | |  | || |____ | |\  || |__| |        / ____ \| |____    | |    _| |_    \  /  | |__| | ____) |
 |_|  |_||______||_| \_| \____/        /_/    \_\\_____|   |_|   |_____|    \/    \____/ |_____/ 
                                                                                                 
                                                                                                 
              1. AGREGAR
              2. EDITAR
              3. ELIMINAR
              4. BUSCAR
              5. REGRESAR AL MENU PRINCIPAL

''')
        try:
            OPCIONES= int(input("Ingrese el número de la seleccion deseada: "))
            if OPCIONES == 1:
                print()
            elif OPCIONES == 2:
                idActivo = input("Ingrese el id del activo : ")
                print(tabulate( upAc.updateActivos(idActivo), headers="keys", tablefmt="double_outline"))
                input(f"""
                      
                                         OPRIMA UNA TECLA PARA CONTINUAR... """)
               
            elif OPCIONES == 3:
                idActivo = input("Ingrese el id del activo : ")
                print(tabulate(delAc.deleteActivos(idActivo), headers="keys", tablefmt="double_outline"))
                input(f"""
                                         OPRIMA UNA TECLA PARA CONTINUAR... """)
               
            elif OPCIONES == 4:
                idActivo = input("Ingrese el id del activo : ")
                print(tabulate(getAc.BuscarActivos(idActivo), headers="keys", tablefmt="double_outline"))
                input(f"""
                                         OPRIMA UNA TECLA PARA CONTINUAR... """)
                
            elif OPCIONES == 5:
                break
            elif OPCIONES == 20051120:
                idActivo = input("Ingrese el id del activo : ")
                print(tabulate(delAc.DeletePersonal(idActivo), headers="keys", tablefmt="double_outline"))
                input(f"""
                                         OPRIMA UNA TECLA PARA CONTINUAR... """)
        except ValueError as error:
            print(error)
            input("Oprima enter para volver a cargar el programa")
        except KeyboardInterrupt as error:
              print(error)
              input("Oprima alguna tecla para continuar con el programa")


def menuAsignaciones():
    while True:
        clear_screen()
        animateTextDeLosMenus('''

  __  __  ______  _   _  _    _                    _____  _____  _____  _   _            _____  _____  ____   _   _  ______   _____  
 |  \/  ||  ____|| \ | || |  | |           /\     / ____||_   _|/ ____|| \ | |    /\    / ____||_   _|/ __ \ | \ | ||  ____| / ____| 
 | \  / || |__   |  \| || |  | |          /  \   | (___    | | | |  __ |  \| |   /  \  | |       | | | |  | ||  \| || |__   | (___   
 | |\/| ||  __|  | . ` || |  | |         / /\ \   \___ \   | | | | |_ || . ` |  / /\ \ | |       | | | |  | || . ` ||  __|   \___ \  
 | |  | || |____ | |\  || |__| |        / ____ \  ____) | _| |_| |__| || |\  | / ____ \| |____  _| |_| |__| || |\  || |____  ____) | 
 |_|  |_||______||_| \_| \____/        /_/    \_\|_____/ |_____|\_____||_| \_|/_/    \_\\_____||_____|\____/ |_| \_||______||_____/  
                       _____   ______                        _____  _______  _____ __      __ ____    _____                       
                      |  __ \ |  ____|                /\    / ____||__   __||_   _|\ \    / // __ \  / ____|                      
                      | |  | || |__                  /  \  | |        | |     | |   \ \  / /| |  | || (___                        
                      | |  | ||  __|                / /\ \ | |        | |     | |    \ \/ / | |  | | \___ \                       
                      | |__| || |____              / ____ \| |____    | |    _| |_    \  /  | |__| | ____) |                      
                      |_____/ |______|            /_/    \_\\_____|   |_|   |_____|    \/    \____/ |_____/                       
                                                                                                                                     
                                                                                                                                     
  
                                                                                                 
              1. CREAR ASIGNACION
              2. BUSCAR ASIGNACION
              3. REGRESAR AL MENU PRINCIPAL
''')
        try:
            OPCIONES= int(input("Ingrese el número de la seleccion deceada: "))
            if OPCIONES == 1:
                print()
            elif OPCIONES == 2:
                print()
            elif OPCIONES == 3:
                break
        except ValueError as error:
            print(error)
            input("Oprima enter para volver a cargar el programa")
        except KeyboardInterrupt as error:
              print(error)
              input("Oprima alguna tecla para continuar con el programa")
def menuReportes():
    while True:
        clear_screen()
        animateTextDeLosMenus('''


  __  __  ______  _   _  _    _         _____   ______  _____    ____   _____  _______  ______   _____ 
 |  \/  ||  ____|| \ | || |  | |       |  __ \ |  ____||  __ \  / __ \ |  __ \|__   __||  ____| / ____|
 | \  / || |__   |  \| || |  | |       | |__) || |__   | |__) || |  | || |__) |  | |   | |__   | (___  
 | |\/| ||  __|  | . ` || |  | |       |  _  / |  __|  |  ___/ | |  | ||  _  /   | |   |  __|   \___ \ 
 | |  | || |____ | |\  || |__| |       | | \ \ | |____ | |     | |__| || | \ \   | |   | |____  ____) |
 |_|  |_||______||_| \_| \____/        |_|  \_\|______||_|      \____/ |_|  \_\  |_|   |______||_____/ 
                                                                                                       
                                                                                                                                                     
                                                                                                 
              1. LISTAR TODOS LOS ACTIVOS
              2. LISTAR ACTIVOS POR CATEGORIA
              3. LISTAR ACTIVOS DADOS DE BAJA POR DAÑO
              4. LISTAR ACTIVOS Y ASIGNACION
              5. LISTAR HISTORIAL DE MOV. DE ACTIVO
              6. REGRESAR AL MENU PRINCIPAL

''')
        try:
            OPCIONES= int(input("Ingrese el número de la seleccion deceada: "))
            if OPCIONES == 1:
                print(tabulate(getRep.getAllActivos(), headers="keys", tablefmt="rounded_grid"))
                print(tabulate(getRep.getAllMarcas(), headers="keys", tablefmt="rounded_grid"))
                input('''
                                       OPRIMA ALGUNA TECLA PARA CONTINUAR...        ''')
            elif OPCIONES == 2:
                categoria = input("Ingrese el ID de la categoria que decea ver: ")
                print(tabulate(getRep.getAllCategoria(categoria),headers="keys", tablefmt="rounded_grid"))
                print(tabulate(getRep.getAllMarcas(), headers="keys", tablefmt="rounded_grid"))
                input(f"""
                                         OPRIMA UNA TECLA PARA CONTINUAR... """)
            elif OPCIONES == 3:
                print(tabulate(getRep.getAllDadosDeBajaPorDaño(),headers="keys", tablefmt="rounded_grid"))
                print(tabulate(getRep.getAllMarcas(), headers="keys", tablefmt="rounded_grid"))
                input(f"""
                                         OPRIMA UNA TECLA PARA CONTINUAR... """)
            elif OPCIONES == 4:
                asignaciones = input("Ingrese el ID del activo al que decea ver su asignación: ")
                print(tabulate(getRep.getAllActivosAsignaciones(asignaciones),headers="keys", tablefmt="rounded_grid"))
                input(f"""
                                         OPRIMA UNA TECLA PARA CONTINUAR... """)
                
            elif OPCIONES == 5:
                Historial = input("Igrese el ID del activo al que quiere visualizar su historial: ")
                print(tabulate(getRep.getAllHistorialDeMovDeActivo(Historial),headers="keys", tablefmt="rounded_grid"))
                input(f"""
                                         OPRIMA UNA TECLA PARA CONTINUAR... """)
            elif OPCIONES == 6:
                break
        except ValueError as error:
            print(error)
            input("Oprima enter para volver a cargar el programa")
        except KeyboardInterrupt as error:
              print(error)
              input("Oprima alguna tecla para continuar con el programa")

def menuMovimientoDeActivos():
    while True:
        clear_screen()
        animateTextDeLosMenus('''


  __  __  ______  _   _  _    _         __  __   ____ __      __ _____  __  __  _____  ______  _   _  _______  ____  
 |  \/  ||  ____|| \ | || |  | |       |  \/  | / __ \\ \    / /|_   _||  \/  ||_   _||  ____|| \ | ||__   __|/ __ \ 
 | \  / || |__   |  \| || |  | |       | \  / || |  | |\ \  / /   | |  | \  / |  | |  | |__   |  \| |   | |  | |  | |
 | |\/| ||  __|  | . ` || |  | |       | |\/| || |  | | \ \/ /    | |  | |\/| |  | |  |  __|  | . ` |   | |  | |  | |
 | |  | || |____ | |\  || |__| |       | |  | || |__| |  \  /    _| |_ | |  | | _| |_ | |____ | |\  |   | |  | |__| |
 |_|  |_||______||_| \_| \____/        |_|  |_| \____/    \/    |_____||_|  |_||_____||______||_| \_|   |_|   \____/ 
                _____   ______                   _____  _______  _____ __      __ ____    _____                      
               |  __ \ |  ____|           /\    / ____||__   __||_   _|\ \    / // __ \  / ____|                     
               | |  | || |__             /  \  | |        | |     | |   \ \  / /| |  | || (___                       
               | |  | ||  __|           / /\ \ | |        | |     | |    \ \/ / | |  | | \___ \                      
               | |__| || |____         / ____ \| |____    | |    _| |_    \  /  | |__| | ____) |                     
               |_____/ |______|       /_/    \_\\_____|   |_|   |_____|    \/    \____/ |_____/                      
                                                                                                                     
                                                                                                                     
                                                                
  
                                                                                                 
              1. RETORNO DE ACTIVO
              2. DAR DE BAJA ACTIVO
              3. CAMBIAR ASIGNACION DE ACTIVO
              4. ENVIAR A GARANTIA ACTIVO
              5. REGRESAR AL MENU PRINCIPAL

''')
        try:
            OPCIONES= int(input("Ingrese el número de la seleccion deceada: "))
            if OPCIONES == 1:
                Historial = input("Igrese el ID del activo al que dar como estado no asignado: ")
                print(tabulate(MovAc.deleteActivos(Historial),headers="keys", tablefmt="double_outline"))
                input(f"""
                      
                                         OPRIMA UNA TECLA PARA CONTINUAR... """)
            elif OPCIONES == 2:
                DadoDeBaja = input("Igrese el ID del activo al que dar como estado de dado de baja: ")
                print(tabulate(MovAc.darActivoPorDeBaja(DadoDeBaja),headers="keys", tablefmt="double_outline"))
                input(f"""
                      
                                         OPRIMA UNA TECLA PARA CONTINUAR... """)

                
            elif OPCIONES == 3:
                print()
            elif OPCIONES == 4:
                DadoDeBaja = input("Igrese el ID del activo para dar el estado en garantia: ")
                print(tabulate(MovAc.darActivoPorGarantia(DadoDeBaja),headers="keys", tablefmt="double_outline"))
                input(f"""
                      
                                         OPRIMA UNA TECLA PARA CONTINUAR... """)
            elif OPCIONES == 5:
                
                break
        except ValueError as error:
            print(error)
            input("Oprima enter para volver a cargar el programa")
        except KeyboardInterrupt as error:
              print(error)
              input("Oprima alguna tecla para continuar con el programa")
        
if (__name__ == "__main__"):
    while True:
        clear_screen()
        animate_text('''
              

                                                                                                                
                                                                                                                                                                                            
                                              @@@@@@@@@@@@@@@@@@@@@@@
                                            @@@@@/,,,,,,,,,,,,,,,@@@@@
                                        @@@@@,,,,,,,,,,,,,,*******//////((@@@@@
                                   @@@@@,,,,,,,,,,,*********/////(((((######%@@@@
                               @@@@@,,,,,,,&@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%&&&&@@@@@
                            @@@@@,,,,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%&@@@@@
                           @@@@@***@@@@@@@@@@@@@@@@ ,,,,,,,,*****/#@@@@@@@@@@@@@@@%%%@@@@@
                         @@@@@**@@@@@@@@@@@@&,,,,,/@@@@@@@@@@@@@@@@###%%&@@@@@@@@@@@@%@@@@@
                        @@@@@/@@@@@@@@@@@,.,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@@@@@@@@@@&%@@@@@
                       @@@@@(@@@@@@@@@,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@#@@@@@
                      @@@@@#@@@@@@@@**@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@#@@@@@
                 @@@@@##@@%@@@@@@@@//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@@@@@@@@#@@##@@@@@
                @@@@@%%@@&&@@@@@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@@@@@@@##@@##@@@@@
               @@@@@&&@@@%@@@@@@@%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%@@@@@@@#@@@#@@@@@
                @@@@@%@@@%@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@@@@@@@#@@@#@@@@@
                 @@@@@%@&%@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@@@@@@@#@@#@@@@@
                    @@@@@%@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#(@@@@@@@#@@@@@
                    @@@@@%&@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(&@@@@@@(#@@@@@
                    @@@@@%%@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(@@@@@@@#(@@@@@
                     @@@@@##@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@((@@@@@
                      @@@@@#%@@@@@@@@@@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#@@@@@@@@@@((@@@@@
                      @@@@@&##@@@@@@@@@@@@@@@&%%%%%###%%&&%%%#(###(((((#@@@@@@@@@@@@@@@((@@@@@
                        @@@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@((@@@@@
                         @@@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#((@@@@@
                           @@@@@#############(#@@@@@@@@@@@@@@@@@@@@@@@@@%(((((((((((((@@@@@
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                      
   _____  _____   _____  _______  ______  __  __                   _____           _____       _____   ______  
  / ____||_   _| / ____||__   __||  ____||  \/  |    /\           / ____|  ___    / ____|     |  __ \ |  ____| 
 | (___    | |  | (___     | |   | |__   | \  / |   /  \         | |  __  ( _ )  | |          | |  | || |__    
  \___ \   | |   \___ \    | |   |  __|  | |\/| |  / /\ \        | | |_ | / _ \/\| |          | |  | ||  __|   
  ____) | _| |_  ____) |   | |   | |____ | |  | | / ____ \       | |__| || (_>  <| |____      | |__| || |____  
 |_____/ |_____||_____/    |_|   |______||_|  |_|/_/    \_\       \_____| \___/\/ \_____|     |_____/ |______| 
            _____  _   _ __      __ ______  _   _  _______         _____   _____  ____                         
           |_   _|| \ | |\ \    / /|  ____|| \ | ||__   __| /\    |  __ \ |_   _|/ __ \                        
             | |  |  \| | \ \  / / | |__   |  \| |   | |   /  \   | |__) |  | | | |  | |                       
             | |  | . ` |  \ \/ /  |  __|  | . ` |   | |  / /\ \  |  _  /   | | | |  | |                       
            _| |_ | |\  |   \  /   | |____ | |\  |   | | / ____ \ | | \ \  _| |_| |__| |                       
           |_____||_| \_|    \/    |______||_| \_|   |_|/_/    \_\|_|  \_\|_____|\____/                        
                 _____            __  __  _____   _    _   _____  _                 _   _  _____    _____                
                / ____|    /\    |  \/  ||  __ \ | |  | | / ____|| |         /\    | \ | ||  __ \  / ____|               
               | |        /  \   | \  / || |__) || |  | || (___  | |        /  \   |  \| || |  | || (___                 
               | |       / /\ \  | |\/| ||  ___/ | |  | | \___ \ | |       / /\ \  | . ` || |  | | \___ \                
               | |____  / ____ \ | |  | || |     | |__| | ____) || |____  / ____ \ | |\  || |__| | ____) |               
                \_____|/_/    \_\|_|  |_||_|      \____/ |_____/ |______|/_/    \_\|_| \_||_____/ |_____/                
                                                                                                               
                                                                                                    
                                        
               MENU PRINCIPAL
                                                                                                                 
    OPCIONES
                                                                                                                    
        1. ACTIVOS
        2. PERSONAL 
        3. ZONAS
        4. ASIGNACION DE ACTIVOS
        5. REPOTES 
        6. MOVIMIENTO DE ACTIVOS
        7. SALIR  
    ''')
        try:
            OPCIONES= int(input("Ingrese el número de la seleccion deceada: "))
            if OPCIONES == 1:
                menuActivos()
                
            elif OPCIONES == 2:
                menuPersonal()

            elif OPCIONES == 3:
                menuZonas()

            elif OPCIONES == 4:
                menuAsignaciones()
                
            elif OPCIONES == 5:
                menuReportes()

            elif OPCIONES == 6:
                menuMovimientoDeActivos()

                
            elif OPCIONES == 7:
                break
        except ValueError as error:
            print(error)
            input("Oprima enter para volver a cargar el programa")
        except KeyboardInterrupt as error:
              print(error)
              input("Oprima alguna tecla para continuar con el programa")

    