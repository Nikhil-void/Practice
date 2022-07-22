#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::vector;
using std::max;

int compute_min_refills(int n, int dist, int tank, vector<int> & stops) {
    int current = 0; 
    int total = 0;
    stops.push_back(dist);
    for (int i = 0 ; i < n ; i++){
        if (i == 0){
            if(stops[i] > tank){
                return -1;
            }
        }
        if( (stops[i+1] - current) > tank ){
            current = stops[i];
            total += 1;
            //std::cout << current << ' ';
            if((stops[i+1] - current) > tank){
                return -1;
            }
        }
        else{
            if (stops[i] == current){
                return -1;
            }
        }
    }
    //std::cout << std::endl;
    return total;
}


int main() {
    int d = 0;
    cin >> d;
    int m = 0;
    cin >> m;
    int n = 0;
    cin >> n;

    vector<int> stops(n);
    for (size_t i = 0; i < n; ++i)
        cin >> stops.at(i);

    cout << compute_min_refills(n, d, m, stops) << "\n";

    return 0;
}
