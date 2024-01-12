# Calculadora de AIH (Autorização de Internação Hospitalar) para o Sistema MV SOUL

Esta classe Python, `CalcularAih`, foi desenvolvida para facilitar o cálculo dos números de Autorização de Internação Hospitalar (AIH) no contexto do Sistema MV SOUL. A AIH é uma numeração utilizada para identificar e autorizar internações hospitalares.

## Como Usar

1. **Instalação:**

   Não é necessário instalar nada separadamente. Basta incluir a classe `CalcularAih` no seu código Python.

2. **Detalhes da Classe:**

   - `__init__(self, codigo_ibge_uf, ano_referencia, quinto_digito, is_inicial)`: Inicializa a classe com os parâmetros necessários para o cálculo da AIH.
   - `get_numero_aih()`: Retorna a representação formatada do número AIH calculado.

3. **Lógica de Numeração AIH:**

   - Os dígitos 1 e 2 correspondem ao código do IBGE da UF ou 99, caso o tipo de AIH informado seja CNRAC.
   - Os dígitos 3 e 4 correspondem aos dois últimos algarismos do ano de referência.
   - O dígito 5 identifica o tipo de AIH (1 para uso geral, 3 para AIH específica da CNRAC, 5 para procedimentos cirúrgicos eletivos).
   - Os dígitos 6 a 12 seguem uma ordem crescente começando por 0000001.
   - O último dígito é o verificador, calculado de acordo com uma fórmula específica.

## Contribuições e Melhorias

Contribuições são bem-vindas! Se encontrar algum problema ou tiver sugestões de melhoria, sinta-se à vontade para criar uma issue ou enviar um pull request.

## Licença

Este código é distribuído sob a licença [MIT](LICENSE).
