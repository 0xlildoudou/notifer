import notify2
import subprocess
import argparse
import os

def parser():
    _parser = argparse.ArgumentParser()
    _parser.add_argument('-c','--command',help='Command to execute', type=str,required=True, nargs=argparse.REMAINDER)
    return _parser.parse_args()

def runCommand(command):
    with subprocess.Popen(
            command,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True
        ) as process:
        for line in process.stdout:
            print(line, end='')

        for line in process.stderr:
            print(line, end='')
    process.wait()
    return process.returncode

def sendmessage(title, message, icon):
    notify2.init("Notifer")
    icon_path = os.path.join(os.path.dirname(__file__), icon)
    notice = notify2.Notification(title, message, icon_path)
    notice.show()
    return

def main():
    args = parser()

    rc = runCommand(args.command)

    if rc != 0:
        icon = 'assets/error.png'
        title = 'Error'
        message = f'{" ".join(args.command)}'
    else:
        icon = 'assets/ok.png'
        title = 'Done'
        message = f'{" ".join(args.command)}'

    sendmessage(title,message, icon)

if __name__ == '__main__':
    main()
