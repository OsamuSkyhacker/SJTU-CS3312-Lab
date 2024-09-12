import subprocess
import time

process = subprocess.Popen(['./race'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

process.stdin.write(b'1\n')
process.stdin.flush()


process.stdin.write(b'2\n')
process.stdin.flush()
time.sleep(0.1)

process.stdin.write(b'1\n')
process.stdin.flush()
time.sleep(0.1)

process.stdin.write(b'2\n')
process.stdin.flush()
time.sleep(0.1)

process.stdin.write(b'1\n')
process.stdin.flush()

process.stdin.write(b'3\n')
process.stdin.flush()

output, error = process.communicate()

print("Output:\n")
print(output.decode())

if len(error.decode())>0:
    print("Error:", error.decode())

