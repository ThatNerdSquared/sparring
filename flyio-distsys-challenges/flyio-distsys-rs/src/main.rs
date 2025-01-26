pub mod maelstrom;

fn main() {
    println!("Hello, world!");

    let mut node = maelstrom::create_node();
    node.use_default_init_handler();
}
