/**
 * Implements a dictionary's functionality.
 */

#include <stdbool.h>
#include "dictionary.h"

// define struct for a node
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// creating array of nodes
node *hashtable[HTABLE_SIZE];
// mainting pointer to the head of linked list
node *new_node;
// global variable to keep track of size of dictionary
unsigned int wordsInDictionary = 0;

// found the following hash fucntion on stack overflow https://stackoverflow.com/questions/20462826/hash-function-for-strings-in-c
int hashing(char *word)
{
    unsigned int hash = 0;
    for (int i = 0 ; word[i] != '\0' ; i++)
    {
        hash = 31 * hash + word[i];
    }
    return hash % HTABLE_SIZE;
}

/**
 * Returns true if word is in dictionary else false.
 */
bool check(const char *word)
{
    // create char array and store copy of word
    int len = strlen(word);
    char lowercaseWord[len + 1];

    // convert word to lowercase and store it in lowercaseWord
    for (int i = 0; i < len; i++)
    {
        lowercaseWord[i] = tolower(word[i]);
    }

    // add null terminator to indicate end of char array
    lowercaseWord[len] = '\0';

    // get hash value (aka linked list or bucket)
    int hv = hashing(lowercaseWord);

    // assign cursor node to the first node in linked list
    node *cursor = hashtable[hv];

    // compare strings until the end of the linked list
    while (cursor != NULL)
    {
        if (strcmp(cursor->word, lowercaseWord) == 0)
        {
            // word is in dictionary
            return true;
        }
        // check next node
        cursor = cursor->next;
    }
    return false;
}


/**
 * Loads dictionary into memory. Returns true if successful else false.
 * Loads the dictionary into a data structure called a hash table.
 * For each word in the dictionary text file, store it in the dictionary's hash table
 * Hash tables are an array of linked lists and each element in the are is an node *
 * Hash function returns the bucket that a given key or value belongs to
 */
bool load(const char *dictionary)
{
    // open dictionary
    FILE *fpdict = fopen(dictionary, "r");
    int index = 0;
    char word[LENGTH + 1];

    if (fpdict == NULL)
    {
        printf("Dictionary wouldn't open.\n");
        return false;
    }

    // make htable elements NULL
    for (int i = 0; i < HTABLE_SIZE; i++)
    {
        hashtable[i] = NULL;
    }

    while (fscanf(fpdict, "%s", word) != EOF)
    {
        // dynamically allocate memory using malloc to create a node for each new word
        node *new_node = malloc(sizeof(node));
        // unload dictionary if malloc returns NULL to quit speller
        if (new_node == NULL)
        {
            printf("You've run out of memory.\n");
            unload();
            return false;
        }

        // if succeeds proceed & copy word from dictionary and store it into new node.
        strcpy(new_node->word, word);

        // if not at the end of the file dictionary
        if (!feof(fpdict))
        {
            // use the hash function to calculate index in word
            // (new_node->word) has the word from the dictionary
            // hashing(new_node->word) will give you the index of a bucket in the hash table that the word will go in
            index = hashing(new_node->word);

            // if linked list is empty, insert the first node
            if (hashtable[index] == NULL)
            {
                hashtable[index] = new_node;
                new_node->next = NULL;
            }
            // if linked list is not empty, attach node to front of list
            else
            {
                new_node->next = hashtable[index];
                hashtable[index] = new_node;
            }
            // increment the number of words read
            wordsInDictionary++;
        }
    }
    // close dictionary
    fclose(fpdict);
    if (wordsInDictionary > 0)
    {
        return true;
    }
    return false;
}

/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{
    return wordsInDictionary;
    return 0;
}

/**
 * Unloads dictionary from memory. Returns true if successful else false.
 */
bool unload(void)
{
    for (int i = 0; i < HTABLE_SIZE; i++)
    {
        node *cursor = hashtable[i];
        while (cursor != NULL)
        {
            // free linked lists
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }
    free(new_node);
    return true;
}