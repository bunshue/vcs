import glob
import os
import time

print("多線程建立縮圖")

from concurrent.futures import ThreadPoolExecutor
from threading import Thread

from PIL import Image

def gen_thumbnail(infile):
    file, ext = os.path.splitext(infile)
    filename = file[file.rfind('/') + 1:]
    for size in (32, 64, 128):
        outfile = f'thumbnails/{filename}_{size}_{size}.png'
        image = Image.open(infile)
        image.thumbnail((size, size))
        image.save(outfile, format='PNG')

def main():
    pool = ThreadPoolExecutor(max_workers=30)
    futures = []
    start = time.time()
    print('aaaa')
    for infile in glob.glob('images/*'):
        print(infile)
        # submit方法是非阻塞式的方法 
        # 即便工作线程数已经用完，submit方法也会接受提交的任务 
        future = pool.submit(gen_thumbnail, infile)
        futures.append(future)
    for future in futures:
        # result方法是一个阻塞式的方法 如果线程还没有结束
        # 暂时取不到线程的执行结果 代码就会在此处阻塞
        future.result()
    end = time.time()
    print(f'耗时: {end - start}秒')
    # shutdown也是非阻塞式的方法 但是如果已经提交的任务还没有执行完
    # 线程池是不会停止工作的 shutdown之后再提交任务就不会执行而且会产生异常
    pool.shutdown()

if __name__ == '__main__':
    main()

