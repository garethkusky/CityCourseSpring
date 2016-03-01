__author__ = 'acpb968'

class main():
    rec1=rectangle(4,40)
    rec2=rectangle(3.5,35.7)
    print("rectangle 1: width is ", str(int(rec1.width*100)/100)," Height is ",str(int(rec1.height*100)/100),\
        " Area is ", str(int(rec1.getArea()*100)/100), " Permimiter is ", str(int(rec1.getPerimeter()*100)/100))
    print("rectangle 2: width is ", str(int(rec2.width*100)/100)," Height is ",str(int(rec2.height*100)/100),\
        " Area is ", str(int(rec2.getArea()*100)/100), " Permimiter is ", str(int(rec2.getPerimeter()*100)/100))


main()