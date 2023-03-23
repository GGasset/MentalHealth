from sqlite3 import Cursor, connect

from manually_explore import db_path

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

mental_health = connect(db_path).cursor()
try:
    questions = [{'question': question[0], 'id': question[1]} for question in mental_health.execute('SELECT questiontext, questionid FROM Question').fetchall()]
    for question in questions:
        print(f'{question["id"]}. {question["question"]}')
    input()
finally:
    mental_health.close()