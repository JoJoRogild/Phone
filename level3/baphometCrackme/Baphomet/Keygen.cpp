#include <iostream>
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        cout << "Usage: " << argv[0] << " <yourname>" << endl;
        return 0;
    }

    string S(argv[1]);
    int Sum = 0, t;
    for (long i = 0; i < S.length(); ++i)
    {
        t = S[i];
        for (int j = 0; j < S[i] + 74; ++j)
            t = (137 * t + 187) % 2048;
        Sum += 666 * t * 666 * t;
    }

    S = to_string(Sum);
    if (Sum < 0 || S.length() < 9)
    {
        cout << "Sorry, your name are too ugly!" << endl;
        return 0;
    }

    string PW;
    long x = 0, xx;
    for (long i = 0; i < 9; ++i)
    {
        xx = S[i] - '0';
        if (x < xx)
            PW += string(xx - x, 'D');
        else if (x > xx)
            PW += string(x - xx, 'U');
        PW += "RR";
        x = xx;
    }

    PW.pop_back();
    cout << "Your serial is: " << PW << endl;
}