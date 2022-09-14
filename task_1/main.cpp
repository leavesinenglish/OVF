#include <iostream>

template<class T>
T get_epsilon() {
    T epsilon = 1;
    while (!(1 + epsilon / 2 == 1 and 1 + epsilon != 1)) {
        epsilon /= 2;
    }
    return epsilon;
}

template<class T>
size_t get_num_of_digits() {
    T epsilon = 1;
    size_t i = 0;
    while (!(1 + epsilon / 2 == 1 and 1 + epsilon != 1)) {
        epsilon /= 2;
        i++;
    }
    return i;
}

template<class T>
size_t get_max_power() {
    T i = 1;
    size_t max_power = 0;
    while (10 * i != i) {
        i *= 10;
        max_power++;
    }
    return max_power;
}

template<class T>
int get_min_power() {
    T i = 1;
    int min_power = 0;
    while (i / 10 != i) {
        i /= 10;
        min_power--;
    }
    return min_power;
}

template<class T>
void comparison() {
    std::cout << "1 < 1 + e/2 is " << std::boolalpha << (1 < 1 + get_epsilon<T>() / 2) << std::endl;
    std::cout << "1 < 1 + e is " << std::boolalpha << (1 < 1 + get_epsilon<T>()) << std::endl;
    std::cout << "1 < 1 + e + e/2 is " << std::boolalpha << (1 < 1 + get_epsilon<T>() + get_epsilon<T>() / 2)
              << std::endl;
    std::cout << "1 + e/2 < 1 + e is " << std::boolalpha << (1 + get_epsilon<T>() / 2 < 1 + get_epsilon<T>())
              << std::endl;
    std::cout << "1 + e/2 < 1 + e + e/2 is " << std::boolalpha
              << (1 + get_epsilon<T>() / 2 < 1 + get_epsilon<T>() + get_epsilon<T>() / 2) << std::endl;
    std::cout << "1 + e < 1 + e + e/2 is " << std::boolalpha
              << (1 + get_epsilon<T>() < 1 + get_epsilon<T>() + get_epsilon<T>() / 2) << std::endl;
}

int main() {
    std::cout << "epsilon for float: "<< get_epsilon<float>() << std::endl;
    std::cout << "epsilon for double: "<< get_epsilon<double>() << std::endl;

    std::cout << "number of digits in mantissa for float: " << get_num_of_digits<float>() << std::endl;
    std::cout << "number of digits in mantissa for double: " << get_num_of_digits<double>() << std::endl;

    std::cout << "max and min power for float: " << get_max_power<float>() << "; " << get_min_power<float>() << std::endl;
    std::cout << "max and min power for double: " << get_max_power<double>() << "; " << get_min_power<double>() << std::endl;

    std::cout << "float: " << std::endl;
    comparison<float>();

    std::cout << "double: " << std::endl;
    comparison<double>();

    return 0;
}