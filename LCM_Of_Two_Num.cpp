#include <iostream>

long long lcm_naive(int a, int b) {
  for (long l = 1; l <= (long long) a * b; ++l)
    if (l % a == 0 && l % b == 0)
      return l;

  return (long long) a * b;
}

long long lcm_fast(long long a, long long b) {
    long long larger;
    long long smaller;
    long long num;
    if (a > b){
        larger = a;
        smaller = b;
    }
    else {
         larger = b;
        smaller = a;
    }
    for(int i = 1; i <= larger; i++){
        num = larger*i;
        if (num % smaller == 0){
            break;
        }
    }
    return num;
}

int main() {
  long long a, b;
  std::cin >> a >> b;
  //std::cout << lcm_naive(a, b) << std::endl;
  std::cout << lcm_fast(a, b) << std::endl;
  return 0;
}
