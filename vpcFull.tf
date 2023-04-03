provider "aws" {
  region = "us-west-2"
}

resource "aws_vpc" "vpc1" {
  cidr_block = "${var.cidr}"
  enable_dns_hostnames = true
  enable_dns_support = true
  tags = {
    Name = "${var.VPCtag}"
  }
}

resource "aws_internet_gateway" "IGWY1" {
  vpc_id = aws_vpc.IGY1.id
  tags = {
    Name = "${var.igwytag"
  }
}

resource "aws_route_table" "RT1" {
  vpc_id = aws_vpc.vpc1.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.IGWY1.id
  }
  tags = {
    Name = "${var.RTTag}"
  }
}

resource "aws_subnet" "sb1" {
  vpc_id = aws_vpc.vpc1.id
  cidr_block = "${var.scidr}"
  availability_zone = "us-west-2a"
  tags = {
    Name = "${var.SubnetTag}"
  }
}

resource "aws_route_table_association" "my_route_table_association" {
  subnet_id = aws_subnet.sb1.id
  route_table_id = aws_route_table.RT1.id
}
