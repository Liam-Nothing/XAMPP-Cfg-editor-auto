# Variables

httpd_path = "C:/xampp/apache/conf/httpd.conf"
doc_root_path = input("DocumentRoot : ").replace("\\", "/")
target_lines = 258

# Open file
with open(httpd_path, 'r', encoding='utf-8') as file:
	data = file.readlines()

# Edit lines
data[target_lines] = "DocumentRoot \"" + doc_root_path + "\"\n"
data[target_lines+1] = "<Directory \"" + doc_root_path + "\">\n"

# Rewrite file
with open(httpd_path, 'w', encoding='utf-8') as file:
	file.writelines(data)