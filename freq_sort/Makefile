
EXECUTABLE = freq_sort
SOURCES = main.cpp utility.cpp 


OBJECTS = $(patsubst %.cpp,%.o,$(SOURCES))
DEPENDS = $(OBJECTS:.o=.d)
CFLAGS = -c -g -MMD -MP -std=c++11 -Wall -pedantic
LFLAGS = 
CC=g++

all: $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(OBJECTS) $(LFLAGS) -o $@

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@

.PHONY: clean
clean:
	rm -f $(EXECUTABLE) $(OBJECTS) $(DEPENDS)

run: $(EXECUTABLE)
	./$(EXECUTABLE)

-include $(DEPENDS)
