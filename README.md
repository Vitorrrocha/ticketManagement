

<h1 align="center"><b>Ticket Management Api 🎫</b></h1>

### For successfully completing this task create a rudimentary event ticket managementsolution. The overall goal is to be able to create events and manage the number of people accessing each event.

## 🚀 Technologies

This project was developed with the following technologies:

- Back-End
  - [Python](https://www.python.org/)
  - Pytest
  - Pylint
  - Alembic
  - Black
  - SQLAlchemy
  - SQLite
  - Coverage

### Available Scripts 💻
 <p>
  
  **Cloning repository**

  ```bash
  $ git clone https://github.com/Vitorrrocha/ticketManagement.git && cd ticketManagement
  ```

  **Installing dependencies**

  ```bash
  $ python3 -m venv venv
  $ source venv/bin/activate
  $ pip3 install -r requirements.txt
  $ alembic upgrade head  # to add the migrations and the database
  ```
  **!! Before start please populate the database !!**

  **Getting Started**

  ```bash
  $ flask --app ticket.manage --debug run
  ```
**Or you can use the configuration bellow at your launch.json**
```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    // flask --app ticket.manage run
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "ticket.manage.py",
                "FLASK_DEBUG": "1"
            },
            "args": [
                "run",
                "--debugger",
                "--reload"
            ],
            "jinja": true,
            "justMyCode": true
        }
    ]
}
```
    

 </p>


## Your task


### Request:
        GET /redeem/<ticketIdentifier>
### Response:
    200 OK: If the ticket is OK.
    
    410 GONE: If the ticket has been redeemed.



from ticket.config import *
from ticket.model import *
db_conn = DBConnectionHandler()
engine = db_conn.get_engine()
Base.metadata.create_all(engine)




