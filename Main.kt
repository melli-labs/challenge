import java.io.File
import java.io.IOException

/**
 * Exception class for VM interpreter errors
 * @param message String with error message
 */
class VMException(message: String): IOException(message)

/**
 * Interface class for interpreter instructions
 */
interface VMInstruction {
    /**
     * Execute function for vm
     * @param vm Reference to executing VM interpreter for register and line pointer access
     * @throws VMException will be thrown if invalid instruction has been encountered
     */
    fun execute(vm: VMInterpreter)
}

/**
 * Class for storing mov instructions and their arguments
 * @property arg1 Register where value of register/constant from second argument will be stored
 * @property arg2 Register/Constant that should be stored inside register of first argument
 *
 */
data class MovInstruction(val arg1: String, val arg2: String): VMInstruction {
    override fun execute(vm: VMInterpreter) {
        if (arg1.isEmpty() || arg2.isEmpty()) {
            throw VMException("Invalid mov instruction: invalid arguments $arg1 $arg2")
        }
        vm.register[arg1] = arg2.toIntOrNull()?:vm.register[arg2]?:0
        vm.pointer += 1
    }
}

/**
 * Class for storing add instructions and their arguments
 * @property arg1 Register of first value from add operation, will also store result of instructions
 * @property arg2 Register that should be added to register from first argument
 *
 */
data class AddInstruction(val arg1: String, val arg2: String): VMInstruction {
    override fun execute(vm: VMInterpreter) {
        if (arg1.isEmpty() || arg2.isEmpty()) {
            throw VMException("Invalid add instruction: invalid arguments $arg1 $arg2")
        }
        vm.register[arg1] = (vm.register[arg1]?:0) + (vm.register[arg2]?:0)
        vm.pointer += 1
    }
}

/**
 * Class for storing print instructions and their arguments
 * @property arg1 Register/constant with unicode value that shall be printed to stdout
 *
 */
data class PrintInstruction(val arg1: String): VMInstruction {
    override fun execute(vm: VMInterpreter) {
        if (arg1.isEmpty()) {
            throw VMException("Invalid print instruction: invalid arguments $arg1")
        }
        print(String(Character.toChars(vm.register[arg1] ?: 0)))
        vm.pointer += 1
    }
}

/**
 * Class for storing jnz instructions and their arguments
 * @property arg1 Register/Constant for not zero check
 * @property arg2 Register/Constant for modifying line pointer of interpreter
 *
 */
data class JumpNotZeroInstruction(val arg1: String, val arg2: String): VMInstruction {
    override fun execute(vm: VMInterpreter) {
        if (arg1.isEmpty() || arg2.isEmpty()) {
            throw VMException("Invalid jnz instruction: invalid arguments $arg1 $arg2")
        }
        if ((arg1.toIntOrNull()?:vm.register[arg1]?:0) == 0) {
            vm.pointer +=1
        } else {
            val newAddress = vm.pointer + (arg2.toIntOrNull()?:vm.register[arg2]?:0)
            if (newAddress < 0) {
                throw VMException("Invalid jnz instruction: invalid jump address $newAddress")
            }
            vm.pointer = newAddress
        }
    }
}

/**
 * Class for storing vm data
 * @property code List of instructions
 * @property register HashMap mapping register String keys to Integer values
 * @property pointer Integer pointing to current code line
 */
class VMInterpreter (
    private val code: List<VMInstruction>,
    val register: HashMap<String, Int> = hashMapOf(),
    var pointer: Int = 0) {

    /**
     * Function executing code instructions
     * @throws VMException Will be thrown if invalid commands have been encountered
     */
    fun run() {
        while (pointer < code.size) {
            code[pointer].execute(this)
        }
    }

    companion object {
        /**
         * Function reading vm instructions from file at path
         * @param path String with path to asm file
         * @return VMInterpreter with VM instructions
         * @throws VMException Will be thrown if invalid instruction commands have been encountered during parsing
         */
        fun readFromFile(path: String): VMInterpreter {
            val code = File(path)
                .bufferedReader()
                .readLines()
                .mapNotNull { line ->
                    val content = line.split(" ")
                    return@mapNotNull if (content.isNotEmpty()) {
                        when (content[0].trim()) {
                            "mov" -> {
                                MovInstruction(
                                    content.getOrNull(1)?.trim()?:"",
                                    content.getOrNull(2)?.trim()?:""
                                )
                            }
                            "add" -> {
                                AddInstruction(
                                    content.getOrNull(1)?.trim()?:"",
                                    content.getOrNull(2)?.trim()?:""
                                )

                            }
                            "print" -> {
                                PrintInstruction(
                                    content.getOrNull(1)?.trim()?:""
                                )
                            }
                            "jnz" -> {
                                JumpNotZeroInstruction(
                                    content.getOrNull(1)?.trim()?:"",
                                    content.getOrNull(2)?.trim()?:""
                                )
                            }
                            else -> {
                                throw VMException("Unknown command ${content[0]}")
                            }
                        }
                    } else {
                        null
                    }
                }
            return VMInterpreter(code)
        }
    }
}

fun main(args: Array<String>) {
    if (args.size == 1) {
        VMInterpreter
            .readFromFile(args[0])
            .run()
    } else {
        println("java -jar Challenge.jar path/to/file.ex")
    }
}