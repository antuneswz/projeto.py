print ('ATHLETE DEVELOPMENT')

input('diga SIM caso deseje entrar:')

print('Bom dia, aqui falamos da Atlhete Development, analisamos a media que os jogadores correm, em diferentes ligas na europa.')
nome_ligas=['liga','liga','liga','liga']
=[33,28,27,29]
=[22,27,26,31]
=[25,26,18,29]
=[21,24,28,32]
quais_ligas= input('''quais ligas vc quer comparar?
1-premier league
2-league one
3-bundesliga
4-laliga
''')
l=ligas.split('')

for i in range(len(l)):
    print(f'A liga {nome_ligas[int(l[i])]} te a media')
