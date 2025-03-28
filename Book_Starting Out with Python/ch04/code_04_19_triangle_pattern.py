# code_04_19_triangle_pattern.py
# This program displays a triangle pattern. 
BASE_SIZE = 8
for r in range(BASE_SIZE): 
    for c in range(r + 1):
        print('*', end='') 
    print()