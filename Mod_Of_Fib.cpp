#include <iostream>

long long get_fibonacci_fast(long long n, long long m, long long* pattern) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;

    /*for (long long i = 0; i < n - 1; ++i) {
        //std::cout << (long long) current % m << ' ';
        //std::cout << (long long) current << ' ';
        long long tmp_previous = previous;
        previous = current;
        current = (tmp_previous + current)% m ;
        std::cout << (long long) current << ' ';
        if (current == 1){
            std::cout << "\n" << " CURRENT I: " << i << "\n";
        }
    }*/
    long long value = 0;
    long long i = 2;
    while (i <= n){
        long long tmp_previous = previous;
        previous = current;
        current = (tmp_previous + current)% m ;
        if ((i > 2) && tmp_previous == 0 && current == 1){
            *pattern = 1;
            value = i-2;
            break;
        }
        i++;
    }
    if (value != 0){
        current = n % value;
    }
    return current;

}

int main() {
    long long n, m;
    std::cin >> n >> m;
    long long pattern = 0;
    long long ans = get_fibonacci_fast(n, m, &pattern);
    if (pattern == 0){
        std::cout << ans << '\n';
    }
    else{
        std::cout << get_fibonacci_fast(ans, m, &pattern) << '\n';
    }
    return 0;
}
