aws lambda create-function \
--function-name shrink-image \
--zip-file fileb:///home/ec2-user/shrink-image.zip \
--role arn:aws:iam::512081569182:role/lambda \
--handler shrink_image.handler \
--runtime python2.7 \
--timeout 10 \
--memory-size 1024
