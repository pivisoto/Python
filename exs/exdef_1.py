def entrada(p1,p2,p3,p4,p5):
    if (0 <= p1<= 100) and (0 <= p2<= 100)  and (0 <= p3<= 100) and (0 <= p4<= 100) and (0 <= p5<= 100):
        lista = [p1,p2,p3,p4,p5]
    else:
        print('notas invalidas')
    print('suas notas foram =',lista)
def media(p1,p2,p3,p4,p5):
    media = (p1 + p2 + p3 + p4 + p5)/5
    return media
        

