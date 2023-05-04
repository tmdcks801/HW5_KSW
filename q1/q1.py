import csv

if __name__ == '__main__':

    f=open('q1.csv',encoding='ANSI')

    data=csv.reader(f)
    header=next(data)

    max=0
    min=0
    av=0
    cnt=0

    for row in data:
        if row[2]=='' or row[3]==''or  row[4]=='' :
            row[2]=0
        else:
            row[2]=float(row[2])
            av+=row[2]
            cnt+=1
            max+=float(row[4])
            min+=float(row[3])
    print("Annual Temperature Report for Seoul in 2022")
    print("Average Temperature:",round(av/cnt,2))
    print("Average minimum Temperature:",round(min/cnt,2))
    print("Average maximum Temperature:",round(max/cnt,2))
