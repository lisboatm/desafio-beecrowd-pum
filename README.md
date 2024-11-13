# Desafio Beecrowd: PUM

## 📋 Descrição do Problema
Você deve escrever um programa que, dado um número inteiro **N**, imprime **N** linhas de saída seguindo um padrão específico. Cada linha deve conter três números inteiros consecutivos seguidos pela palavra "PUM".

## 📝 Exemplo de Funcionamento
Para cada linha impressa, três números consecutivos devem ser exibidos, seguidos da palavra "PUM". A sequência começa com o número 1 e avança de 4 em 4 números.

### 🖥️ Exemplo de Entrada
```
7
```

### 📤 Exemplo de Saída
```
1 2 3 PUM
5 6 7 PUM
9 10 11 PUM
13 14 15 PUM
17 18 19 PUM
21 22 23 PUM
25 26 27 PUM
```

## 🚀 Solução em Python
Para resolver o problema, o programa começa com o número 1 e, a cada linha, imprime três números consecutivos seguidos pela palavra "PUM". O próximo conjunto de números começa 4 unidades à frente do anterior.

### 🔧 Código
```python
def main():
    N = int(input())
    num = 1
    
    for _ in range(N):
        # Imprime os três números seguidos por "PUM"
        print(f"{num} {num + 1} {num + 2} PUM")
        # Incrementa o número para a próxima linha
        num += 4

if __name__ == "__main__":
    main()
```

## 📚 Explicação do Código
1. **Leitura de Entrada**:
   - O programa lê um número inteiro **N**, que representa a quantidade de linhas de saída que devem ser impressas.

2. **Impressão da Saída**:
   - Usamos um loop `for` que se repete **N** vezes.
   - A cada iteração, imprimimos três números consecutivos seguidos pela palavra "PUM".
   - Após cada linha, o valor base é incrementado em 4 para garantir que o próximo conjunto de números siga o padrão.

3. **Resultado**:
   - O programa gera a sequência correta de acordo com o exemplo fornecido.

## 🛠️ Como Rodar o Programa
Certifique-se de ter o Python instalado. Salve o código em um arquivo, por exemplo, `pum.py`. No terminal, execute:
```bash
python3 pum.py
```

## 🏆 Exemplos de Teste
Aqui estão alguns exemplos adicionais para testar o programa:

### Entrada:
```
3
```
### Saída:
```
1 2 3 PUM
5 6 7 PUM
9 10 11 PUM
```
