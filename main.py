from ctypes import windll

# Runas admin function
# https://stackoverflow.com/questions/56251908/running-batch-file-as-administrator-in-python#answer-72792517
def runAdmin(path):
    return windll.shell32.ShellExecuteW(
        None,  # handle to parent window
        'runas',  # verb
        'cmd.exe',  # file on which verb acts
        ' '.join(['/c', path]),  # parameters
        None,  # working directory (default is cwd)
        1,  # show window normally
    )

# Variables
start_apache_path = r"C:\xampp\apache_start.bat"
stop_apache_path = r"C:\xampp\apache_stop.bat"
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

# Restart XAMPP
runAdmin(stop_apache_path)
runAdmin(start_apache_path)