#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;

bool sortcol(const vector<double>& v1, const vector<double>& v2)
{
    return v1[2] > v2[2];
}

double get_optimal_value(int n, int capacity, vector<vector<double>> values) {
    double return_val = 0;
    for(int i=0; i<n; i++){
        double num1 = (double) values[i][0] / (double) values[i][1];
        //std::cout << (double) values[i][0] << ' ' << (double) values[i][1] << ' ' << (double) values[i][0] / (double) values[i][1] << std::endl;
        values[i].push_back(num1);
    }
    
    std::sort(values.begin(), values.end(), sortcol);

    /*for(int i=0; i<n; i++){
        std::cout << values[i][0] << ' ' << values[i][1] << ' ' << values[i][2] << std::endl;
    }*/
  
    for (int i = 0; i<n; i++){
        if (values[i][1] <= capacity){
            return_val += values[i][0];
            capacity -= values[i][1];
        }
        else{
            return_val += capacity * values[i][2];
            break;
        }
    }

    return return_val;
}

int main() {
  int n;
  int capacity;
  std::cin >> n >> capacity;
  vector<vector<double>> values(n);
  double temp;
  for (int i = 0; i < n; i++) {
    std::cin >> temp;
    values[i].push_back(temp) ;
    std::cin >> temp;
    values[i].push_back(temp) ;
  }

  double optimal_value = get_optimal_value(n, capacity, values);

  std::cout.precision(10);
  std::cout << optimal_value << std::endl;
  return 0;
}
