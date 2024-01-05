import pages_generator
import LRU
import FIFO
from frame import Frame


def printing(num, pag):

    frames_LRU = pages_generator.frames_generator(num)
    frames_FIFO = pages_generator.frames_generator(num)
    print('\nLRU page errors:', LRU.LRU(frames_LRU, pag), '\n')
    print('FIFO page errors:', FIFO.FIFO(frames_FIFO, pag), '\n')
    return


for i in range(5):

    print('\n\nOutput nr: ', i + 1)

    # 1.1
    print("\n3 frames of memory and 15 references to 10 pages")

    frames_num = 3
    pages = pages_generator.ref_generator(15, 10)
    printing(frames_num, pages)

    # 1.2
    print("\n4 frames of memory and 15 references to 10 pages")

    frames = 4
    printing(frames, pages)

    # 1.3
    print("\n5 frames of memory and 15 references to 10 pages")

    frames = 5
    printing(frames, pages)

    # 2.1
    print("\n3 frames of memory and 50 references to 10 pages")

    frames = 3
    pages = pages_generator.ref_generator(50, 10)
    printing(frames, pages)

    # 2.2
    print("\n4 frames of memory and 50 references to 10 pages")

    frames = 4
    printing(frames, pages)

    # 2.3
    print("\n5 frames of memory and 50 references to 10 pages")

    frames = 5
    printing(frames, pages)

    # 3.1
    print("\n3 frames of memory and 100 references to 10 pages")

    frames = 3
    pages = pages_generator.ref_generator(100, 10)
    printing(frames, pages)

    # 3.2
    print("\n4 frames of memory and 100 references to 10 pages")

    frames = 4
    printing(frames, pages)

    # 3.3
    print("\n5 frames of memory and 100 references to 10 pages")

    frames = 5
    printing(frames, pages)

    # 4.1
    print("\n10 frames of memory and 1000 references to 50 pages")

    frames = 10
    pages = pages_generator.ref_generator(500, 50)
    printing(frames, pages)

    # 4.2
    print("\n20 frames of memory and 500 references to 50 pages")

    frames = 20
    printing(frames, pages)

    # 4.3
    print("\n30 frames of memory and 500 references to 50 pages")

    frames = 30
    printing(frames, pages)

    # 5.1
    print("\n10 frames of memory and 1000 references to 50 pages")
    
    frames = 10
    pages = pages_generator.ref_generator(1000, 50)
    printing(frames, pages)
    
    # 5.2
    print("\n20 frames of memory and 1000 references to 50 pages")
    
    frames = 20
    printing(frames, pages)
    
    # 5.3
    print("\n30 frames of memory and 1000 references to 50 pages")
    
    frames = 30
    printing(frames, pages)
    
    # 6.1
    print("\n10 frames of memory and 10000 references to 50 pages")
    
    frames = 10
    pages = pages_generator.ref_generator(10000, 50)
    printing(frames, pages)
    
    # 6.2
    print("\n20 frames of memory and 10000 references to 50 pages")
    
    frames = 20
    printing(frames, pages)
    
    # 6.3
    print("\n30 frames of memory and 10000 references to 50 pages")
    
    frames = 30
    printing(frames, pages)
