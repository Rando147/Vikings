"""
Created on Thu Sep 8 9:54:45 2022

@author: boyro
"""
import os


class App:
    def __init__(self):
        self.__monitor_configuration = 1
        #self.__module = Lectura()
    
    def __menu(self):
        os.system('cls')
        print(" ==================================================== ")
        print(" [1] Collect Resources ")
        print(" [2] ")
        print(" [3] ")
        print(" [4] ")
        print(" [5] " )
        print(" [6] " )
        print(" [7] ")
        print(" [8] Salir")
        print(" ==================================================== ")
        return input("> ")
    

    
    def main(self):
        user_input = ""
        while user_input != "7":
            user_input = self.__menu()
            if user_input == "1":
                self.__lista.append(self.__lec.LeerDatosRepuesto())          
            '''elif user_input == "2":
                self.__lista.append(self.__lec.LeerDatosRepuestoNoOriginal())
            elif user_input == "3":
                self.__lista.append(self.__lec.LeerDatosRepuestoNuevo())
            elif user_input == "4":
                self.__lista.append(self.__lec.LeerDatosRepuestoUsado())
            elif user_input == "5":
                self.__lista.append(self.__lec.LeerDatosRepuestoNoNuevo())
            elif user_input == "6":
                self.__lista.append(self.__lec.LeerDatosRepuestoOriginal())
            elif user_input == "7":
                self.__mostrarLista()
                input("Press Any Key to continue")
            elif user_input == "8":
                self.__lista.clear()'''
            


run = App()
run.main()