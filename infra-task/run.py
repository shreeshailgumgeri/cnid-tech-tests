# Run This code first to run the application

begining_space = '      '
print("_"*100)
print("{}Below are the Steps & set of commands Required to use this Application".format(begining_space))

print("_"*100)

print("{}===PRE-REQUISITES===\n{}[  CREATE KEY PAIR with name - us-east-key in aws account in us-east region & Download it locally  ]\n".format(begining_space, begining_space))

print("{}Step 1 (Initialize Terraform ) :\n{}terraform init".format(begining_space, begining_space))

print("{}Step 2 (Validate Terraform) :\n{}terraform validate".format(begining_space, begining_space))

print("{}Step 3 (Plan Terraform) :\n{}terraform plan".format(begining_space, begining_space))

print("{}Step 4 (Build IAAC) :\n{}terraform apply".format(begining_space, begining_space))

print("_"*100)

print("\n{}Steps to LOGIN to AWS EC2 instance & Install Web App Server".format(begining_space))

key_pair_path = raw_input("{}Enter the Key Path (Ex : ~/Downloads/us-east-key.cer) : ".format(begining_space))

public_ip = raw_input("{}Enter EC2 Public IP (Ex : 34.224.174.132 ) : ".format(begining_space))

print("_"*100)

print("{}Step 1 (LOGIN to instance) : \n{}ssh - i {} ec2-user@{}".format(begining_space, begining_space, key_pair_path, public_ip))

print("{}Step 2 (Switch to Super User) : \n{}sudo su - ".format(begining_space, begining_space))

print("{}Step 3 (Install Apache Server and check status) : \n{}yum install -y httpd ; systemctl start httpd ; systemctl status httpd".format(begining_space, begining_space))

print('{}Step 4 (Edit HTML Content) : \n{}touch /var/www/html/index.html ; echo "<html> <h1>Hello World Conde Nast</h1> </html>" > /var/www/html/index.html'.format(begining_space, begining_space))

print("{}Step 5 (Curl Command) : \n{}curl http://{}".format(begining_space, begining_space,public_ip))

print("_"*100)

print("{}===WARNING===\n{}[  DO NOT FORGOT TO DELETE THE INFRASTRUCTURE  ]\n".format(begining_space, begining_space))

print("{}STEP (Destroy IAAC) :\n{}terraform destroy".format(begining_space, begining_space))

print("\n\n{}{}*** THANK YOU FOR USING THE APPLICATION ***".format(begining_space, begining_space))

print("_"*100)
print("_"*100)
print("\n\n")