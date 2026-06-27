try:
    a=int(input('Numerador: '))
    b=int(input('Denomiador: '))
    r=a/b
except(ValueError,TypeError):
   print('Tivemos um problema com o tipo de dados que você digitou: ')
except ZeroDivisionError:
    print('Não é possível dividir qualquer número por ZERO.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados pedidos.')
#except Exception as erro:
    #print(f'O erro encontrado foi: {erro.__cause__}')

else:
    print(f'Resultado: {r}')
finally:
    print('Obrigado pela breve atenção, volte sempre!')