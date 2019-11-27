import csv
import json
import matplotlib.pyplot as plt
import numpy as np

class LinearLearn:

    def __init__(self):
        self.theta0 = 0.0
        self.old_theta0 = 1.0
        self.theta1 = 0.0
        self.data = []
        self.data_length = 1

        self.error = 0.0000001
        self.learn_rate = 0.1

    def estimatePrice(self, dist):
        return self.theta0 + (self.theta1 * dist)

    def load_data(self):
        with open( "data.csv", 'r' ) as theFile:
            reader = csv.DictReader(theFile)
            for line in reader:
                self.data.append([int(line["km"]), int(line["price"])])
        if len(self.data) < 1:
            raise Exception("no data")

        self.data_length = len(self.data)
        self.x,self.y = zip(*self.data)


    def min_error(self):
        if self.theta0 > self.old_theta0:
            er = self.theta0 - self.old_theta0
        else:
            er = self.old_theta0 - self.theta0
        return er > self.error

    def scale_data(self):
        new_data = []
        x_min = min(self.x)
        x_max = max(self.x)
        y_min = min(self.y)
        y_max = max(self.y)
        for i in range(self.data_length):
            # x = (self.x[i] - x_min) / (x_max - x_min)
            # y = (self.y[i] - y_min) / (y_max - y_min)
            x = (self.x[i] - x_min)
            y = (self.y[i] - y_min)
            new_data.append([x,y])
        self.data = new_data



    def calc_theta(self):
        #data = [km, price]
        while self.min_error():
            val0 = 0.0
            val1 = 0.0

            for dist, price in self.data:
                val0 += self.estimatePrice(dist) - price
                val1 += (self.estimatePrice(dist) - price) * dist
            #
            # print("val   c", val0, "val m", val1)
            # print("theta c", self.theta0, "theta m", self.theta1)

            self.old_theta0 = self.theta0
            self.theta0 = self.theta0 - self.learn_rate * (val0 / self.data_length)
            self.theta1 = self.theta1 - self.learn_rate * (val1 / self.data_length)

            # print()
            # print("val   c", val0)
            # print("theta c", self.theta0)
            # print("val0div", val0 / self.data_length)
            # print("learn", self.learn_rate * (val0 / self.data_length))

    def write_values(self):
        data = {"theta0": self.theta0, "theta1": self.theta1}
        with open('theta_values.json', 'w') as outfile:
            json.dump(data, outfile)

    def plot(self):
        self.x,self.y = zip(*self.data)
        plt.scatter(self.x,self.y)

        x_max = max(self.x)
        x = np.linspace(0, x_max)

        plt.plot(x, self.theta0 + (self.theta1 * x))

        plt.show()



def main():

    # estPrice = theta0 + (theata1 * dist)
    # theta0 = learnRate * 1/m * SUM(estPrice(dist) - price)
    # theta1 = learnRate * 1/m * SUM((estPrice(dist) - price)*dist)
    # error = theta0_i  -  theta0_i-1

    linear = LinearLearn()
    linear.load_data()
    linear.scale_data()
    linear.calc_theta()
    linear.write_values()
    linear.plot()

    print("numpy", np.polyfit(linear.x, linear.y, 1))
    print(linear.theta1, linear.theta0)


if __name__ == "__main__":
    main()