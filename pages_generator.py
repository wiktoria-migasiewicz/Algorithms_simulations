from frame import Frame
import numpy as np


def ref_generator(references_num, pages_num):

    references = []

    # Creating a list of references of pages
    for i in range(references_num):
        references.append(np.random.randint(0, pages_num))

    print('\nReferences:\n', references, '\n')

    return references


def frames_generator(frames_num):

    frames = []

    # Creating frames of memory
    for i in range(frames_num):
        frames.append(Frame(i))

    return frames

