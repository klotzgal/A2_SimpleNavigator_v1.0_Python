cdef extern from "../../cpp/stack/stack.h" namespace "s21":
    cdef cppclass stack[T]:
        void push(T)
        void pop()
        T top()
        bint empty()
        size_t size()

cdef class PyStack:
    cdef stack[int]* c_stack

    def __cinit__(self):
        self.c_stack = new stack[int]()

    def push(self, int value):
        self.c_stack.push(value)

    def pop(self):
        self.c_stack.pop()

    def top(self):
        return self.c_stack.top()

    def empty(self):
        return self.c_stack.empty()

    def size(self):
        return self.c_stack.size()

    def __dealloc__(self):
        del self.c_stack
