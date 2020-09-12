"""
(2) Write a generic function to compute various scenarios for the following optimization problem:
A farmer owns X acres of land.
She profits P1 dollars per acre of corn and P2 dollars per acre of oats.
Her team has Y hours of labor available.
The corn takes H1 hours of labor per acre and oats require H2 hours of labor per acre.
How many acres of each can be planted to maximize profits?

Test the function for the following cases:

a) X = 240, Y = 320, P1 = $40, P2 = $30, H1 = 2, H2 = 1

b) X = 300, Y = 380, P1 = $70, P2 = $45, H1 = 3, H2 = 1

c) X = 180, Y = 420, P1 = $65, P2 = $55, H1 = 3, H2 = 2
"""
import math


# I'm sure there's a mathematical way to solve this problem, but I couldn't figure it out
class FarmerProfitMaximization():
    def __init__(self, X: int, Y: int, P1: int, P2: int, H1: int, H2: int):
        self.total_acres_of_land = X
        self.total_labor_hours = Y
        self.profit_acre_corn = P1
        self.profit_acre_oats = P2
        self.labor_per_acre_corn = H1
        self.labor_per_acre_oats = H2

        self.acres_used_oats = 0
        self.acres_used_corn = 0

    def determine_profit(self, profit_crop_one, acres_used_crop_one, profit_crop_two, acres_used_crop_two) -> int:
        return profit_crop_one * acres_used_crop_one + profit_crop_two * acres_used_crop_two

    def farmer_profit_maximization(self):
        if self.labor_per_acre_oats == self.labor_per_acre_corn:
            if self.profit_acre_oats > self.profit_acre_corn:
                self.acres_used_oats = min(self.total_acres_of_land, self.total_labor_hours / self.labor_per_acre_oats)
            else:
                self.acres_used_corn = min(self.total_acres_of_land, self.total_labor_hours / self.labor_per_acre_corn)
        elif self.labor_per_acre_oats > self.labor_per_acre_corn:
            self.acres_used_oats, self.acres_used_corn = self.calculate_max_profit(
                larger_labor_per_acre=self.labor_per_acre_oats,
                lesser_labor_per_acre=self.labor_per_acre_corn,
                profit_per_acre_larger_labor=self.profit_acre_oats,
                profit_per_acre_lesser_labor=self.profit_acre_corn)
        else:
            self.acres_used_corn, self.acres_used_oats = self.calculate_max_profit(
                larger_labor_per_acre=self.labor_per_acre_corn,
                lesser_labor_per_acre=self.labor_per_acre_oats,
                profit_per_acre_larger_labor=self.profit_acre_corn,
                profit_per_acre_lesser_labor=self.profit_acre_oats)

        print(f"Acres for corn: {self.acres_used_corn}; Acres for oats: {self.acres_used_oats}")

    def calculate_max_profit(self, larger_labor_per_acre, lesser_labor_per_acre, profit_per_acre_larger_labor, profit_per_acre_lesser_labor):
        acres_used_larger_labor = min(self.total_acres_of_land, math.floor(self.total_labor_hours / larger_labor_per_acre))
        larger_labor_used = acres_used_larger_labor * larger_labor_per_acre
        acres_used_lesser_labor = 0
        acres_available = self.total_acres_of_land - acres_used_larger_labor
        labor_available = self.total_labor_hours - larger_labor_used
        profit = self.determine_profit(profit_per_acre_larger_labor, acres_used_larger_labor,
                                       profit_per_acre_lesser_labor, acres_used_lesser_labor)
        potential_profit = profit
        while potential_profit >= profit and acres_used_larger_labor > 0:
            acres_used_larger_labor -= 1
            larger_labor_used -= larger_labor_per_acre
            acres_available += 1
            labor_available += larger_labor_per_acre
            acres_used_lesser_labor = min(acres_available, labor_available / lesser_labor_per_acre)
            potential_profit = self.determine_profit(profit_per_acre_larger_labor, acres_used_larger_labor,
                                                     profit_per_acre_lesser_labor, acres_used_lesser_labor)
            if potential_profit > profit:
                profit = potential_profit
            else:
                acres_used_larger_labor += 1
                larger_labor_used += larger_labor_per_acre
                acres_available -= 1
                labor_available -= larger_labor_per_acre
                acres_used_lesser_labor = min(acres_available, labor_available / lesser_labor_per_acre)

        return acres_used_larger_labor, acres_used_lesser_labor


if __name__ == '__main__':
    FarmerProfitMaximization(X=240, Y=320, P1=40, P2=30, H1=2, H2=1).farmer_profit_maximization()
    FarmerProfitMaximization(X=300, Y=380, P1=70, P2=45, H1=3, H2=1).farmer_profit_maximization()
    FarmerProfitMaximization(X=180, Y=420, P1=65, P2=55, H1=3, H2=2).farmer_profit_maximization()
