resource "aws_iam_role" "machine" {
  name = "${local.system_name}-machine-role"

  assume_role_policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "cloudwatch:*",
                "ec2:*",
                "elasticloadbalancing:*",
                "autoscaling:*"
            ],
            "Resource": "*"
        }
    ]
}
EOF
}

resource "aws_iam_instance_profile" "machine" {
  name_prefix = "${local.system_name}-instance"
  role = aws_iam_role.machine.name
}
