use std::{
    any::{Any, TypeId},
    collections::HashMap,
    io,
};

pub struct MaelstromMsg<T> {
    src: String,
    dest: String,
    body: T,
}

struct MaelstromMsgBodyBase {
    r#type: String,
    msg_id: Option<i32>,
    in_reply_to: Option<i32>,
}

struct MaelstromInitMsgBody {
    metadata: MaelstromMsgBodyBase,
    node_id: String,
    node_ids: Vec<String>,
}

pub fn create_node() -> MaelstromNode {
    MaelstromNode {
        stdin_handle: io::stdin(),
        handlers: HashMap::new(),
    }
}

pub struct MaelstromNode {
    stdin_handle: io::Stdin,
    handlers: HashMap<TypeId, Box<dyn Any>>,
}

impl MaelstromNode {
    pub fn register_handler<T: 'static>(&mut self, handler: impl Fn(T) -> () + 'static) {
        self.handlers.insert(TypeId::of::<T>(), Box::new(handler));
    }

    pub fn init(&self) {
        // self.stdin_handle.
        println!("test");
    }

    pub fn use_default_init_handler(&mut self) {
        self.register_handler(&|msg: MaelstromMsg<MaelstromInitMsgBody>| {
            println!(
                "{{
              \"type\":        \"init_ok\",
              \"in_reply_to\": 1
            }}"
            );
        });
    }
}
