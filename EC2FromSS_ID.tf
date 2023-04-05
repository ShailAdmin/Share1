variable "snapshot_id" {}

provider "aws" {
  region = "us-west-2" 

data "aws_snapshot" "SS1" {
  snapshot_id = var.snapshot_id
}

resource "aws_instance" "INC1" {
  ami           = data.aws_snapshot.example.id
  instance_type = "t2.micro"
  key_name      = "my_key_pair"
  subnet_id     = "subnet-12345678" 
  vpc_security_group_ids = ["sg-12345678"] 
  associate_public_ip_address = true
  tags = {
    Name = "Backup Instance"
  }
}
