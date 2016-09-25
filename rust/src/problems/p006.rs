fn sum_squares(min: i32, max: i32, step: i32) -> i32 {
    (min..max)
        .filter(|i| (i - min) % step == 0)
        .map(|i| i.pow(2))
        .fold(0, |a,b| a+b)
}

fn square_sum(min: i32, max: i32, step: i32) -> i32 {
    (min..max)
        .filter(|i| (i - min) % step == 0)
        .fold(0, |a,b| a+b).pow(2)
}

#[allow(dead_code)]
pub fn solution() -> i32 {
    square_sum(1, 100, 1) - sum_squares(1, 100, 1)
}
