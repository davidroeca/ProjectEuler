fn fib_even_sum(max_num: i32) -> i32 {
    let mut i1 = 1i32;
    let mut i2 = 1i32;
    let mut sum = 0i32;
    while i2 < max_num {
        if i2 % 2 == 0 {
            sum += i2;
        }
        let tmp = i1;
        i1 = i2;
        i2 = tmp + i2;
    }
    sum
}

#[allow(dead_code)]
pub fn solution() -> i32 {
    fib_even_sum(4e6 as i32)
}
