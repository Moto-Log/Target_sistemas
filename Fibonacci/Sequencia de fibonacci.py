def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Digite um número: "))
validacao = False
for i in range(num):
    if fibonacci(i) > num:
        break
    if fibonacci(i) == num:
        print(num,"pertence à sequência de Fibonacci!")
        validacao = True
        break
if not validacao:
    print(num,"não pertence à sequência de Fibonacci.")
