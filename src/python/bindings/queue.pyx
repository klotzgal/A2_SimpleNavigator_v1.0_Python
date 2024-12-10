cdef extern from "../../cpp/queue/queue.h" namespace "s21":
    cdef cppclass queue[T]:
        void push(T)
        T front()
        void pop()
        bint empty()
        size_t size()

cdef class PyQueue:
    cdef queue[int]* c_queue

    def __cinit__(self):
        self.c_queue = new queue[int]()

    def push(self, int value):
        self.c_queue.push(value)

    def front(self):
        return self.c_queue.front()

    def pop(self):
        self.c_queue.pop()

    def empty(self):
        return self.c_queue.empty()

    def size(self):
        return self.c_queue.size()

    def __dealloc__(self):
        del self.c_queue
