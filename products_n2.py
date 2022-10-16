products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
    	break
    price = input('請輸入商品價格: ')
    products.append([name, price])
print(products)

for d in products:
	print(d[0], '的價格是', d[1])

with open('products.txt', 'w') as f:
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')
        
    