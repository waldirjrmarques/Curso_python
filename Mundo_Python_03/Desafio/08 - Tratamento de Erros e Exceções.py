'''
Exceções em python
    https://docs.python.org/pt-br/3/tutorial/errors.html
    Exception
        NameError
        ValueError
        ZeroDivisionError
        TypeError
        IndexError
        KeyError
        EOFError
        KeiboardInterrupt
        OSError
        MemoryError
        ConnectionError
        RuntimeError
'''
try: #teste
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except Exception as erro: #se aparecer erro
    print(f'problema encontrado foi {erro.__class__}')
except Exception as erro: #se aparecer erro
    print(f'problema encontrado foi {erro.__cause__}')
except(ValueError, TypeError):
    print('TIVEMOS PROBLEMA COM O TIPO DE DADOS QUE VC DIGITOU')
except(ZeroDivisionError):
    print('Não é possível dividir um numero por zero')
except(KeyboardInterrupt):
    print('Usuário prefere não informar os dados.')
else:#se não der erro
    print(f'Resultado é {r}')

finally: #acontece sempre independente se deu erro ou nao
    print("Volte sempre")