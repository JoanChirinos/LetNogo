import os

from flask import Flask, render_template, redirect, url_for, session, request, flash, get_flashed_messages
import datetime
import uuid # tentative

from util import db, api

app = Flask(__name__)
app.secret_key = os.urandom(32)


DB_FILE = 'data/tuesday.db'
db.create_db()

db.get_quote()






if __name__ == '__main__':
    app.debug = True
    app.run()

