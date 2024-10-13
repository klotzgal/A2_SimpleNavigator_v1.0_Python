CXX = g++
CXXFLAGS = -fPIC -std=c++17

LIB_DIR = ../lib

STACK_SOURCES = stack/stack.h stack/mystack.h
STACK_OUTPUT = $(LIB_DIR)/libstack.so

QUEUE_SOURCES = queue/queue.h
QUEUE_OUTPUT = $(LIB_DIR)/libqueue.so

LIST_SOURCES = list/list.h
LIST_OUTPUT = $(LIB_DIR)/liblist.so

all: $(STACK_OUTPUT) $(QUEUE_OUTPUT) $(LIST_OUTPUT)

$(STACK_OUTPUT): $(STACK_SOURCES)
	$(CXX) $(CXXFLAGS) -shared -o $@ $(STACK_SOURCES)

$(QUEUE_OUTPUT): $(QUEUE_SOURCES)
	$(CXX) $(CXXFLAGS) -shared -o $@ $(QUEUE_SOURCES)

$(LIST_OUTPUT): $(LIST_SOURCES)
	$(CXX) $(CXXFLAGS) -shared -o $@ $(LIST_SOURCES)

clean:
	rm -f $(LIB_DIR)/*.so
