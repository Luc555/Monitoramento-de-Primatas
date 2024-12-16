import random
import geopandas as gpd
import pandas as pd
import folium
from folium.plugins import AntPath
import webbrowser
import math
from datetime import date
import os.path
from pathlib import Path
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt


# https://netdiario.com.br/noticias/hoje-e-o-dia-do-sagui-da-serra-escuro/
#Inspiração, pois a espécie é nativa da região e está ameaçada.
#https://pt.wikipedia.org/wiki/Callithrix_aurita#https://institutolife.org/wp-content/uploads/2018/11/Lista-da-Fauna-Ameacada-de-Extincao-RJ.pdf
# https://ava.icmbio.gov.br/pluginfile.php/15302/mod_folder/content/0/LEVANTAMENTO%20E%20DIAGN%C3%93STICO%20DE%20CALLITHRIX%20AURITA%20(E.%20GEOFFROY,%201812)%20E%20CONG%C3%8ANERES%20INVASORES%20EM%20FRAGMENTOS%20FLORESTAIS%20NA%20MICRORREGI%C3%83O%20DE%20VI%C3%87OSA,%20MG,%20BACIA%20HIDROGR%C3%81FICA%20DO%20RIO%20DOCE.pdf?forcedownload=1#:~:text=O%20Callithrix%20aurita%20(E.,Paulo%20e%20Rio%20de%20Janeiro.
#https://matanativa.com.br/sagui-da-serra-escuro/
#Expectativa vida(25 anos):
#https://guiaanimal.net/articles/1136



#Variaveis para setar:
#Vive próximo da área urbana
#Pertence à algum grupo
#idade
#próximo de espécie concorrente?
#É hibrido

#Para os dados de treino:
#Encontra-se morto ou vivo
#Caso morto
#Causa da morte

class Train:
    digite_n_animals = input('Favor informar o número de amostras de treino: ')
    datetime = []
    data = []
    id_animal_list = []
    sexAnimalAnimalList = []
    #É provavelmente a maior espécie do gênero Callithrix pesando 400-450 g e 
    weightAnimal = []
    # Com comprimento de corpo de 19-25 cm e 27-35 cm de cauda.[11]
    sizeAnimal = []
    inAGroupList = []
    ageList = []
    hybridList = []
    nextUrbanAreaList = []
    liveAndLetDieList = []


    for animal in range(int(digite_n_animals)):
        #lista para as coordenadas
        #print(data)
        sexAnimal =  random.choice(["male", "female"])
        weight = int(random.uniform(400, 450))
        size = int(random.uniform(19, 25))
        inAGroup =  random.choice(["yes", "no", "yes", "yes", "yes"])
        age = int(random.uniform(1, 25))
        hybrid = random.choice(["no", "no", "yes", "no", "no"])
        nextUrbanArea = random.choice(["yes", "no", "no"])
        
        id_animal = id_animal_list.append(animal)
        sexAnimalAnimalList.append(sexAnimal)
        weightAnimal.append(weight)
        sizeAnimal.append(size)
        inAGroupList.append(inAGroup)
        ageList.append(age)
        hybridList.append(hybrid)
        nextUrbanAreaList.append(nextUrbanArea)

            
        if sexAnimal =="male" and weight <= 430 and size < 21 and inAGroup == "no" and age <= 3 or age >=20 and hybrid == "yes" and nextUrbanArea=="yes":
            # Probabilidade de morte
            p_resposta = (random.uniform(0.0, 0.53)) 
            # Gerar amostras aleatórias da distribuição binomial
            if p_resposta < 0.5:
                liveAndLetDie = 0
                liveAndLetDieList.append(liveAndLetDie)
            else:
                liveAndLetDie = 1
                liveAndLetDieList.append(liveAndLetDie)
        
        elif sexAnimal =="male" and weight > 430 and size >= 21 and inAGroup == "yes" and  age >=3 or age <=20 and hybrid == "no" and nextUrbanArea=="no":
            # Probabilidade de morte
            p_resposta = (random.uniform(0.48, 1.0)) 
            # Gerar amostras aleatórias da distribuição binomial
            if p_resposta < 0.5:
                liveAndLetDie = 0
                liveAndLetDieList.append(liveAndLetDie)
            else:
                liveAndLetDie = 1
                liveAndLetDieList.append(liveAndLetDie)
        
        elif sexAnimal =="male" and weight > 430 and size < 21 and inAGroup == "yes" and  age >=3 or age <=20 and hybrid == "no" and nextUrbanArea=="yes":
            # Probabilidade de morte
            p_resposta = (random.uniform(0.1, 0.6)) 
            # Gerar amostras aleatórias da distribuição binomial
            if p_resposta < 0.5:
                liveAndLetDie = 0
                liveAndLetDieList.append(liveAndLetDie)
            else:
                liveAndLetDie = 1
                liveAndLetDieList.append(liveAndLetDie)
        
        
        elif sexAnimal =="female" and weight <= 430 and size < 21 and inAGroup == "yes" and age <=3 or age >=20 and hybrid == "yes" and nextUrbanArea=="yes":
            # Probabilidade de morte
            p_resposta = (random.uniform(0.3, 0.6)) 
            # Gerar amostras aleatórias da distribuição binomial
            if p_resposta < 0.5:
                liveAndLetDie = 0
                liveAndLetDieList.append(liveAndLetDie)
            else:
                liveAndLetDie = 1
                liveAndLetDieList.append(liveAndLetDie)
        
        elif sexAnimal =="female" and weight <= 430 and size < 21 and inAGroup == "no" and age <= 3 or age >=20 and hybrid == "yes" and nextUrbanArea=="yes":
            # Probabilidade de morte
            p_resposta = (random.uniform(0.1, 0.55)) 
            # Gerar amostras aleatórias da distribuição binomial
            if p_resposta < 0.5:
                liveAndLetDie = 0
                liveAndLetDieList.append(liveAndLetDie)
            else:
                liveAndLetDie = 1
                liveAndLetDieList.append(liveAndLetDie)
        
        elif sexAnimal =="female" and weight > 430 and size >= 21 and inAGroup == "yes" and  age >=3 or age <=20 and hybrid == "no" and nextUrbanArea=="yes":
            # Probabilidade de morte
            p_resposta = (random.uniform(0.45, 1.0)) 
            # Gerar amostras aleatórias da distribuição binomial
            if p_resposta < 0.5:
                liveAndLetDie = 0
                liveAndLetDieList.append(liveAndLetDie)
            else:
                liveAndLetDie = 1
                liveAndLetDieList.append(liveAndLetDie)
        
        else:
            p_resposta = (random.uniform(0.0, 1.0)) 
            # Gerar amostras aleatórias da distribuição binomial
            if p_resposta < 0.5:
                liveAndLetDie = 0
                liveAndLetDieList.append(liveAndLetDie)
            else:
                liveAndLetDie = 1
                liveAndLetDieList.append(liveAndLetDie)


    # Cria um DataFrame 
    df = pd.DataFrame({'Id_primata': id_animal_list, 
                        'Sexo do animal': sexAnimalAnimalList, 
                        'Tamanho do animal(cm)': sizeAnimal[0:], 'Peso do animal(gramas)': weightAnimal[0:],
                        'Algum grupo': inAGroupList, 'Idade(ano)': ageList,  'Area urbana?': nextUrbanAreaList, 'Hibrído?': hybridList, 'DeadOrAlive': liveAndLetDieList})
    # Salva em arquivo Excel
    nome_arquivo_excel = 'C:/Users/Lucas/OneDrive/Documents/PYTHON PROJECTS/Machine Learning/Knn algorithm/knnPrimateMonitoring/Data/trainData.xlsx'
    df.to_excel(nome_arquivo_excel, index=False) 


class Test:
    digite_n_animals = input('Favor informar o número de amostras de teste:  ')
    datetime = []
    data = []
    id_animal_list = []
    sexAnimalAnimalList = []
    #É provavelmente a maior espécie do gênero Callithrix pesando 400-450 g e 
    weightAnimal = []
    # Com comprimento de corpo de 19-25 cm e 27-35 cm de cauda.[11]
    sizeAnimal = []
    inAGroupList = []
    ageList = []
    hybridList = []
    nextUrbanAreaList = []
    liveAndLetDieList = []


    for animal in range(int(digite_n_animals)):
        #lista para as coordenadas
        #print(data)
        sexAnimal =  random.choice(["male", "female"])
        weight = int(random.uniform(400, 450))
        size = int(random.uniform(19, 25))
        inAGroup =  random.choice(["yes", "no", "yes", "yes"])
        age = int(random.uniform(1, 25))
        hybrid = random.choice(["no", "no", "yes", "no"])
        nextUrbanArea = random.choice(["yes", "no"])
        

        id_animal = id_animal_list.append(animal)
        sexAnimalAnimalList.append(sexAnimal)
        weightAnimal.append(weight)
        sizeAnimal.append(size)
        inAGroupList.append(inAGroup)
        ageList.append(age)
        hybridList.append(hybrid)
        nextUrbanAreaList.append(nextUrbanArea)

    # Cria um DataFrame 
    df = pd.DataFrame({'Id_primata': id_animal_list, 
                        'Sexo do animal': sexAnimalAnimalList, 
                        'Tamanho do animal(cm)': sizeAnimal[0:], 'Peso do animal(gramas)': weightAnimal[0:],
                        'Algum grupo': inAGroupList, 'Idade(ano)': ageList, 'Area urbana?': nextUrbanArea, 'Hibrído?': hybridList})
    # Salva em arquivo Excel
    nome_arquivo_excel = 'C:/Users/Lucas/OneDrive/Documents/PYTHON PROJECTS/Machine Learning/Knn algorithm/knnPrimateMonitoring/Data/testData.xlsx'
    df.to_excel(nome_arquivo_excel, index=False) 