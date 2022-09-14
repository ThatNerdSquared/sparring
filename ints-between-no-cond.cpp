#include <iostream>

int main() {
    int a,b;
    std::cin >> a >> b;
    std::cout << std::max(0, b-a+1);
}

/*
// debashis' implementation using sign bit for maxing
int main() 
{
    int a, b;
    cin >> a >> b;
    int result = ((unsigned int)(a-b) >> (sizeof(int) * 8 - 1)) * (b - a + 1);
    cout << result << endl;
}
*/