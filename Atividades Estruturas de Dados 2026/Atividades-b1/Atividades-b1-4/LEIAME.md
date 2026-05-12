**Instituição:** Fatec São Caetano do Sul - Antônio Russo 





**Disciplina:** Estruturas de Dados 





**Professor:** Veríssimo 





**Data:** 31/03/2026 





**Equipe:** NN





**Integrantes:**

* Eric Fracassi de Gois
* Gabriel Lasinskais
* Yuri Shinnishi de Queiroz Rossi





#### **Descrição da Atividade**



O projeto consiste na implementação e demonstração prática de um simulador da calculadora HP12c em linguagem Python. O sistema utiliza a estrutura de dados de pilha para gerenciar as memórias X, Y, Z e T, operando através da Notação Polonesa Reversa (RPN).



O objetivo é mostrar com um fluxo gráfico da utilização da pilha em cada momento da operação matemática.





###### **Funcionalidades do Código:**



* **Simulação de Registradores:** O programa mapeia e exibe os estados das memórias T, Z, Y e X a cada novo dado inserido na pilha.
* **Validação de Erros:** Tratamento para falta de operandos na pilha, entradas de caracteres inválidos e divisões por zero.
* **Conversor RPN para algébrico:** Além do cálculo, o programa reconstrói e exibe a expressão algébrica equivalente em tempo real.
* **Tratamento de Localização:** Suporte para entrada de números com vírgula (exemplo: 0,03), convertendo-os automaticamente para o ponto de formato flutuante.





#### **Casos de Teste Implementados**



A demonstração abrange os seguintes cenários obrigatórios:



* **Entrada Inválida:** Tratamento de erro para a RPN fora do padrão.
* **Expressão Algébrica I:** ((10+2) \* 3 - 6)/5.
* **Expressão Algébrica II:** \[(1/(1 - (0,03 \* 4)/30)) - 1] \* 100.





#### **Conteúdo do Pacote**



Este repositório contém os artefatos exigidos para a entrega:



* **atv3-LIFO.py:** Código-fonte em Python com a lógica da pilha e RPN.
* **HP12C_1.pdf:** Demonstração gráfica do funcionamento.
* **LEIAME.md:** Documentação com identificação e descrição desta atividade.





#### **Como Executar**



1. Certifique-se de ter o Python instalado.
2. Execute o arquivo principal: python atv3-LIFO.py
3. Digite a expressão RPN separando cada elemento por espaço.

&#x09;Exemplo: 10 2 + 3 \*

4\. Para encerrar o programa, digite sair.











