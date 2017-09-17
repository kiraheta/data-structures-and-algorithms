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
