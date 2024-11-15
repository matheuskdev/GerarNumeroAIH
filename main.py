class AihBase:
    """
    Classe base para a geração e cálculo do número AIH (Autorização de Internação Hospitalar) com dígito verificador.

    Args:
        codigo_ibge_uf (int): Código IBGE que identifica o estado da Unidade Federativa (UF) onde a AIH é emitida.
            Deve ser fornecido como um número inteiro, mas será convertido para um formato de dois dígitos com zero à esquerda.
        ano_referencia (int): Ano de referência da AIH.
            Este valor também será formatado para dois dígitos (por exemplo, 2024 será '24').
        quinto_digito (int): O quinto dígito que identifica o tipo de AIH. Os valores típicos são:
            - 1: AIH de uso geral.
            - 3: AIH para uso específico em casos de CNRAC.
            - 5: AIH para procedimentos cirúrgicos eletivos.
    """  # noqa: E501

    def __init__(
        self, codigo_ibge_uf: int, ano_referencia: int, quinto_digito: int
    ) -> None:
        self._codigo_ibge_uf: str = str(codigo_ibge_uf).zfill(2)
        self._ano_referencia: str = str(ano_referencia).zfill(2)
        self._quinto_digito: int = quinto_digito
        self._numero_aih_base: str = (
            f"{self._codigo_ibge_uf}{self._ano_referencia}{self._quinto_digito}"  # noqa: E501
        )

    def _calcular_digito_verificador(self, numero_aih: str) -> int:
        """
        Método público para calcular o dígito verificador baseado na regra do módulo 11.
        Remove o último dígito e aplica o cálculo do dígito verificador.

        Args:
            numero_aih (str): Número da AIH sem o dígito verificador.

        Returns:
            int: O dígito verificador calculado.
        """  # noqa: E501
        numero_sem_digito_verificador = int(numero_aih[:-1])
        resto_divisao: int = int(numero_sem_digito_verificador) % 11
        return resto_divisao if resto_divisao < 10 else 0

    def get_numero_aih_completo(self) -> str:
        """
        Método público abstrato que retorna o número AIH completo (a ser implementado pelas subclasses).

        Raises:
            NotImplementedError: Se não for implementado pelas subclasses.
        """  # noqa: E501
        raise NotImplementedError(
            "Este método deve ser implementado pelas subclasses."
        )


class AihInicial(AihBase):
    """
    Classe derivada para gerar o número AIH inicial.
    """

    def get_numero_aih_completo(self) -> str:
        """
        Retorna o número AIH completo para a AIH inicial, incluindo o sufixo '0000'
        e o dígito verificador calculado.

        Returns:
            str: O número AIH completo com dígito verificador.
        """  # noqa: E501
        numero_aih: str = f"{self._numero_aih_base}0000"
        digito_verificador: int = self._calcular_digito_verificador(numero_aih)
        return f"{numero_aih}000{digito_verificador}"


class AihFinal(AihBase):
    """
    Classe derivada para gerar o número AIH final.
    """

    def get_numero_aih_completo(self) -> str:
        """
        Retorna o número AIH completo para a AIH final, incluindo o sufixo '9999'
        e o dígito verificador calculado.

        Returns:
            str: O número AIH completo com dígito verificador.
        """  # noqa: E501
        numero_aih: str = f"{self._numero_aih_base}9999"
        digito_verificador: int = self._calcular_digito_verificador(numero_aih)
        return f"{numero_aih}999{digito_verificador}"


class AihFactory:
    """
    Fábrica para criar instâncias de AIH (inicial ou final) de acordo com o parâmetro fornecido.
    """  # noqa: E501

    @staticmethod
    def criar_aih(
        codigo_ibge_uf: int,
        ano_referencia: int,
        quinto_digito: int,
        is_inicial: bool
    ) -> AihBase:
        """
        Método estático que cria uma instância de AihInicial ou AihFinal, dependendo do valor de `is_inicial`.

        Args:
            codigo_ibge_uf (int): Código IBGE da UF.
            ano_referencia (int): Ano de referência (2 dígitos).
            quinto_digito (int): Quinto dígito identificador.
            is_inicial (bool): Se True, cria uma AihInicial; caso contrário, cria uma AihFinal.

        Returns:
            AihBase: Uma instância de AihInicial ou AihFinal.
        """  # noqa: E501
        if is_inicial:
            return AihInicial(codigo_ibge_uf, ano_referencia, quinto_digito)
        else:
            return AihFinal(codigo_ibge_uf, ano_referencia, quinto_digito)


# Exemplos AIH de uso geral
aih_inicial: AihBase = AihFactory.criar_aih(
    codigo_ibge_uf=26, ano_referencia=24, quinto_digito=1, is_inicial=True
)
print(f"AIH Inicial: {aih_inicial.get_numero_aih_completo()}")

aih_final: AihBase = AihFactory.criar_aih(
    codigo_ibge_uf=26, ano_referencia=24, quinto_digito=1, is_inicial=False
)
print(f"AIH Final: {aih_final.get_numero_aih_completo()}")


# Exemplos AIH Eletiva
aih_eletiva_inicial: AihBase = AihFactory.criar_aih(
    codigo_ibge_uf=26, ano_referencia=24, quinto_digito=5, is_inicial=True
)
print(f"AIH Eletiva Inicial: {aih_eletiva_inicial.get_numero_aih_completo()}")

aih_eletiva_final: AihBase = AihFactory.criar_aih(
    codigo_ibge_uf=26, ano_referencia=24, quinto_digito=5, is_inicial=False
)
print(f"AIH Eletiva Final: {aih_eletiva_final.get_numero_aih_completo()}")
