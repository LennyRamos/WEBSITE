def main():
    listOfGroceries = ["bread", "milk", "vegetable", "apples"]
    list = []
    #Python stops the accessing at the end of the array automatically 
    print(listOfGroceries[1])

    #appends to the end of the list
    listOfGroceries.append("olive oil")
    print(listOfGroceries)

    #inserts into specific part of the array index
    listOfGroceries.insert(3, "Bananas")

    