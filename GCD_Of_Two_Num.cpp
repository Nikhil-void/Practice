#include <iostream>

int gcd_naive(int a, int b) {
  int current_gcd = 1;
  for (int d = 2; d <= a && d <= b; d++) {
    if (a % d == 0 && b % d == 0) {
      if (d > current_gcd) {
        current_gcd = d;
      }
    }
  }
  return current_gcd;
}

long long gcd_fast(long long a, long long b){
    long long larger;
    long long smaller;
    if (a > b){
        larger = a;
        smaller = b;
    }
    else {
         larger = b;
        smaller = a;
    }
    while (smaller != 0 && smaller != 1){
        long long remainder = larger % smaller;
        larger = smaller;
        smaller = remainder;
        
       
        //std::cout << "smaller: " << smaller << " Larger: " << larger << std::endl;
    }
     if (smaller == 1){
            larger = 1;
        }
    return larger;
}

int main() {
  long long a, b;
  std::cin >> a >> b;
  //std::cout << gcd_naive(a, b) << std::endl;
  std::cout << gcd_fast(a, b) << std::endl;
  return 0;
}
