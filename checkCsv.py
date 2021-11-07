import csv
with open(r'savedrecs.csv', 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    headers = next(csv_reader)  # 获取第一行，可能是头
    with open(r'savedrecsA.csv', 'w', newline='') as file:
        fileWriter = csv.writer(file, delimiter=',')
        for row in csv_reader:
            fileWriter.writerow(row)
#把第二个csv文件续写进来，合并
with open(r'savedrecs 2.csv', 'r', newline='') as csvfile2:
    csv_reader2 = csv.reader(csvfile2, delimiter=',')
    with open(r'savedrecsA.csv', 'a', newline='') as file:
        fileWriter = csv.writer(file, delimiter=',')
        for row in csv_reader2:
            fileWriter.writerow(row)

    # 每一行索引用
    # for row in csv_reader:
    #     print(row[0])


    # 返回所有的列的信息
    # for row in csv_reader:
    #     print(row)