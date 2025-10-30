#include <cs50.h>
#include <stdio.h>

int main(void)
{
    printf("bu program sadece american express/visa/mastercard kartlarını test edebilir\n");

    long card = get_long("KART NUMARASI\n");

    long first, second, third, fourth, fifth, sixth, seventh, eight, nineth, tenth, eleventh, twelveth, thirteenth, fourteenth, fifteenth, sixteenth ;
    long firstp, secondp, thirdp, fourthp, fifthp, sixthp, seventhp, eightp, ninethp, tenthp, eleventhp, twelvethp, thirteenthp, fourteenthp, fifteenthp, sixteenthp ;


    first = card % 10;

    secondp = (card - first) / 10;
    second = secondp % 10;

    thirdp = (secondp - second) / 10;
    third = (thirdp)  % 10;

    fourthp = (thirdp - third) / 10;
    fourth = (fourthp) % 10;

    fifthp = (fourthp - fourth) / 10;
    fifth = (fifthp) % 10;

    sixthp = (fifthp - fifth) / 10;
    sixth = (sixthp) % 10;

    seventhp = (sixthp - sixth) / 10;
    seventh = (seventhp) % 10;

    eightp = (seventhp - seventh) / 10;
    eight = (eightp) % 10;

    ninethp = (eightp - eight) / 10;
    nineth = (ninethp) % 10;

    tenthp = (ninethp - nineth) / 10;
    tenth = (tenthp) % 10;

    eleventhp = (tenthp - tenth) / 10;
    eleventh = (eleventhp) % 10;

    twelvethp = (eleventhp - eleventh) / 10;
    twelveth = (twelvethp) % 10;

    thirteenthp = (twelvethp - twelveth) / 10;
    thirteenth = (thirteenthp) % 10;

    fourteenthp = (thirteenthp - thirteenth) / 10;
    fourteenth = (fourteenthp) % 10;

    fifteenthp = (fourteenthp - fourteenth) / 10;
    fifteenth = (fifteenthp) % 10;

    sixteenthp = (fifteenthp - fifteenth) / 10;
    sixteenth = (sixteenthp) % 10;

//lets calculate the correctness here

//first we have to do the multiplication and then the seperation of digits

    int msecond = second * 2;
    int msecondone = msecond % 10;
    int msecondtwo = (msecond - msecondone) / 10;

    int mfourth = fourth * 2;
    int mfourthone = mfourth % 10;
    int mfourthtwo = (mfourth - mfourthone) / 10;

    int msixth = sixth * 2;
    int msixthone = msixth % 10;
    int msixthtwo = (msixth - msixthone) / 10;

    int meight = eight * 2;
    int meightone = meight % 10;
    int meighttwo = (meight - meightone) / 10;

    int mtenth = tenth * 2;
    int mtenthone = mtenth % 10;
    int mtenthtwo = (mtenth - mtenthone) / 10;

    int mtwelveth = twelveth * 2;
    int mtwelvethone = mtwelveth % 10;
    int mtwelvethtwo = (mtwelveth - mtwelvethone) / 10;

    int mfourteenth = fourteenth * 2;
    int mfourteenthone = mfourteenth % 10;
    int mfourteenthtwo = (mfourteenth - mfourteenthone) / 10;

    int msixteenth = sixteenth * 2;
    int msixteenthone = msixteenth % 10;
    int msixteenthtwo = (msixteenth - msixteenthone) / 10;

// lets add them up now

    int sumsixteendigiteverytwo = (msecondone + msecondtwo + mfourthone + mfourthtwo + msixthone + msixthtwo + meightone + meighttwo + mtenthone + mtenthtwo + mtwelvethone + mtwelvethtwo + mfourteenthone + mfourteenthtwo + msixteenthone + msixteenthtwo);
    int sumsixteendigitother = (first + third + fifth + seventh + nineth + eleventh + thirteenth + fifteenth);

    int sumfifteendigiteverytwo = sumsixteendigiteverytwo - (msixteenthone + msixteenthtwo);
    int sumfifteendigitother = sumsixteendigitother;

    int sumthirteendigiteverytwo = sumfifteendigiteverytwo - (mfourteenthone + mfourteenthtwo);
    int sumthirteendigitother = sumsixteendigitother - fifteenth;



// and now lets set the correctness values

    short correctness = 0;

    if (sixteenth > 0)
    {
            if (((sumsixteendigiteverytwo + sumsixteendigitother) % 10) == 0)
            {
                correctness = 1;
            }

            else
            {
                correctness = 0;
            }
    }


    else if (fifteenth > 0)
    {
            if (((sumfifteendigiteverytwo + sumfifteendigitother) % 10) == 0)
            {
                correctness = 1;
            }

            else
            {
                correctness = 0;
            }

    }

    else if (thirteenth > 0)
    {
            if (((sumthirteendigiteverytwo + sumthirteendigitother) % 10) == 0)
            {
                correctness = 1;
            }

            else
            {
                correctness = 0;
            }
    }

    else
    {
        correctness = 0;
    }



// if they are valid this is the next stage, check the validness here


if (correctness == 1)
{
    if (sixteenth > 0)
    {
        if (sixteenth == 5)
        {
            if (fifteenth == 0)
            {
                printf("INVALID\n");
            }

            else if (fifteenth < 6)
            {
                printf("MASTERCARD\n");
            }

            else
            {
                printf("INVALID\n");
            }
        }


        else if (sixteenth == 4)
        {
            printf("VISA\n");
        }

        else
        {
            printf("INVALID\n");
        }
    }




    else if (fifteenth > 0)
    {
        if (((fifteenth * 10) + fourteenth) == 34)
        {
            printf("AMERICAN EXPRESS\n");
        }

        else if (((fifteenth * 10) + fourteenth) == 37)
        {
            printf("AMERICAN EXPRESS\n");
        }

        else
        {
            printf("INVALID\n");
        }
    }


    else if (thirteenth > 0)
    {
        if (thirteenth == 4)
        {
            printf("VISA\n");
        }

        else
        {
            printf("INVALID\n");
        }
    }

    else
    {
        printf("INVALID\n");
    }
}


else
{
    printf("INVALID\n");
}



}
