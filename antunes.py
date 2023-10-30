print ('ATHLETE DEVELOPMENT')

while True:
    escolha = input('diga SIM caso deseje entrar:')
    if(escolha[0] == 's' or escolha[0] == 'S'):
        break
    
print('Bom dia, aqui falamos da Atlhete Development, analisamos a media que os jogadores correm, em diferentes ligas na europa.')
nome_ligas=['','premier league','league one','bundesliga','laliga']
valores=[
    [],
    [33,28,27,29],
    [22,27,26,31],
    [25,26,18,29],
    [21,24,28,32],
    ]

while True:
    ligas= input('''
    quais ligas vc deseja saber a média de corrida?
    1-premier league
    2-league one
    3-bundesliga
    4-laliga
    ''')
    l=ligas.split(' ')

    print()
    for i in range(len(l)):
        print(f'A liga {nome_ligas[int(l[i])]} tem a media {sum(valores[int(l[i])])/4}')
    resp=input('  gostou de saber isso?caso queira saber a media de alguma outra liga digite (sim) siga a lista abaixo, caso não queira digite (não):')
    if(resp.upper())[0] == "N":
        break
print('então espero que tenham gostado, muito obrigado tenha um bom dia!')
