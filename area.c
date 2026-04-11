#include<stdio.h>
int main()
{
    int radius;
    printf("Enter the radius of the circle: ");
    scanf("%d", &radius);
    float area = 3.14 * radius * radius;
    printf("The area of the circle is: %.2f\n", area);
    return 0;
}