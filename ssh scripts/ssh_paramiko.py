import sys
import getopt
import paramiko

target = ""
user_name = ""
pass_word = ""
command_x = ""

def ssh_connection(ip, user, passwd, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(ip, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        print(ssh_session.recv(1024))

def main():
    global target
    global user_name
    global pass_word
    global command_x

    opts, args = getopt.getopt(sys.argv[1:], 'ht:u:p:c:', ['--target=', '--username=', '--password=', '--command='])
    for o, a in opts:
        if o in ['-t', '--target']:
            target = a
        elif o in ['-u', '--username']:
            user_name = a
        elif o in ['-p', '--password']:
            pass_word = a
        elif o in ['-c', '--command']:
            command_x = a

    ssh_connection(target, user_name, pass_word, command_x)

if __name__ == "__main__":
    main()