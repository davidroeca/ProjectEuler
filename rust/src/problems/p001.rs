fn sum_fizz_buzz(max_num: i32) -> i32 {
    (1..max_num).filter(|i| i % 5 == 0 || i % 3 == 0).fold(0, |a,b| a+b)
}

#[allow(dead_code)]
pub fn solution() -> i32 {
    sum_fizz_buzz(1000)
}
