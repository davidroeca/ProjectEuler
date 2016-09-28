use std::io::{Error, ErrorKind};
use rand::{self, Rng};

pub fn is_prime(n: i32) -> bool {
    if n < 2 {
        false
    } else if n == 2 {
        true
    } else if n % 2 == 0 {
        false
    } else {
        let mut check = 3;
        while check * check <= n {
            if n % check == 0 {
                return false;
            }
            check += 2
        }
        true
    }
}

pub fn byte_to_i64(b: u8) -> Result<i64, Error> {
    if b < 48u8 || b > 57u8 {
        Err(Error::new(ErrorKind::Other, "Byte in question is not a number"))
    } else {
        Ok((b - 48u8) as i64)
    }
}

pub fn get_random_range_vec(start: usize, stop: usize) -> Vec<usize> {
    let mut v: Vec<usize> = (start..stop).collect();
    rand::thread_rng().shuffle(v.as_mut_slice());
    v
}
