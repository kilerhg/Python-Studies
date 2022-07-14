# 
if __name__ == '__main__':
    pessoas = []
    pessoa = []
    scores = []
    penultimo = []
    for x in range(int(input().strip())):
        name = input().strip()
        score = float(input().strip())
        pessoa.append(name)
        pessoa.append(score)
        scores.append(score)
        pessoas.append(pessoa[:])
        pessoa.clear()
    for x in range(scores.count(min(scores))):
        scores.remove(min(scores))
    scores.sort()
    for x in range(scores.count(min(scores))):
        penultimo.append(scores[x])
    if pessoas[0][0] != 'Test1':
        pessoas.reverse()
    for x in pessoas:
        if x[1] == penultimo[0]:
            print(x[0])
