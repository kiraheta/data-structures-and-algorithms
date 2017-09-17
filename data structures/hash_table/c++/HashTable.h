//
//  HashTable.h
//  Hash Table
//

#include <iostream>
#include <string>
#include <cstring>

#ifndef HashTable_h
#define HashTable_h


class HashTable {

private:
    static const int TABLE_SIZE = 11;

    struct item{
        std::string name;
        std::string drink;
        item* next;
    };

    item* Hash_Table[TABLE_SIZE];

public:

    HashTable();
    ~HashTable();
    int hash(std::string key);
    int numOfItemsInIndex(int index);
    void printTable();
    void printItemsInIndex(int index);
    void findDrink(std::string name);
    void addItem(std::string name, std::string drink);
    void removeItem(std::string name);
};

#endif /* HashTable_h */
