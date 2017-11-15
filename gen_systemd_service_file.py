from systemd_template import *
import argparse

parser = argparse.ArgumentParser(description='Generate service file')
parser.add_argument('-p', '--path', required=True,
                   help='absolute path of script run in service')
parser.add_argument('-n', '--service_name',
                   help='name of service')
parser.add_argument('-i', '--interpreter_path', default='/usr/bin/python',
                   help='absolute path of interpreter (default: /usr/bin/python)')

args = parser.parse_args()

if __name__ == "__main__":
	if args.service_name is None:
		args.service_name = os.path.splitext(os.path.basename(args.path))[0]
	if os.path.isfile(args.path):
		gen_service_file(args.service_name, args.interpreter_path, args.path)
	else:
		print("Can not find input script file")
	
	