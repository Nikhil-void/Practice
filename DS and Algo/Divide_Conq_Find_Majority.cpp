#include <algorithm>
#include <iostream>
#include <vector>

using std::vector;

/*int get_majority_element(vector<int> &a, int left, int right) {
  if (left == right) return -1;
  if (left + 1 == right) return a[left];
  //write your code here
  return -1;
}*/

int get_majority_element(vector<int> &a, int left, int right) {
  if (left == right) return -1;
  if (left + 1 == right) return a[left];
  //write your code here
  int ind = (right) / 2;
  //std::cout << ind;
  std::sort(a.begin(), a.end());
  int count = 1;
  for (int i = 0; i < a.size() ; i++){
      if (count > ind){
          return a[i];
      }
      if(a[i] == a[i+1]){
          count++;
      }
      else{
          count = 1;
          if(i+1 > ind){
              //std::cout << "return" << std::endl;
              break;
          }
      }
  }
  return -1;
}


int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cin >> a[i];
  }
  std::cout << (get_majority_element(a, 0, a.size()) != -1) << '\n';
}
