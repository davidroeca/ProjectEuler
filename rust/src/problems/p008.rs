use std::fs::File;
use std::io::{BufRead, BufReader, Error};
use problems::utils;

fn dat_file_to_num_array(file_path: &str) -> Result<Vec<i64>, Error> {
    let f = try!(File::open(file_path));
    let reader = BufReader::new(f);
    let mut nums = Vec::new();
    for line in reader.lines() {
        match line {
            Ok(valid_line) => {
                for b in valid_line.bytes() {
                    match utils::byte_to_i64(b) {
                        Ok(num) => nums.push(num),
                        Err(e) => return Err(e),
                    }
                }
            },
            Err(e) => return Err(e),
        }
    }
    Ok(nums)
}

fn get_max_prod<'a>(arr: &'a [i64]) -> i64 {
    // returns the max left index
    let mut max_prod = 0i64;
    let mut left_idx = 0usize;
    let length = arr.len();
    while left_idx + 12 < length {
        let prod = arr[left_idx..left_idx+ 13].into_iter().fold(1, |a,b| a * b) as i64;
        if prod > max_prod {
            max_prod = prod;
        }
        left_idx += 1;
    }
    max_prod
}

#[allow(dead_code)]
pub fn solution() -> Option<i64> {
    match dat_file_to_num_array("problem_files/p008.txt") {
        Ok(nums) => Some(get_max_prod(&nums)),
        Err(_) => None,
    }
}

