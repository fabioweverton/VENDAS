# ===============================================
# Gerador Automático de Relatórios de Vendas
# ===============================================

nome_arquivo = "vendas.txt"

total_vendas = 0.0
contador_itens = 0

print("===========================================")
print("Iniciando a geração do relatório de vendas.")
print("===========================================")

try:
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            try:
                valor_venda = float(linha.strip())
                total_vendas = total_vendas + valor_venda
                contador_itens = contador_itens + 1
            except ValueError:
                print(f"Aviso: Linha inválida encontrada e ignorada: '{linha.strip()}'")

except FileNotFoundError:
    print(f"\nErro: O arquivo '{nome_arquivo}' não foi encontrado.")
    print("Certifique-se de que ele está na mesma pasta que o script.")
    exit()

if contador_itens > 0:
    media_vendas = total_vendas / contador_itens
    
    print("\n--- Relatório Final ---")
    print(f"Total de vendas: R${total_vendas:.2f}")
    print(f"Número de itens vendidos: {contador_itens}")
    print(f"Média de vendas por item: R${media_vendas:.2f}")
else:
    print("\nO arquivo foi encontrado, mas não contém dados de vendas válidos.")