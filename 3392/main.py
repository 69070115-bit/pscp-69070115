"""Array ฮาเฮ"""
a = []

for i in range(1, 4):
    a.append(int(input()))
    print(f"Input number {i} stored.")

while True:
    menu = int(input())

    if menu == 1:
        print("Original order:", *a)
    elif menu == 2:
        print("Descending order:", *sorted(a, reverse=True))
    elif menu == 3:
        print("Ascending order:", *sorted(a))
    elif not menu :
        break
