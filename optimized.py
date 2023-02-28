class Dynamique:
    def __init__(self, data, price):
        self.data = data
        self.data_conv = []
        self.max_spend = price
        self.matrice = []

    def main(self):
        self.calculate_renta(self.data)
        result = self.dynamique()
        self.calculate_gain_action(result)
        # print(result)

    def calculate_renta(self, dictionnaire):
        for value in dictionnaire:
            self.data_conv.append([value, dictionnaire[value]["prix"], (dictionnaire[value]["prix"] * dictionnaire[value]["pourcentage"])/100])

    def dynamique(self):
        self.matrice = [[0 for x in range(self.max_spend + 1)] for x in range(len(self.data_conv) + 1)]

        for data in range(1, len(self.data_conv) + 1):
            for price in range(1, self.max_spend + 1):
                if self.data_conv[data-1][1] <= price:
                    self.matrice[data][price] = max(self.data_conv[data - 1][2] +
                                                    self.matrice[data - 1][price - self.data_conv[data - 1][1]],
                                                    self.matrice[data - 1][price])
                else:
                    self.matrice[data][price] = self.matrice[data-1][price]

        # search values start
        price_max = self.max_spend
        lenght_data = len(self.data_conv)
        elements_selection = []

        while price_max >= 0 and lenght_data >= 0:
            last_element = self.data_conv[lenght_data - 1]
            if (self.matrice[lenght_data][price_max] ==
                    self.matrice[lenght_data - 1][price_max - last_element[1]] + last_element[2]):
                elements_selection.append(last_element)
                price_max -= last_element[1]

            lenght_data -= 1

        return self.matrice[-1][-1], elements_selection

    def calculate_gain_action(self, result):
        result_data = 0
        result_data_gain = 0
        for action in result[1]:
            result_data += self.data[action[0]]["prix"]
            result_data_gain += self.data[action[0]]["prix"] + action[2]

        print("Algo dynamique : ", result_data, result_data_gain)
        print("Algo dynamique : ", result)
