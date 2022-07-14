import data

result = []
idx = 0
for pack in data.data_1:
    for d in pack:
        result.append(d * data.data_2[idx])
        idx += 1

print(result[:10])
print(len(result))
