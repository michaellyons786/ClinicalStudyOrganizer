import statistics as stat


def mean(query_result):
    aliases = []
    ages = []

    for row in query_result:
        aliases.append(row[0])
        ages.append(row[1])

    return stat.mean(ages)



