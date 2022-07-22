#include <iostream>
#include <algorithm>
using namespace std;

int get_change(int m, int arr[], int res[]) {
  //cout<<m<<"M"<<endl;
  int ans = 10000;
  if (m == 0) return 0;
  if(res[m] != -1){
    //for(int i=0; i<600; i++){
    //std::cout << res[i] << ' ';
    //}
    //std::cout << endl << endl << m << endl << endl;
   return res[m];
  }
  for (int i = 0; i < 3 ; i++){
    if(m-arr[i] < 0){
      continue;
    }
    int subans = get_change(m-arr[i], arr, res);
    //cout<<subans<< ' ';
    if(subans != 10000 && subans+1 < ans){
      ans = subans + 1;
    }
  }
  //cout<<endl<<endl;
  res[m] = ans;
  return ans;
}


int main() {
  int m;
  int arr[] = {1,3,4};
  std::cin >> m;
  
  

  /*for(int i = 0; i< 1010 ; i++){
    int res[i+1];
    fill(res, res+ (i+1), -1);
    res[0] = 0;
    int op =  get_change(i, arr, res);
    //cout << op << ' ';
    int op2 = minCoins(arr, 3, i);
    //cout << op2 << endl;
    if (op != op2){
      cout<< i << ' ' << op << op2 << endl;
      break;
    }
    else{
      cout<<"same"<<i<<endl;
    }
  }*/

  int res[m+1];
  fill(res, res+ (m+1), -1);
  res[0] = 0;
  int op =  get_change(m, arr, res);
  //int op2 = minCoins(arr, 3, m);
  cout << op << endl;
  //cout << op2 << endl;
  //for(int i=0; i<m+1; i++){
  // std::cout << i << ' ' << res[i] << endl;
  //}
}

