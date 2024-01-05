#include<stdio.h>
int main(){
    float height, weight, BMI;
    printf("請輸入身高(cm): ");
    scanf("%f", &height);
    printf("請輸入體重(kg): ");
    scanf("%f", &weight);
    height = height / 100.0;
    BMI = weight / (height * height);
    printf("BMI = %f", BMI);

	return 0;
}
