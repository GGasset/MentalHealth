from sqlite3 import connect, Cursor

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
                pass
        finally:
                mental_health_connection.close()
                print('Connection closed.')

def select_survey(cursor: Cursor):
        survey_years = []


if __name__ == '__main__':
        main()