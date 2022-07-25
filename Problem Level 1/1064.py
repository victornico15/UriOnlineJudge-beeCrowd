y = 0
media=0
for x in range(1,7):
    a = float(input())
    
    if a > 0:
        media=a+media
        y = y + 1
media=media/y
print(y,"valores positivos")

print("%.1f" %media)

