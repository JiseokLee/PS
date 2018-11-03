#include <vector>
#include <algorithm>

using namespace std;

class Cryptography {
public:
    long long encrypt(vector <int> numbers) {
        long long ret = 1;
        sort(numbers.begin(), numbers.end());
        numbers[0]++;
        
        for (int i=0; i<numbers.size(); i++) {
            ret *= numbers[i];
        }

        return ret;
    }
};