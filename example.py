start = int(input("enter the start number:"))
end = int(input("enter the nd index :"))
for num in range(start,end+1):
    if num%2 !=1:
        print(num)