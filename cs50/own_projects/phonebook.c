#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string isim = get_string("İsmin ne?\n");
    int yil = get_int("Hangi yilda dogdun?\n");
    int yas = 2024 - yil;
    int ay = get_int("%i'lik citir %s, %i'un kacinci ayinda dogdun?\n",yas, isim, yil);
    int gun = get_int("%i. ayin kacinci gununde dogdun?\n", ay);

    int gecenzaman = (((2023 - yil) * 365) + ((8 - ay) * 30) + (26 - gun) + 280);
    printf("Tek söyleceğim %i gun once annenle tanismis olabilirim\n", gecenzaman);
}
