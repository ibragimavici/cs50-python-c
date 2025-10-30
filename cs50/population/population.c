#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int n;
    do
    {
        n = get_int("start size:\n");
    }
    while (n < 9);
    // TODO: Prompt for end size
    int k;
    do
    {
        k = get_int("end size:\n");
    }
    while (n > k);
    // TODO: Calculate number of years until we reach threshold
    int years;
    years = 0;
    do
    {
        years = years + 1;
        n = n + (n / 3) - (n / 4);
    }
    while (n < k);

    // TODO: Print number of years

    printf("end population will be reached in %i years\n", years);
}

