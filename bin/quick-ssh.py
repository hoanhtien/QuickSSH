import os
import sys
import json
import subprocess
import boto
import settings

def ssh(instance):
  info = {
    'id': instance.id,
    'name': instance.tags['Name'],
    'instance type': instance.instance_type,
    'state': instance.state,
    'public_dns_name': instance.public_dns_name,
    'ssh_private_key': instance.key_name
  }
  print json.dumps(info)
  
  if info['state'] != 'running':
    print 'Error: Not a running instance.'
    return

  pem_file_name, usernames = settings.key_to_credentials_mapping[info['ssh_private_key']]
  
  pem_file_directory = os.path.abspath(settings.pem_file_directory)
  pem_file_path = os.path.join(pem_file_directory, pem_file_name)

  for username in usernames:
    command = 'ssh -i %s %s@%s' % (pem_file_path, username, info['public_dns_name'])
    print command
    return_code = subprocess.call(command, shell=True)
    if return_code == 0:
      break

def get_all_instances(keyword):
  conn = boto.connect_ec2(settings.aws_access_key_id, settings.aws_secret_access_key)
  reservations = conn.get_all_instances()

  matching_instances = []
  for reservation in reservations:
    for instance in reservation.instances:
      if 'Name' in instance.tags:
        if instance.tags['Name'].lower().find(keyword) != -1:
          matching_instances.append(instance)

  if len(matching_instances) == 0:
    print 'No matches could be found.'
  elif len(matching_instances) > 1:
    matching_instance_names = map(lambda instance: instance.tags['Name'], matching_instances)
    print 'Multiple matches:', json.dumps(sorted(matching_instance_names))
  else:
    print '1 match is found:',
    ssh(matching_instances[0])

if __name__ == '__main__':
  if len(sys.argv) > 1:
    keyword = sys.argv[1].strip().lower()
  else:
    keyword = ''
  get_all_instances(keyword)

