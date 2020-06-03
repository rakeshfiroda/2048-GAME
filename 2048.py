import numpy as np
import random as rd

output = np.zeros([4,4])
position = np.zeros([4,4])
elements = [2,4,8,16]
p1 = rd.randint(0,3)
p2 = rd.randint(0,3)
output[p1][p2] = elements[rd.randint(0,3)]
position[p1][p2] = 1

def add_element():
    status = 0
    for i in range(0,4):
        for j in range(0,4):
            if position[i][j] == 0:
                status = 1
                break
    if status == 1:
        while status:
            x,y = rd.randint(0,3),rd.randint(0,3)
            status = position[x][y]
        output[x][y] = elements[rd.randint(0,3)]
    else:
        print("Game Over! No space available...")
  
def add_element():
    status = 1
    
    while status:
        x,y = rd.randint(0,3),rd.randint(0,3)
        status = position[x][y]
    output[x][y] = elements[rd.randint(0,3)]
    position[x][y] = 1
    
    
def operation_a(score):
    for i in range(0,4):
        for j in range(1,4):
            for k in range(j,0,-1):
                if position[i][k] == 1:
                    if position[i][k-1] == 0:
                        output[i][k-1] = output[i][k]
                        output[i][k] = 0
                        position[i][k-1] = 1
                        position[i][k] = 0
                    elif output[i][k-1] == output[i][k]:
                        output[i][k-1] = output[i][k-1]*2
                        output[i][k] = 0
                        position[i][k] = 0
                        score = score + output[i][k-1]
    add_element()
    return score

def operation_d(score):
    for i in range(0,4):
        for j in range(2,-1,-1):
            for k in range(j,3):
                if position[i][k] == 1:
                    if position[i][k+1] == 0:
                        output[i][k+1] = output[i][k]
                        output[i][k] = 0
                        position[i][k+1] = 1
                        position[i][k] = 0
                    elif output[i][k+1] == output[i][k]:
                        output[i][k+1] = output[i][k+1]*2
                        output[i][k] = 0
                        position[i][k] = 0
                        score = score + output[i][k+1]
    add_element()
    return score

def operation_w(score):
    for i in range(0,4):
        for j in range(1,4):
            for k in range(j,0,-1):
                if position[k][i] == 1:
                    if position[k-1][i] == 0:
                        output[k-1][i] = output[k][i]
                        output[k][i] = 0
                        position[k-1][i] = 1
                        position[k][i] = 0
                    elif output[k-1][i] == output[k][i]:
                        output[k-1][i] = output[k-1][i]*2
                        output[k][i] = 0
                        position[k][i] = 0
                        score = score + output[k-1][i]
    add_element()
    return score

def operation_s(score):
    for i in range(0,4):
        for j in range(2,-1,-1):
            for k in range(j,3):
                if position[k][i] == 1:
                    if position[k+1][i] == 0:
                        output[k+1][i] = output[k][i]
                        output[k][i] = 0
                        position[k+1][i] = 1
                        position[k][i] = 0
                    elif output[k+1][i] == output[k][i]:
                        output[k+1][i] = output[k+1][i]*2
                        output[k][i] = 0
                        position[k][i] = 0
                        score = score + output[k+1][i]
    add_element()
    return score

print("*DOCUMENTATION*")
print("Use W,A,S,D to Move and E to exit()")
add_element()
score = 0
user = 1
while user!= 'E':
    print("Your Score:",int(score))
    print(output)
    user = input("Enter Operation: ").upper()
    if user == 'W':
        score = operation_w(score)
    elif user == 'A':
        score = operation_a(score)
    elif user == 'S':
        score = operation_s(score)
    elif user == 'D':
        score = operation_d(score)
        
    if score >= 2048:
        break
        
        
if score>= 2048:
    print("Congrats! You finished it.")
else:
    print("ThankYou! Its yours, You can try again!")
    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




