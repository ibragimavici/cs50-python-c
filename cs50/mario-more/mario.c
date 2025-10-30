#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    int row;
    int column;
    int dot;
    do
    {
        height = get_int("Input height:\n");
    }
    while( height<1 || height>8 );


    for(row = 0; row < height; row++)
    {
            for (dot = 0; dot < height - row - 1 ; dot++)
            {
            printf(" ");
            }

            for (column = 0; column <= row; column++)
            {
            printf("#");
            }

            printf("  ");

            for (column = 0; column <= row; column++)
            {
            printf("#");
            }
        printf("\n");
    }
}