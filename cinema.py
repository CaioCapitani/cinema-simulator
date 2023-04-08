filmes = {
    "Procurando Nemo": [3,5],
    "Tarzan": [15,5],
    "Interestellar": [12, 5],
    "Her": [14, 5]
    }

while True:

    escolha = input("Qual filme você gostaria de assistir? ").strip().title()

    if escolha in filmes:
        age = int(input("Qual a sua idade?: ").strip())

        # checar idade do usuário

        if age >= filmes[escolha][0]:

            # checar assentos livres

            num_assentos = filmes[escolha][1]

            if filmes[escolha][1] > 0:
                print("Aproveite o filme!")
                filmes[escolha][1] = filmes[escolha][1] - 1
            else:
                print("Desculpa, a sessão esgotou!")  
        else:
            print("Você é muito novo para assistir esse filme")
    else:
        print("Não temos esse filme em cartaz...") 

