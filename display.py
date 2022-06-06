def display_hangman(tries):
    stages = [
        '''
        *   _______
|         |     
O         |     
\|/       |    
|         |     
/ \        |  
       |  ПИНПЕЦ!

        ''',
        '''
        *   _______
|         |     
O        |     
\|/       |    
|         |     
/          |    
        |  
        ''',
        '''
        *   _______
|        |     
О       |     
\|/      |    
|        |    
        |    
        |  
        ''',
        '''
        *   _______
|        |     
O       |     
\|        |    
|        |    
        |    
        |  
        ''',
        '''
        *   _______
|        |     
O       |     
|        |     
|        |     
        |     
        |  
        ''',
        '''
        *   _______
|        |     
О       |     
        |    
        |     
        |    
        |  
        ''',
        '''
        *   _______
|         |     
         |     
         |    
         |       
         |  
        '''
    ]
    return stages[tries]

