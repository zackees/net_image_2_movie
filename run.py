
#! /bin/python3


from datetime import datetime
import time
import os

import requests
import argparse


try:
	os.makedirs('data')
except:
	pass

def make_fetch_cmd(url: str) -> str:
	date_suffix = datetime.now().strftime("%m-%d-%Y_%H:%M:%S")
	return f'curl -X GET {url} --output ./data/{date_suffix}.png'


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--url', help='Image url to fetch')
	parser.add_argument('--sample_seconds', help='How often to fetch it', type=int)
	args = parser.parse_args()
	url = args.url
	if url is None:
		url = input('Enter url to fetch: ')
	sample_seconds = args.sample_seconds
	if sample_seconds is None:
		sample_seconds = int(input('Sample every X seconds: '))

	while True:
		#cmd = make_fetch_cmd(url)
		#print(f'Executing "{cmd}"')
		#os.system(cmd)

		data = requests.get(url).content
		print(f'Data was {len(data)} bytes')
		file_name = datetime.now().strftime("image%m-%d-%Y_%H_%M_%S.png")
		print(f'Filename: {file_name}')
		file_path = f'data/{file_name}'
		with open(file_path, 'wb') as fd:
			print(f'Writing to {file_path}')
			fd.write(data)
		print(f'sleeping {sample_seconds} seconds')
		time.sleep(sample_seconds)

if __name__ == '__main__':
	main()