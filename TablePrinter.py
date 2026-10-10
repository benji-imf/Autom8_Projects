def printTable(tableData):
    colWidths = [0] * len(tableData)

    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if len(tableData[i][j]) > colWidths[i]:
                colWidths[i] = len(tableData[i][j])

    
    for row in range(len(tableData[0])):
        for col in range(len(tableData)):
            print(tableData[col][row].rjust(colWidths[col]), end=' ')
        print()


tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

printTable(tableData)