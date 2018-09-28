#include <iostream>
#include <string>
using namespace std;

int calcDet(int a1, int b1, int a2, int b2, int a3, int b3)
{
    return (a1*b2+b1*a3+a2*b3)-(a3*b2+b3*a1+a2*b1);
}

int getPossibleTriangles(int n, int* x, int* y) {
    int res = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i+1; j < n; j++) {
            for (int k = j+1; k < n; k++) {
                if (calcDet(x[i], y[i], x[j], y[j], x[k], y[k])!=0) {
                    res++;
                }
            }
        }
    }
    return res;
}

int main() {
    int n;
    int* x = new int[n];
    int* y = new int[n];
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x[i] >> y[i];
    }
    cout << getPossibleTriangles(n, x, y) << endl;
    delete[] x;
    delete[] y;
    return 0;
}