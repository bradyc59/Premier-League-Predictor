import bayes, knn

results = []
for i in range(5):
    result_bayes = knn.main()
    results.append(result_bayes)

print(sum(results) / len(results), "%")