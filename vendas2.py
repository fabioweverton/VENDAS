# Gerador de Relatórios V2.0 

def ler_dados(nome_arquivo):
    """Lê os dados de vendas de um arquivo e retorna uma lista de valores.
    
    Ignora linhas que não podem ser convertidas para número.
    """
    lista_de_vendas = []
    
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                try:
                    valor = float(linha.strip())
                    lista_de_vendas.append(valor)
                except ValueError:
                    print(f"Aviso: Linha inválida encontrada e ignorada: '{linha.strip()}'")
        return lista_de_vendas
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None


def processar_dados(lista_de_vendas):
    """Calcula o total e a média de uma lista de valores de venda."""
    if not lista_de_vendas:
        return 0, 0
    
    total = sum(lista_de_vendas)
    media = total / len(lista_de_vendas)
    return total, media


def gerar_relatorio(total, media, itens_processados):
    """Exibe o relatório final com os totais calculados."""
    print("\n--- Relatório Final ---")
    print(f"Total de vendas: R${total:.2f}")
    print(f"Número de itens processados: {itens_processados}")
    print(f"Média de vendas por item: R${media:.2f}")


def main():
    """Função principal que orquestra a execução do programa."""
    nome_do_arquivo = "vendas.txt"
    lista_de_vendas = ler_dados(nome_do_arquivo)
    
    if lista_de_vendas:
        total, media = processar_dados(lista_de_vendas)
        gerar_relatorio(total, media, len(lista_de_vendas))


if __name__ == "__main__":
    main()