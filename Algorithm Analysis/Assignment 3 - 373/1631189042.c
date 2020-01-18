#include<stdio.h>

int v,e;
int g[200][200];
int visit[200];
int color[200];

int biColor(int u)
{
    visit[u]=1;
    int i;
    for(i=0; i<v; i++)
    {
        if(g[u][i]==1)
        {
            if(visit[i]==1)
            {
                if(color[u]==color[i])
                {
                    return 0;
                }
            }
            else
            {
                color[i]=-1*color[u];
                biColor(i);
            }
        }

    }
    return 1;
}
int main()
{
    int i,j;
    int s,d,result;

    scanf("%d%d",&v,&e);

    for(i=0; i<v; i++)
    {
        visit[i] = 0;
        color[i] = 0;
    }

    for(i=0; i<e; i++)
    {
        scanf("%d%d",&s,&d);

        g[s][d]=1;
        g[d][s]=1;
    }

    color[s]=1;
    result = biColor(s);

    if(result == 1)
    {
        printf("Yes");
    }
    else
    {
        printf("No");
    }


}


