variable "name" {
  description = "VM name"
  type        = string
}
variable "ami" {
  description = "AMI ID"
  type        = string
}
variable "instance_type" {
  description = "Instance type"
  type        = string
  default     = "t2.micro"
}
variable "subnet_id" {
  description = "Subnet ID"
  type        = string
}

resource "aws_instance" "main" {
  ami           = var.ami
  instance_type = var.instance_type
  subnet_id     = var.subnet_id

  tags = {
    Name = var.name
  }
}

output "instance_id" {
  value = aws_instance.main.id
}