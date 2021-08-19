# dict_1={"word1":"rat","word2":"muose","age":8}
# print(dict_1)
# print(dict_1["word1"])

from termcolor import colored

dict_rec={"наименование":"Мясо",
          "аннотация":"вкусный кусок свежего мяса",
          "время приготовления":7,
          "Количество этапов приготовления":2,
          "краткое описание":{"шаг первый":"положить мясо на гриль",
                              "шаг второй":"убрать мясо с гриля"},
        }
# print(dict_rec)
dict_rec["список ингредиентов"]= ["мясо","укроп"]
print(dict_rec)
dict_rec2={"наименование":"Картошка",
          "аннотация":"Вареная картошка",
          "время приготовления":20,
          "Количество этапов приготовления":2,
          "краткое описание":{"шаг первый":"почистить картофель",
                              "шаг второй":"положить его к кипящую воду"},
           "список ингредиентов":["картошка","вода"]
          }
print(dict_rec2["краткое описание"]["шаг первый"])

dict_rec3={"наименование":"вареное яйцо",
           "аннотация":"яйцо сваренное в крутую",
           "время приготовления":20,
           "Количество этапов приготовления":2,
           "краткое описание":{"шаг первый":"положите яйцо в кипящую воду",
                               "шаг второй":"достаньте яйцо из воды"},
           "список ингредиентов":["яйцо","вода"]
           }
dictionary={"rec1":dict_rec,"rec2":dict_rec2,"rec3":dict_rec3}
from termcolor import colored
print ("",colored(dictionary["rec1"],'green'),"\n", colored(dictionary["rec2"],'red'),"\n",colored(dictionary["rec3"],'blue'))
