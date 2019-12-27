import pandas as pd
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, current_app, jsonify
from app import db
from app.models import Sortable
from app.main import bp
import os
import json

import pandas as pd
import numpy as np

info = json.loads(os.getenv('SEG_INFO'))
s_names = info['Segment Names']
s = info['Items']
coef = info['Coef']
t='?'

@bp.route('/index')
@bp.route('/')
def index():
    sort = Sortable.query.filter_by(id=1).first()
    if sort:
        ordem = str(sort.data)
    else:
        items = json.loads(os.getenv('SEG_INFO'))['Items']
        ordem = "+".join([str(i) for i in range(1, len(items)+1)])

    return render_template('index.html', ordem=ordem, s=s, t=t)

@bp.route('/post', methods=['GET', 'POST'])
def post():
    json = request.json
    final = ("+".join(json))
    sort = Sortable.query.filter_by(id=1).first()
    sort.data = final
    db.session.commit()

    return str('')

@bp.route('/gettype', methods=['POST'])
def get_type():
    final = ("+".join(request.form['final'][1:-1].replace('"', "").split(",")))
    #model = pd.DataFrame(coef)
    l = [int(c) for c in final.split('+')]
    #print(l)
    l = pd.Series([l.index(i)+1 for i in range(1, len(l)+1)])
    #seg = pd.Series([(l * model[col]).sum() for col in model]).idxmax()

    return jsonify({'Segment' : list(l)})
