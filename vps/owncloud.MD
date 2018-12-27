## owncloud

yum install httpd -y

yum install php -y

yum install mariadb mariadb-server -y

systemctl restart httpd

Job for httpd.service failed because the control process exited with error code. See "systemctl status httpd.service" and "journalctl -xe" for details.

(98)Address already in use: AH00072: make_sock: could not bind to address 0.0.0.0:80

netstat -tulpn | grep :80

kill -9 [PID]

systemctl status httpd

systemctl start mariadb

ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)