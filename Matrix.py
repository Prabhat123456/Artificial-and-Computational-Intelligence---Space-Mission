#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 14:55:38 2021

@author: p0g02rj
"""
import sys
from collections import deque




# To Store th input from the users

class UserInput:
    def __init__(self):
        self.oxygentLevel = int(input("Enter the oxygen level O:"))
        self.noOfRows = int(input("Enter the number of rows M:"))
        self.noOfColumns = int(input("Enter the number of columns N:"))

# To store matrix cell coordinates
class Point:
    def __init__(self,x: int, y: int):
        self.x = x
        self.y = y

# A data structure for queue used in BFS
class queueNode:
    def __init__(self,pt: Point, dist: int):
        self.pt = pt  # The coordinates of the cell
        self.dist = dist  # Cell's distance from the source

class sourceAndTargetInfo:
     def __init__(self, dest: Point, source: Point):
        self.dest = dest  # The coordinates of the cell
        self.source = source  # Cell's distance from the source

# Check whether given cell(row,col)
# is a valid cell or not
def isValid(row: int, col: int, userInputObj:UserInput):
    return (row >= 0) and (row < userInputObj.noOfRows) and (col >= 0) and (col < userInputObj.noOfColumns)

rowNum = [-1, 0, 1, -1, -1, 1, 0, 1]
colNum = [0, -1, 1, -1, 1, -1, 1, 0]
# Function to find the shortest path between
# a given source cell to a destination cell.
# Will post implementation of this method on Monday 02/08/2021 as there is a live assesment going on.
def BFS(mat, src: Point, dest: Point, userInputObj:UserInput):

   

    # Return -1 if destination cannot be reached
    return -1

#This method is used to get the info for source and target and also to show the the user the input martrix they have entered.
def showInputMatrixToUser(matrix,userInputObj: UserInput):
# For printing the matrix
    print("********* Your Input is **********")
    noOfTargetInputByUser = 0
    noOfSourceInputByUser = 0
    source = Point(0,0)
    dest = Point(0,0)
    sourceAndTargetInfoObj = sourceAndTargetInfo(dest, source)


    for i in range(userInputObj.noOfRows):
        for j in range(userInputObj.noOfColumns):
            if matrix[i][j].capitalize() == 'T':
                noOfTargetInputByUser = noOfTargetInputByUser + 1
                sourceAndTargetInfoObj.dest = Point(i,j)
                if noOfTargetInputByUser > 1 :
                    print("There cannot be more than one target. Terminating the program kindly input the valid input with one source and one target destination")
                    sys.exit()
            if matrix[i][j].capitalize() == 'S':
                noOfSourceInputByUser = noOfSourceInputByUser + 1
                sourceAndTargetInfoObj.source = Point(i,j)
                if noOfSourceInputByUser > 1 :
                    print("There cannot be more than one source. Terminating the program kindly input the valid input with one source and one target destination")
                    sys.exit()
            print(matrix[i][j], end = " ")
        print()
    return sourceAndTargetInfoObj


# Initialize matrix
#This method is used to Initialize matrix and this is the starting point of our program we take input matrix from the user and pass into the function showInputMatrixToUser to fetch the source and destination from the matrix post fetching source and target we are passing these as input to BFS method to find out the distance of optimal path if there is a path if not it will return -1 .
def inputMatrix(matrix,userInputObj: UserInput):
    print("Enter the entries rowwise only from T, #, S, .")
    validInput = ['T', '#', 'S', '.']
# For user input
    for i in range(userInputObj.noOfRows):          # A for loop for row entries
        grid =[]
        userInput = input()
        if userInput:
            if len(userInput) == userInputObj.noOfColumns:
                for j in range(userInputObj.noOfColumns):
                     if userInput[j].capitalize() in validInput:
                         grid.append(userInput[j])
                     else :
                          print("Input is not valid. Enter the entries rowwise only from T, #, S, . Exiting the program try to run again with valid input")
                          sys.exit()
                matrix.append(grid)
            else :
                print("Input is not valid. Exiting the program try to run again with valid input")
                sys.exit()
        else:
            print("Input cannot be empty. Exiting the program try to run again without empty input")
            sys.exit()



    sourceAndTargetInfoObj = showInputMatrixToUser(matrix,userInputObj)
    dist = BFS(matrix,sourceAndTargetInfoObj.source,sourceAndTargetInfoObj.dest,userInputObj)
    if dist == -1:
        print("Impossible. There is no path")
    else:
        if userInputObj.oxygentLevel >= dist :
            print("Possible")
        else :
            print("Impossible")

userInput = UserInput()
matrix = []
inputMatrix(matrix,userInput)
