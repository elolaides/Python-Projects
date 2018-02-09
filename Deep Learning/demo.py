import numpy as np
import time

def main():
    a = np.array([1,2,3,4])
    print(a)

    b = np.random.rand(1000000)
    c = np.random.rand(1000000)
    tic = time.time()
    d = np.dot(b,c)
    toc = time.time()
    print('d: '+str(d))
    print('vectorization version: ' + str(1000*(toc-tic)) + 'ms')

    d = 0
    tic = time.time()
    for i in range(1000000):
        d += b[i]*c[i]
    toc = time.time()
    print('d: '+str(d))
    print('for-loop version: ' + str(1000*(toc-tic)) + 'ms')

if __name__ == '__main__':
    main()
