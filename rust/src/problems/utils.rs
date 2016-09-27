pub fn is_prime(n: i32) -> bool {
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
