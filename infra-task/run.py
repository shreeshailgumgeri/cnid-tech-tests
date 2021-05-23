# Run This code first to run the application

begining_space = '      '
print("_"*100)
print("{}Below are the Steps & set of commands Required to use this Application".format(begining_space))

print("_"*100)

print("{}===PRE-REQUISITES===\n[  Get Key Pair with name - us-east-key created in aws account in us-east region & get it Downloaded locally  ]\n".format(begining_space, begining_space))

print("{}Step 1 (Clone Repo) :\n{}git clone https://github.com/shreeshailgumgeri/cnid-tech-tests.git".format(begining_space, begining_space))

print("{}Step 2 (Initialize Terraform ) :\n{}terraform init".format(begining_space, begining_space))

print("{}Step 3 (Validate Terraform) :\n{}terraform validate".format(begining_space, begining_space))

print("{}Step 4 (Plan Terraform) :\n{}terraform plan".format(begining_space, begining_space))

print("{}Step 5 (Build IAAC) :\n{}terraform apply".format(begining_space, begining_space))

print("_"*100)

print("\n{}Steps to LOGIN to instance & Install Web App Server".format(begining_space))

key_pair_path = raw_input("{}Enter the Key Path (Ex : ~/Downloads/us-east-key.cer) : ".format(begining_space))

public_ip = raw_input("{}Enter EC2 Public IP (Ex : 34.224.174.132 ) : ".format(begining_space))

print("_"*100)

print("{}Step 1 (LOGIN to instance) : \n{}ssh - i {} ec2-user@{}".format(begining_space, begining_space, key_pair_path, public_ip))

print("{}Step 2 (Switch to Super User) : \n{}sudo su - ".format(begining_space, begining_space))

print("{}Step 3 (Install Apache Server and check status) : \n{}yum install -y httpd ; systemctl start httpd ; systemctl status httpd".format(begining_space, begining_space))

print('{}Step 4 (Edit HTML Content) : \n{}touch /var/www/html/index.html ; echo "<html> <h1>Hello World Conde Nast</h1> </html>" > /var/www/html/index.html'.format(begining_space, begining_space))

print("{}Step 5 (Curl Command) : \n{}curl http://{}".format(begining_space, begining_space,public_ip))
