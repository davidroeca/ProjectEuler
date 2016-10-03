use std::fs::File;
use std::io::{BufRead, BufReader, Error};
use std::path::Path;
use problems::utils;

fn dat_file_to_num_array(file_path: &Path) -> Result<Vec<i64>, Error> {
    let f = try!(File::open(file_path));
    let reader = BufReader::new(f);
    let mut nums = Vec::new();
    for line in reader.lines() {
        let valid_line = try!(line);
        for b in valid_line.bytes() {
            nums.push(try!(utils::byte_to_i64(b)));
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
pub fn solution() -> Result<i64, Error> {
    let src_dir = try!(utils::get_project_dir());
    let dat_file = src_dir.join("src/problems/problem_files/p008.txt");
    let num_array = try!(dat_file_to_num_array(dat_file.as_path()));
    Ok(get_max_prod(num_array.as_ref()))
}

