/**
 * fifteen.c
 *
 * Implements Game of Fifteen (generalized to d x d).
 *
 * Usage: fifteen d
 *
 * whereby the board's dimensions are to be d x d,
 * where d must be in [DIM_MIN,DIM_MAX]
 *
 * Note that usleep is obsolete, but it offers more granularity than
 * sleep and is simpler to use than nanosleep; `man usleep` for more.
 */

#define _XOPEN_SOURCE 500

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// constants
#define DIM_MIN 3
#define DIM_MAX 9

// board
int board[DIM_MAX][DIM_MAX];

// dimensions
int d;

// prototypes
void clear(void);
void greet(void);
void init(void);
void draw(void);
bool move(int tile);
bool won(void);

int main(int argc, string argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        printf("Usage: fifteen d\n");
        return 1;
    }

    // ensure valid dimensions
    d = atoi(argv[1]);
    if (d < DIM_MIN || d > DIM_MAX)
    {
        printf("Board must be between %i x %i and %i x %i, inclusive.\n",
            DIM_MIN, DIM_MIN, DIM_MAX, DIM_MAX);
        return 2;
    }

    // open log
    FILE *file = fopen("log.txt", "w");
    if (file == NULL)
    {
        return 3;
    }

    // greet user with instructions
    greet();

    // initialize the board
    init();

    // accept moves until game is won
    while (true)
    {
        // clear the screen
        clear();

        // draw the current state of the board
        draw();

        // log the current state of the board (for testing)
        for (int i = 0; i < d; i++)
        {
            for (int j = 0; j < d; j++)
            {
                fprintf(file, "%i", board[i][j]);
                if (j < d - 1)
                {
                    fprintf(file, "|");
                }
            }
            fprintf(file, "\n");
        }
        fflush(file);

        // check for win
        if (won())
        {
            printf("ftw!\n");
            break;
        }

        // prompt for move
        printf("Tile to move: ");
        int tile = get_int();

        // quit if user inputs 0 (for testing)
        if (tile == 0)
        {
            break;
        }

        // log move (for testing)
        fprintf(file, "%i\n", tile);
        fflush(file);

        // move if possible, else report illegality
        if (!move(tile))
        {
            printf("\nIllegal move.\n");
            usleep(500000);
        }

        // sleep thread for animation's sake
        usleep(500000);
    }

    // close log
    fclose(file);

    // success
    return 0;
}

/**
 * Clears screen using ANSI escape sequences.
 */
void clear(void)
{
    printf("\033[2J");
    printf("\033[%d;%dH", 0, 0);
}

/**
 * Greets player.
 */
void greet(void)
{
    clear();
    printf("WELCOME TO GAME OF FIFTEEN\n");
    usleep(2000000);
}

/**
 * Initializes the game's board with tiles numbered 1 through d*d - 1
 * (i.e., fills 2D array with values but does not actually print them).
 */
void init(void)
{
    // TODO;
    // define grid dimensions and counter variable then populate grid array w/ loops.
    int grid = d * d;
    // integer i iterates over the rows of the game board
    for (int i = 0; i < d; i++)
    {
        // integer j iterates over the columns of the game board
        for (int j = 0; j < d; j++)
        {
            // sets the tile's value numbered 1 through d*d - 1 in descending order.
            board[i][j] = --grid; // this prefix works in c but not python
        }
    }
    // if dimension is even. if d is divisible by 2 then it should equal 0.
    if ((d % 2) == 0)
    {
        // swap 2 tile with 1 tile. see questions text to see how this works.
        int swap = board[d - 1][d - 2]; // swap equal 1
        board[d - 1][d - 2] = board[d - 1][d - 3]; // 1 equals 2
        board[d - 1][d - 3] = swap; // 2 swaps with 1.
    }
}
/**
 * Prints the board in its current state.
 */
void draw(void)
{
    // TODO
    // integer i iterates over the rows of the game board
    for (int i = 0; i < d; i++)
    {
        // integer j iterates over the columns of the game board
        for (int j = 0; j < d; j++)
        {
            // replace 0 tile with underscore so user knows which tile to move
            if (board[i][j] == 0)
            {
                printf(" __ ");
            }
            // print all the other numbered tiles except for the 0 tile
            else
            {
                printf("%2i ", board[i][j]);
            }
        }
        // print two lines after each row to make grid
        printf("\n\n");
    }
}


/**
 * If tile borders empty space, moves tile and returns true, else
 * returns false.
 */
bool move(int tile)
{
    // TODO
    // declare variables to search across grid
    int row = 0, column = 0;
    // searching through rows of find tile location
    for (int i = 0; i < d; i++)
    {
        // searching through columns of find tile location
        for (int j = 0; j < d; j++)
        {
            // find tile location then store location to two variables
            if (board[i][j] == tile)
            {
                row = i;
                column = j;
            }
        }
    }

    // Check if the blank tile is below
    if (row + 1 < d && board[row + 1][column] == 0)
    {
        board[row + 1][column] = board[row][column];
        board[row][column] = 0;
        return true;
    }
    // check if the blank tile is above
    else if (row - 1 >= 0 && board[row - 1][column] == 0)
    {
        board[row - 1][column] = board[row][column];
        board[row][column] = 0;
        return true;
    }
    // check if the blank tile is to the right
    else if (column + 1 < d && board[row][column + 1] == 0)
    {
        board[row][column + 1] = board[row][column];
        board[row][column] = 0;
        return true;
    }
    // check if the blank tile is to the left
    else if (column - 1 >= 0 && board[row][column - 1] == 0)
    {
        board[row][column - 1] = board[row][column];
        board[row][column] = 0;
        return true;
    }

    return false;
}


/**
 * Returns true if game is won (i.e., board is in winning configuration),
 * else false.
 */
bool won(void)
{
    // declare counter variable
    int c = 0;

    // iterate over board to check values to see if it's in order
    for (int i = 0; i < d; i++)
    {
        for (int j = 0; j < d; j++)
        {
            // if any tile doesn't equal counter, return false
            if (++c != d * d && board[i][j] != c)
            {
                return false;
            }
        }
    }
    // all tiles count up from 0 and are increasing order left to right and top to bottom, winner!
    return true;
}
