resource "aws_security_group" "dbsg-1" {
  name_prefix = "dbsg"
  ingress {
    from_port = 3306
    to_port = 3306
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
resource "aws_db_instance" "mysql_rds-1" {
  allocated_storage    = 20
  engine               = "mysql"
  engine_version       = "5.7"
  instance_class       = "db.t2.micro"
  name                 = "dev_db"
  username             = "user1"
  password             = "password"
  parameter_group_name = "default.mysql5.7"
  storage_type         = "gp2"
  vpc_security_group_ids = ["${aws_security_group.dbsg-1.id}"]
}
