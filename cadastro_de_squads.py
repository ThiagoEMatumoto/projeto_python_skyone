#######################################
# CRIANDO CLASSES
#######################################

class Pessoa:
    def __init__(self, nome, fone):
        self.nome = nome
        self.fone = fone

    def exibir(self):
        print(f'-> {self.nome} - {self.fone}')


class Squad:
    def __init__(self, nome, techlead=None, devs=None):
        self.nome = nome
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
        super().__init__( nome, fone, squad)
        self.cargo = cargo

    def exibir(self):
        super().exibir()
        print(f'    Cargo de {self.cargo} na squad {self.squad.nome}\n')


print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- Sky.One Solution -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Bem vindo ao sistema de cadastro de squads! \n')

#######################################
# LOOP DE CADASTRO
#######################################
squads = []

while True:
    #######################################
    # ADICIONANDO SQUAD
    #######################################

    nome_squad = input('\nNome do squad: ')
    nome_techlead = input('Nome do techlead da squad: ')
    fone_techlead = input('Telefone do techlead: ')

    squad = Squad(nome_squad)
    techlead = Colaborador(nome_techlead, fone_techlead)

    #######################################
    # ADICIONANDO TECHLEAD
    #######################################
    techlead = Colaborador(nome_techlead, fone_techlead)
    squad.incluir_techlead(techlead)
    techlead.incluir_squad(squad)

    squads.append(squad)

    #######################################
    # ADICIONANDO DESENVOLVEDOR
    #######################################
    while True:
        nome_dev = input('\nNome do desenvolvedor: ')
        fone_dev = input('Telefone do desenvolvedor: ')
        cargo_dev = input('Cargo do desenvolvedor: ')
        dev = Dev(nome_dev, fone_dev, cargo_dev)
        dev.incluir_squad(squad)
        squad.incluir_dev(dev)

        #######################################
        # OPÇÃO DE RETORNO
        #######################################
        option = input(r'Deseja adicionar mais um desenvolvedor [S\N]: ')
        if option in 'Nn':
            break

    option = input(r"Deseja adicionar mais um squad [S\N]: ")
    if option in 'Nn':
        break

#######################################
# SQUADS CRIADOS E FINALIZADOS
#######################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('\nSquads criados: ')
for squad in squads:
    print(f'\n-----------------------------{nome_squad}--------------------------------------')
    print(f'TechLead: {squad.techlead.nome}')
    print('------------Devs do Squad--------------')
    for dev in squad.devs:
        dev.exibir()
    print(f'-----------------------------{nome_squad}--------------------------------------')

print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- Sky.One Solution -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
