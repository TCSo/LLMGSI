MAKEFILE_LOC = $(dir $(realpath $(firstword $(MAKEFILE_LIST))))

# Paths:
SRC_LOC = $(MAKEFILE_LOC)/src
DATA_LOC = $(MAKEFILE_LOC)/data

# Start the program 
run: 
	python3 $(SRC_LOC)/main.py 