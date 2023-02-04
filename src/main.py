# Dicionário com Opcodes
OPCODES = {
    "andi": "001100",
    "ori": "001101",
    "xori": "001110",
    "addi": "001000",
    "beq": "000100",
    "bne": "000101",
}

# Dicionário com Functions
FUNCTIONS = {
    "and": "100100",
    "or": "100101",
    "xor": "100110",
    "nor": "100111",
    "add": "100000",
    "sub": "100010",
    "slt": "101010",
}


def main():
    input_file = input("Qual arquivo você deseja compilar? > ")

    instructions = read_file(input_file)
    output_commands = ["v2.0 raw"]

    for line in instructions:
        # Para garantirmos que a formatação sempre será minúscula equivalente aos dicionários.
        line = line.lower()

        if is_opcode(line):
            command = format_opcode_command_to_bin(line)
            command = bin_to_hex(command)
        elif is_function(line):
            command = format_function_command_to_bin(line)
            command = bin_to_hex(command)
        else:
            print(
                f"Não foi possível compilar o seguinte comando: '{line.strip()}'"
            )
            continue

        output_commands.append(command)

    write_file(output_commands, "saida.txt")
    print(f"Arquivo '{input_file}' compilado com sucesso!")


def read_file(filename):
    file = open(filename, "r")
    # O método readlines lê as linhas do arquivo
    # e retorna uma lista com cada uma delas.
    lines = file.readlines()
    file.close()

    return lines


def write_file(list_of_values, filename):
    file = open(filename, "w")
    for value in list_of_values:
        file.write(f"{value}\n")

    file.close()

    return None


def is_function(line):
    for function in FUNCTIONS.keys():
        if function in line:
            return True

    return False


def format_function_command_to_bin(line):
    opcode = "000000"
    shift_amount = "00000"
    # O método strip tira os \n e
    # o split gera uma lista a partir da string com um parâmetro de "quebra".
    function, rs, rt, rw = line.strip().split(" ")

    # Para excluirmos o sinal de $ dos registradores...
    rs = to_bin(rs[1:])
    rt = to_bin(rt[1:])
    rw = to_bin(rw[1:])

    function = FUNCTIONS[function]

    # zfill = zero fill = preencher com zeros (funciona para strings).
    return f"{opcode}{rs.zfill(5)}{rt.zfill(5)}{rw.zfill(5)}{shift_amount}{function}"


def is_opcode(line):
    for opcode in OPCODES.keys():
        if opcode in line:
            return True

    return False


def format_opcode_command_to_bin(line):
    opcode, rs, rw, imm = line.strip().split(" ")

    # Para excluirmos o sinal de $ dos registradores...
    rs = to_bin(rs[1:])
    rw = to_bin(rw[1:])
    imm = to_bin(imm)

    opcode = OPCODES[opcode]

    # zfill = zero fill = preencher com zeros (funciona para strings).
    return f"{opcode}{rs.zfill(5)}{rw.zfill(5)}{imm.zfill(16)}"


def to_bin(value):
    binary_representation = bin(int(value))
    # Quando convertemos um número para binário, o Python coloca "0b" na frente, ex:
    # bin(4) => 0b100.
    return binary_representation[2:]


def bin_to_hex(bin_value):
    # Quando chamamos o "int", o segundo parâmetro refere-se a base do número que será convertido.
    # ex: int("1010", 2) => 10.
    # Caso não haja especificação da base, por padrão, ela será base 10.
    decimal_value = int(bin_value, base=2)

    # Para convertermos um número para hexadecimal, precisamos passar um número decimal como parâmetro.
    # Um outro ponto importante é que assim como o "bin()" o "hex" coloca "0x" na frente do número convertido, ex:
    # hex(100) => 0x64.
    return hex(decimal_value)[2:]


# Execução do programa...
main()
