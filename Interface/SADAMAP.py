# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#      Classe Main (Principal)                                                                              #
#      Autor: Alisson Claudino (alisson.claudino@ufrgs.br) -> https://lief.if.ufrgs.br/~itsalissom          #
#      Licença: GNU GPLv2                                                                                   #
#      Propósito: Inicializar o programa                                                                    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sys
from SystemEngine import SystemEngine

if __name__ == '__main__':
    engine=SystemEngine()
    sys.exit(engine.app.exec_())
