#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time
import subprocess


def run_cmd(cmd):
    print("run cmd: " + " ".join(cmd))
    print("")
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    output = ""
    # Poll process for new output until finished
    while True:
        nextline = process.stdout.readline()
        if (nextline == '' or nextline == b'') and process.poll() is not None:
            break

        sys.stdout.write(str(nextline, 'utf-8'))
        sys.stdout.flush()
        output = str(output) + str(nextline, 'utf-8')

    xoutput, err = process.communicate()
    exitCode = process.returncode

    if (exitCode != 0):
        if err is not None:
            print(err)

    print("")
    return output, exitCode


def main():
    print('shell worker will run command once again until no error')
    out = 'err'
    code = 0
    tried = 1

    cmd = sys.argv[1:]

    if len(cmd) > 0:
        while 'err' in out.lower() or code != 0:
            print('run times: ' + str(tried))
            out, code = run_cmd(cmd)
            time.sleep(3)
            tried += 1
    else:
        print("run cmd: " + " ".join(cmd))

    print('Done')


if __name__ == '__main__':
    main()
