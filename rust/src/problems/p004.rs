fn to_digits(n: i32) -> Vec<i32> {
    let mut cur = n;
    let mut v = Vec::new();
    while cur > 0  {
        v.push(cur % 10);
        cur /= 10;
    }
    v.reverse();
    return v;
}

fn is_palindrome(n: i32) -> bool {
    let digits = to_digits(n);
    let length = digits.len();
    (0..length/2)
        .map(|i| digits[i] == digits[length - i - 1])
        .fold(true, |i,j| i && j)
}

#[allow(dead_code)]
pub fn solution() -> Option<i32> {
    let mut max_prod = 0;
    for i in (100..1000).rev() {
        for j in (100..i).rev() {
            let prod = i * j;
            if is_palindrome(prod) {
                max_prod = if prod > max_prod {prod} else {max_prod};
            }
        }
    }
    if max_prod > 0 {
        Some(max_prod)
    }
    else {
        None
    }
}
