#include <iostream>
#include <cassert>
#include <vector>

using std::vector;

int binary_search(const vector<int> &a, int x) {
  int left = 0, right = (int)a.size() - 1; 
  //int count = 0;
  while (left <= right){
      //count++;
      if (left==right){
          if(a[left] == x){
              return left;
          }
          else{
              return -1;
          }
      }
      int mid = ((right - left) / 2) + left;
      //std::cout << mid << '-' << left << '-' << right << std::endl ;
      if (a[mid] == x){
          return mid;
      }
      if(a[mid] > x){
          right = mid - 1;
      }
      if(a[mid] < x){
          left = mid + 1; 
      }

  }
  return -1;
}

int linear_search(const vector<int> &a, int x) {
  for (size_t i = 0; i < a.size(); ++i) {
    if (a[i] == x) return i;
  }
  return -1;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); i++) {
    std::cin >> a[i];
  }
  int m;
  std::cin >> m;
  vector<int> b(m);
  for (int i = 0; i < m; ++i) {
    std::cin >> b[i];
  }
  for (int i = 0; i < m; ++i) {
    //replace with the call to binary_search when implemented
    int op = binary_search(a, b[i]);
    while(1){
        if(a[op] == a[op-1]){
            op--;
        }
        else{
            break;
        }
    }
    std::cout << op << ' ';
  }
  /*std::cout << " Binary " << std::endl;
  for (int i = 0; i < m; ++i) {
    //replace with the call to binary_search when implemented
    std::cout << linear_search(a, b[i]) << ' ';
  }
  std::cout << " Linear " << std::endl;*/
}
