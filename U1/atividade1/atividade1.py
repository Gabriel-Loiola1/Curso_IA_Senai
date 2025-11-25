# Aluno: João Gabriel Miranda Loiola Araújo

print('=================')
print('Iniciando Sistema')
print('=================')
print('\n')

# Definição de uma classe relacionada aos destinos
class Destino:
    def __init__(self, nome, clima, lugar, custo):
        self.nome = nome
        self.clima = clima
        self.lugar = lugar
        self.custo = custo
    
    # Método para comparação dos atributos fornecidos com os atributos dos destinos disponíveis
    def comparacao(self, clima, lugar, orcamento):
        return(self.clima == clima and self.lugar == lugar and self.custo <= orcamento)

# Listas com as opções de clima e tipos de lugares para fins de comporação
opcoes_clima = ['quente', 'frio']
opcoes_lugar = ['natureza', 'paisagens urbanas']

# Lista de destinos disponíveis
destinos = [
    Destino('Fortaleza', opcoes_clima[0], opcoes_lugar[1], 2000.00),
    Destino('Gramado', opcoes_clima[1], opcoes_lugar[1], 2000.00),
    Destino('Saara', opcoes_clima[0], opcoes_lugar[0], 5000.00),
    Destino('Alaska', opcoes_clima[1], opcoes_lugar[0], 5000.00)
]

# Variável para verificação da conclusão do questionário (e interrupção do laço while)
finalizado = False

# Laço while para o questionário
while finalizado == False:
    # Inicialização do questionário, caso condições não sejam atendidas, utiliza o método "continue"
    # para reiniciar o questionário (pula a interação do laço while e vai pra próxima)
    clima = input('\nVocê prefere clima quente ou frio?\n').strip().lower()
    if clima not in opcoes_clima:
        print('\nERRO: Você deve responder "quente" ou "frio"!')
        continue
    lugar = input('\nPrefere lugares com natureza ou paisagens urbanas?\n').strip().lower()
    if lugar not in opcoes_lugar:
        print('\nERRO: Você deve responder "natureza" ou "paisagens urbanas"!')
        continue
    # Bloco try para validação do input relacionado a variável de orçamento
    try:
        orcamento = float(input('\nQual é o seu orçamento disponível para a viagem? (Ex: 1500.50)\nR$'))
        if orcamento <= 0:
            print('\nERRO: O orçamento deve ser um valor positivo!')
            continue
    except ValueError:
        print('\nERRO: Você deve informar um valor numérico válido!')
        continue

    finalizado = True

# Variável para verificar se o destino foi encontrado
encontrado = False

# Laço de repetição for para busca de destino compatível
for destino in destinos:
    if destino.comparacao(clima, lugar, orcamento):
        print(f'\nO destino adequado para sua viagem é {destino.nome}!')
        print(f'O clima é {destino.clima}, o lugar possui {destino.lugar} e o custo (R${destino.custo:.2f}) cabe no orçamento (R${orcamento:.2f})!')
        encontrado = True
        break

# Caso "encontrado" permaneça falso, exibe a mensagem no console
if not encontrado:
    print('\nNão foram encontrados destinos compatíveis com as suas preferências.')