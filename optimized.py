import csv
import time


class DynamiqueFloat:
    def __init__(self, name_csv, price):
        self.name_csv = name_csv
        self.data = self.open_csv()
        self.max_spend = price
        self.matrice = []
        self.elements_selection = []

    def main(self):
        time_start = time.time()
        result = self.dynamique()
        print(f"Le gain est de {result[0]}, pour le prix de vente de {result[2]}. Il y a {len(result[1])} actions,\
                voici la liste des action sélectionné {result[1]}")
        print(f"Temps d'executions: {time.time() - time_start} secondes")

    def open_csv(self):
        with open(self.name_csv, newline="", encoding='utf-8') as csvfile:
            reader = list(csv.reader(csvfile, delimiter=","))
        return reader[1:]

    def dynamique(self):
        range_price = int((self.max_spend * 100) + 1)
        self.matrice = [[0.00 for x in range(range_price)] for x in range(len(self.data) + 1)]

        for data in range(1, len(self.data) + 1):
            """ Parcours toutes les actions """

            for price in range(1, range_price):
                """ Parcours tous les prix pour chaques actions.
                    Dans la variable range_price self.max_spend est mutiplié par 100 afin d'avoir une colonne
                    pour chaque prix décimal exemple: 1.01, 1.02....
                """

                conversion_price_in_float = float(price / 100)
                if float(self.data[data-1][1]) > 0.0 and float(self.data[data-1][1]) <= conversion_price_in_float:
                    """
                        Vérifier si le prit courant n'est pas négatif,
                        ainsi que le prix de l'action sélectionnée n'est pas supérieur au prix courant de la boucle.
                        On récupére le meilleur résultat entre la rentabilité de l'action d'avant pour le prix courant
                        de la boucle et entre résultat de la différence du prix de l'action et du prix courant
                        de la boucle.
                    """

                    calculate_price_difference = conversion_price_in_float - float(self.data[data-1][1])
                    profit_action = self.calculate_rentability(self.data[data-1][2], self.data[data-1][1])
                    action_optimized_for_pricex = self.matrice[data-1][int(calculate_price_difference * 100)]

                    self.matrice[data][price] = max(round(profit_action + action_optimized_for_pricex, 2),
                                                    self.matrice[data-1][price])

                else:
                    """ Si le prix de l'action est au dessus du prix courant de la boucle on garde
                        automatiquement la valeur de la ligne d'avant """

                    self.matrice[data][price] = self.matrice[data-1][price]

        price_max = self.max_spend
        lenght_data = len(self.data)

        while price_max > 0 and lenght_data > 0:
            """ On remonte la matrice en parallèle des données pour retrouver les
                actions sélectionnées """

            last_element = self.data[lenght_data - 1]
            matrice_price_current = self.matrice[lenght_data][int(price_max * 100)]
            matrice_price_less_1 = self.matrice[lenght_data - 1][int(price_max * 100 - float(last_element[1]) * 100)]
            price_last_element = self.calculate_rentability(last_element[2], last_element[1])

            if float(last_element[1]) > 0 and matrice_price_current == (matrice_price_less_1 + price_last_element):
                self.elements_selection.append(last_element)
                price_max -= float(last_element[1])

            lenght_data -= 1

        return self.matrice[-1][-1], self.elements_selection, round(self.max_spend - price_max, 2)

    def calculate_rentability(self, poucentage, price):
        return round((float(price) * float(poucentage)) / 100, 2)


DynamiqueFloat("./data/small_data.csv", 1.0).main()
# DynamiqueFloat("./data/dataset1_Python+P7.csv", 500).main()
# DynamiqueFloat("./data/dataset2_Python+P7.csv", 500).main()

"""
    dataset1_Python+P7.csv
    Prix de vente 499.93
    Le gain est de 198.54
    Temps d'executions: 104.3878984451294 secondes
"""
"""
    dataset2_Python+P7.csv
    Prix de vente 499.92
    Le gain est de 197.95
    Temps d'executions: 72.23420310020447 secondes
"""


class Glouton:
    def __init__(self, name_csv, price_max):
        self.name_csv = name_csv
        self.price_max = price_max

    def main(self):
        time_start = time.time()
        shares_list = self.retrieve_data()
        optimal_combination, spending, profit = self.generate_best_combination(shares_list)
        self.display_result(optimal_combination, spending, profit)

        print(f"Durée d'exécution de l'algorithme : {str(time.time() - time_start)}")

    def retrieve_data(self):
        with open(self.name_csv) as shares_csv:
            next(shares_csv)
            reader = csv.reader(shares_csv, delimiter=",")
            shares_list = []
            for line in reader:
                shares_list.append({
                    "name": line[0],
                    "price": float(line[1]),
                    "percentage_profit": float(line[2]),
                    "profit": round((float(line[1]) * float(line[2])) / 100, 2)
                })
            return shares_list

    def generate_best_combination(self, data):
        data.sort(key=lambda item: item.get("percentage_profit"), reverse=True)
        max_spending = self.price_max
        spending = 0
        profit = 0
        optimal_combination = []
        for share in data:
            if (spending + share["price"]) <= max_spending and share["price"] > 0:
                optimal_combination.append(share)
                profit += share["profit"]
                spending += share["price"]
        return optimal_combination, spending, profit

    def display_result(self, optimal_combination, spending, profit):
        print("La solution optimale est d'acheter les actions suivantes:")
        for share in optimal_combination:
            print("- " + share["name"])
        print("Elle coûtera " + str(round(spending, 2)) + "€ et aura un profit de " + str(round(profit, 2)) + "€.")


# Glouton("./data/dataset1_Python+P7.csv", 500).main()
# Glouton("./data/dataset2_Python+P7.csv", 500).main()
# Glouton("./data/small_data.csv", 1.0).main()

"""
    dataset1_Python+P7.csv
    Prix de vente 499.94
    Le gain est de 198.51
    Avec le round au dictionnaire de la donnée profit a la fonction retrieve_data:  Le gain est de 198.49
    Temps d'executions: 0.004999876022338867 secondes
"""
"""
    dataset2_Python+P7.csv
    Prix de vente 499.98
    Le gain est de 197.77
    Avec le round au dictionnaire de la donnée profit a la fonction retrieve_data:  Le gain est de 197.75
    Temps d'executions: 0.0059893131256103516 secondes
"""
