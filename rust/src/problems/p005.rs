use std::collections::HashMap;

fn prime_factors(n: i32) -> HashMap<i32, i32> {
    let mut current_num = n;
    let mut prime_factors = HashMap::new();
    if current_num % 2 == 0 {
        while current_num > 0 && current_num % 2  == 0 {
            let counter = prime_factors.entry(2).or_insert(0);
            *counter += 1;
            current_num /= 2;
        }
    }
    let mut current_factor = 3;
    while current_num > 1 {
        if current_num % current_factor == 0 {
            while current_num % current_factor == 0 {
                let counter = prime_factors.entry(current_factor).or_insert(0);
                *counter += 1;
                current_num /= current_factor;
            }
        }
        current_factor += 2;
    }
    prime_factors
}

fn joint_prime_factors(min: i32, max: i32) -> HashMap<i32, i32> {
    let mut overall = HashMap::new();
    for i in min..max+1 {
        let cur_factors = prime_factors(i);
        for k in cur_factors.keys() {
            let cur_reps = *cur_factors.get(k).unwrap_or(&0);
            let cur_max_reps = *overall.get(k).unwrap_or(&0);
            if cur_reps > cur_max_reps {
                overall.insert(*k, cur_reps);
            }
        }
    }
    overall
}

fn smallest_evenly_divisible(min: i32, max: i32) -> i32 {
    let joint_factors = joint_prime_factors(min, max);
    joint_factors.keys()
        .map(|k| k.pow(joint_factors[k] as u32)).fold(1, |a,b| a * b)
}

#[allow(dead_code)]
pub fn solution() -> i32 {
    smallest_evenly_divisible(1, 20)
}
