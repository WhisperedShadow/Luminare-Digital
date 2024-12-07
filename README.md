# Luminare Digital - Digital Marketing Company Portfolio

Welcome to the Luminare Digital portfolio website repository. This project is a digital marketing company portfolio, built using HTML, CSS, JavaScript, MailJet, Flask, and MySQL.

## Project Setup

### Prerequisites

- Python 3.x
- Node.js
- MySQL database
- Mailjet API (for email functionality)

### Install Dependencies

1. Clone the repository:

```bash
git clone https://github.com/WhisperedShadow/Luminare-Digital.git
cd Luminare-Digital
```

Install Python dependencies:
```bash
pip install -r requirements.txt
```

Configuration
Before running the project, you need to configure your environment variables.

Create a .env file in the root directory of the project and add the following variables:
```bash
# MySQL Configuration
DB_DATABASE="your_database_name"
DB_HOST="your_mysql_host"
DB_PASSWORD="your_mysql_password"
DB_PORT="your_mysql_port"
DB_USERNAME="your_mysql_username"

# Mailjet Configuration
MAIL_API_KEY="your_mailjet_api_key"
MAIL_SECRET_KEY="your_mailjet_secret_key"
FROM_MAIL="your_sender_email"
TO_MAIL="your_receiver_email"
```

