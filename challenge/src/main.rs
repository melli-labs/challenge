use std::env;
use vm_interpreter::read_file as read_vm;

/// VM interpreter module
mod vm_interpreter {
	use std::fs::File;
	use std::io::{self, BufRead};
	use std::path::Path;
	use std::collections::HashMap;

	/// A VM is represented here
	pub struct VM {
		/// Vector with instructions and their arguments
		pub code: Vec<Vec<String>>,
		/// HashMap mapping register Strings to Integers
		pub register: HashMap<String,i32>,
		/// Usize integer pointing to current code line
		pub pointer: usize,
	}

	impl VM {
		/// Executes a move instruction, panics in case invalid instruction have been encountered
		///
		/// # Arguments
		/// `instruction` - Vector containing instruction and their arguments
		///
		fn mov(&mut self, instruction: &Vec<String>) {
			if instruction.len() != 3 {
				panic!("Invalid mov instruction: Expected instruction length is 3 but was {}", instruction.len());
			}
			let val2 = instruction[2].parse::<i32>().unwrap_or(*self.register.get(&instruction[2]).unwrap_or(&0));
			self.register.insert(instruction[1].clone(), val2);
		}

		/// Executes a add instruction, panics in case invalid instruction have been encountered
		///
		/// # Arguments
		/// `instruction` - Vector containing instruction and their arguments
		///
		fn add(&mut self, instruction: &Vec<String>) {
			if instruction.len() != 3 {
				panic!("Invalid add instruction: Expected instruction length is 3 but was {}", instruction.len());
			}
			let val1 = self.register.get(&instruction[1]).unwrap_or(&0);
			let val2 = self.register.get(&instruction[2]).unwrap_or(&0);
			self.register.insert(instruction[1].clone(), val1 + val2);
		}

		/// Executes a print instruction, panics in case invalid instruction have been encountered
		///
		/// # Arguments
		/// `instruction` - Vector containing instruction and their arguments
		///
		fn print(&mut self, instruction: &Vec<String>) {
			if instruction.len() != 2 {
				panic!("Invalid print instruction: Expected instruction length is 2 but was {}", instruction.len());
			}
			let val1 = *self.register.get(&instruction[1]).unwrap_or(&0);
			match u32::try_from(val1) {
				Ok(unicode) => { 
					match std::char::from_u32(unicode) {
						Some(c) => { print!("{}", c); }
						_ => { panic!("Invalid print instruction: Invalid number for unicode character {}", unicode); }
					} 
				}
				_ => { panic!("Invalid print instruction: Invalid number for unicode character: {}", val1); } 
			}
		}

		/// Executes a jnz instruction, panics in case invalid instruction have been encountered
		///
		/// # Arguments
		/// `instruction` - Vector containing instruction and their arguments
		///
		fn jnz(&mut self, instruction: &Vec<String>) {
			if instruction.len() != 3 {
				panic!("Invalid jnz instruction: Expected instruction length is 3 but was {}", instruction.len());
			}
			let val1: i32;
			match instruction[1].parse::<i32>() {
				Ok(constant) => { val1 = constant; },
				_ => { val1 = *self.register.get(&instruction[1]).unwrap_or(&0); },
			}
			if val1 != 0 {
				match instruction[2].parse::<i32>() {
					Ok(steps) => {
						if steps == 0 {
							self.pointer += 1;
						} else {
							match i32::try_from(self.pointer) {
								Ok(address) => {
									match usize::try_from(address + steps) {
										Ok(new_address) => { self.pointer = new_address}
										_ => { panic!("Invalid jnz instruction: Address calculation failed"); },
									}
								}
								_ => { panic!("Invalid jnz instruction: Line pointer conversion failed"); },
							}	
						}
					}
					_ => { panic!("Invalid jnz instruction: Second parameter must be integer but was {}", instruction[2]); }
				}
			} else {
				self.pointer += 1;
			}
		}

		/// Executes a move instruction, panics in case invalid instruction have been encountered
		///
		/// # Arguments
		/// `instruction` - Vector containing instruction and their arguments
		///
		pub fn execute(&mut self) {
			while self.pointer < self.code.len() {
				let instruction = self.code[self.pointer].clone(); 
				match instruction[0].as_str() {
					"mov" => { 
						self.mov(&instruction);
						self.pointer += 1;
					 }
					"add" => { 
						self.add(&instruction);
						self.pointer += 1;
					 }
					"print" => { 
						self.print(&instruction); 
						self.pointer += 1;
					}
					"jnz" => {
						self.jnz(&instruction);
					}
					_ => { panic!("Unknown command {}", instruction[0]); }
				}
			}
		}
	}

	/// Returns a result object containing a result object for reading lines from file
	///
	/// # Arguments
	/// `filename` - Path to file for reading
	///
	fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>> 
	where P: AsRef<Path>, {
		let file = File::open(filename)?;
		Ok(io::BufReader::new(file).lines())
	}	

	/// Reads vm from file at given path
	///
	/// # Arguments
	/// `path` - String with path to asm file
	///
	pub fn read_file(path: String) -> VM {
		let content = match read_lines(path) {
			Ok(content) => content,
			Err(error) => panic!("Error reading file {:?}", error),
		};
		let mut vm = VM { code: Vec::new(), register: HashMap::new(), pointer: 0 };
		for line in content {
			if let Ok(lp) = line {
				let line_content: Vec<String> = lp.split(" ").map(|s| s.to_string()).collect();
				if line_content.len() >= 1 { //skip empty lines
					vm.code.push(line_content);
				} 
			} else {
				panic!("Error reading line");
			}
		}
		return vm;
	}
}

fn main() {
	let args: Vec<String> = env::args().collect();
	if args.len() == 2 {
		let path = args[1].clone();
		let mut vm = read_vm(path);
		vm.execute();
	} else {
		println!("Usage: cargo run -- path/to/file.ex");
	}
}
