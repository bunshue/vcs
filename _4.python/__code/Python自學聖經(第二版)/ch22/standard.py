from sklearn.preprocessing import StandardScaler

std = StandardScaler()
data = std.fit_transform([[156,56,34,800000], 
                          [180,73,21,620000], 
                          [175,76,18,1000000], 
                          [148,46,26,430000]])
print(data)