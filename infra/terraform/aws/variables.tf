variable "region" {
  default = "us-east-1"
}

variable "ami" {
  description = "AMI to use"
}

variable "instance_type" {
  default = "t2.micro"
}