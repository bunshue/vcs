#小班制的同學清單
classmate={'陳大慶','許大為','朱時中','莊秀文','吳彩鳳',
           '黃小惠','曾明宗','馬友友','韓正文','胡天明'}
test1={'陳大慶','許大為','朱時中','馬友友','胡天明'} #中高級名單
test2={'許大為','朱時中','吳彩鳳','黃小惠','馬友友','韓正文'} #中級名單
goodguy=test1 | test2
print("全班有 %d 人通過兩種檢定其中一種" %len(goodguy), goodguy)
bestguy=test1 & test2
print("全班有 %d 人兩種檢定全部通過" %len(bestguy), bestguy)
poorguy=classmate -goodguy
print("全班有 %d 人沒有通過任何檢定" %len(poorguy), poorguy)
