import pexpect

child = pexpect.spawn("ssh 172.20.20.2")
child.expect("Username")