# 抽數
times = int(input('請輸入抽卡次數: '))

# SSR 2.5 %
# SR  7.5 %
def draw(times) :
    import random as r
    for p in range(times) :    
        p = int(r.randint(1,1000))
        if p <= 25 :
            return 'SSR'
        elif p <= 100 :
            return 'SR'
        else :
            return 'UR'

# 讀取獎勵,並分類
gift_1 = []  # 5  項
gift_2 = []  # 8  項
gift_3 = []  # 17 項
with open ('gift.csv', 'r' ,encoding = 'utf-8') as g_l :
    for g in g_l :
        level, item = g.strip().split(',')
        if '品級' in g :
            continue
        elif 'SSR' in g :
            gift_1.append(item)
        elif 'SR' in g :
            gift_2.append(item)
        else :
            gift_3.append(item)

# 結果,加入列表
result = []
count = 1
import random as r
for c in range(times) :
    quality = draw(times) # 定義結果
    draw(times)
    if quality == 'SSR' :
        get = int(r.randint(0,4))
        gift_f = gift_1[get]
    elif quality == 'SR' :
        get = int(r.randint(0,7))
        gift_f = gift_2[get]
    else :
        get = int(r.randint(0,16))
        gift_f = gift_3[get]
    result.append([count,quality,gift_f])
    count += 1

# 寫入結果
with open ('result.csv', 'w', encoding = 'utf-8') as f :
    f.write('次數,結果,獎品\n')
    for r in result :
        f.write(str(r[0]) + ',' + r[1] + ',' + r[2] + '\n')
