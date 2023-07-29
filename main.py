# Dados para popular o bd
estados = {
    1: {"Nome_Estado": "Bahia", "Sigla": "BA"},
    2: {"Nome_Estado": "Rio de Janeiro", "Sigla": "RJ"}
}

cidades = {
    1: {"Nome_Cidade": "Jequié", "Codigo_Municipio": 123, "ID_Estado": 1},
    2: {"Nome_Cidade": "Rio de Janeiro", "CodigoMunicipio": 456, "ID_Estado": 2}
}

bairros = {
    1: {"Nome_Bairro": "Jequiezinho", "Regiao": "Zona Oeste", "CEP": "45208-010", "ID_Cidade": 1},
    2: {"Nome_Bairro": "Copacabana", "Regiao": "Zona Sul", "CEP": "22000-000", "ID_Cidade": 2}
}

logradouros = []

# Funcao que gera CEP automaticamente para um novo logradouro
def gerar_cep_logradouro(nome_rua, numero, complemento, nome_bairro, nome_cidade, nome_estado):
    # Captacao dos IDs das entidades do bd
    id_estado = None
    for key, estado in estados.items():
        if estado["Nome_Estado"] == nome_estado:
            id_estado = key
            break

    id_cidade = None
    for key, cidade in cidades.items():
        if cidade["Nome_Cidade"] == nome_cidade and cidade["ID_Estado"] == id_estado:
            id_cidade = key
            break

    id_bairro = None
    for key, bairro in bairros.items():
        if bairro["Nome_Bairro"] == nome_bairro and bairro["ID_Cidade"] == id_cidade:
            id_bairro = key
            break

    if id_estado is None or id_cidade is None or id_bairro is None:
        print("Dados inválidos!!! Verifique se o estado, cidade e bairro existem.")
        return None

    # Gera o CEP com base nas informacoes das entidades
    cep = f"{cidades[id_cidade]['Codigo_Municipio']:03}{id_bairro:04}{len(logradouros)+1:04}"

    # Novo logradouro eh lista de logradouros
    logradouros.append({
        "Nome_Rua": nome_rua,
        "Numero": numero,
        "Complemento": complemento,
        "ID_Bairro": id_bairro,
        "ID_Cidade": id_cidade,
        "ID_Estado": id_estado,
        "CEP": cep
    })

    return cep

# Chamada da funcao
novo_cep = gerar_cep_logradouro("Rua Germana", 123, "Casa", "Cidade Nova", "Jequié", "Bahia")
print("CEP gerado:", novo_cep)
