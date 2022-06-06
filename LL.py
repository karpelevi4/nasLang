class LL:

    def __init__(self, value, previous=None, is_start=False):
        self.is_start = is_start
        if previous is None:
            self.is_start = True
        self.link_previous = previous
        self.link_next = None
        self.value = value

    def setLinkPrevious(self, link):
        self.link_previous = link

    def setLinkNext(self, link):
        self.link_next = link

    def setValue(self, value):
        self.value = value

    def setStartStatus(self, new_status):
        self.is_start = new_status

    def isStart(self):
        return self.is_start

    def getLinkPrevious(self):
        return self.link_previous

    def getLinkNext(self):
        return self.link_next

    def getValue(self):
        return self.value


def createLinkedList(first_value):
    return LL(first_value)


def goNext(linked_list):
    result = linked_list.getLinkNext()
    if result is not None:
        return result


def goPrevious(linked_list):
    if not linked_list.isStart():
        return linked_list.getLinkPrevious()


def goToStart(linked_list):
    while True:
        status = linked_list.is_start
        if status:
            break
        linked_list = goPrevious(linked_list)
    return linked_list


def goToEnd(linked_list):
    while True:
        if linked_list.getLinkNext() is None:
            break
        linked_list = goNext(linked_list)
    return linked_list


def addElement(linked_list, value):
    linked_list = goToEnd(linked_list)
    new_link = LL(value, previous=linked_list)
    linked_list.setLinkNext(new_link)


def insertElement(linked_list, value, index):
    linked_list = goToStart(linked_list)
    if index == 0:
        new_link = LL(value, is_start=True)
        linked_list.setLinkPrevious(new_link)
        new_link.setLinkNext(linked_list)
        linked_list.setStartStatus(False)
        linked_list = goPrevious(linked_list)
        linked_list.isStart()
    else:
        for ii in range(index):
            if linked_list.getLinkNext() is None:
                break
            linked_list = goNext(linked_list)

        link_previous = linked_list.getLinkPrevious()
        new_link = LL(value, previous=link_previous)
        new_link.setLinkNext(linked_list)
        link_previous.setLinkNext(new_link)
        linked_list.setLinkPrevious(new_link)


def deleteElement(linked_list, index):
    linked_list = goToStart(linked_list)
    if index == 0:
        value = linked_list.getValue()
        next_link = goNext(linked_list)
        next_link.setLinkPrevious(None)
        next_link.setStartStatus(True)
    else:
        for ii in range(index):
            if linked_list.getLinkNext() is None:
                break
            linked_list = goNext(linked_list)
        value = linked_list.getValue()
        linked_previous = linked_list.getLinkPrevious()
        linked_next = linked_list.getLinkNext()
        linked_previous.setLinkNext(linked_next)
        linked_next.setLinkPrevious(linked_previous)
    return value


def foundElementIndex(linked_list, index):
    linked_list = goToStart(linked_list)
    for ii in range(index):
        if linked_list.getLinkNext() is None:
            break
        linked_list = goNext(linked_list)

    return linked_list.getValue()


def isEmpty(linked_list):
    link_next = linked_list.getLinkNext()
    link_previous = linked_list.getLinkPrevious()
    if link_previous is None and link_next is None:
        return True
    else:
        return False


def show(linked_list):
    print(linked_list)
    print(linked_list.getValue())
    print(linked_list.getLinkNext())
    print(linked_list.getLinkPrevious())
    print(linked_list.isStart())


def showAll(linked_list):

    linked_list = goToStart(linked_list)
    while True:
        # show(linked_list)
        print(linked_list.getValue())
        if linked_list.getLinkNext() is None:
            break
        linked_list = goNext(linked_list)


def showAllValues(linked_list):
    linked_list = goToStart(linked_list)
    while True:
        # show(linked_list)
        print(linked_list.getValue())
        if linked_list.getLinkNext() is None:
            break
        linked_list = goNext(linked_list)