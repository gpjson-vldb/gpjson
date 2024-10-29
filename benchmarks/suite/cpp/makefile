DIR = bin

CC = g++
CC_FLAGS = -O3 -std=c++11 -mavx -mavx2 -msse -msse2 -msse4 -msse4.2 -mpclmul
POST_FLAGS = -lpthread -mcmodel=medium -static-libstdc++

PISON_DIR = $(DIR)/pison
PISON_SRC = ../../engine/pison.cpp ../../src/pison/*.cpp

RAPIDJSON_DIR = $(DIR)/rapidjson
RAPIDJSON_SRC = ../../engine/rapidjson.cpp

SIMDJSON_DIR = $(DIR)/simdjson
SIMDJSON_SRC = ../../engine/simdjson.cpp ../../src/simdjson/*.cpp

all: %

dirs:
	mkdir -p $(DIR)
	mkdir -p $(PISON_DIR)
	mkdir -p $(RAPIDJSON_DIR)
	mkdir -p $(SIMDJSON_DIR)

%: dirs %.cpp

	$(CC) $(CC_FLAGS) -o $(PISON_DIR)/$@ $@.cpp $(PISON_SRC) $(POST_FLAGS)
	$(CC) $(CC_FLAGS) -o $(RAPIDJSON_DIR)/$@ $@.cpp $(RAPIDJSON_SRC) $(POST_FLAGS)
	$(CC) $(CC_FLAGS) -o $(SIMDJSON_DIR)/$@ $@.cpp $(SIMDJSON_SRC) $(POST_FLAGS)

clean:
	-$(RM) -r $(DIR)