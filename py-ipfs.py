from prettytable import PrettyTable
import ipfsapi, subprocess

api = ipfsapi.connect('127.0.0.1', 5001)

# python 2 and 3 supported
try:
	message = raw_input("Enter a message to be written in a file : ")
except NameError:
	message = input("Enter a message to be written in a file : ")

with open('test.txt', 'w') as f:
	f.write(message)

file_hash = api.add('test.txt')
publish = subprocess.check_output(['ipfs', 'name', 'publish', file_hash['Hash']])

print("File uploaded to ipfs node")
print("View the file at :- https://gateway.ipfs.io/ipfs/{0}".format(file_hash['Hash']))

peer_data = PrettyTable(["Peer", "Bytes Received", "Bytes Sent"])

peers = []
with open('peers_list.txt', 'w') as f:
	for i in list(api.bitswap_stat()["Peers"]):
		f.write("{0}\n".format(i))

		if not i in peers:
			output = list(subprocess.check_output(['ipfs', 'bitswap', 'ledger', i]).split('\n'))
			output = [d.split(':\t') for d in output]
			output_dict = {item[0]: item[1] for item in output if len(item) == 2}

			peer_data.add_row([i, output_dict['Bytes received'], output_dict['Bytes sent']])
			peers.append(i)

print(peer_data)
