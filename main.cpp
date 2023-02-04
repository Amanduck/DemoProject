#include <iostream>
#include <math.h>
#include <string>
#include <string.h>

using namespace std;
int choice, k;
double a, b, c, delta, x1, x2;
string p;

int main()
{
    cout<<"MENU DZIAŁAŃ Z FUNKCJI KWADRATOWEJ"<<endl<<"1. OBLICZ MIEJSCA ZEROWE"<<endl<<"2. WZORY VIETTE'A"<<endl<<"3. FUNKCJA Z PARAMETREM"<<endl<<"4. FUNKCJA Z PARAMETREM I WARTOSCIA BEZWZGLEDNA"<<endl<<"5. FUNKCJA OD M (DYSKUSJA)"<<endl<<"Twoj wybor: ";
    cin>>choice;
        switch (choice)
        {
            case 1:
            {
        cout<<"Funkcja kwadratowa ma formę y=ax^2+bx+c"<<endl;
        cout<<"Podaj a: ";
        cin>>a;
        cout<<endl<<"Podaj b: ";
        cin>>b;
        cout<<endl<<"Podaj c: ";
        cin>>c;
        if (a==0)
        {
        cout<<endl<<"Twoja funkcja ma postac liniowa.";
        }
    else
    {
        delta=b*b-4*a*c;
    

        if (delta<0)
        {
        cout<<endl<<"Delta mniejsza od 0, brak miejsc zerowych. Delta: "<<delta;
        }
        else if (delta==0) 
        {
        x1=(-b)/2*a;
        cout<<endl<<"Delta = 0, jej jedyne miejsce zerowe to: "<<x1;
         }
        else
        {
        x1=(-b+sqrt(delta))/2*a;
        x2=(-b-sqrt(delta))/2*a;
        cout<<endl<<"Delta = "<<delta<<", a jej miejsca zerowe wynosza: "<<x1<<" oraz "<<x2<<". "<<endl;
            p="inf";
            cout<<"Wspolczynnik a jest wiekszy od 0 i funckja ma 2 miejsca zerowe."<<endl;
            cout<<"Funkcja ma wartosci>0 na przedzialach: xe("<<p<<", "<<x2<<") u ("<<x1<<", "<<p<<").";
            cout<<"Funkcja ma wartosci<0 na przedzialach: xe("<<x2<<", "<<x1<<").";
            cout<<endl<<endl<<endl;
        }
    
        break;
    }
            
    
    default:
        break;
            }
            
        }


    return 0;}