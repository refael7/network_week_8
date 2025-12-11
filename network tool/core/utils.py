def input_mask():
    while True:
        mask=input("Please enter four numbers between 0 and 255 and put a period between each number dot:\nmask number:")
        mask_temp=mask.split('.')
        if len(mask_temp)!=4 :
            print("Missing dot between number and number Try again")
            continue
        else:
            count=0
            for i in range(len(mask_temp)):
                x = mask_temp[i].isdigit()
                if x is False:
                    print("input only digit")
                    continue
                int_number=int(mask_temp[i])
                if  mask_temp[i] is  None or int_number < 0  or int_number > 255:
                    print("You did not enter a valid number")
                    continue
                elif count < 3:
                    count += 1
                else:
                   return ".".join(mask_temp)

def input_ip():
    while True:
        ip=input("Please enter four numbers between 0 and 255 and put a period between each number dot :\nip number:")
        ip_temp=ip.split('.')
        if len( ip_temp)!=4 :
            print("Missing dot between number and number Try again")
            continue
        else:
            count=0
            for i in range(len( ip_temp)):
                x = ip_temp[i].isdigit()
                if x is False:
                    print("input only digit")
                    continue
                int_number=int( ip_temp[i])
                if   ip_temp[i] is  None or int_number < 0  or int_number > 255:
                    print("You did not enter a valid number")
                    continue
                elif count < 3:
                    count += 1
                else:
                   return ".".join( ip_temp)

def decimal_to_binary_masc(binary_number):
    result = ""
    for i in range(len(binary_number)):
        number = format(int(binary_number[i]), "08b")
        result += number + "."
    return result[:-1]


def count_zero(mask_binary):
    mask_binary = mask_binary.replace(".", "")
    return mask_binary.count("0")

def cidr_mask(mask_binary):
    return mask_binary.replace(".", "").count("1")

def get_class(ip_first_octet,mask_binary):
    ip_first_octet = int(ip_first_octet)
    if 0 <= ip_first_octet <= 127 and cidr_mask(mask_binary) == 8:
        return "A"
    elif 128 <= ip_first_octet <= 191 and cidr_mask(mask_binary) == 16:
        return "B"
    elif 192 <= ip_first_octet <= 223 and cidr_mask(mask_binary) == 24:
        return "C"
    else:
        return "classless"


def network_ip(ip, prefix):
        ip_bin = ""
        for octet in ip:
            octet_int = int(octet)
            octet_bin = format(octet_int, "08b")
            ip_bin = ip_bin + octet_bin
        network_bits = ""
        for index in range(prefix):
            network_bits = network_bits + ip_bin[index]

        remaining_bits = 32 - prefix
        for _ in range(remaining_bits):
            network_bits = network_bits + "0"

        result_octets = []
        start = 0
        while start < 32:
            binary_chunk = network_bits[start:start + 8]
            decimal_value = int(binary_chunk, 2)
            result_octets.append(str(decimal_value))
            start = start + 8

        network_address = ".".join(result_octets)
        return network_address


def broadcast_ip(ip, prefix):
    ip_bin = ""
    for octet in ip:
        octet_int = int(octet)
        octet_bin = format(octet_int, "08b")
        ip_bin = ip_bin + octet_bin
    network_bits = ""
    for index in range(prefix):
        network_bits = network_bits + ip_bin[index]

    remaining_bits = 32 - prefix
    for _ in range(remaining_bits):
        network_bits = network_bits + "1"

    result_octets = []
    start = 0
    while start < 32:
        binary_chunk = network_bits[start:start + 8]
        decimal_value = int(binary_chunk, 2)
        result_octets.append(str(decimal_value))
        start = start + 8

    network_address = ".".join(result_octets)
    return network_address

def number_hosts(mask_binary):
    temp_number = 32 -cidr_mask(mask_binary)
    number = 2 ** temp_number -2
    return number


def next_subnet_ip(broadcast):
    octets = list(map(int, broadcast.split(".")))
    octets[3] += 1

    for i in range(3, -1, -1):
        if octets[i] > 255:
            octets[i] = 0
            if i > 0:
                octets[i - 1] += 1

    return ".".join(map(str, octets))

def write_to_file(filename, text):
    with open(filename, "w") as f:
        f.write(text)