data "aws_ami" "amazon_linux" {
  most_recent = true

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  filter {
    name = "architecture"
    values = ["x86_64"]
  }

  owners = ["amazon"]
}

#resource "aws_key_pair" "test" {
#  public_key = var.public_key
#}


resource "aws_security_group" "http_server_sg" {
  name = "http_server_sg"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = -1
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    name = "http_server_sg"
  }
}

resource "aws_instance" "http_server" {
  ami                    = data.aws_ami.amazon_linux.id
  instance_type          = "t2.micro"
  associate_public_ip_address = true

  root_block_device {
    volume_size = 30
    volume_type = "gp2"
  }

  tags = {
    Name = local.system_name
  }

  vpc_security_group_ids = [aws_security_group.http_server_sg.id]
  
  key_name = us-east-key

#  connection {
#    type        = "ssh"
#    host        = self.public_ip
#    user        = "ec2-user"
#    private_key = file(var.aws_key_pair)
#  }
#
#  provisioner "remote-exec" {
#    inline = [
#      "sudo yum install httpd -y",
#      "sudo service httpd start",
#      "echo HELLO WORLD | sudo tee /var/www/html/index.html"
#    ]
#  }
}
