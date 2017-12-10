use std::io;
use std::io::prelude::*;

fn main() {
    let stdin = io::stdin();
    let stdin = stdin.lock().lines();
    let mut part1 = 0;
    let mut part2 = 0;
    for line in stdin {
        let line = line.unwrap();
        let line: Vec<u32> = line.split('\t').map(|n| n.parse().unwrap()).collect();
        let max = line.iter().max().unwrap();
        let min = line.iter().min().unwrap();
        for n1 in &line {
            for n2 in &line {
                if n1 % n2 == 0 && n1 != n2 {
                    part2 += n1 / n2;
                }
            }
        }
        part1 += max - min;
    }
    println!("Part 1: {}", part1);
    println!("Part 2: {}", part2);
}
