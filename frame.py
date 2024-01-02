class Frame:
    def __init__(self, index):
        self.index = index
        self.page = None
        self.change = None

    # Setting a page and time of change
    def set_page(self, new_page, time):
        self.page = new_page
        self.change = time

    # Setting only time for when page already in frame
    def set_change(self, time):
        self.change = time


