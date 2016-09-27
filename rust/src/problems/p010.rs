use problems::utils;

fn sum_primes_below(max: i64) -> i64 {
    if max < 2 {
        0
    } else if max == 2 {
        2
    } else {
        let mut sum = 2i64;
        let mut cur_candidate = 1i64;
        while cur_candidate + 2 < max {
            cur_candidate += 2;
            if utils::is_prime(cur_candidate as i32) {
                sum += cur_candidate;
            }
        }
        sum
    }
}

#[allow(dead_code)]
pub fn solution() -> i64 {
    sum_primes_below(2e6 as i64)
}
