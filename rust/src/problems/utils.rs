use std::io::{Error, ErrorKind};
use std::env;
use std::path::PathBuf;
use rand;

pub fn get_project_dir() -> Result<PathBuf, Error>{
    let exe_path = try!(env::current_exe());
    if let Some(run_dir) = exe_path.parent() {
        if let Some(target_dir) = run_dir.parent() {
            if let Some(project_dir) = target_dir.parent() {
                return Ok(project_dir.join(""));
            }
        }
    }
    Err(Error::new(ErrorKind::Other, "target dir not found"))
}

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

pub fn get_random_idx(start: usize, stop: usize) -> Result<usize, Error> {
    if stop <= start {
        Err(Error::new(ErrorKind::Other, "Stop must be greater than start"))
    } else {
        Ok(rand::random::<usize>() % (stop - start) - start)
    }
}
