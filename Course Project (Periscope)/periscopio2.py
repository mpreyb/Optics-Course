"""-------------------------CODIGO 1------------------------------"""
#codigo rellenando
import numpy as np
import math 
from PIL import Image

#Ray tracing function
def ray_tracing(width, height, rayo, so1, n1, si1, sL, obj, pixels):
    
    #Potencia de la superficie
    D1 = (nl - 1)/R1      # potencia del lente 1
    D2 = (nl - 1)/(-R2)

    D3 = (nl - 1)/R3        # potencia del lente 2
    D4 = (nl - 1)/(-R4)

    #Matriz dela lente
    a1 = (1 - (D2*dl)/nl)
    a2 = -D1-D2+(D1*D2*dl/nl)
    a3 = dl/nl
    a4 = (1 - (D1*dl)/nl)
    #a4=1 ?
    A = np.array([[a1,a2],[a3,a4]]) #matriz del lente 1

    #Propagaciones despues,antes y entre los lentes
    # PROFE: P2 = np.array([[1,0],[si/n2,1]])
    # P1 = np.array([[1,0],[-so/n1,1]])

    # ANDRES: P2 = np.array([[1,0],[si1/n5,1]])#despues
    # P1 = np.array([[1,0],[so1/n5,1]])#antes
    # P3 = np.array([[1,0],[sL/n5,1]]) #entre


     for i in range(width):
        for j in range(height):

            #Get pixel value
             pos_x = i
            pos_y = j
            pixel = obj.getpixel((pos_x, pos_y))
            
            x = pos_x - width/2
            y = pos_y - height/2

            #we must measure the distance from the particular pixel to the center of the object (in pixels)
            #each pixel equals 1 mm
            r = math.sqrt( x*x + y*y ) + 1 #Corrección de redondeo / distancia Euclidiana

            #Vector rayo de entrada (punto en el objeto)
            y_objeto = r*0.0001                                 #each pixel equals 0.1 mm
            if rayo == 0:                                       #principal
                alpha_entrada = math.atan(y_objeto/so)          #Entra en dirección del centro de la lente
            elif rayo == 1:                                     #paralelo
                alpha_entrada = 0                               #Entra paralelo al eje del sistemna óptico
            V_entrada = np.array([n1*alpha_entrada,y_objeto])

            #Cálculo del vector del rayo de salida
            #ANDRES: V_salida = P2.dot(A1.dot(P3.dot(A.dot(P1.dot(V_entrada)))))
            #PROFE:  V_salida = P2.dot(A.dot(P1.dot(V_entrada)))

            #Transversal magnification
            y_imagen = V_salida[1]
            if rayo == 0:                     #principal
                Mt = (-1)*y_imagen/y_objeto   #atan correction
            elif rayo == 1:                   #paralelo
                Mt = y_imagen/y_objeto 
                
            #Conversion from image coordinates to lens coordinates        
            x_prime = Mt*x
            y_prime = Mt*y
            
            pos_x_prime = int(x_prime + width_output/2)
            pos_y_prime = int(y_prime + height_output/2)
            
            if  pos_x_prime < 0 or pos_x_prime >= width_output:
            	continue
            	
            if  pos_y_prime < 0 or pos_y_prime >= height_output:
            	continue
                     
            if rayo == 0: #principal   
                pixels[pos_x_prime, pos_y_prime] = (int(pixel), int(pixel), int(pixel))
            elif rayo == 1: #paralelo    
                new_gray = (int(pixel) + pixels[pos_x_prime, pos_y_prime][0])/2
                pix_fin = ( int(new_gray), int(new_gray), int(new_gray) )        
                pixels[pos_x_prime, pos_y_prime] = pix_fin
            
            # +ANDRES:
            for k in range(0,50): #Inicializo el recorrer en el eje x
              for m in range (0,50): #Inicializo el recorrer en el eje y
                if  pos_x_prime+k < 0 or pos_x_prime+k >= width_output or pos_y_prime+m < 0 or pos_y_prime+m >= height_output:
                  continue
                pixels[pos_x_prime+k,pos_y_prime+m ]=pixels[pos_x_prime, pos_y_prime]
    return pixels

#Lente 1
R1 = 0.3
R2 = -0.3
dl = 0.01
nl = 1.5        #indice de refraccion
# +ANDRES:
R3 = 0.0109
R4 = -0.0109

#Calculamos la focal de la lente
f = R1*R2/((R2-R1)*(nl-1))           #foco del primer lente
print("focal: ", f)
#f2= R3*R4/((R4-R3)*(nl-1))          #foco del segundo lente
#print("focal1 y focal 2: ", f, f2)

#Propagaciones en el aire antes y despues de la lente
#Después
si = 0.526         #Distancia desde el verticce del lente hasta el plano imagen
#si = 0.751
n2 = 1             #Indice de refracción del aire 
so = 0.7           #Distancia desde el verticce del lente hasta el plano objeto
#so = 0.5
so = 1.2

#to guarantee image plane
# (Andrés quita esto): si = (f*so)/(so-f)       #ec/ley de Gauss
print("si: ", si)

# n1 = 1 #Indice de refracción del aire (Andres vuelve a declararlo)

#Magnification
Mt = -si/so
#Mt= 50 (Andres)
print ("Mt: ", Mt)

#load image (Object!)
obj = Image.open("idk.jpg", "r")
width, height = obj.size

width_output = int(width*(abs(Mt)))
height_output = int(height*(abs(Mt)))

# Create new Image and a Pixel Map
image = Image.new("RGB", (width_output, height_output), "white")
pixels = image.load()              #matriz de pixeles
#PROFE
pixels = ray_tracing(width, height, 0, so, n1, si, obj, pixels)
pixels = ray_tracing(width, height, 1, so, n1, si, obj, pixels)
#ANDRES
pixels = ray_tracing(width, height, 0, so1, n1, si1, sL, obj, pixels)
pixels = ray_tracing(width, height, 1, so1, n1, si1, sL, obj, pixels)

#Save Images to File
image.save('output.png', format='PNG')