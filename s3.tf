resource "aws_s3_bucket" "s3-1" {
  bucket = "Bucket_Name"
  acl    = "private"

  versioning {
    enabled = true
  }

  lifecycle {
    prevent_destroy = true
  }
}
resource "aws_s3_bucket_tag" "s3-1_tags" {
  for_each = {
    "Environment" = "Production",
    "Application" = "Test"
  }

  bucket = aws_s3_bucket.s3-1.id

  key   = each.key
  value = each.value
}

