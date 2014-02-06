# boto configuration
# set both to None if you want to use boto default configuration
aws_access_key_id = None
aws_secret_access_key = None

# path to directory that contains pem files
# can be relative path or absolute path
pem_file_directory = 'pem_files'

# mapping ssh private key to pem file and usernames
key_to_credentials_mapping = {  
  # For this private key, config quick-ssh to try connecting using username=ubuntu first; 
  # if failed, try connect using username=root
  'firstExampleKey': ('first.pem', ['ubuntu', 'root']),

  'secondExampleKey': ('second.pem', ['ubuntu']),
}
