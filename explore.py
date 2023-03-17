from sqlite3 import connect, Cursor

from util import *

db_path = './mental_health.sqlite'
'''
If you run .schema on the database the result will be:
CREATE TABLE IF NOT EXISTS "Answer" (     
        "AnswerText" VARCHAR(10000) NULL, 
        "SurveyID" INTEGER NULL,
        "UserID" INTEGER NULL,
        "QuestionID" INTEGER NULL
);
CREATE TABLE IF NOT EXISTS "Question" (   
        "questiontext" VARCHAR(1000) NULL,
        "questionid" INTEGER NULL
);
CREATE TABLE IF NOT EXISTS "Survey" (
        "SurveyID" INTEGER NOT NULL,
        "Description" VARCHAR(255) NULL,
        PRIMARY KEY ("SurveyID")
);
CREATE TABLE sqlite_sequence(name,seq);
'''

def main():
    mental_health_connection = connect(db_path)
    mental_health = mental_health_connection.cursor()
    print('Set-up completed.')

    try:
        survey_id = select_survey(mental_health)
        question_id = select_question(mental_health)
    finally:
        mental_health_connection.close()
        print('Connection closed.')

def select_survey(cursor: Cursor) -> int:
    survey_years = []
    cursor.execute('SELECT Description FROM Survey')
    returned = cursor.fetchall()
    print('Naming surveys...')
    for description in returned:
        description = description[0]
        splitted = description.split(' ')
        survey_years.append(int(splitted[-1]))
        print(description)

    while True:
        selected_survey_year = GetInputInt('Select a year from the list to select a survey to investigate.')
        if selected_survey_year in survey_years:
            cursor.execute(f'SELECT SurveyId, Description FROM Survey WHERE Description LIKE "%{selected_survey_year}"')
            returned = cursor.fetchall()
            print('Selected ' + returned[0][1])
            return returned[0][0]
        
        print('The selected year doesn\'t exists in the data.')
                
def select_question(cursor: Cursor) -> int:
    ids = []
    cursor.execute('SELECT questionid, questiontext FROM Question')
    results = cursor.fetchall()
    print('Naming questions...')
    for result in results:
        question_id = result[0]
        ids.append(question_id)
        print(f'{question_id}. {result[1]}')
    while True:
        selected_id = GetInputInt('Select a question id.')
        if selected_id not in ids:
            print('Id doesn\'t exists.')
            continue

        cursor.execute(f'SELECT questiontext FROM Question WHERE questionid = {selected_id}')
        result = cursor.fetchall()
        print('Selected "' + result[0][0] + '"')
        return selected_id

if __name__ == '__main__':
    main()