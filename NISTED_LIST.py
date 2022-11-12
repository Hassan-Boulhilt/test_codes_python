if __name__ == '__main__':
    names_scores=[]
    scores = []
    second_score=[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())        
        names_scores.append([name,score])
    
    
    
    for i in names_scores:
        for j in i:            
            if type(j)== float and  j not in scores:
                scores.append(j)
    scores.sort()
    second_score=[nm_sc[0] for nm_sc in names_scores if nm_sc[1] == scores[1]]
    second_score.sort()
    for i in second_score:
        print(i)
    
    
        
               
       
        
        
            
   
               
        
        
        
            
    
