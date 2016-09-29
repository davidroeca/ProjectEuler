use std::cmp::Ordering;
use std::collections::BinaryHeap;

use std::io::{BufRead, BufReader, Error, ErrorKind};
use std::fs::File;
use problems::utils;

#[derive(Copy, Clone, Eq, PartialEq)]
struct State {
    cost: Option<i64>,
    next: usize,
}

impl Ord for State {
    fn cmp(&self, other: &State) -> Ordering {
        // flipped comparison for min heap
        other.cost.cmp(&self.cost)
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &State) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

fn get_undirected_graph_weight(adj_mat: &[Vec<Option<i64>>], v: usize) -> Result<i64, Error> {
    let mut sum = 0i64;
    for i in 0..v {
        for j in i+1..v {
            if let Some(cost) = adj_mat[i][j] {
                sum += cost;
            }
        }
    }
    Ok(sum)
}

fn prims_algo_find_mst_weight(adj_mat: &[Vec<Option<i64>>], v: usize) -> Result<i64, Error> {
    let mut cost_sum = 0i64; // will be part of final answer

    let mut utilized: Vec<bool> = (0..v).map(|_| false).collect();
    let rand_start = try!(utils::get_random_idx(0, v));
    let mut next_pq = BinaryHeap::new();
    next_pq.push(State { cost: None, next: rand_start });
    while let Some(State { cost, next }) = next_pq.pop() {
        if !utilized[next] {
            utilized[next] = true;
            if let Some(c) =  cost {
                cost_sum += c;
            }
            // look only at unutilized vertices
            for i in (0..v).filter(|idx| !utilized[*idx]) {
                // only handle cases where an edge exists
                if let Some(edge_cost) = adj_mat[i][next] {
                    next_pq.push(State { cost: Some(edge_cost), next: i});
                }
            }
        }
    }
    Ok(cost_sum)
}

fn find_min_spanning_tree_prod(adj_mat: &[Vec<Option<i64>>], v: usize) -> Result<i64, Error> {
    // Goal: first must find min spanning tree
    if (&adj_mat).into_iter().map(|row| row.len()).any(|l| l != v) {
        return Err(Error::new(ErrorKind::Other, "Must be v x v adjacency matrix"));
    }
    prims_algo_find_mst_weight(&adj_mat, v)
}

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

pub fn solution() -> Result<i64, Error> {
    let adj_mat = try!(dat_file_to_adj_mat("problem_files/p107.txt"));
    let v = adj_mat.len();
    let original_weight = try!(get_undirected_graph_weight(&adj_mat, v));
    let mst_weight = try!(find_min_spanning_tree_prod(&adj_mat, v));
    Ok(original_weight - mst_weight)
}
