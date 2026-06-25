# A instrução if

- A instrução if de Python permite analisar o estado atual de um programa e responder de forma apropriada a esse estado.

- Testes condicionais: A instrução if realiza "testes condicionais", analisa a expressão e retorna True ou False. Python usa os valores
True e False para decidir se o código em uma instrução if deve ser executado. Se um teste condicional for avaliado como True, Python executará o código após a instrução if. Se o teste for avaliado como False, o interpretador ignorará o código depois da instrução if.

- Verificando a igualdade: O operador de igualdade é ( == ). Para se comparar duas expressões/valores utiliza-se esse operador. Vai retornar True ou False.
--> Testes de igualdade diferenciam letras maiúsculas de minúsculas em Python.
--> Para evitar isso utilize lower() uqando necessário. A função lower() não altera o valor originalmente armazenado em car, portanto você pode fazer esse tipo de comparação sem afetá-lo.
---> EXEMPLO: Por exemplo, um site pode usar um
teste condicional desse tipo para garantir que todos os usuários tenham um nome realmente único, e não apenas uma variação quanto ao uso de letras maiúsculas em relação ao nome de usuário de outra pessoa. Quando alguém submeter um novo nome de usuário, esse nome será convertido para letras minúsculas e comparado às versões com letras minúsculas de todos os nomes de usuário existentes. Durante essa verificação, um nome de usuário como 'John' será rejeitado se houver qualquer variação de 'john' já em uso.

- Verificando a diferença: Se quiser determinar se dois valores não são iguais, você poderá combinar um ponto de exclamação e um sinal de igualdade (!=). O ponto de exclamação representa não, como ocorre em muitas linguagens de programação.

