#include <iostream>
#include <stdlib.h>
using namespace std;

class Calculator
{

private:
    float x, y;

public:
    Calculator(float _x, float _y)
    {
        x = _x;
        y = _y;
    };

    void Addition();

    void Subtraction();

    void Multiplication();

    void Division();
};

int main()
{

    int opt;

    float num1, num2;

    Calculator *operation;

    /*  system("cls"); */

    cout << "Enter an option:" << endl;

    cout << "1. Addition\n";

    cout << "2. Subtraction\n";

    cout << "3. Multiplication\n";

    cout << "4. Division\n";

    cin >> opt;

    /* system("cls"); */

    while (opt != 0)

    {

        switch (opt)
        {
        case 1:

            cout << "Write the first number: ";
            cin >> num1;

            cout << "Write the second number: ";
            cin >> num2;

            operation = new Calculator(num1, num2);

            operation->Addition();

            /*  system("pause");
             system("cls"); */

            break;

        case 2:

            cout << "Write the first number: ";
            cin >> num1;

            cout << "Write the second number: ";
            cin >> num2;

            operation = new Calculator(num1, num2);

            operation->Subtraction();

            /* system("pause");
            system("cls"); */

            break;

        case 3:

            cout << "Write the first number: ";
            cin >> num1;

            cout << "Write the second number: ";
            cin >> num2;

            operation = new Calculator(num1, num2);

            operation->Multiplication();

            /*  system("pause");
             system("cls"); */

            break;

        case 4:

            cout << "Write the first number: ";
            cin >> num1;

            cout << "Write the second number: ";
            cin >> num2;

            operation = new Calculator(num1, num2);

            operation->Division();

            /*  system("pause");
             system("cls"); */

            break;
        }

        cout << "Want to do something else?" << endl;

        cout << "Type the option:" << endl;

        cout << "1. Addition\n";

        cout << "2. Subtraction\n";

        cout << "3. Multiplication\n";

        cout << "4. Division\n";

        cout << "0. Go out\n";

        cin >> opt;

        /*  system("pause");
         system("cls"); */
    }

    return 0;
}

void Calculator ::Addition()
{

    float result = x + y;

    cout << "Result = " << result << endl;
}

void Calculator ::Subtraction()
{
    float result = x - y;

    cout << "Result = " << result << endl;
}

void Calculator ::Multiplication()
{
    float result = x * y;

    cout << "Result = " << result << endl;
}

void Calculator ::Division()
{
    float result;

    if (y != 0)
    {
        result = x / y;

        cout << "Result = " << result << endl;
    }
    else
    {
        cout << "Division by zero is illegal" << endl;
    }
}