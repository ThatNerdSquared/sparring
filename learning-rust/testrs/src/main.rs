fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}

fn main() {
    let item = 42; // outputs i32
    let otheritem = -42; // outputs i32
    print_type_of(&item);
    print_type_of(&otheritem);
    println!("Hello, world!");
}
