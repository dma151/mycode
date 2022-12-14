#!/usr/bin/env python3

import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def main():
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Crit', 'Specialization', 'Endurance', 'Expertise', 'Domination', 'Swiftness'
    sizes = [65, 10, 0, 0, 0, 25]
    explode = (0.05, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title("Attribute for Sharpshooter")

    plt.savefig("/home/student/static/pie.png")



if __name__ == "__main__":
    main()
