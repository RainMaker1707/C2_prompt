import pyshark

# Load the PCAP file
pcap_file_path = './data/sessions/mtls/session_mtls_open_before_and_stay_open.pcap'
capture = pyshark.FileCapture(pcap_file_path)

# Function to extract relevant details from packets
def extract_packet_info(packet):
    info = {}
    if 'IP' in packet:
        info['src_ip'] = packet.ip.src
        info['dst_ip'] = packet.ip.dst
    if 'TCP' in packet:
        info['src_port'] = packet.tcp.srcport
        info['dst_port'] = packet.tcp.dstport
        info['flags'] = packet.tcp.flags
    if 'UDP' in packet:
        info['src_port'] = packet.udp.srcport
        info['dst_port'] = packet.udp.dstport
    if 'DNS' in packet:
        info['dns_query'] = packet.dns.qry_name
    if 'HTTP' in packet:
        info['http_host'] = packet.http.host
        info['http_uri'] = packet.http.request_uri
    return info

# Extract details from all packets
# packet_details = [extract_packet_info(packet) for packet in capture]

# Display the first few packet details for inspection
for packet in capture:
    print(packet)
    print("-----------------------------------------------------------------\n----------------------------------------------------------------")