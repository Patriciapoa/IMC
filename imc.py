print('Este programa calcula o IMC\n')
peso=input('Informe o peso:')
altura=input('Informe a altura com ponto como no exemplo 1.65\nSua altura:')
p = float( peso )
a = float( altura )
imc=p/(a*a)
print('Seu IMC é ',round(imc))
if imc < 18.5:
  print('Você está abaixo do peso')
elif imc > 18.5 and imc < 24.99:
  print('IMC considerado normal')
elif imc > 25 and imc < 29.99:
  print('Você está com sobre peso')
elif imc > 30 and imc < 39.99:
  print('IMC indica obesidade')
else:
  print('IMC indica obesidade grave')
print('\nDe acordo com o resultado de IMC também é possível prever o risco que cada pessoa tem de desenvolver doenças crônicas.\nIsto porque quanto maior é o valor do IMC, maior é a quantidade de gordura acumulada no corpo e maior o risco de doenças como pressão alta, diabetes e problemas cardíacos.')