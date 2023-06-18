def int32_to_ip(int32):
    ip = bin(int32)[2:]
    ip = "0" * (32 - len(ip)) + ip
    ip = [ip[i:i + 8] for i in range(0, 4 * 7, 8)]
    return ".".join([str(int(ip[i], 2)) for i in range(4)])