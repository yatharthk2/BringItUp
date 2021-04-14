#include<stdio.h>
 
struct student
{
    int sr_no,price;                                                              //rollnumber = srnum , name  = name , marks = price
    char name[25];
}cars[100],t;
 
void main()
{
    int i,j,n;
    printf("Enter the no of cars\n");
    scanf("%d",&n);
    printf("enter cars info as sr_no , name , price\n");
    for(i=0;i<n;i++)
    {
        scanf("%d %s %d",&cars[i].sr_no,cars[i].name,&cars[i].price);
    }
    
    for(i=0;i<n;i++)
    {
        for(j=0;j<n-1;j++)
        {
            if(cars[j].price<cars[j+1].price)
            {
                t=cars[j];
                cars[j]=cars[j+1];
                cars[j+1]=t;
            }
        }
    }
    
    printf("\ncars info in terms of price from highest to lowest\n");
    printf("\nsr_NO\t\tNAME\t\tprice\n");
    printf("-------------------------------------------------------------------------------\n");
    for(i=0;i<n;i++)
    {
        printf("%d\t\t\t%s\t\t\t%d\n",cars[i].sr_no,cars[i].name,cars[i].price);
    }
}