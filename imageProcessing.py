from __future__ import division
import numpy as np
import pandas as pd
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_slope(pointA, pointB):
    dy = float(pointA.y) - float(pointB.y)
    dx = float(pointA.x) - float(pointB.x)
    slope = dy / dx
    return slope


def find_correction_angle(binary_image):

    # Read the CSV-file
    A = pd.read_csv(binary_image)
    rows = A.shape[0]
    columns = A.shape[1]
    A = np.array(A)
    A = A.flatten().reshape([rows, columns]).transpose()

    ## Getting the co-ordinates of the inner rectangle
    # Get the top-most corner for the x-axis
    iTopCorner = 0
    jTopCorner = 0
    singleTopRow = []
    for i, row in enumerate(A):
        if list(row).count(1) == 1:
            jTopCorner = i
            singleTopRow.append(row)

    for j, col in enumerate(singleTopRow[0]):
        if col == 1:
            iTopCorner = j

    # print('Top-most corner co-ordinates')
    # print('(x =', iTopCorner, ', y =', jTopCorner, ')')

    # Get the right-most corner from the y-axis
    iRightCorner = 0
    jRightCorner = 0
    singleRightRow = []

    for i, row in enumerate(A.transpose()):
        if list(row).count(1) == 1:
            iRightCorner = i
            singleRightRow.append(row)

    for j, col in enumerate(singleRightRow[0]):
        if col == 1:
            jRightCorner = j

    # print('Right-most corner co-ordinates')
    # print('(x =', iRightCorner, ', y =', jRightCorner, ')')

    # slope of inner rectangle line
    p1 = Point(iTopCorner, jTopCorner)
    p2 = Point(iRightCorner, jRightCorner)

    m1 = get_slope(p1, p2)


    # slope of outer rectangle line
    p3 = Point(0, 0)
    p4 = Point(iTopCorner, 0)

    m2 = get_slope(p3, p4)

    tanTheta = (m2 - m1) / (1 + (m1 * m2))

    rotated_angle = math.degrees(math.atan(tanTheta))

    # # Validate rotation angle for x-axis
    # distInner = math.hypot(iTopCorner - iRightCorner, jTopCorner - jRightCorner)
    # distOuter = math.hypot(iTopCorner - 0, 0)
    #
    # if distInner > distOuter:
    #     return -1 * (180 - (90 + int("%d" % round(rotated_angle, 0))))
    # else:
    #     return "%d" % round(rotated_angle, 0)

    return int("%d" % round(rotated_angle, 0))


input_file = "F:/Spring 2018/Internship/Quantumscape/rotated.csv"

print(find_correction_angle(input_file))
