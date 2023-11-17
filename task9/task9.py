#Функция для подсчета среднего балла по отдельным предметам
def avg(all_points):
    avg = 0
    for i in all_points:
        avg += i
    return(avg/len(all_points))

all_math = []                                   #список баллов по математике
all_physics = []                                #список баллов по физике
all_rsLang = []                                 #список баллов по русскому языку

with open("dataset_3363_4.txt", 'r') as inf:    #открываем файл на чтение
    for line in inf:                            #читаем строку из файла
        line = line.strip().split(';')          #удаляем лишние символы переноса на след. строку и разделяем по символу ';'

        count = 0                               #счетчик предметов
        for point in line[1:]:                  #для каждой оценци из строки, начиная с первого элемента (т.к. фамилия учащегося не интересует)
            if count==0:                        #если это первая оценка, то значит она по математике
                all_math.append(int(point))
            if count==1:                        #если это первая оценка, то значит она по физике
                all_physics.append(int(point))
            if count==2:                        #если это первая оценка, то значит она по русскому языку
                all_rsLang.append(int(point))
            count += 1                          #каждый следующий элемент в списке - оценка по новому предмету 

    with open("test9.txt", 'a') as ouf:         #открываем файл на дозапись (создается при отсутсвии)
        for i in range(0,len(all_math)):        #запускаем цикл от нулевого ученика до количества их общего количества
            avg_str = str((all_math[i]+all_physics[i]+all_rsLang[i])/3) + "\n"  #средняя оценка по трём предметам
            ouf.write(avg_str)
        avg_all = str(avg(all_math)) + " " + str(avg(all_physics)) + " "+ str(avg(all_rsLang)) #средние баллы по математике, физике и русскому языку по всем абитуриентам
        ouf.write(avg_all)   