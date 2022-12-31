import statistics

class ArgumentError(Exception): pass

def getaction(dataset:list, action):
    if action == 'mean':
        return statistics.mean(dataset)
    elif action == 'median':
        return statistics.median(dataset)
    elif action == 'mode':
        return statistics.mode(dataset)
    elif action == 'range':
        return max(dataset) - min(dataset)
    elif action == 'iqr' or action == 'inter quartile range':
        q1 = statistics.quantiles(dataset)[0]
        q3 = statistics.quantiles(dataset)[2]
        return q3 - q1
    elif action == 'psd' or action == 'population standard deviation':
        return statistics.pstdev(dataset)
    elif action == 'pv' or action == 'population variance':
        return statistics.pvariance(dataset)
    elif action == 'ssd' or action == 'sample standard deviation':
        return statistics.stdev(dataset)
    elif action == 'sv' or action == 'sample variance':
        return statistics.variance(dataset)
    else:
        raise ArgumentError(f"Invalid action: '{action}'.")

while True:
    data = list()
    dataset = input("Dataset = ")
    for i in dataset.split(", "):
        data.append(float(i))
    action = input("Action [mean, median, mode, range, iqr (inter-quartile range), psd (population standard deviation), ssd (sample standard deviation), pv (population variance), sv (sample variance), pss (population standard score), sss (sample standard score)]: ")
    try:
        if action == 'pss' or action == 'population standard score':
            datum = float(input("Target datum = "))
            mean = statistics.mean(data)
            print((datum - mean) / statistics.pstdev(data))
        elif action == 'sss' or action == 'sample standard score':
            datum = float(input("Target datum = "))
            mean = statistics.mean(data)
            print((datum - mean) / statistics.stdev(data))
        else:
            print(getaction(data, action))
    except ZeroDivisionError:
        print("Zero division occurred. Your dataset is either incorrect or invalid. Please check again if there is any mistakes.")