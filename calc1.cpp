#include <iostream>

using namespace std;

int main()
{

    char op;

    float num1, num2;

    cout << "\nType a number option: ";

    cout << "\n1. Addition";

    cout << "\n2. Subtraction";

    cout << "\n3. Multiplication";

    cout << "\n4. Division\n";

    cin >> op;

    cout << "\nNow, write the first number please: ";

    cin >> num1;

    cout << "\nFinally, write the second number please: ";

    cin >> num2;

    switch (op)
    {
    case '1':

        cout << "The result is: " << num1 + num2;

        break;

    case '2':

        cout << "The result is: " << num1 - num2;

        break;

    case '3':

        cout << "The result is: " << num1 * num2;

        break;

    case '4':

        cout << "The result is: " << num1 / num2;

        break;
    }
}