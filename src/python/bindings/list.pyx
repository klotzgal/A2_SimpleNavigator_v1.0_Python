cdef extern from "../../cpp/list/list.h" namespace "s21":
    cdef cppclass list[T]:
        void push_back(T)
        void pop_back()
        void push_front(T)
        void pop_front()
        bint empty()
        size_t size()

cdef class PyList:
    cdef list[int]* c_list

    def __cinit__(self):
        self.c_list = new list[int]()

    def push_back(self, int value):
        self.c_list.push_back(value)

    def pop_back(self):
        self.c_list.pop_back()

    def push_front(self, int value):
        self.c_list.push_front(value)

    def pop_front(self):
        self.c_list.pop_front()

    def empty(self):
        return self.c_list.empty()

    def size(self):
        return self.c_list.size()

    def __dealloc__(self):
        del self.c_list
