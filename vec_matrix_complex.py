import numpy as np

def len_vec(v1,v2):
    if len(v1)==len(v2):
        return True
    return False

def sum_vec_complex(vec1,vec2):
    if len_vec(vec1,vec2) == True:
        return np.add(vec1,vec2)
    else:
        raise Exception ("Error: Los vectores no son del mismo tamaño")

def inv_vec_complex(vec1):
    return np.negative(vec1)

def mult_esc_vec(num, vec1):
    return np.multiply(num,vec1)

def len_matrix(matrix1,matrix2):
    if len(matrix1) == len(matrix2):
        for i in range (len(matrix1)):
            if len(matrix1[i])==len(matrix2[i]):
                return True
            return False
    return False

def sum_matrix(matrix1,matrix2):
    if len_matrix(matrix1,matrix2) == True:
        return np.add(matrix1,matrix2)
    else:
        raise Exception("Error: Las matrices no cumplen con las condiciones para su suma")

def inv_matrix(matrix1):
    return np.negative(matrix1)

def mult_esca_matrix(num, matrix1):
    return np.multiply(num,matrix1)

def trans_matrix(matrix1):
    return np.transpose(matrix1)

def conj_matrix(matrix1):
    return np.conjugate(matrix1)

def adj_matrix(matrix1):
    result = np.conjugate(matrix1)
    mat_result = np.transpose(result)
    return mat_result

def act_matrix_vec(matrix1, vec1):
    return np.dot(matrix1,vec1)

def len_col_row(matrix1,matrix2):
    if len(matrix1[0])== len(matrix2):
        return True
    return False

def mult_matrix(matrix1,matrix2):
    if len_col_row(matrix1, matrix2) == True:
        return np.dot(matrix1,matrix2)
    else:
        raise Exception ("Error: El numero de columnas de la matriz 1 no es igual al numero de columnas de la matriz 2")
"""
v1 = [complex(3.5,2.35), complex(1.78,-8.25)]
v2 = [complex(-1.8,2.5), complex(2.78,3.2)]
v3 = [complex(-3,-2.1),complex(1.5,-8.0)]

print("                Suma de dos vectore             ")
print(sum_vec_complex(v2,v3))
print("                Inversa de un vector                      ")
print(inv_vec_complex(v1))
print("        Multiplicacion por un escalar con un vector                     ")
print(mult_esc_vec(2,v1))

m1 = [[complex(3.5, 2.8), complex(1.5, -8.2)], [complex(1.5, 2.8), complex(2.7, 3.25)]]
m2 = [[complex(-1.25, 5.15), complex(1.2, 3.70)], [complex(1.2, 2.78), complex(1.7, -1.78)]]
m3 = [[complex(8.7, 2.1), complex(1.1, -8.2)], [complex(1.7, -5.5), complex(-2, -3)]]

print("                Suma de matrices                        ")
print(sum_matrix(m1,m2))
print("              Inversa de una matriz                ")
print(inv_matrix(m1))
print("            Multiplicacion de un escalar con una matriz                 ")
print(mult_esc_vec(2,m1))
print("               Transpuesta de matriz              ")
print(trans_matrix(m1))
print("                 Conjungada de una matriz            ")
print(conj_matrix(m1))
print("               Adjunta de una matriz              ")
print(adj_matrix(m1))
print("                 Multiplicar dos matrices            ")
result =mult_matrix(m1,m2)
print(result)
print("          Accion de una matriz sobre un vector                   ")
print(act_matrix_vec(m1,v1))"""