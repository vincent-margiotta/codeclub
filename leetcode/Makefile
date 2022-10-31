install:
clean:
	rm -ri $(PROBLEM) $(PROBLEM).out
new:
	cp template.cc $(PROBLEM).cc
	touch $(PROBLEM).in
build:
	g++ -std=c++0x -O2 -Wall -g $(PROBLEM).cc -o $(PROBLEM)
run: $(PROBLEM) $(PROBLEM).in
	./$(PROBLEM) < $(PROBLEM).in > $(PROBLEM).out
