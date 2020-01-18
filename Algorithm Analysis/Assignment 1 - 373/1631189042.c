#include<stdio.h>

struct activity
{
    int start,finish;
} inputActivity[100001],resultActivity[100001],key[5];


int main()
{
    int m; //ending point of the targeted segment

    scanf("%d",&m);

    int s,f; //temporary for start and finish variable
    int totalActivity = 0;
    int i,j;

    for(i=0; ; i++)
    {
        scanf("%d%d",&s,&f);

        if (s == 0 && f == 0)
        {
            break;
        }

        totalActivity++;
        inputActivity[i].start = s;
        inputActivity[i].finish = f;
    }

    //for sorting I've used insertion sort

    for(i= 1; i<totalActivity; i++)
    {
        key[0] = inputActivity[i];
        j = i-1;

        while(j>=0 && inputActivity[j].start > key[0].start)
        {
            inputActivity[j+1] = inputActivity[j];
            j--;
        }
        inputActivity[j+1] = key[0];
    }

    //main activity selection segment

    int totalSolutionActivity = 0;
    int resultPosition = 0; //ending point that a selected activity can cover
    int countResult =0; //index for resultActivity
    resultActivity[countResult].finish = 0; //initialization for the first iteration
    int temp =-1; //for initializing the  inner loop's j's value


    if(inputActivity[0].start<=0)
    {
        for(i = 0; i<totalActivity; i++)
        {

            if(resultPosition >=m)
            {
                break;
            }

            for(j = temp+1; inputActivity[j].start<=resultPosition; j++)
            {
                if(inputActivity[j].finish>resultActivity[countResult].finish)
                {
                    resultActivity[countResult] = inputActivity[j];
                    temp = j;
                }
            }
            resultPosition = resultActivity[countResult].finish;
            countResult++;
        }
    }


    if(resultPosition >=m)
    {
        printf("%d\n",countResult);
        for(i=0; i<countResult; i++)
        {
            printf("%d %d",resultActivity[i].start,resultActivity[i].finish);

            if(i<countResult-1)
            {
                printf("\n");
            }
        }
    }
    else
    {
        printf("0");
    }


}
