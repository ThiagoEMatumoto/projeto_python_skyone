
#######################################
# CRIANDO CLASSES
#######################################

class Pessoa:
    def __init__(self, nome, fone):
        self.nome = nome
        self.fone = fone

class Squad:
    def __init__(self, nome, techlead = None, devs=None):
        self.nome =  nome
        self.devs = []
        self.techlead = techlead

    def incluir_techlead(self, techlead):
        self.techlead = techlead

    def incluir_dev(self, dev):
        self.devs.append(dev)

class Colaborador(Pessoa):
    def __init__(self, nome, fone, squad=None):
        super().__init__(nome, fone)
        self.squad = squad

    def incluir_squad(self, squad):
        self.squad = squad

class Dev(Colaborador):
    def __init__(self, nome, fone, cargo, squad=None):
        super().__init__(self, nome, fone, squad)
        self.cargo =  cargo


#######################################
# LOOP DE CADASTRO
#######################################
while True:
    #######################################
    # ADICIONANDO SQUAD
    #######################################
    squad = []

    nome_squad = input('\n Nome do squad: ')
    nome_techlead =  input('\n Nome do techlead da squad: ')
    fone_techlead = input('\n Telefone do techlead: ')

    squad = Squad(nome_squad)
    techlead = Colaborador(nome_techlead, fone_techlead)

    #######################################
    # ADICIONANDO TECHLEAD
    #######################################
    techlead = Colaborador(nome_techlead,fone_techlead)
    squad.incluir_techlead(techlead)
    techlead.incluir_squad(squad)

    squad.append(squad)

    #######################################
    # ADICIONANDO DESENVOLVEDOR
    #######################################
    while True:
        nome_dev = input('\n Nome do desenvolvedor: ')
        fone_dev = input('\n Telefone do desenvolvedor: ')
        cargo_dev = input('\n Cargo do desenvolvedor: ')
        dev = Dev(nome_dev, fone_dev, cargo_dev)
        dev.incluir_squad(squad)
        squad.incluir_dev(dev)
        option
        option = input('\n Deseja adicionar mais um desenvolvedor [S\N]: ')
        if option in 'Nn':
            break

    option = input("\n Deseja adicionar mais um squad [S\N]: ")
    if option in 'Nn':
        break










