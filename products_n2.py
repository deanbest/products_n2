products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
    	break
    price = input('請輸入商品價格: ')
    price = int(price)
    #int 把價格轉成整數
    products.append([name, price])
print(products)

for d in products:
	print(d[0], '的價格是', d[1])


# w為寫入模式, 若沒此檔案, 就產生它
# 寫成f, f.write > 只要用f, 就能稱呼它
#當然要先open才能寫入
# 用for...loop來一個個存取清單中的商品
# with < 幫你自動close檔案, 
# 因有open就要有close的動作
# 程式走到24, with就自動幫你close
# encoding='utf-8' << 好像不需要用到, 除非excel開變亂碼
# encoding是編碼的意思, utf-8是最廣泛使用
with open('products.csv', 'w') as f:
    f.write('商品,價格\n')
    for p in products:
        #原p[1]已轉為整數, 但字串才能與字串相加
        #所以要用str轉成字串
        f.write(p[0] + ',' + str(p[1]) + '\n')
        
