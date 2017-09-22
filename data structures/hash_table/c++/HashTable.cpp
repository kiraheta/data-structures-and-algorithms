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

void HashTable::addItem(std::string name, std::string drink){

    int index = hash(name);

    if(Hash_Table[index]->name == "empty"){
        Hash_Table[index]->name = name;
        Hash_Table[index]->drink = drink;
    }
    else {
        item* Ptr = Hash_Table[index];
        item* n = new item;
        n->name = name;
        n->drink = drink;
        n->next = NULL;

        while(Ptr->next != NULL){
            Ptr = Ptr->next;
        }

        Ptr->next = n;
    }
}

void HashTable::removeItem(std::string name){

    int index = hash(name);

    item* delPtr;
    item* P1;
    item* P2;

    // Case 0: Empty is bucket
    if(Hash_Table[index]->name == "empty" && Hash_Table[index]->drink == "empty"){
        std::cout << name << " was not found in hash table." << std::endl;
    }

    //Case 1: Only 1 item inside bucket and item has matching name
    else if (Hash_Table[index]->name == name && Hash_Table[index]->next == NULL){
        Hash_Table[index]->name = "empty";
        Hash_Table[index]->drink = "empty";

        std::cout << name << " was removed from hash table." << std::endl;
    }

    //Case 2: Match is located in first item and bucket has more than 1 item
    else if (Hash_Table[index]->name == name){
        delPtr = Hash_Table[index];
        Hash_Table[index] = Hash_Table[index]->next;
        delete delPtr;

        std::cout << name << " was removed from hash table." << std::endl;
    }

    //Case 3: Bucket contains multiple items but first item is not a match
    else{
        P1 = Hash_Table[index]->next;
        P2 = Hash_Table[index];

        while(P1 != NULL && P1->name != name){
            P2 = P1;
            P1 = P1->next;
        }
        // Case 3.1: No match
        if(P1 == NULL){
            std::cout << name << " was not found from hash table." << std::endl;
        }
        // Case 3.2: Match found
        else{
            delPtr = P1;
            P1 = P1->next;
            P2->next = P1;

            delete delPtr;
            std::cout << name << " was removed from hash table." << std::endl;
        }
    }
}

int HashTable::numOfItemsInIndex(int index){

    int count = 0;

    if(Hash_Table[index]->name == "empty"){
        return count;
    }
    else {
        count++;
        item* Ptr = Hash_Table[index];
        while(Ptr->next != NULL){

            count++;
            Ptr = Ptr->next;
        }
    }

    return count;
}
