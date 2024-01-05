score=[97,76,89,76,90,100,87,65]
print('本學期總共考過的數學小考次數', len(score))
print('所有成績由小到大排序的結果為: {}'.format(sorted(score)))
print('本學期所有分數的總和', sum(score))
print('本學期所有分數的平均', round(sum(score)/len(score),1))
print('本學期考最差的分數為', min(score))
print('本學期考最好的分數為', max(score))
