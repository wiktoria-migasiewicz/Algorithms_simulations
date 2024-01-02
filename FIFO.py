from frame import Frame


def FIFO(frames, pages):

    page_error = 0
    time = 0

    for page in pages:
        page_found = False

        # When page is already in a frame
        for frame in frames:
            if frame.page == page:
                page_found = True
                break

        if page_found:
            time += 1
            continue

        # Checking if any frame is empty
        for frame in frames:
            if frame.page is None:
                frame.set_page(page, time)
                page_found = True
                page_error += 1
                break

        if page_found:
            time += 1
            continue

        current = None
        frame_chosen = None

        # Choosing a first-in frame
        for frame in frames:
            if current is None or frame.change < current:
                current = frame.change
                frame_chosen = frame

        # Changing page for the first-in page
        frame_chosen.set_page(page, time)
        page_error += 1
        time += 1

    # Returning number of page errors
    return page_error
