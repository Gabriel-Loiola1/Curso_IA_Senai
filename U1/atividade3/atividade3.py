# Aluno: João Gabriel Miranda Loiola Araújo

# Importação do numpy
import numpy as np

# Declaração da classe dos sensores
class Sensor:
    # Método para inicialização dos atributos
    def __init__(self, nome):
        self.nome = nome
        self.temperatura = None
        self.dados = []

    # Método para leitura dos dados
    def leitura(self, temperatura):
        self.temperatura = temperatura
        # Caso a temperatura esteja dentro dos limites, apenas a adiciona na lista de dados
        # Caso contrário, exibe um alerta antes de adicionar
        if temperatura >= 20 and temperatura <= 80:
            self.dados.append(temperatura)
        else:
            print(f'\nALERTA: Temperatura medida no sensor {self.nome} está fora do intervalo seguro.')
            print(f'Temperatura Medida: {temperatura}°C')
            self.dados.append(temperatura)

    # Método para análise dos dados
    def analise(self):
        # Verifica se a lista de dados está vazia
        if not self.dados:
            print(f'\nNenhum dado foi coletado pelo sensor {self.nome} para análise')
            return

        # Conversão da lista de dados para um array numpy
        arr_dados = np.array(self.dados)

        # Operações de análise no array de dados
        max_temp = np.max(arr_dados)
        min_temp = np.min(arr_dados)
        media_temp = np.mean(arr_dados)

        # Exibição das informações obtidas pós-análise
        print(f'\nTemperaturas medidas em °C: {arr_dados}')
        print(f'\nTemperatura máxima medida: {max_temp:.1f}°C')
        print(f'\nTemperatura mínima medida: {min_temp:.1f}°C')
        print(f'\nTemperatura média: {media_temp:.1f}°C')

# Declaração de uma variável de teste para simulação
sensor_teste = Sensor('SensorTemp')

# Função para inicializar a simulação das medições
def inicializar_medicoes(sensor):
    print('\n=================================')
    print('Inicializando ciclo de 5 medições')
    print('=================================')

    # Variável para simular a temperatura
    temperatura = 100

    # Laço for para simular 5 leituras de dados do sensor
    for i in range(5):
        sensor.leitura(temperatura)
        temperatura -= 15

    # Análise dos dados simulados
    print('\n\nMedições finalizadas...')
    print('Inicializando análise dos dados...')
    sensor.analise()

# Input para iniciar o sistema
iniciar = input('Pressione 1 para inicializar as medições do sensor.\n')
if iniciar == '1':
    inicializar_medicoes(sensor_teste)
else:
    print('Inicialização cancelada.')