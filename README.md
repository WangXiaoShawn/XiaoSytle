# XiaoSytle
Ecommerce by Django
## Setting Up a Development Environment:
pip install -r requirements.txt
## Set the peojetc ：
Create a .env file in the 'Xiao' directory and fill in the following fields:

SECRET_KEY=
Explanation: This is a secret key used by your application for cryptographic signing. It should be kept secret and unique for security reasons.

DEBUG=
Explanation: When set to True, the application will display detailed error pages when an error occurs, useful during development.

EMAIL_HOST=
Explanation: This is the address of the email server that will be used to send emails from your application.

EMAIL_PORT=587
Explanation: This is the port used by the email server for outgoing mail, typically used for TLS encryption.

EMAIL_HOST_USER=
Explanation: This is the email address used as the username for the email server.

EMAIL_HOST_PASSWORD=
Explanation: This is the password corresponding to the email host user. It should be kept secure.

EMAIL_USE_TLS=
Explanation: This indicates that TLS (Transport Layer Security) should be used when connecting to the email server, which enhances security.