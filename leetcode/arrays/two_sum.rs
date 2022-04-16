use std::collections::HashMap;

fn main() {
    println!("{:?}", two_sum(vec![3, 2, 1], 4));
}
fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut map: HashMap<i32, i32> = HashMap::new();
    for (i, num) in nums.iter().enumerate() {
        let diff = target - num;
        if map.contains_key(&diff) {
            return vec![map.remove(&diff).unwrap(), i as i32];
        } else {
            map.insert(*num as i32, i as i32);
        }
    }
    return vec![-1, -1];
}
