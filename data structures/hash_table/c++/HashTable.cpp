//
//  HashTable.cpp
//  Hash Table
//

#include "HashTable.h"

HashTable::HashTable(){

  for (int i = 0; i < TABLE_SIZE; i++){
      Hash_Table[i] = new item;
      Hash_Table[i]->name = "empty";
      Hash_Table[i]->drink = "empty";
      Hash_Table[i]->next = NULL;
  }
}

HashTable::~HashTable() {

    item* Ptr;

    for(int i = 0; i < TABLE_SIZE; i++){
        while(Hash_Table[i] != NULL){
            Ptr = Hash_Table[i];
            Hash_Table[i] = Hash_Table[i]->next;
            delete Ptr;
        }
    }
}

void HashTable::printTable(){

    int number;
    for(int i = 0; i < TABLE_SIZE; i++){

        number = numOfItemsInIndex(i);
        std::cout << "-----------------" << std::endl;
        std::cout << "Index = " << i << std::endl;
        std::cout << Hash_Table[i]->name << std::endl;
        std::cout << Hash_Table[i]->drink << std::endl;
        std::cout << "# of items = " << number << std::endl;
        std::cout << "-----------------" << std::endl;
    }
}

void HashTable::printItemsInIndex(int index){

    item* Ptr = Hash_Table[index];

    if(Ptr->name == "empty"){
        std::cout << "Index = " << index << " is empty." << std::endl;
    }
    else{
        std::cout << "Index = " << index << " contains the following items"
        << std::endl;

        while(Ptr != NULL){
            std::cout << "-----------------" << std::endl;
            std::cout << Ptr->name << std::endl;
            std::cout << Ptr->drink << std::endl;
            std::cout << "-----------------" << std::endl;
            Ptr = Ptr->next;
        }
    }
}

int HashTable::hash(std::string key){

    int hash = 0;
    for (size_t i = 0; i < key.length(); i++){
        hash += (31 * hash) + (int)key[i]; // Horner's Method
    }

    return (hash % 0x7fffffff) % TABLE_SIZE;
}
