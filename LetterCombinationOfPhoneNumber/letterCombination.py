def letterCombinations(self, digits: str) -> List[str]:
        #print(digits)
        if digits == "":
            return []
        el1 = []
        el2 = []
        el3 = []
        el4 = []
        master_list = []
        combinations = [[2,"a","b","c"], [3,"d", "e", "f"], [4, "g","h", "i"], [5,"j","k","l"],[6,"m","n","o"],[7,"p","q","r","s"],[8,"t","u","v"],[9,"w","x","y","z"]]
        for x in digits:
            for y in combinations:
                if x == str(y[0]):
                    if len(el1) == 0:
                        
                        el1 = y
                        #del el1[0]
                        master_list.append(el1[1:])
                    elif len(el2) == 0:
                        
                        el2 = y
                        #del el2[0]
                        master_list.append(el2[1:])
                    elif len(el3) == 0:
                        
                        el3 = y
                        #del el3[0]
                        master_list.append(el3[1:])
                    else:
                        
                        el4 = y
                        #del el4[0]
                        master_list.append(el4[1:])
        #print(master_list)
        #output = list(itertools.product(*master_list))
        prep_combinations = list(item for item in itertools.product(*master_list))
        output = []
        for x in prep_combinations:
            output.append(''.join(x))

        #print(output)
        return output