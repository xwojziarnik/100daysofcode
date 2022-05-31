"""Help survivors using Bayesian Theorem"""

import sys
import random
import numpy as np
import cv2 as cv
import itertools

MAP_FILE = 'cape_python.png'

# coordinates of search fields; LG stands for left upper corner, PD means right lower corner
SA1_CORNERS = (130, 265, 180, 315)  # LG X, LG Y, PD X, PD Y
SA2_CORNERS = (80, 255, 130, 305)   # LG X, LG Y, PD X, PD Y
SA3_CORNERS = (105, 205, 155, 255)  # LG X, LG Y, PD X, PD Y


class Search():
    """Bayesian game which simulates searching for survivors with three fields for searching"""

    def __init__(self, name):
        self.name = name
        self.img = cv.imread(MAP_FILE, cv.IMREAD_COLOR)
        if self.img is None:
            print("Cannot load map filel {}.".format(MAP_FILE), file=sys.stderr)
            sys.exit(1)

        self.area_actual = 0

        # coordinates of current searching
        self.sailor_actual = [0, 0]

        self.sa1 = self.img[SA1_CORNERS[1]: SA1_CORNERS[3],
                            SA1_CORNERS[0]: SA1_CORNERS[2]]

        self.sa2 = self.img[SA2_CORNERS[1]: SA2_CORNERS[3],
                            SA2_CORNERS[0]: SA2_CORNERS[2]]

        self.sa3 = self.img[SA3_CORNERS[1]: SA3_CORNERS[3],
                            SA3_CORNERS[0]: SA3_CORNERS[2]]

        self.p1 = 0.2
        self.p2 = 0.5
        self.p3 = 0.3

        self.sep1 = 0
        self.sep2 = 0
        self.sep3 = 0

    def draw_map(self, last_known):
        """
        Prints maps with scale, last known position and searching areas
        """
        # scale line
        cv.line(self.img, (20, 370), (70, 370), (0, 0, 0), 2)

        cv.putText(self.img, '0', (8,370), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))
        cv.putText(self.img, '50 nautical miles', (71,370), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))

        # first searching area, args: map reference, four corners of area, tuple with colour of rectangle, line width
        cv.rectangle(self.img, (SA1_CORNERS[0], SA1_CORNERS[1]), (SA1_CORNERS[2], SA1_CORNERS[3]), (0, 0, 0), 1)
        cv.putText(self.img, '1', (SA1_CORNERS[0] + 3, SA1_CORNERS[1] + 15), cv.FONT_HERSHEY_PLAIN, 1, 0)

        cv.rectangle(self.img, (SA2_CORNERS[0], SA2_CORNERS[1]), (SA2_CORNERS[2], SA2_CORNERS[3]), (0, 0, 0), 1)
        cv.putText(self.img, '2', (SA2_CORNERS[0] + 3, SA2_CORNERS[1] + 15), cv.FONT_HERSHEY_PLAIN, 1, 0)

        cv.rectangle(self.img, (SA3_CORNERS[0], SA3_CORNERS[1]), (SA3_CORNERS[2], SA3_CORNERS[3]), (0, 0, 0), 1)
        cv.putText(self.img, '3', (SA2_CORNERS[0] + 3, SA2_CORNERS[1] + 15), cv.FONT_HERSHEY_PLAIN, 1, 0)

        cv.putText(self.img, '+', last_known, cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))

        cv.putText(self.img, '+ = last known position', (240, 355), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
        cv.putText(self.img, '* = real position', (242, 370), cv.FONT_HERSHEY_PLAIN, 1, (255, 0, 0))

        cv.imshow('Areas for search', self.img)
        cv.moveWindow('Areas for search', 750, 10)
        cv.waitKey(500)

    def sailor_final_location(self, num_search_areas):
        """Returns x and y of survivors real position"""

        # finds position of a sailor against subarray of search area
        self.sailor_actual[0] = np.random.choice(self.sa1.shape[1], 1)
        self.sailor_actual[1] = np.random.choice(self.sa1.shape[0], 1)

        area = int(random.triangular(1, num_search_areas + 1))

        if area == 1:
            x = self.sailor_actual[0] + SA1_CORNERS[0]
            y = self.sailor_actual[1] + SA1_CORNERS[1]
            self.area_actual = 1
        elif area == 2:
            x = self.sailor_actual[0] + SA2_CORNERS[0]
            y = self.sailor_actual[1] + SA2_CORNERS[1]
            self.area_actual = 2
        elif area == 3:
            x = self.sailor_actual[0] + SA3_CORNERS[0]
            y = self.sailor_actual[1] + SA3_CORNERS[1]
            self.area_actual = 3
        return x, y

    def calc_search_effectiveness(self):
        """Returns operations effectiveness for every area"""

        self.sep1 = random.uniform(0.2, 0.9)
        self.sep2 = random.uniform(0.2, 0.9)
        self.sep3 = random.uniform(0.2, 0.9)

    def conduct_search(self, area_num, area_array, effectiveness_prob):
        """Returns effect of searching and list of checked coordinates"""
        local_y_range = range(area_array.shape[0])
        local_x_range = range(area_array.shape[1])
        coords = list(itertools.product(local_x_range, local_y_range))
        random.shuffle(coords)
        coords = coords[:int((len(coords) * effectiveness_prob))]
        loc_actual = (self.sailor_actual[0], self.sailor_actual[1])
        if area_num == self.area_actual and loc_actual in coords:
            return 'Survivor was found in area number {}.'.format(area_num), coords
        else:
            return 'Not found.', coords

    def revise_target_probs(self):
        """This func updates probability for every area on the basis of operations effectiveness"""

        denom = self.p1 * (1 - self.sep1) + self.p2 * (1 - self.sep2) + self.p3 * (1 - self.sep3)
        self.p1 = self.p1 * (1 - self.sep1) / denom
        self.p2 = self.p2 * (1 - self.sep2) / denom
        self.p3 = self.p3 * (1 - self.sep3) / denom

def draw_menu(search_num):
    """Func prints menu with selection of area to search."""
    print('\nTry nr {}'.format(search_num))
    print(
        """
        Select one of above:
        
        0 - Exit,
        1 - Search in two times first area,
        2 - Search in two times second area,
        3 - Search in two times third area,
        4 - Search in first and second area,
        5 - Search in first and third area,
        6 - Search in second and third area,
        7 - Start from the beggining
        """
    )

def main():
    app = Search('Cape_Python')
    app.draw_map(last_known=(160,290))
    sailor_x, sailor_y = app.sailor_final_location(num_search_areas=3)
    print("-" * 65)
    print("\nInitial estimation of the probability (P): ")
    print("P1 = {:.3f}, P2 = {:.3f}, P3 = {:.3f}".format(app.p1, app.p2, app.p3))
    search_num = 1

    while True:
        app.calc_search_effectiveness()
        draw_menu(search_num)
        choice = input("Choose option: ")

        if choice == "0":
            sys.exit()

        elif choice == "1":
            results_1, coords_1 = app.conduct_search(1, app.sa1, app.sep1)
            results_2, coords_2 = app.conduct_search(1, app.sa1, app.sep1)
            app.sep1 = (len(set(coords_1 + coords_2))) / (len(app.sa1)**2)
            app.sep2 = 0
            app.sep3 = 0

        elif choice == "2":
            results_1, coords_1 = app.conduct_search(3, app.sa3, app.sep3)
            results_2, coords_2 = app.conduct_search(3, app.sa3, app.sep3)
            app.sep1 = 0
            app.sep2 = (len(set(coords_1 + coords_2))) / (len(app.sa2)**2)
            app.sep3 = 0

        elif choice == "3":
            results_1, coords_1 = app.conduct_search(2, app.sa2, app.sep2)
            results_2, coords_2 = app.conduct_search(2, app.sa2, app.sep2)
            app.sep1 = 0
            app.sep2 = 0
            app.sep3 = (len(set(coords_1 + coords_2))) / (len(app.sa2)**2)

        elif choice == "4":
            results_1, coords_1 = app.conduct_search(1, app.sa1, app.sep1)
            results_2, coords_2 = app.conduct_search(2, app.sa2, app.sep2)
            app.sep3 = 0

        elif choice == "5":
            results_1, coords_1 = app.conduct_search(1, app.sa1, app.sep1)
            results_2, coords_2 = app.conduct_search(3, app.sa3, app.sep3)
            app.sep2 = 0

        elif choice == "6":
            results_1, coords_1 = app.conduct_search(2, app.sa2, app.sep2)
            results_2, coords_2 = app.conduct_search(3, app.sa3, app.sep3)
            app.sep1 = 0

        elif choice == "7":
            main()

        else:
            print("\nThis is incorrect choice.", file=sys.stderr)
            continue

        app.revise_target_probs()

        print("\nTry nr {} - result 1: {}".format(search_num, results_1), file=sys.stderr)

        print("\nTry nr {} - result 2: {}\n".format(search_num, results_2), file=sys.stderr)

        print("Effectiveness of searching (E) for try nr {}: ".format(search_num))
        print("E1 = {:.ef}, E2 = {:.3f}, E3 = {:.3f}".format(app.sep1, app.sep2, app.sep3))

        if results_1 == "Not found." and results_2 == "Not found.""":
            print("\n New estimation of the probability (P) "
                  "for try nr {}:".format(search_num + 1))
            print("P1 = {:.ef}, P2 = {:.3f}, P3 = {:.3f}".format(app.p1, app.p2, app.p3))

        else:
            cv.circle(app.img, (sailor_x[0], sailor_y[0]), 3, (255, 0, 0), -1)
            cv.imshow("Areas for search", app.img)
            cv.waitKey(1500)
            main()
        search_num += 1

if __name__ == '__main__':
    main()

