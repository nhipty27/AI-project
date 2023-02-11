import os
class resolution:
    clauseKB: list
    alpha: list
    result: list

    def __init__(self) -> None:
        self.alpha = []
        self.clauseKB=[]
        self.result = []
        

    def compactLiteral(self, clause)-> list:
        res = []
        for literal in clause:
            if literal.strip() not in res :
                res.append(literal.strip())
        return res
    
    def resultLiteral(self, clause)-> list:
        clause = self.compactLiteral(clause)
        res = []
        for literal in clause:
            if self.invertLiteral(literal.strip()) not in res :
                res.append(literal.strip())
        return res

    def compactKB(self)-> None:
        res = []
        for kb in self.clauseKB:
            if kb not in res:
                res.append(kb)
        self.clauseKB = res

    def splitClause(self, clause)-> list:
        listLiteral = clause.split('OR')
        listLiteral = self.compactLiteral(listLiteral)
        return listLiteral

    def invertLiteral(self, literal)-> list:
        if '-' in literal:
            return literal[1]
        return '-' + literal

    def negateClause(self, clause)-> list:
        listLiteral = clause.split('OR')
        listLiteral = self.compactLiteral(listLiteral)

        res = []
        for literal in listLiteral:
            literal = literal.strip()
            if(len(literal) == 2):
                res.append(literal[1])
            elif len(literal) == 1:
                res.append('-'+ literal)
        return res

    def initSolution(self, fileName) ->bool:
        path = os.path.join(os.path.dirname(__file__),r'INPUT/'+fileName)
        with open(path, 'r') as f:
            try:
                self.alpha = f.readline().strip()
                numberOfKB = int(f.readline())
                self.clauseKB = []

                for i in range(numberOfKB):
                    self.clauseKB.append(f.readline().strip())
                listLiteral = self.negateClause(self.alpha)
                for literal in listLiteral:
                    self.clauseKB.append(literal)
                return True
            except:
                return False
    
    def outputSolution(self, fileName)->None:
        path = os.path.join(os.path.dirname(__file__),r'OUTPUT/'+fileName)
        pl_resolution = self.PL_RESOLUTION()
        with open(path, 'w') as f:
            for step in self.result:
                f.write(f"{len(step)}\n")
                for clause in step:
                    f.write(f"{clause}\n")
            f.write("YES" if pl_resolution else "NO")
            
    def sortClause(self, clause) -> list:
        literals = self.splitClause(clause)
        literals = sorted(literals, key = lambda x: x[-1])
        res= ""
        for i in range(len(literals)):
            if i== len(literals)-1:
                res +=  literals[i]
            else: 
                res += literals[i] + ' OR ' 
        return res

    def sortLiterals(self, literals) -> list:
        literals = self.compactLiteral(literals)
        literals = sorted(literals, key = lambda x: x[-1])
        return literals
    
    def checkClause(self, clause1, clause2) -> bool:
        literals1 = self.splitClause(clause1)
        literals2 = self.splitClause(clause2)
        for i in literals1:
            for j in literals2:
                if self.invertLiteral(i) == j:
                    return True
        return False

    def solveClause(self, clause1, clause2)-> list:
        clause1 = self.splitClause(clause1)
        clause2 = self.splitClause(clause2)
        res = []

        for i in range(len(clause1)):
            for j in range(len(clause2)):
                if self.invertLiteral(clause1[i]) == clause2[j]:
                    resolve = clause1[:i]  + clause1[i + 1:] + clause2[:j] + clause2[j + 1:]
                    resolve = self.compactLiteral(resolve)
                    resClauses = ''
                    for k in range(len(resolve)):
                        if k== len(resolve)-1:
                            resClauses +=  resolve[k]
                        else: 
                            resClauses += resolve[k] + ' OR '
                    if(resClauses == ''):
                        res.append('')
                    else :
                        res.append(self.sortClause(resClauses))

        return res

    def checkValid(self, clause) -> bool:
        clause = self.splitClause(clause)
        for i in range(len(clause) - 1):
            for j in range(i + 1, len(clause)):
                if (self.invertLiteral(clause[i]) == clause[j]):
                    return True
        return False


    def PL_RESOLUTION(self)-> bool:
        detailStep = []
        check = False
        while True:
            self.result.append([])
            detailStep.append([])
            new_clauses = []
            new_steps = []
            n = len(self.clauseKB)
            for i in range(n):
                for j in range(i+1, n):
                    resultClauses = self.solveClause(self.clauseKB[i], self.clauseKB[j])

                    if '' in resultClauses:
                        new_clauses.append({})
                        new_steps.append((self.clauseKB[i], self.clauseKB[j]))
                        check = True
                        continue
                    for r in resultClauses:
                        if self.checkValid(r):
                            continue
                        if r not in self.clauseKB and r not in self.result:
                            new_clauses.append(r)
                            new_steps.append((self.clauseKB[i], self.clauseKB[j]))
                
            if len(new_clauses) == 0:
                return False
            
            for i in range(len(new_clauses)):
                if new_clauses[i] not in self.clauseKB: 
                    self.clauseKB.append(new_clauses[i])

                if new_clauses[i] not in self.result[-1]: 
                    self.result[-1].append(new_clauses[i])
                    detailStep[-1].append(new_steps[i])
            if check:
                return True


