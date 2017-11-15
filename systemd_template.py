import os
serviceFileTemplate = \
"""[Unit]
Description=%s
After=multi-user.target

[Service]
Type=simple
ExecStart=%s -u %s
StandardOutput=journal+console
Restart=always

[Install]
WantedBy=multi-user.target
"""

def gen_service_file(service_name, interpreter_path, file_path):
	if service_name is None or interpreter_path is None or file_path is None:
		print("Can not gen service file (missing parameters)")
		return -1
	if os.path.isfile("%s.service" % service_name):
		print("Can not gen service file (file already exits)")
		return -1
	with open("%s.service" % service_name, 'w') as _f:
		_f.write(serviceFileTemplate % (service_name, interpreter_path, file_path))
		
	print("Generated service file %s.service" % service_name)
	return 0

if __name__ == "__main__":
	srvName = "TestSrv"
	interpreterPath =  "TestPath"
	filePath = "TestFilePath"
	gen_service_file(srvName, interpreterPath, filePath)
	
	