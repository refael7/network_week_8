from core.utils import *
from core.output_string import *


def main():
    ip = input_ip()
    masc = input_mask()

    ip_split = ip.split(".")
    masc_split = masc.split(".")

    # binary_mask
    mask_after_conversion = decimal_to_binary_masc(masc_split)

    # the func return cidr
    cidr = cidr_mask(mask_after_conversion)
    # print("Prefix:", cidr)

    # the func return where class
    Class = get_class(ip_split[0],mask_after_conversion)
    # network
    network = network_ip(ip_split, cidr)
    # print("Network:", network)

    # broadcast
    broadcast = broadcast_ip(ip_split, cidr)



    output = f"""
{format_input_ip(ip)}
{format_subnet_mask(masc)}
{format_classful_status(Class)}
{format_network_address(network )}
{format_broadcast_address(broadcast)}
{format_num_hosts(number_hosts(mask_after_conversion))}
{format_cidr_mask(cidr)}

"""

    write_to_file("subnet_info_[test]_[322998881].txt", output)


if __name__ == "__main__":
    main()