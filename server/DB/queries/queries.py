
import pymysql


connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="recipes_app",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor,
)



def get_all_gluten_or_dairy_types(sensitivity):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT name
                    FROM ingredients
                    WHERE sensitivity = '{sensitivity}'
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            return [e["name"] for e in result]
    except Exception as e:
        print(e)
