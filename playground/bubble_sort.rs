const LEN: usize = 7;
fn main() {
    let mut a: [i32; LEN] = [12, 200, 1, 3000, 30023, 123, 12];

    bubble_sort(&mut a);
    println!("{:?}", a);
}

fn bubble_sort(a: &mut [i32; LEN]) {
    let mut i = 0;
    let mut j = 0;

    while i < a.len() {
        j = i;
        while j < a.len() {
            if j == 0 {
                j += 1;
                continue;
            }
            if a[j] < a[j - 1] {
                let temp = a[j];
                a[j] = a[j - 1];
                a[j - 1] = temp;
            }
            j += 1;
        }
        i += 1;
    }
}
