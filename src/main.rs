use std::collections::HashMap;
use std::fs;

fn main() {
    let input = fs::read_to_string("input-2.asm").unwrap();
    let mut vm = VirtualMachine::new();
    vm.interpreter(input);
}

pub struct VirtualMachine {
    registers: HashMap<String, i32>
}

impl VirtualMachine {
    pub fn new() -> VirtualMachine {
        VirtualMachine {
            registers: HashMap::new()
        }
    }

    pub fn interpreter(&mut self, program: String) {
        let split = program.split("\n").collect::<Vec<&str>>();
        let mut i = 0;

        while i < split.len() - 1 {
            let instruction = split[i].split_whitespace().collect::<Vec<&str>>();
            match instruction[..] {
                ["mov", x, y] => {
                    self.registers.insert(x.to_string(), match self.parse_register_handler(y) {
                        Ok(value) => value,
                        Err(error) => {
                            self.error_printer(&split[i], &i, &error);
                            return;
                        }
                    });
                },
                ["add", x, y] => {
                    let temp = match self.parse_register_handler(y) {
                        Ok(value) => value,
                        Err(error) => {
                            self.error_printer(&split[i], &i, &error);
                            return;
                        }
                    };
                    let Some(value) = self.registers.get_mut(x) else {println!("Uninitialized register"); return;};
                    *value += temp;
                },
                ["print", x] => {
                    let temp = match self.get_register_handler(x) {
                        Ok(value) => value,
                        Err(error) => {
                            self.error_printer(&split[i], &i, &error);
                            return;
                        }
                    };
                    match char::from_u32(temp as u32) {
                        Some(value) => print!("{}", value),
                        None => println!("Invalid Unicode Character")
                    }
                },
                ["jnz", x, y] => {
                    let temp = match self.parse_register_handler(x) {
                        Ok(value) => value,
                        Err(error) => {
                            self.error_printer(&split[i], &i, &error);
                            return;
                        }
                    };

                    if temp != 0 {
                        let y = match self.parse_register_handler(y) {
                            Ok(value) => value,
                            Err(error) => {
                                self.error_printer(&split[i], &i, &error);
                                return;
                            }
                        };
                        i = (i as i32 + y - 1) as usize;
                    }
                }
                _ => {
                    self.error_printer(&split[i], &i, &"".to_string());
                    return;
                }
            }
            i += 1;
        }
    }

    fn parse_register_handler(&self, x: &str) -> Result<i32, String> {
        match x.parse::<i32>() {
            Ok(value) => Ok(value),
            Err(_) => self.get_register_handler(x)
        }
    }

    fn get_register_handler(&self, x: &str) -> Result<i32, String> {
        match self.registers.get(x) {
            Some(value) => Ok(*value),
            None => Err(format!("Uninitialized register <{}>", x))
        }
    }

    fn error_printer(&self, instruction: &str, index: &usize, error: &String) {
        if error != "" {println!("{}", error)}
        println!("Invalid instruction <{}> at line {}", instruction, index+1);
    }
}