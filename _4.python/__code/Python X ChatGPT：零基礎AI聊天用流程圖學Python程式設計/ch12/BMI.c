#include<stdio.h>
int main(){
    float height, weight, BMI;
    printf("�п�J����(cm): ");
    scanf("%f", &height);
    printf("�п�J�魫(kg): ");
    scanf("%f", &weight);
    height = height / 100.0;
    BMI = weight / (height * height);
    printf("BMI = %f", BMI);

	return 0;
}
