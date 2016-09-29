use std::io::{BufRead, BufReader, Error, ErrorKind};
use std::fs::File;
use problems::utils;

fn line_to_adj_row(line: &[u8]) -> Result<Vec<Option<i64>>, Error> {
    let length = line.len();
    if length == 0 {
        Err(Error::new(ErrorKind::Other, "Empty Row"))
    } else {
        let mut cur_num = None;
        let mut adj_row = Vec::new();
        for i in 0..length+1 {
            if i == length || line[i] == b',' {
                adj_row.push(cur_num);
                cur_num = None;
            } else if line[i] != b'-' {
                let cur_digit = try!(utils::byte_to_i64(line[i]));
                match cur_num {
                    Some(num) => cur_num = Some(num * 10 + cur_digit),
                    None => cur_num = Some(cur_digit),
                }
            }
        }
        Ok(adj_row)
    }
}

fn dat_file_to_adj_mat(file_path: &str) -> Result<Vec<Vec<Option<i64>>>, Error> {
    let f = try!(File::open(file_path));
    let reader = BufReader::new(f);
    let mut adj_mat = Vec::new();
    for line in reader.lines() {
        let valid_line = try!(line);
        adj_mat.push(try!(line_to_adj_row(valid_line.as_bytes())));
    }
    Ok(adj_mat)
}



fn find_min_spanning_tree_prod() -> Result<i64, Error> {
    // Goal: first must find min spanning tree
    let adj_mat = try!(dat_file_to_adj_mat("problem_files/p107.txt"));
    let v = adj_mat.len();
    if (&adj_mat).into_iter().map(|row| row.len()).any(|l| l != v) {
        return Err(Error::new(ErrorKind::Other, "Must be v x v adjacency matrix"));
    }
    // Now: build out minimum spanning tree subroutine
    // TO DO
    //  - build or find a min heap/priority queue data structure and utilize
    //  - keep track of vertices both in and not in mst yet
    //  - maintain running product, starting at 1
    //
    //  - arbitrarily pick one vertex and initialize its key to -inf; add it to queue
    //  - while queue is not empty:
    //      - remove the item with the smallest key
    //      - if node is already in mst, skip
    //      - else
    //          - mark element as added to mst
    //          - add its predecessors to the queue
    //          - if the key is not -inf, multiply running prod by the key
    //  - we have both the solution of the mst as well as its edge-weight product
    Ok(123)
}

pub fn solution() -> Result<i64, Error> {
    println!("{:?}", dat_file_to_adj_mat("problem_files/p107.txt"));
    println!("{}", i64::max_value());
    for _ in 0..100 {
        println!("{:?}", try!(utils::get_random_idx(0, 40)));
    }
    find_min_spanning_tree_prod()
}
