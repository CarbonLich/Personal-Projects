from time import time

class SudokuPuzzle:
    def __init__(self, startingPuzzleString):
        from math import sqrt
        cellsListedOut = []
        for i in startingPuzzleString:
            cellsListedOut.append(int(i))
        cellLastEmpty =0
        for i in range (0, len(startingPuzzleString)):
            if cellsListedOut[i] == 0:
                cellLastEmpty = i
        puzzleSize = int(sqrt(len(startingPuzzleString)))
        cellNeighbors = {}
        cellNeighborsTemp = []
        for a in range (0, len(startingPuzzleString)):
            for b in range (0, len(startingPuzzleString)):
                if a == b:
                    continue
                if int(a/puzzleSize) == int(b/puzzleSize):
                    cellNeighborsTemp.append(b)
                    continue
                if int((a/sqrt(puzzleSize))%3) == int((b/sqrt(puzzleSize))%3) and int(a/(puzzleSize*sqrt(puzzleSize))) == int(b/(puzzleSize*sqrt(puzzleSize))):
                    cellNeighborsTemp.append(b)
                    continue
                if a%puzzleSize == b%puzzleSize:
                    cellNeighborsTemp.append(b)
                    continue
            cellNeighbors[a] = cellNeighborsTemp.copy()
            cellNeighborsTemp.clear()

        self.cellNeighbors = cellNeighbors
        self.puzzleSize = puzzleSize
        self.cellLastEmpty = cellLastEmpty
        self.cellsListedOut = cellsListedOut
        self.startingPuzzleString = startingPuzzleString
        
    def checkCellVal(self, cell, val, tempList):
        for i in self.cellNeighbors[cell]:
            if tempList[i] == val:
                return False
        return True

    def checkPuzzleErrorDisplay(self):
        puzzleErrorDisplayTemp = []
        for i in range (0, self.puzzleSize):
            for j in range (0, self.puzzleSize):
                if self.cellsListedOut[j+int(i*self.size)] == 0:
                    puzzleErrorDisplayTemp.append("-")
                    continue
                if self.checkCellVal(j+int(i*self.size), self.cellsListedOut[j+int(i*self.size)], self.cellsListedOut):
                    puzzleErrorDisplayTemp.append("C")
                    continue
            puzzleErrorDisplayTemp.append("W")
            print(puzzleErrorDisplayTemp)
            puzzleErrorDisplayTemp.clear()

    def solvePuzzlePiecewise(self, cell:int, val:int, tempList:list, tempLastCell:int, tempPuzzleSize:int):
        if tempList[cell] != 0:
            self.solvePuzzlePiecewise(cell+1, 1, tempList, tempLastCell, tempPuzzleSize)
            return
        if not self.checkCellVal(cell, val, tempList):
            if val == tempPuzzleSize:
                return
            self.solvePuzzlePiecewise(cell, val+1, tempList, tempLastCell, tempPuzzleSize)
            return
        tempList[cell] = val
        if tempList[tempLastCell] != 0:
            return
        self.solvePuzzlePiecewise(cell+1, 1, tempList, tempLastCell, tempPuzzleSize)
        if tempList[tempLastCell] != 0:
            return
        tempList[cell] = 0
        if val == tempPuzzleSize:
            return
        self.solvePuzzlePiecewise(cell, val+1, tempList, tempLastCell, tempPuzzleSize)
    
    def solvePuzzleEasy(self, tempList):
        cellSolNum = 0
        secondVal = 0
        for c in range (0,self.puzzleSize*self.puzzleSize):
            if tempList[c]!=0:
                continue
            for v in range (0,self.puzzleSize):
                if self.checkCellVal(c,v,tempList):
                    cellSolNum+=1
                    secondVal = v
            if cellSolNum > 1:
                cellSolNum = 0
                continue
            tempList[c] = secondVal
        self.solvePuzzleEasy(tempList)
    
    def solvePuzzle(self):
        tempCellsListedOut = self.cellsListedOut.copy()
        tempPuzzleSize = self.puzzleSize
        tempCellLastEmpty = self.cellLastEmpty
        self.solvePuzzlePiecewise(0, 1, tempCellsListedOut, tempCellLastEmpty, tempPuzzleSize)
        return tempCellsListedOut
    
fred = time()
puzzleInput = "000801000000000430500000000000070800000000100020030000600000075003400000000200600"

testPuzzle = SudokuPuzzle(puzzleInput)
bob = testPuzzle.solvePuzzle()
print (time()-fred)
print(bob)