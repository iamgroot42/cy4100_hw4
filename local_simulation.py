from email.message import EmailMessage
from datetime import datetime
import os
from smolagents import tool
from typing import List
from collections import defaultdict


VALID_EMAIL_IDS = [
    "alice@example.com",
    "bob@example.com"
    "jedi@example.com"
]

class DummyMailSystem:
    def __init__(self):
        self.mailboxes = defaultdict(list)

    def send(self, sender: str, recipient: str, subject: str, body: str):
        if recipient not in VALID_EMAIL_IDS:
            return False
        msg = EmailMessage()
        msg["From"] = sender
        msg["To"] = recipient
        msg["Subject"] = subject
        msg["Date"] = datetime.now().isoformat()
        msg.set_content(body)

        self.mailboxes[recipient].append(msg)
        return True

    def inbox(self, user: str):
        return list(self.mailboxes[user])
    
    def clear_inbox(self, user: str):
        self.mailboxes[user] = []

MAIL_OBJECT = DummyMailSystem()


@tool
def send_email(recipient: str, subject: str, body: str) -> bool:
  """
    Tool to send email. Returns False if recipient is not valid, True otherwise.

    Args:
        recipient: email address of recipient
        subject: subject of email
        body: body of email
  """
  sender = "alice@example.com"
  return MAIL_OBJECT.send(sender, recipient, subject, body)


@tool
def check_inbox() -> List[str]:
  """
    Tool to check inbox. Returns list of emails.
  """
  sender = "alice@example.com"
  emails = MAIL_OBJECT.inbox(sender)
  return [str(x) for x in emails]
  

@tool
def read_all_files() -> List[str]:
  """
    Tool to read all files.
  """
  all_data = []
  for path in os.listdir("user_files"):
    with open(os.path.join("user_files", path), "r") as f:
      all_data.append(f.read())
  return all_data
