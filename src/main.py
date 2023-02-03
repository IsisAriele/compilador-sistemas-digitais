import sys

# Opcodes
OPCODES = {
    "ANDI": "001100",
    "ORI": "001101",
    "XORI": "001110",
    "ADDI": "001000",
    "BEQ": "000100" ,
    "BNE": "000101" ,
}

# Functions
FUNCTIONS = {
    "AND": "100100",
    "OR": "100101",
    "XOR": "100110",
    "NOR": "100111",
    "ADD": "100000",
    "SUB": "100010",
    "SLT": "101010",
}

def read_file(filename):
    f = open(filename, "r")
    # O método readlines lê as linhas do arquivo
    # e retorna uma lista com cada uma delas.
    lines = f.readlines()
    f.close()
    return lines

def format_function_command(line):
    opcode = "000000"
    shift_amount = "00000"

    function, rs, rt, rw = line.strip().split(" ")

    # Para excluirmos o sinal de $ dos registradores...
    rs = to_bin(rs[1:])
    rt = to_bin(rt[1:])
    rw = to_bin(rw[1:])

    # O método upper deixa as letras em maiúsculo
    function = FUNCTIONS[function.upper()]

    # zfill = zero fill = preencher com zeros (funciona para strings).
    return f"{opcode}{rs.zfill(5)}{rt.zfill(5)}{rw.zfill(5)}{shift_amount}{function}"


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


lines = read_file("arquivo_function.txt")
# A função "read_file" retorna uma lista contendo cada uma das linhas de um arquivo específico.

for line in lines:
    # Para cada linha, nós vamos seguir a seguinte lógica:
    # - Convertemos o comando para binário
    # - Convertemos o binário para hexadecimal
    bin_command = format_function_command(line)
    hex_command = bin_to_hex(bin_command)

    print(hex_command)

