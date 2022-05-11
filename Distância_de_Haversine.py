import math
def haversine(raio,Q1,A1,Q2,A2):
    q1=math.radians(Q1)
    a1=math.radians(A1)
    q2=math.radians(Q2)
    a2=math.radians(A2)
    sinq=math.sin((q2-q1)/2)
    qq=sinq**2
    sina=math.sin((a2-a1)/2)
    aa=sina**2
    raiz=qq+(math.cos(q1))*(math.cos(q2))*aa
    b=math.asin((raiz**0.5))
    d=(2*raio)*b
    return d
