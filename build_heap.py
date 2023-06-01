# KarlisOlmanis
import os

def build_heap(data):
    mainja = []
    lielums = len(data)
    for i in range(lielums // 2, -1, -1):
        maz(data, i, mainja)
    return mainja

def maz(data, i, mainja):
    lielums = len(data)
    min_inde = i
    kreisais = 2 * i + 1
    labais = 2 * i + 2
    if kreisais < lielums and data[kreisais] < data[min_inde]:
        min_inde = kreisais
    if labais < lielums and data[labais] < data[min_inde]:
        min_inde = labais
    if min_inde != i:
        mainja.append((i, min_inde))
        data[i], data[min_inde] = data[min_inde], data[i]
        maz(data, min_inde, mainja)
        
def main():
    ievade = input()
    if "I" in ievade:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
    elif "F" in ievade:
        fails = input()
        atrasanas = './tests/'
        faila_vieta = os.path.join(atrasanas, fails)
        with open(faila_vieta, mode="r") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
    mainja = build_heap(data)
    print(len(mainja))
    for i, j in mainja:
        print(i, j)
        
if __name__ == "__main__":
    main()
