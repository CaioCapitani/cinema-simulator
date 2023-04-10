filmes = {
    "Procurando Nemo": {"Classificação":3,"Ingresso":5},
    "Tarzan": {"Classificação":15, "Ingresso":5},
    "Interestellar": {"Classificação":12, "Ingresso":5},
    "Her": {"Classificação":14, "Ingresso":5}
    }

while True:
    barra = "="*62 # criação da barra para formatar terminal
    print(barra)

    print("Bem vindo ao Cinema, essas são as nossas sessões disponíveis:")

    for key, info in filmes.items():
        print("\nFilme:" , key)

        for key in info:
            print(key + ":", info[key], "anos" if key == "Classificação" else "disponíveis")


    escolha = input("\nQual filme você gostaria de assistir? ").strip().title()

    if escolha in filmes:
        age = int(input("Qual a sua idade?: ").strip())

        # checar idade do usuário

        if age >= filmes[escolha]["Classificação"]:

            # checar assentos livres

            num_assentos = filmes[escolha]["Ingresso"]

            if filmes[escolha]["Ingresso"] > 0:
                print("Aproveite o filme!")
                filmes[escolha]["Ingresso"] = filmes[escolha]["Ingresso"] - 1
            else:
                print("\nDesculpa, a sessão esgotou!")  
        else:
            print("\nVocê é muito novo para assistir esse filme")
    else:
        print("\nNão temos esse filme em cartaz...") 

