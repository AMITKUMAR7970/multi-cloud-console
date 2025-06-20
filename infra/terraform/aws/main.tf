provider "aws" {
  region = var.region
}

resource "aws_instance" "app" {
  ami           = var.ami
  instance_type = var.instance_type

  tags = {
    Name = "hybrid-cloud-app"
  }
}

output "instance_id" {
  value = aws_instance.app.id
}