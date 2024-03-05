# from flask import Flask, render_template, request, redirect, flash,  url_for, session
# import pandas as pd
# import tensorflow as tf
# from tensorflow import keras

# model = tf.keras.models.load_model('AQ10_model_weights.h5')
# app = Flask(__name__)
# app.secret_key = 'app_secret_key'

# @app.route('/submit', methods=['POST'])
# def submit():
#     scores = {
#         'A1_Score': 0,
#         'A2_Score': 0,
#         'A3_Score': 0,
#         'A4_Score': 0,
#         'A5_Score': 0,
#         'A6_Score': 0,
#         'A7_Score': 0,
#         'A8_Score': 0,
#         'A9_Score': 0,
#         'A10_Score': 0,
#         'A11_Score': 0,
#         'A12_Score': 0,
#         'A13_Score': 0,
#         'A14_Score': 0,
#         'A15_Score': 0,
#         'A16_Score': 0,
#         'A17_Score': 0,
#         'A18_Score': 0

#     }
    
#     for i in range(1, 19):
#         key = 'A{}_Score'.format(i)
#         answer = request.form.get('q{}'.format(i))
#         if answer:
#             if answer == 'agree':
#                 scores[key] = 1
#             elif answer == 'disagree':
#                 scores[key] = 0

#     df = pd.DataFrame(scores, index=[0])
#     predictions = model.predict(df)
#     percentage_yes = predictions[0][1] * 100
#     percentage_no = predictions[0][0] * 100
#     if percentage_yes >= percentage_no: diagnosis = "Yes"
#     else: diagnosis = "No"
#     session['diagnosis'] = diagnosis
#     session['scores'] = scores
#     flash(f"Autism Prediction: {diagnosis}")
#     return redirect(url_for('index'))

# @app.route('/')
# def index():
#     diagnosis = session.get('diagnosis', None)
#     scores = session.get('scores', {
#         'A1_Score': '',
#         'A2_Score': '',
#         'A3_Score': '',
#         'A4_Score': '',
#         'A5_Score': '',
#         'A6_Score': '',
#         'A7_Score': '',
#         'A8_Score': '',
#         'A9_Score': '',
#         'A10_Score': '',
#         'A11_Score': '',
#         'A12_Score': '',
#         'A13_Score': '',
#         'A14_Score': '',
#         'A15_Score': '',
#         'A16_Score': '',
#         'A17_Score': '',
#         'A18_Score': ''
#     })
#     return render_template('index.html', diagnosis=diagnosis, scores=scores)


# @app.route('/contact')
# def contact():
#     return render_template('contact.html')



# if __name__ == '__main__':
#     app.run(debug=True)

#################################################################################################

# from flask import Flask, render_template, request, redirect, flash, url_for, session
# import pandas as pd
# import tensorflow as tf

# model = tf.keras.models.load_model('AQ10_model_weights.h5')
# app = Flask(__name__)
# app.secret_key = 'app_secret_key'

# @app.route('/submit', methods=['POST'])
# def submit():
#     scores = {
#         'A1_Score': 0,
#         'A2_Score': 0,
#         'A3_Score': 0,
#         'A4_Score': 0,
#         'A5_Score': 0,
#         'A6_Score': 0,
#         'A7_Score': 0,
#         'A8_Score': 0,
#         'A9_Score': 0,
#         'A10_Score': 0,
#         'A11_Score': 0,
#         'A12_Score': 0,
#         'A13_Score': 0,
#         'A14_Score': 0,
#         'A15_Score': 0,
#         'A16_Score': 0,
#         'A17_Score': 0,
#         'A18_Score': 0
#     }
    
#     for i in range(1, 19):
#         key = 'A{}_Score'.format(i)
#         answer = request.form.get('q{}'.format(i))
#         if answer:
#             if answer == 'agree':
#                 scores[key] = 1
#             elif answer == 'disagree':
#                 scores[key] = 0

#     df = pd.DataFrame(scores, index=[0])
#     predictions = model.predict(df)
#     percentage_yes = predictions[0][1] * 100
#     percentage_no = predictions[0][0] * 100
#     if percentage_yes >= percentage_no: 
#         diagnosis = "Yes"
#     else: 
#         diagnosis = "No"
#     session['diagnosis'] = diagnosis
#     session['scores'] = scores
#     flash(f"Autism Prediction: {diagnosis}")
#     return redirect(url_for('index'))

# @app.route('/')
# def index():
#     diagnosis = session.get('diagnosis', None)
#     scores = session.get('scores', {})
#     # Clear the scores dictionary to uncheck radio buttons
#     for key in scores:
#         scores[key] = ''
#     return render_template('index.html', diagnosis=diagnosis, scores=scores)

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

# if __name__ == '__main__':
#     app.run(debug=True)


#####################################################################################




# from flask import Flask, render_template, request, redirect, flash, url_for, session
# import pandas as pd
# import joblib

# # Load the decision tree model
# decision_tree_model = joblib.load('./decision_tree_model_02.joblib',)

# app = Flask(__name__)
# app.secret_key = 'app_secret_key'

# @app.route('/submit', methods=['POST'])
# def submit():
#     scores = {
#         'online_acitivity_1': 0,
#         'online_acitivity_2': 0,
#         'online_acitivity_3': 0,
#         'online_acitivity_4': 0,
#         'online_acitivity_5': 0,
#         'online_acitivity_6': 0,
#         'online_acitivity_7': 0,
#         'online_acitivity_8': 0,
#         'online_acitivity_9': 0,
#         'online_acitivity_10': 0,
#         'online_acitivity_11': 0,
#         'online_acitivity_12': 0,
#         'online_acitivity_13': 0,
#         'online_acitivity_14': 0,
#         'online_acitivity_15': 0,
#         'online_acitivity_16': 0,
#         'online_acitivity_17': 0,
#         'online_acitivity_18': 0
#     }
    
#     for i in range(1, 19):
#         key = 'online_acitivity_{}'.format(i)
#         answer = request.form.get('q{}'.format(i))
#         if answer:
#             if answer == 'agree':
#                 scores[key] = 1
#             elif answer == 'disagree':
#                 scores[key] = 0

#     df = pd.DataFrame(scores, index=[0])
    
#     # Use the decision tree model for predictions
#     prediction = decision_tree_model.predict(df)[0]
    
#     # Convert prediction to diagnosis
#     diagnosis = "Yes" if prediction == 1 else "No"

#     session['diagnosis'] = diagnosis
#     session['scores'] = scores
#     flash(f"Autism Prediction: {diagnosis}")
#     return redirect(url_for('index'))

# @app.route('/')
# def index():
#     diagnosis = session.get('diagnosis', None)
#     scores = session.get('scores', {})
#     # Clear the scores dictionary to uncheck radio buttons
#     for key in scores:
#         scores[key] = ''
#     return render_template('index.html', diagnosis=diagnosis, scores=scores)

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')


# if __name__ == '__main__':
#     app.run(debug=True)

#########################################################################

from flask import Flask, render_template, request, redirect, flash, url_for, session
import pandas as pd
import joblib

# Load the decision tree model
decision_tree_model = joblib.load('./decision_tree_model_INTER3.joblib')

app = Flask(__name__)
app.secret_key = 'app_secret_key'

@app.route('/submit', methods=['POST'])
def submit():
    scores = {
        'online_acitivity_1': 0,
        'online_acitivity_2': 0,
        'online_acitivity_3': 0,
        'online_acitivity_4': 0,
        'online_acitivity_5': 0,
        'online_acitivity_6': 0,
        'online_acitivity_7': 0,
        'online_acitivity_8': 0,
        'online_acitivity_9': 0,
        'online_acitivity_10': 0,
        'online_acitivity_11': 0,
        'online_acitivity_12': 0,
        'online_acitivity_13': 0,
        'online_acitivity_14': 0,
        'online_acitivity_15': 0,
        'online_acitivity_16': 0,
        'online_acitivity_17': 0,
        'online_acitivity_18': 0
    }
    
    for i in range(1, 19):
        key = 'online_acitivity_{}'.format(i)
        answer = request.form.get('q{}'.format(i))
        if answer:
            if answer == 'agree':
                scores[key] = 1
            elif answer == 'disagree':
                scores[key] = 0

    df = pd.DataFrame(scores, index=[0])
    
    # Use the decision tree model for predictions
    prediction_proba = decision_tree_model.predict_proba(df)[0]
    percentage_yes = prediction_proba[1] * 100
    percentage_no = prediction_proba[0] * 100
    
    # Convert prediction to diagnosis
    diagnosis = "Yes" if prediction_proba[1] > 0.5 else "No"
    
    # Flash the message
    flash(f"Autism Prediction: {diagnosis} ({percentage_yes:.2f}% Yes, {percentage_no:.2f}% No)")

    # Store data in session
    session['diagnosis'] = diagnosis
    session['percentage_yes'] = percentage_yes
    session['percentage_no'] = percentage_no
    
    # Render the pop-up message
    return render_template('popup.html', diagnosis=diagnosis, percentage_yes=percentage_yes, percentage_no=percentage_no)

@app.route('/')
def index():
    diagnosis = session.get('diagnosis', None)
    percentage_yes = session.get('percentage_yes', None)
    percentage_no = session.get('percentage_no', None)
    scores = session.get('scores', {})  # Retrieve scores from session
    return render_template('index.html', diagnosis=diagnosis, percentage_yes=percentage_yes, percentage_no=percentage_no, scores=scores)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

