fn find_largest_prime_factor(num: i64) -> i64 {
    let mut current_num = num;
    let mut last_factor = 1;
    // first, make the number odd
    if current_num % 2 == 0 {
        while current_num > 1 && current_num % 2 == 0 {
            current_num /= 2;
        }
        last_factor = 2;
    }
    let mut current_factor = 3;
    while current_num > 1 {
        if current_num % current_factor == 0 {
            while current_num % current_factor == 0 {
                current_num /= current_factor;
            }
            last_factor = current_factor;
        }
        current_factor += 2;
    }
    last_factor
}

#[allow(dead_code)]
pub fn solution() -> i64 {
    find_largest_prime_factor(600851475143i64)
}
