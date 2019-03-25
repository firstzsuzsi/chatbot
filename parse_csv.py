import csv

filePath = ("/home/zsuzsi/study/python/chatbot/crime_stats.csv")
with open(filePath, "rt") as stats:
    read = csv.reader(stats, delimiter = ",", quotechar = "'")
    for line in read:
        print(line)
