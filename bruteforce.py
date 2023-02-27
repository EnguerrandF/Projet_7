ACTIONS = {
    'Action-1': {'prix': 20, 'pourcentage': 5},
    'Action-2': {'prix': 30, 'pourcentage': 10},
    'Action-3': {'prix': 50, 'pourcentage': 15},
    'Action-4': {'prix': 70, 'pourcentage': 20},
    'Action-5': {'prix': 60, 'pourcentage': 17},
    'Action-6': {'prix': 80, 'pourcentage': 25},
    'Action-7': {'prix': 22, 'pourcentage': 7},
    'Action-8': {'prix': 26, 'pourcentage': 11},
    'Action-9': {'prix': 48, 'pourcentage': 13},
    'Action-10': {'prix': 34, 'pourcentage': 27},
    'Action-11': {'prix': 42, 'pourcentage': 17},
    'Action-12': {'prix': 110, 'pourcentage': 9},
    'Action-13': {'prix': 38, 'pourcentage': 23},
    'Action-14': {'prix': 14, 'pourcentage': 1},
    'Action-15': {'prix': 18, 'pourcentage': 3},
    'Action-16': {'prix': 8, 'pourcentage': 8},
    'Action-17': {'prix': 4, 'pourcentage': 12},
    'Action-18': {'prix': 10, 'pourcentage': 14},
    'Action-19': {'prix': 24, 'pourcentage': 21},
    'Action-20': {'prix': 114, 'pourcentage': 18},
}


class BestActionsForThePrice:
    def __init__(self, dictionnaire_action):
        self.dictionnaire_action = dictionnaire_action
        self.max_spend = 500
        self.dic_result_profitability = {}
        self.list_selection_action = []

    def main(self):
        self.check_action()
        self.action_to_select()
        self.calculate_gain_action()
        # print(self.dic_result_profitability)

    def check_action(self):
        for action in self.dictionnaire_action:
            result = self.calculate_action(self.dictionnaire_action[action]["prix"],
                                           self.dictionnaire_action[action]["pourcentage"])
            self.dic_result_profitability[action] = result

        self.dic_result_profitability = dict(sorted(self.dic_result_profitability.items(),
                                                    key=lambda x: x[1], reverse=True))

    def calculate_action(self, prix, pourcentage):
        return ((prix * pourcentage) / 100)

    def action_to_select(self):
        """ Sélectionne 500 euro d'action"""
        for action in self.dic_result_profitability:
            if (self.max_spend - self.dictionnaire_action[action]["prix"]) < 0:
                pass
            else:
                self.max_spend = self.max_spend - self.dictionnaire_action[action]["prix"]
                self.list_selection_action.append(action)

    def calculate_gain_action(self):
        result = 0
        result_gain = 0
        for action in self.list_selection_action:
            result += self.dic_result_profitability[action] + self.dictionnaire_action[action]["prix"]
            result_gain += self.dictionnaire_action[action]["prix"]
        print("Alogo 1 : ", result_gain, result)


class BestActionsForThePriceThee:
    def __init__(self):
        self.data = []
        self.max_spend = 500
        self.matrice = []

    def main(self):
        self.calculate_renta(ACTIONS)
        result = self.dynamique()
        self.calculate_gain_action(result)
        # print(result)

    def calculate_renta(self, dictionnaire):
        for value in dictionnaire:
            self.data.append([value, dictionnaire[value]["prix"], (dictionnaire[value]["prix"] * dictionnaire[value]["pourcentage"])/100])

    def dynamique(self):
        self.matrice = [[0 for x in range(self.max_spend + 1)] for x in range(len(self.data) + 1)]
        for i in range(1, len(self.data) + 1):
            for w in range(1, self.max_spend + 1):
                if self.data[i-1][1] <= w:
                    self.matrice[i][w] = max(self.data[i-1][2] + self.matrice[i-1][w-self.data[i-1][1]], self.matrice[i-1][w])
                else:
                    self.matrice[i][w] = self.matrice[i-1][w]

        # Retrouver les éléments en fonction de la somme
        w = self.max_spend
        n = len(self.data)
        elements_selection = []

        while w >= 0 and n >= 0:
            e = self.data[n-1]
            if self.matrice[n][w] == self.matrice[n-1][w-e[1]] + e[2]:
                elements_selection.append(e)
                w -= e[1]

            n -= 1

        return self.matrice[-1][-1], elements_selection

    def calculate_gain_action(self, result):
        result_data = 0
        result_data_gain = 0
        for action in result[1]:
            result_data += ACTIONS[action[0]]["prix"]
            result_data_gain += ACTIONS[action[0]]["prix"] + action[2]

        print("Alogo 2 : ", result_data, result_data_gain)


BestActionsForThePrice(ACTIONS).main()
BestActionsForThePriceThee().main()
