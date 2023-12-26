# ex15_9.py
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s : %(message)s')
logging.debug('程式開始')

def sumrange(n):
    logging.debug('sumrange %s 計算開始' % n)
    ans = 0
    for i in range(1, n + 1):
        ans += i
        logging.debug('i = ' + str(i) + ', ans = ' + str(ans))
    logging.debug('sumrange %s 計算結束' % n)
    return ans

num = 5
print("sumrange(%d) = %d" % (num, sumrange(num)))
logging.debug('程式結束')




