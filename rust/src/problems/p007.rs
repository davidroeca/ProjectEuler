use problems::utils;

fn find_nth_prime(n: i32) -> Option<i32> {
    if n < 1 {
        return None
    }
    if n == 1 {
        Some(2)
    } else {
        let mut count = 1;
        let mut cur_candidate = 1;
        while count < n {
            cur_candidate += 2;
            if utils::is_prime(cur_candidate) {
                count += 1
            }
        }
        Some(cur_candidate)
    }
}

#[allow(dead_code)]
pub fn solution() -> i32 {
    find_nth_prime(10001).unwrap_or(-1)
}
