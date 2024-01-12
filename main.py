class CalcularAih:
    """
    Calcula o Valor Inicial e Final da AIH para o Sistema MV SOUL.\n
    Params:
        -codigo_ibge_uf: int 
        -ano_referencia: int
        -quinto_digito: int
        -is_inicial: bool

    A numeração de AIH deve obedecer às seguintes regras:\n
    - Os dígitos 1 e 2 correspondem ao código do IBGE da UF ou 99, caso o tipo de AIH informado seja CNRAC;\n
    - Os dígitos 3 e 4 correspondem aos dois últimos algarismos do ano de referência. Ex: 24 para 2024;\n
    - O dígito 5 deverá obedecer a observação citada abaixo;\n
        "O quinto dígito [da numeração inicial da faixa de AIH] identifica:\n
        a) 1 (um) que a numeração é de [AIH] – uso geral;\n
        b) 3 (três) que a numeração é de AIH específica da CNRAC;\n
        c) 5 (cinco) que a numeração é de AIH específica para os procedimentos cirúrgicos eletivos de média complexidade e Campanhas;\n

    - Os dígitos 6, 7, 8, 9, 10, 11, e 12 obedecem a uma ordem crescente começando por 0000001;\n
    - O último dígito é o verificador, calculado da seguinte forma: deve-se recuperar o número
    da AIH informada (removendo o dígito) e dividi-lo por 11. O resto dessa divisão é o DV. Se
    o resto for igual a 10, o DV é 0.

    """

    def __init__(self, codigo_ibge_uf: int, ano_referencia: int, quinto_digito: int, is_inicial: bool) -> None:
        # Inicializa os atributos da classe
        self.__codigo_ibge_uf = str(codigo_ibge_uf).zfill(2)
        self.__ano_referencia = str(ano_referencia).zfill(2)
        self.__quinto_digito = quinto_digito
        self.__is_inicial = is_inicial
        self.__numero_aih = f"{self.__codigo_ibge_uf}{self.__ano_referencia}{self.__quinto_digito}"
        # Métodos necessários para realizar os cálculos
        self.__inicial_or_final()
        self.__calcula_digito_verificador()
        self.__adiciona_digito_verificador()

    def __inicial_or_final(self):
        """Determina se é uma AIH inicial ou final e ajusta o número AIH."""
        self.__numero_aih += "0000" if self.__is_inicial else "9999"

    def __calcula_digito_verificador(self):
        """Calcula o dígito verificador conforme a lógica definida.
        - Recuperar o número da self.__numero_aih(removendo o dígito) e dividi por 11. 
        - O resto dessa divisão é o DV. Se o resto for igual a 10, o DV é 0.
        """
        numero_sem_dv = int(self.__numero_aih[:-1])  # Remove o último dígito
        resto_divisao = numero_sem_dv % 11
        self.__dv = resto_divisao if resto_divisao < 10 else 0

    def __adiciona_digito_verificador(self):
        """Adiciona o dígito verificador ao número AIH."""
        self.__numero_aih += f"000{self.__dv}" if self.__is_inicial else f"999{self.__dv}"

    def get_numero_aih(self):
        """Retorna a representação formatada do número AIH calculado."""
        return print(f"Número de AIH Calculado: {self.__numero_aih}")


# Exemplos AIH Normal
aih_normal_inicial = CalcularAih(26, 24, 1, True).get_numero_aih()
aih_normal_final = CalcularAih(26, 24, 1, False).get_numero_aih()

# Exemplos AIH Eletiva
aih_eletiva_inicial = CalcularAih(26, 24, 5, True).get_numero_aih()
aih_eletiva_final = CalcularAih(26, 24, 5, False).get_numero_aih()