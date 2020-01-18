#include<stdio.h>

unsigned long long int AweSum(int k, int n)
{
    unsigned long long int x[k+1][n+1];
    int i,j;

    for(i=0; i<=n; i++)
    {
        x[0][i] = i;
    }

    for(i=0; i<=k; i++)
    {
        x[i][0] = 0;
    }

    for(i=1; i<=k; i++)
    {
        for(j=1; j<=n; j++)
        {
            x[i][j] = x[i][j-1]+x[i-1][j];
        }
    }

    return x[k][n];


}


int main()
{
    int k,n;
    unsigned long long int result;
    scanf("%d%d",&k,&n);
    result = AweSum(k,n);
    printf("%llu",result);
}



