# Calculadora de AIH (Autorização de Internação Hospitalar) para o Sistema MV SOUL

Esta classe Python foi desenvolvida para facilitar o cálculo dos números de Autorização de Internação Hospitalar (AIH) no contexto do Sistema MV SOUL. A AIH é uma numeração utilizada para identificar e autorizar internações hospitalares.

## Como Usar

1. **Instalação:**

   Não é necessário instalar nada separadamente. Basta incluir o código da classe no seu projeto Python.

2. **Detalhes da Classe:**

   A calculadora de AIH foi refatorada para seguir princípios de **SOLID**, **Design Patterns** e **Clean Code**, tornando o código mais modular e flexível. A seguir, as principais mudanças:

   - **Classe Abstrata `AihBase`**: Define a estrutura base para o cálculo do número da AIH.
   - **Classe `AihInicial`**: Responsável por gerar números de AIH iniciais.
   - **Classe `AihFinal`**: Responsável por gerar números de AIH finais.
   - **Factory `AihFactory`**: Facilita a criação das instâncias de AIH, de forma a escolher entre uma AIH inicial ou final com base no parâmetro fornecido.

   - **Métodos**:
     - `get_numero_aih_completo()`: Retorna a representação formatada do número AIH calculado, incluindo o dígito verificador.
     - `_calcular_digito_verificador()`: Calcula o dígito verificador baseado na fórmula do Sistema MV SOUL.

3. **Lógica de Numeração AIH:**

   - Os dígitos 1 e 2 correspondem ao código do IBGE da UF ou 99, caso o tipo de AIH informado seja CNRAC.
   - Os dígitos 3 e 4 correspondem aos dois últimos algarismos do ano de referência.
   - O dígito 5 identifica o tipo de AIH:
     - `1` para uso geral
     - `3` para AIH específica da CNRAC
     - `5` para procedimentos cirúrgicos eletivos
   - Os dígitos 6 a 12 seguem uma ordem crescente começando por `0000001`.
   - O último dígito é o **dígito verificador**, calculado com base na fórmula do MV SOUL, que envolve a divisão do número por 11 e o cálculo do resto da divisão.

4. **Exemplo de Uso**:

   ```python
   # Criando uma AIH Inicial para uso geral
   aih_inicial: AihBase = AihFactory.criar_aih(
      codigo_ibge_uf=26, ano_referencia=24, quinto_digito=1, is_inicial=True
   )
   print(f"AIH Inicial: {aih_inicial.get_numero_aih_completo()}")

   # Criando uma AIH Final para uso geral
   aih_final: AihBase = AihFactory.criar_aih(
      codigo_ibge_uf=26, ano_referencia=24, quinto_digito=1, is_inicial=False
   )
   print(f"AIH Final: {aih_final.get_numero_aih_completo()}")

   # Criando uma AIH Inicial para procedimento cirúrgico eletivo
   aih_eletiva_inicial: AihBase = AihFactory.criar_aih(
      codigo_ibge_uf=26, ano_referencia=24, quinto_digito=5, is_inicial=True
   )
   print(f"AIH Eletiva Inicial: {aih_eletiva_inicial.get_numero_aih_completo()}")

   # Criando uma AIH Final para procedimento cirúrgico eletivo
   aih_eletiva_final: AihBase = AihFactory.criar_aih(
      codigo_ibge_uf=26, ano_referencia=24, quinto_digito=5, is_inicial=False
   )
   print(f"AIH Eletiva Final: {aih_eletiva_final.get_numero_aih_completo()}")

## Contribuições e Melhorias

Contribuições são bem-vindas! Se encontrar algum problema ou tiver sugestões de melhoria, sinta-se à vontade para criar uma issue ou enviar um pull request.

## Licença

Este código é distribuído sob a licença [MIT](LICENSE).