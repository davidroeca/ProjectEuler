fn is_prime(n: i32) -> bool {
    if n < 2 {
        false
    } else if n == 2 {
        true
    } else if n % 2 == 0 {
        false
    } else {
        let mut check = 3;
        while check * check <= n {
            if n % check == 0 {
                return false;
            }
            check += 2
        }
        true
    }
}

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
            if is_prime(cur_candidate) {
                count += 1
            }
        }
        println!("{}", count);
        Some(cur_candidate)
    }
}

#[allow(dead_code)]
pub fn solution() -> i32 {
    find_nth_prime(10001).unwrap_or(-1)
}
