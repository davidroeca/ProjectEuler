use std::cmp;
use std::fs::File;
use std::io::{BufRead, BufReader, Error, ErrorKind};
use problems::utils;

fn line_to_num_vec(s: &[u8]) -> Result<Vec<i64>, Error> {
    let length = s.len();
    let mut cur_num = None;
    let mut num_vec = Vec::new();
    for i in 0..length+1 {
        if i == length || s[i] == b' ' {
            if let Some(num) = cur_num {
                num_vec.push(num);
            }
            cur_num = None;
        } else {
            let cur_digit = try!(utils::byte_to_i64(s[i]));
            match cur_num {
                None => {
                    cur_num = Some(cur_digit);
                },
                Some(d) => {
                    cur_num = Some(d * 10 + cur_digit);
                },
            }
        }
    }
    Ok(num_vec)
}

fn dat_file_to_num_boxes(file_path: &str) -> Result<Vec<Vec<i64>>, Error> {
    let f = try!(File::open(file_path));
    let reader = BufReader::new(f);
    let mut rows = Vec::new();
    for line in reader.lines() {
        let valid_line = try!(line);
        let row = try!(line_to_num_vec(valid_line.as_bytes()));
        rows.push(row);
    }
    Ok(rows)
}

fn get_right_diag_prod(
    v: &[Vec<i64>], row_idx: usize, col_idx: usize, num_elems: usize
) -> i64 {
    let mut prod = 1i64;
    for offset in 0..num_elems {
        prod *= v[row_idx + offset][col_idx + offset];
    }
    prod
}

fn get_left_diag_prod(
    v: &[Vec<i64>], row_idx: usize, col_idx: usize, num_elems: usize
) -> i64 {
    let mut prod = 1i64;
    for offset in 0..num_elems {
        prod *= v[row_idx + offset][col_idx - offset];
    }
    prod
}

fn get_horiz_prod(
    v: &[Vec<i64>], row_idx: usize, col_idx: usize, num_elems: usize
) -> i64 {
    let mut prod = 1i64;
    for offset in 0..num_elems {
        prod *= v[row_idx][col_idx + offset];
    }
    prod
}

fn get_vert_prod(
    v: &[Vec<i64>], row_idx: usize, col_idx: usize, num_elems: usize
) -> i64 {
    let mut prod = 1i64;
    for offset in 0..num_elems {
        prod *= v[row_idx + offset][col_idx];
    }
    prod
}

fn find_max_prod(n: usize) -> Result<i64, Error> {
    // n is number of elements to make into product
    let grid = try!(dat_file_to_num_boxes("problem_files/p011.txt"));
    let height = grid.len();
    let width = grid[0].len();
    if (&grid).into_iter().map(|row| row.len()).any(|l| l != width) {
        return Err(Error::new(ErrorKind::Other, "Unequal widths in grid"));
    }
    let mut max_prod = 0;
    for j in 0..width {
        for i in 0..height {
            if i <= height - n {
                // do a vertical check
                max_prod = cmp::max(get_vert_prod(&grid, i, j, n), max_prod);
                if j <= width - n {
                    // do a right diagonal check
                    max_prod = cmp::max(get_right_diag_prod(&grid, i, j, n), max_prod);
                }
                if j >= n - 1 {
                    // do a left diagonal check
                    max_prod = cmp::max(get_left_diag_prod(&grid, i, j, n), max_prod);
                }
            }
            if j <= width - n {
                // do a horizontal check
                max_prod = cmp::max(get_horiz_prod(&grid, i, j, n), max_prod);
            }
        }
    }
    Ok(max_prod)
}

pub fn solution() -> Option<i64> {
    match find_max_prod(4) {
        Ok(v) => Some(v),
        Err(_) => None,
    }
}
