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