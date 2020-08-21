#------------------ Баннер -----------------#

# Функция баннера.
def banner(): 
	print('''
          Калькулятор
████████████████████████████████
████░░██░░░░██░░████████████████
██░░██░░████░░██░░██████████████
░░██░░██░░░░██░░██░░████████████
░░██░░████░░██░░██░░░░██████████
██░░░░░░░░██░░░░░░░░██░░████████
██████░░██░░████░░██░░██░░██████
████░░██░░░░██████░░░░██░░██████
████░░████████████████░░████████
██████░░██░░░░░░░░░░██░░████████
████████░░░░██████░░░░██████████
██░░░░████░░░░░░░░░░████████████
██░░██░░████████████████████████
██░░░░██████░░████░░░░░░████████
██░░██░░██░░██░░████░░██████████
██░░░░██████░░██████░░██████████
#------------------------------#''')

#------------- Калькулятор -----------------#

# Операторы:
OP = {
    '+': (1, lambda x, y: x + y),
    '-': (1, lambda x, y: x - y),
    '*': (2, lambda x, y: x * y),
    '/': (2, lambda x, y: x / y)
    } 

# Функция. Ждет пример.
def func(example):

    # Вызываем функцию, если юзверь вводит не целые числа.
    def user(a): 
        while a < 100:                          
            print('Юзверь, используй целые числа! ЦЕЛЫЕ ЧИСЛА! Ответ ниже неверный!')     
            a += 1                              
            if a == 100:                        
                print('Надеюсь, понятно.')      
                print('')                       
                print('Ответ ниже - неверный!') 
                break                           
            
    # Вызываем функцию. Парсинг.
    def parse(example_string): 
        a = ''                          
        for s in example_string:        
            if s in '1234567890':       
                a += s                  
            elif s in '.':              
                user(0)                 # Вызываем функцию user(). 0 вписываем, чтобы занять переменную a. Юзверь написал не целое число!
            elif a:                     
                yield float(a)          
                a = ''                  
            if s in OP or s in "()":    
                yield s                 
        if a:                          
            yield float(a)              
            
    # Вызываем функцию. Парсим пример (Последний в скобочках).
    def parsed_example_(parsed_example):
        stack = []                      
        for s1 in parsed_example:       
            if s1 in OP:                
                while stack and stack[-1] != "(" and OP[s1][0] <= OP[stack[-1]][0]: 
                    yield stack.pop()   
                stack.append(s1)        
            elif s1 == ")":             
                while stack:            
                    x = stack.pop()    
                    if x == "(":        
                        break           
                    yield x             
            elif s1 == "(":             
                stack.append(s1)        
            else:                       
                yield s1                
        while stack:                    
            yield stack.pop()          

   
    def calc(RevPolNot):     
        stack = []                           
        for s1 in RevPolNot:                       
            if s1 in OP:                            
                y, x = stack.pop(), stack.pop()     
                stack.append(OP[s1][1](x, y))     
            else:                                  
                stack.append(s1)                
        
        return stack[0]                             
    return calc(parsed_example_(parse(example)))   
    
def main():
    banner();                               
    print('Введите пример!')                
    example = input('> ').replace(' ', '')  
    #example = '10+(3/3)+(3*(3*3))'         # Временно. Создает пример. ОТВЕТ: 38
    print('|%|', example, '=', func(example), '|%|')  
    
main() # Запуск программы.