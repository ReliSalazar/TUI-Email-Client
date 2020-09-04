# TUI Email Client

This is a small project for a course. It can receive emails, and the idea is that in the future It can send them too.


### Usage

I recommend you to use a Python enviroment

```sh
$ Python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python email_tui.py
```

if you use a email client like gmail that needs a second verification login, you can google how to get an app password to use this.

Also, the port usually is something like *"imap.gmail.com"* and the port 993, but you can google that stuff too if don't work to you.


### The other files

* **email_retrieve.py** is a class needed in **email_tui.py**
* **receive_email.py** is a script that print in terminal the new emails with a flag of *'UNSEEN'*
* **send_email** is a script that sendme an email with a image, I have it as a guide for when I implement a form to compose emails and send them.


### Todos

 - Write MORE Tests
 - In the emailListForm add button to write a new email, that send you to de write form
 - Create a write form with three widgets:
    - TitleText from
    - TitleText subject
    - TitleText send-to
    - MultiLine content
  - The write form has two buttons:
    - send to send the email
    - cancel to go back to the emailListForm
 
