#Obter a instalação do Pretty Table com o pip
from prettytable import PrettyTable

class AUVs:

    def __init__ (self, nome, thursters, sensores, ano, hidrofones):
    
        self.nome = nome
        self.thursters = thursters
        self.sensores = sensores
        self.ano = ano
        self.hidrofones = hidrofones


    def apresenta (self):

        lista_sensores = ''
        for key in self.sensores:
            lista_sensores += key + ' ' + str(self.sensores[key]) + '\n'
        lista_sensores = lista_sensores.replace('\'','')

        print ('Nome -> ' + self.nome + '\nnumero de Thursters -> ' + str(self.thursters) + 
                '\nlista de sensores: \n' + lista_sensores + '\nAno de Fabricacao -> ' + str(self.ano) + 
                '\nnumero de hidrofones -> ' + str(self.hidrofones) + '\n')

def compara_sensores(drone1, drone2):
    for key in drone1.sensores:
        for i in range(len(drone1.sensores[key])):
            for j in range(len(drone2.sensores[key])):
                if i == j:
                    return True
    return False
    

def tabela(drone1, drone2):
    
    tabela = PrettyTable()

    sensores1 = 0
    sensores2 = 0

    for key in drone1.sensores:
        sensores1 += len(drone1.sensores[key])
        sensores2 += len(drone2.sensores[key])

    tabela.field_names = ['AUV', 'Thursters', 'Sensores', 'ano', 'Hidrofones']
    tabela.add_row([drone1.nome, drone1.thursters, sensores1, drone1.ano, drone1.hidrofones])
    tabela.add_row([drone2.nome, drone2.thursters, sensores2, drone2.ano, drone2.hidrofones])
    
    print(tabela,'\n')

def ranking(drone1, drone2):
    
    ranking = PrettyTable()
    
    print('Ranking em ordem crescente de construção dos AUVs:')
    
    ranking.field_names = ['AUV', 'Ano']
    ranking.add_row([drone1.nome, drone1.ano])
    ranking.add_row([drone2.nome, drone2.ano])
    print(ranking.get_string(sortby="Ano"), '\n')


brhue = AUVs(('BrHue'), 6, 
             {'Sensor de Pressão': ['Kalman Filter'], 
              'Sensor de Localização': ['SLAM', 'UFK', 'EKF'], 
              'Sensor de Profundidade': ['Beamforming algorithm']}
             , 2020, 4)
lua = AUVs('Lua', 8, 
           {'Sensor de Pressão': ['BMP180', 'BAR30'], 
            'Sensor de Profundidade': ['beamforming algorithm w/ Kalman Filter'], 
            'Sensor de Localização': ['SLAM']}, 
           2016, 4)
tabela(brhue, lua)
brhue.apresenta()
lua.apresenta()
ranking(brhue, lua)
if compara_sensores(brhue,lua):
    print('\nHá sensores iguais')
else:
    print('\nNão há sensores iguais')
