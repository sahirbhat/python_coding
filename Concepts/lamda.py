import pymysql
import os
import json

# Fetching credentials from environment variables
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
database = os.getenv('DATABASE')

def lambda_handler(event, context):
    try:
        # Connect to MySQL database
        conn = pymysql.connect(
            host=host,
            user=username,
            password=password,
            database=database,
            connect_timeout=5
        )
    except pymysql.MySQLError as e:
        print(f'Connection error: {e}')
        return {
            'statusCode': 500,
            'body': json.dumps('Database connection error')
        }

    try:
        user_id = event.get('id')
        if not user_id:
            return {
                'statusCode': 400,
                'body': json.dumps('User ID is missing')
            }

        with conn.cursor() as cursor:
            query = 'SELECT * FROM student WHERE id = %s'
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()

        if result:
            return {
                'statusCode': 200,
                'body': json.dumps({'data': result})
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps('No record found for the given ID')
            }

    except Exception as e:
        print(f'Query error: {e}')
        return {
            'statusCode': 500,
            'body': json.dumps('An error occurred while processing the request')
        }

    finally:
        conn.close()
