#include <iostream>

using namespace std;

class Person{
private:
	int age;
public:
	Person();
	Person(int n);
	~Person();
	void setAge(int n);
};
Person::Person(){
                cout << "建立一個Person物件 年齡為0\n";
}
Person::Person(int n){
                cout << "建立一個Person物件 年齡為" << n << "\n";
                setAge(n);
}
void Person::setAge(int n){
                   printf("david: setAge(), set age = %d\n",n);
                   age=n;
}
Person::~Person(){
                cout << "清除一個Person物件\n";
}

class Phone{
private:
        int phone_state;
public:
       Phone();
       ~Phone();
       void setSwitch1(int state);
};

Phone::Phone()
{
     printf("Create an object for Phone\n");
}

Phone::~Phone()
{
     printf("Delete an object for Phone\n");
}

void Phone::setSwitch1(int state)
{
    phone_state=state;
    printf("set state = %d\n",state);
}

class Printer{
private:
        int printer_state;
public:
       Printer();
       ~Printer();
       void setSwitch2(int state);
};

Printer::Printer()
{
     printf("Create an object for Printer\n");
}

Printer::~Printer()
{
     printf("Delete an object for Printer\n");
}

void Printer::setSwitch2(int state)
{
    printer_state=state;
    printf("set state = %d\n",state);
}

class Fax : public Phone, public Printer{
private:
        int fax_state;
public:
       Fax();
       ~Fax();
       void setSwitch3(int state);
};

Fax::Fax()
{
     printf("Create an object for Fax\n");
}

Fax::~Fax()
{
     printf("Delete an object for Fax\n");
}

void Fax::setSwitch3(int state)
{
    fax_state=state;
    printf("set state = %d\n",state);
}

       

int main() {
    cout << " hello\n";
    Person Wang;
    Person Li;
    Person Wang2(20);
    Person Li2(15);
    Person* person1 = new Person;              //產生物件 
    cout << " hello again\n";
    delete person1;                            //刪除物件
    
    int* pNum1 = new int;
    delete pNum1;
    
    int* pNum2 = (int*) malloc(sizeof(int));
    free(pNum2);

    int* pNum3 = new int[10];
    delete [] pNum3;
    
    Person* person2;
    person2 = new Person[10];              //產生物件 
    cout << " hello again\n";
    delete [] person2;                     //刪除物件
    
    //Phone myPhone1;
    //Printer myPrinter1;
    Fax myFax1;
    
    myFax1.setSwitch1(1);
    myFax1.setSwitch2(2);    
    myFax1.setSwitch3(3);
    
    
    
    /*
    
    Phone* myPhone2 = new Phone;
    Printer* myPrinter2 = new Printer;
    Fax* myFax2 = new Fax;
    
    delete myPhone2;
    delete myPrinter2;
    delete myFax2;
    */
    
   
    
    system("pause");
}
