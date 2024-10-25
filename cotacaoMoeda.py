import http.client
import json

def verificarCotacaoEmReais():
    
    # Obtendo os valores

    precoDollar, precoEuro, precoBitCoin = buscarPrecoDasMoedas()

    # Apresentando os resultados
    print(f"Preço do Bitcoin: {formatar_valor(float(precoBitCoin))}")
    print(f"Preço do Dolar: {formatar_valor(float(precoDollar))}")
    print(f"Preço do Euro: {formatar_valor(float(precoEuro))}")
    return

# Funçao para formatar o valor
def formatar_valor(valor):
    return f"R$ {valor:,.2f}".replace(',','x').replace('.',',').replace('x','.')

# Função para obter as taxas de câmbio
def buscarPrecoDasMoedas():
    awesomeapi = http.client.HTTPSConnection("economia.awesomeapi.com.br")
    awesomeapi.request("GET", "/json/last/USD-BRL,EUR-BRL,BTC-BRL")
    response = awesomeapi.getresponse()
    data = response.read()
    cotacoes = json.loads(data)

    return cotacoes['USDBRL']['bid'], cotacoes ['EURBRL']['bid'], cotacoes ['BTCBRL']['bid']

verificarCotacaoEmReais()