import scheme
from sqlalchemy.orm import Session, joinedload
from model import Account, Question, IQ, Inteverview


def find_account_by_email(db: Session, email):
    db_account = db.query(Account).filter(email == Account.email)
    if db_account:
        for acc in db_account:
            return acc
