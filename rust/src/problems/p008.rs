use std::fs::File;
use std::io::{BufRead, BufReader};

fn byte_to_i32(b: u8) -> Result<i32, &'static str> {
    if b < 48u8 || b > 57u8 {
        Err("Byte in question is not a number")
    } else {
        Ok((b - 48u8) as i32)
    }
}

fn dat_file_to_num_array(file_path: &str) -> Result<Vec<i32>, &'static str> {
    let f = try!(File::open(file_path));
    let mut reader = BufReader::new(f);
    let mut nums = Vec::new();
    for line in reader.lines() {
        match line {
            Ok(valid_line) => {
                for b in valid_line.bytes() {
                    match byte_to_i32(b) {
                        Ok(num) => nums.push(num),
                        Err(s) => return Err(s),
                    }
                }
            },
            Err(s) => return Err(s),
        }
    }
    Ok(nums)
}

fn get_max_left_idx<'a>(vec: &'a Vec<i32>) -> i32 {
    // returns the max left index
    let mut left_idx = 0;
    let mut max_prod = 0;
    let mut max_left_idx = 0;
    let length = vec.len();
    while left_idx + 12 < length {
        let prod = vec[left_idx..left_idx+ 13].into_iter().fold(1, |a,b| a * b);
        if prod > max_prod {
            max_left_idx = left_idx;
        }
        left_idx += 1;
    }
    max_left_idx
}

pub fn solution() -> Option<Vec<i32>> {
    match dat_file_to_num_array("problem_files/p008.txt") {
        Ok(nums) => Some(get_max_left_idx(nums)),
        Err(_) => None,
    }
}

