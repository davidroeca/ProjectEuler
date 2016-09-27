fn find_pythagorean_triplets_with_sum(sum: i32) -> Vec<(i32, i32, i32)> {
    let mut out = Vec::new();
    for a in 1..sum-1 {
        for b in 1..a {
            let c = sum - a - b;
            if c * c == a * a + b * b {
                out.push((a,b,c));
            }
        }
    }
    out
}

#[allow(dead_code)]
pub fn solution() -> Vec<i32> {
    find_pythagorean_triplets_with_sum(1000).into_iter()
        .map(|i| {
            let (a,b,c) = i;
            a * b * c
        }).collect()
}
