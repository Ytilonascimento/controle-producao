import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Função para entrada de dados
def entrada_dados():
    operador = input('Digite o nome do operador: ')
    try:
        total_produzido = int(input('Digite a quantidade de peças produzidas: '))
        defeituosas = int(input('Digite a quantidade de peças com defeito: '))
        return operador, total_produzido, defeituosas
    except ValueError:
        print('Erro: por favor, digite apenas números válidos.')
        return None, None, None

# Função de validação
def validar_dados(total_produzido, defeituosas):
    if total_produzido is None or defeituosas is None:
        return False
    if total_produzido <= 0:
        print('Erro: a quantidade produzida deve ser maior que zero.')
        return False
    if defeituosas < 0 or defeituosas > total_produzido:
        print('Erro: quantidade de defeitos inválida.')
        return False
    return True

# Função de cálculo
def calcular_relatorio(total_produzido, defeituosas):
    pecas_boas = total_produzido - defeituosas
    taxa_defeito = (defeituosas / total_produzido) * 100

    if taxa_defeito < 2:
        desempenho = 'Excelente'
    elif taxa_defeito <= 5:
        desempenho = 'Bom'
    else:
        desempenho = 'Crítico'

    return pecas_boas, taxa_defeito, desempenho

# Função para exibir relatório
def exibir_relatorio(operador, total_produzido, pecas_boas, defeituosas, taxa_defeito, desempenho):
    print('\n--- RELATÓRIO DE PRODUÇÃO ---')
    print(f'Operador: {operador}')
    print(f'Total produzido: {total_produzido} peças')
    print(f'Peças boas: {pecas_boas} peças')
    print(f'Peças defeituosas: {defeituosas} peças')
    print(f'Taxa de defeito: {taxa_defeito:.2f}%')
    print(f'Desempenho: {desempenho}')

# Função para salvar CSV
def salvar_csv(operador, total_produzido, pecas_boas, defeituosas, taxa_defeito, desempenho):
    arquivo = 'relatorio_producao.csv'
    with open(arquivo, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(['Data', 'Operador', 'Total Produzido', 'Peças Boas', 'Peças Defeituosas', 'Taxa de Defeito (%)', 'Desempenho'])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), operador, total_produzido, pecas_boas, defeituosas, f"{taxa_defeito:.2f}", desempenho])

# Função para gerar gráfico de desempenho
def gerar_grafico():
    datas, taxas = [], []
    with open('relatorio_producao.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for linha in reader:
            datas.append(linha['Data'])
            taxas.append(float(linha['Taxa de Defeito (%)']))

    plt.figure(figsize=(10,6))
    plt.plot(datas, taxas, marker='o', linestyle='-', color='blue', linewidth=2, markersize=8)
    plt.title('📊 Taxa de Defeito ao longo do tempo', fontsize=16, fontweight='bold')
    plt.xlabel('Data', fontsize=12)
    plt.ylabel('Taxa de Defeito (%)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('grafico_producao.png')
    plt.show()

# Função principal
def main():
    operador, total_produzido, defeituosas = entrada_dados()

    if validar_dados(total_produzido, defeituosas):
        pecas_boas, taxa_defeito, desempenho = calcular_relatorio(total_produzido, defeituosas)
        exibir_relatorio(operador, total_produzido, pecas_boas, defeituosas, taxa_defeito, desempenho)
        salvar_csv(operador, total_produzido, pecas_boas, defeituosas, taxa_defeito, desempenho)
        gerar_grafico()  # gera gráfico após salvar CSV

if __name__ == "__main__":
    main()
