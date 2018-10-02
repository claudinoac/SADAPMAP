# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#      Classe Main (Principal)                                                                              #
#      Autor: Alisson Claudino (alisson.claudino@ufrgs.br) -> https://lief.if.ufrgs.br/~itsalissom          #
#      Licença: GNU GPLv2                                                                                   #
#      Propósito: Inicializar o programa                                                                    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sys
from MainWindow import Ui_MainWindow

if __name__ == '__main__':
    mainWindow = Ui_MainWindow()
    #engine=SystemEngine()
    sys.exit(mainWindow.app.exec_())
