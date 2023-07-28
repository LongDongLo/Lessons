# Function for printing 2D arrays in grid format
def gridPrint(x, y):
    for i in range(x):  # Index on the row
        for j in range(x):  # Index on the column
            print(y[i][j], end=" ")
        print()


# Function for rotating grids
def rotateGrid(x, y):
    rotatedGrid = []  # Initializing the new 2D array
    for i in range(x):
        appList = []  # Initializing a list used to append
        count = x - 1
        for j in range(x):
            appList.append(y[count][i])  # Turning each column to a new row
            count = count - 1
        rotatedGrid.append(appList)  # Appending the new rows into the 2D array
    return rotatedGrid  # Returning the rotated grid


# Main Function
def main():
    # User inputs
    inputGrid = []
    N = int(input())  # Value of N
    for i in range(N):
        appList = []
        for j in range(N):
            appValue = int(input())  # Input numbers
            appList.append(appValue)  # Adding the numbers to a list to be appended
        inputGrid.append(appList)  # Appending the lists

    if inputGrid[0][0] < inputGrid[N - 1][0] and inputGrid[0][0] < inputGrid[0][N - 1]:
        gridPrint(N, inputGrid)  # Printing out the grid if already in the correct position
    else:
        rotatedGrid = rotateGrid(N, inputGrid)  # Rotating the original grid
        while rotatedGrid[0][0] > inputGrid[N-1][0] or rotatedGrid[0][0] > inputGrid[0][N-1]:
            rotatedGrid = rotateGrid(N, rotatedGrid)  # Continuously rotating until correct position is reached
        gridPrint(N, rotatedGrid)  # Printing out the grid


# Executing the main function
if __name__ == "__main__":
    main()
