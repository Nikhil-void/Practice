#include <iostream>

int get_change(int m) {
    long long coins = 0;
    while(m > 0){
        if (m >= 10){
            coins += m / 10;
            m = m % 10;
        }
        else if (m >= 5){
            coins += m / 5;
            m = m % 5;
        }
        else{
            coins += m;
            break;
        }
  }
  return coins;
}

int main() {
  int m;
  std::cin >> m;
  std::cout << get_change(m) << '\n';
}
