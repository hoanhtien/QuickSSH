# QuickSSH

QuickSSH lets you quickly ssh to Amazon EC2 instances using the instances&#8242; name or just part of the instances&#8242; name (keyword). As a result, you no longer need to remember any ip address, public/private key (pem file), and username.

## HOW TO USE

Just one command: `./quick-ssh.sh <keyword>`

If there are more than one matches, QuickSSH reports all matching servers:

```sh
Tien@hoanhtien-pc:~/QuickSSH$ ./quick-ssh.sh tcloud
Multiple matches: ["tCloudWebsiteDev", "tCloudWebsiteProd", "tCloudWebsiteTest", "tcloud_trainer"]
```

If there is exacly one match, QuickSSH ssh you to the matching server:

```sh
Tien@hoanhtien-pc:~/QuickSSH$ ./quick-ssh.sh tcloud_train
1 match is found: {"name": "tcloud_trainer", "instance type": "m3.2xlarge", "state": "running", "ssh_private_key": "akeerthiKey", "public_dns_name": "ec2-54-224-104-18.compute-1.amazonaws.com", "id": "i-4c48242b"}
ssh -i /cygdrive/e/workspace/pem/ubuntu.pem root@ec2-54-224-104-18.compute-1.amazonaws.com
ec2Unix: /root>
```

Of course, ssh to a non-running server will not work:

```sh
Tien@hoanhtien-pc:~/QuickSSH$ ./quick-ssh.sh gpu
1 match is found: {"name": "GPU Instance Ondemand", "instance type": "cg1.4xlarge", "state": "stopped", "ssh_private_key": "lusongkey", "public_dns_name": "", "id": "i-68fcc909"}
Error: Not a running instance.
```

`quick-ssh.sh` can be run at any directory. You do not have to "cd QuickSSH" all the times.

```sh
Tien@hoanhtien-pc:~/some_folder/some_sub_folder$ ../../QuickSSH/quick-ssh.sh redis
Multiple matches: ["2g3c-Redis-Server", "2g3c-redis-test"]
```

## INSTALLATION

Nothing special, just need to get a copy of QuickSSH folder. You will need python (version 2.7.x or above) with boto installed beforehand.

## CONFIGURATION

Input your configuration in file settings.py. By default, QuickSSH looks for pem files in directory QuickSSH/pem_files. Copy your pem files to this directory and you should be ready to go. If you get error `Permisson denined (public key)`, `chmod 600` for all the pem files might help.
