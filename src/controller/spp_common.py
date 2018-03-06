from Queue import Queue

PRIMARY = ''
SECONDARY_LIST = []

# Initialize primary comm channel
MAIN2PRIMARY = Queue()
PRIMARY2MAIN = Queue()

# Maximum num of sock queues for secondaries
MAX_SECONDARY = 16

PRIMARY = ''
SECONDARY_COUNT = 0

REMOTE_COMMAND = "RCMD"
RCMD_EXECUTE_QUEUE = Queue()
RCMD_RESULT_QUEUE = Queue()


class GrowingList(list):
    """Growing List

    Custom list type for appending index over the range which is
    similar to ruby's Array. Empty index is filled with 'None'.
    It is used to contain queues for secondaries with any sec ID.

    >>> gl = GrowingList()
    >>> gl.[3] = 0
    >>> gl
    [None, None, None, 0]
    """

    def __setitem__(self, index, value):
        if index >= len(self):
            self.extend([None]*(index + 1 - len(self)))
        list.__setitem__(self, index, value)


# init secondary comm channel list
MAIN2SEC = GrowingList()
SEC2MAIN = GrowingList()
