import os
import mysql.connector
from dotenv import load_dotenv
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
load_dotenv()
localhost = os.getenv("MYSQL_HOST")
user = os.getenv("MYSQL_USERNAME")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

def get_db_connection():
    try:
        db_connection = mysql.connector.connect(
            host=localhost,
            user=user,
            password=password,
            database=database,
            auth_plugin="caching_sha2_password"
        )
        return db_connection
    except mysql.connector.Error as err:
        print(err)

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
def is_admin(telegram_user_id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            SELECT COUNT(*) AS count FROM admins WHERE telegram_user_id = %s
        """
        cursor.execute(query, (telegram_user_id,))
        result = cursor.fetchone()
        return result['count'] > 0
    except mysql.connector.Error:
        return False
    finally:
        cursor.close()
        db_connection.close()

def is_absolute_admin(telegram_user_id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            SELECT status FROM admins WHERE telegram_user_id = %s 
        """
        cursor.execute(query, (telegram_user_id,))
        result = cursor.fetchone()
        return result['status'] == 'absolute_admin' if result else False
    except mysql.connector.Error:
        return False
    finally:
        cursor.close()
        db_connection.close()


def get_user_status(telegram_user_id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            SELECT status FROM admins WHERE telegram_user_id = %s
        """
        cursor.execute(query, (telegram_user_id,))
        result = cursor.fetchone()
        return result['status'] if result else None
    except mysql.connector.Error:
        return None
    finally:
        cursor.close()
        db_connection.close()

def get_whoever(telegram_user_id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query_admins = """
            SELECT * FROM admins WHERE telegram_user_id = %s
        """
        cursor.execute(query_admins, (telegram_user_id,))
        admin = cursor.fetchone()

        if admin:
            return ["admin",admin]
        
        query_users = """
            SELECT * FROM users WHERE telegram_user_id = %s
        """
        cursor.execute(query_users, (telegram_user_id,))
        user = cursor.fetchone()

        if user:
            return ["user",user]
        
        return None

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return None
    finally:
        cursor.close()
        db_connection.close()
def is_user(telegram_user_id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        select_query = """
            SELECT * FROM users WHERE telegram_user_id = %s
        """
        cursor.execute(select_query, (telegram_user_id,))
        user = cursor.fetchone()
        if user:
            return True
        return False
    except mysql.connector.Error as err:
        return None
    finally:
        cursor.close()
        db_connection.close()

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
def create_admin(telegram_user_id, status='admin'):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            INSERT INTO admins (telegram_user_id, status) VALUES (%s, %s)
        """
        cursor.execute(query, (telegram_user_id, status))
        db_connection.commit()
        return True
    except mysql.connector.Error as err:
        return False
    finally:
        cursor.close()
        db_connection.close()

def get_admin(telegram_user_id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            SELECT * FROM admins WHERE telegram_user_id = %s
        """
        cursor.execute(query, (telegram_user_id,))
        admin = cursor.fetchone()
        return admin
    except mysql.connector.Error as err:
        return None
    finally:
        cursor.close()
        db_connection.close()

def get_admins():
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            SELECT * FROM admins
        """
        cursor.execute(query, )
        admin = cursor.fetchall()
        return admin
    except mysql.connector.Error as err:
        return None
    finally:
        cursor.close()
        db_connection.close()

def get_only_admins():
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            SELECT * FROM admins WHERE status = %s
        """
        cursor.execute(query, ("admin",))
        admin = cursor.fetchall()
        return admin
    except mysql.connector.Error as err:
        return None
    finally:
        cursor.close()
        db_connection.close()

def admins_have_chat_id():
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            SELECT * FROM admins WHERE chat_id IS NOT NULL
        """
        cursor.execute(query,)
        admin = cursor.fetchall()
        return admin
    except mysql.connector.Error as err:
        return None
    finally:
        cursor.close()
        db_connection.close()

    
def update_admin_status(telegram_user_id, new_status):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            UPDATE admins SET status = %s WHERE telegram_user_id = %s
        """
        cursor.execute(query, (new_status, telegram_user_id))
        db_connection.commit()
        return True
    except mysql.connector.Error as err:
        return False
    finally:
        cursor.close()
        db_connection.close()

def update_admin_chat_id(telegram_user_id, chat_id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            UPDATE admins SET chat_id = %s WHERE telegram_user_id = %s
        """
        cursor.execute(query, (chat_id, telegram_user_id))
        db_connection.commit()
        return True
    except mysql.connector.Error as err:
        return False
    finally:
        cursor.close()
        db_connection.close()

def update_admin_lang(telegram_user_id, lang):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            UPDATE admins SET lang = %s WHERE telegram_user_id = %s
        """
        cursor.execute(query, (lang, telegram_user_id))
        db_connection.commit()
        return True
    except mysql.connector.Error as err:
        return False
    finally:
        cursor.close()
        db_connection.close()


def delete_admin(telegram_user_id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            DELETE FROM admins WHERE telegram_user_id = %s
        """
        cursor.execute(query, (telegram_user_id,))
        db_connection.commit()
        return True
    except mysql.connector.Error as err:
        return False
    finally:
        cursor.close()
        db_connection.close()
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
def create_user(telegram_user_id, lang='uzb'):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        insert_query = """
            INSERT INTO users (telegram_user_id, lang) 
            VALUES (%s, %s)
        """
        cursor.execute(insert_query, (telegram_user_id, lang))
        db_connection.commit()
        return True
    except mysql.connector.Error as err:
        return False
    finally:
        cursor.close()
        db_connection.close()

def get_user(telegram_user_id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        select_query = """
            SELECT * FROM users WHERE telegram_user_id = %s
        """
        cursor.execute(select_query, (telegram_user_id,))
        user = cursor.fetchone()
        return user
    except mysql.connector.Error as err:
        return None
    finally:
        cursor.close()
        db_connection.close()

def update_user_lang(telegram_user_id, lang=None):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = f"UPDATE users SET lang = %s WHERE telegram_user_id = %s"
        cursor.execute(query, (lang,telegram_user_id,))
        db_connection.commit()
        return True
    except mysql.connector.Error as err:
        return False
    finally:
        cursor.close()
        db_connection.close()

def delete_user(telegram_user_id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        delete_query = """
            DELETE FROM users WHERE telegram_user_id = %s
        """
        cursor.execute(delete_query, (telegram_user_id,))
        db_connection.commit()
        return True
    except mysql.connector.Error as err:
        return False
    finally:
        cursor.close()
        db_connection.close()

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
def create_channel(channel_data):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            INSERT INTO channels (username, for_work_as_admin, for_post_ads, for_users_to_follow) 
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (
            channel_data['username'], 
            channel_data['for_work_as_admin'], 
            channel_data['for_post_ads'], 
            channel_data['for_users_to_follow']
        ))
        db_connection.commit()
        return True
    except mysql.connector.Error as err:
        print(err)
        return False
    finally:
        cursor.close()
        db_connection.close()


def get_channel(id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            SELECT * FROM channels WHERE id = %s
        """
        cursor.execute(query, (id,))
        channel = cursor.fetchone()
        return channel
    except mysql.connector.Error as err:
        print(err)
        return None
    finally:
        cursor.close()
        db_connection.close()
def is_channel_exists(username):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            SELECT * FROM channels WHERE username = %s
        """
        cursor.execute(query, (username,))
        channel = cursor.fetchone()
        if channel:
            return True
        return False 
    except mysql.connector.Error as err:
        print(err)
        return None
    finally:
        cursor.close()
        db_connection.close()



def get_channels():
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            SELECT * FROM channels 
        """
        cursor.execute(query, )
        channels = cursor.fetchall()
        return channels
    except mysql.connector.Error as err:
        print(err)
        return None
    finally:
        cursor.close()
        db_connection.close()

def get_channels_sp1():
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            SELECT * FROM channels WHERE for_users_to_follow = True
        """
        cursor.execute(query)
        channel = cursor.fetchall()
        return channel
    except mysql.connector.Error as err:
        return None
    finally:
        cursor.close()
        db_connection.close()

def get_channels_sp2():
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            SELECT * FROM channels WHERE for_post_ads = True
        """
        cursor.execute(query)
        channel = cursor.fetchall()
        return channel
    except mysql.connector.Error as err:
        return None
    finally:
        cursor.close()
        db_connection.close()

def update_channel(telegram_id, username=None, for_work_as_admin=None, for_post_ads=None, for_users_to_follow=None):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        update_fields = []
        values = []

        if username is not None:
            update_fields.append("username = %s")
            values.append(username)
        if for_work_as_admin is not None:
            update_fields.append("for_work_as_admin = %s")
            values.append(for_work_as_admin)
        if for_post_ads is not None:
            update_fields.append("for_post_ads = %s")
            values.append(for_post_ads)
        if for_users_to_follow is not None:
            update_fields.append("for_users_to_follow = %s")
            values.append(for_users_to_follow)

        if update_fields:
            query = f"UPDATE channels SET {', '.join(update_fields)} WHERE telegram_id = %s"
            values.append(telegram_id)
            cursor.execute(query, tuple(values))
            db_connection.commit()
            return True
    except mysql.connector.Error as err:
        return False
    finally:
        cursor.close()
        db_connection.close()

def delete_channel(id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            DELETE FROM channels WHERE id = %s
        """
        cursor.execute(query, (id,))
        db_connection.commit()
        return True
    except mysql.connector.Error as err:
        return False
    finally:
        cursor.close()
        db_connection.close()



#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

def create_ads_vacancy(ad_data):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            INSERT INTO ads_vacancy (telegram_id, skills, company, activity, hr, phone_number, territory, 
            work_time, salary, additionals, channel) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            ad_data['telegram_id'], 
            ad_data['skills'], 
            ad_data['company'], 
            ad_data['activity'], 
            ad_data['hr'], 
            ad_data['phone_number'], 
            ad_data['territory'], 
            ad_data['work_time'], 
            ad_data['salary'], 
            ad_data['additionals'], 
            ad_data['channel']
        ))
        db_connection.commit()
        new_id = cursor.lastrowid
        return new_id
    except mysql.connector.Error as err:
        print(err)
        return False
    finally:
        cursor.close()
        db_connection.close()

def get_ads_vacancy(id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            SELECT * FROM ads_vacancy WHERE id = %s
        """
        cursor.execute(query, (id,))
        vacancy = cursor.fetchone()
        return vacancy
    except mysql.connector.Error as err:
        return None
    finally:
        cursor.close()
        db_connection.close()

def update_ads_vacancy(telegram_id, skills=None, company=None, activity=None, hr=None, phone_number=None, teritory=None, work_time=None, salary=None, additionals=None, channel=None):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        update_fields = []
        values = []

        if skills is not None:
            update_fields.append("skills = %s")
            values.append(skills)
        if company is not None:
            update_fields.append("company = %s")
            values.append(company)
        if activity is not None:
            update_fields.append("activity = %s")
            values.append(activity)
        if hr is not None:
            update_fields.append("hr = %s")
            values.append(hr)
        if phone_number is not None:
            update_fields.append("phone_number = %s")
            values.append(phone_number)
        if teritory is not None:
            update_fields.append("teritory = %s")
            values.append(teritory)
        if work_time is not None:
            update_fields.append("work_time = %s")
            values.append(work_time)
        if salary is not None:
            update_fields.append("salary = %s")
            values.append(salary)
        if additionals is not None:
            update_fields.append("additionals = %s")
            values.append(additionals)
        if channel is not None:
            update_fields.append("channel = %s")
            values.append(channel)

        if update_fields:
            query = f"UPDATE ads_vacancy SET {', '.join(update_fields)} WHERE telegram_id = %s"
            values.append(telegram_id)
            cursor.execute(query, tuple(values))
            db_connection.commit()
            return True
    except mysql.connector.Error as err:
        return False
    finally:
        cursor.close()
        db_connection.close()

def delete_ads_vacancy(telegram_id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            DELETE FROM ads_vacancy WHERE telegram_id = %s
        """
        cursor.execute(query, (telegram_id,))
        db_connection.commit()
        return True
    except mysql.connector.Error as err:
        return False
    finally:
        cursor.close()
        db_connection.close()


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
def create_ads_employee(employee_data):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            INSERT INTO ads_employee (telegram_id, name, age, job, experience, phone_number, territory, 
            salary, additionals, channel) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            employee_data['telegram_id'], 
            employee_data['name'], 
            employee_data['age'], 
            employee_data['job'], 
            employee_data['experience'], 
            employee_data['phone_number'], 
            employee_data['territory'], 
            employee_data['salary'], 
            employee_data['additionals'], 
            employee_data['channel']
        ))
        db_connection.commit()
        new_id = cursor.lastrowid
        return new_id
    except mysql.connector.Error as err:
        return False
    finally:
        cursor.close()
        db_connection.close()


def get_ads_employee(id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            SELECT * FROM ads_employee WHERE id = %s
        """
        cursor.execute(query, (id,))
        employee = cursor.fetchone()
        return employee
    except mysql.connector.Error as err:
        return None
    finally:
        cursor.close()
        db_connection.close()

def update_ads_employee(telegram_id, name=None, age=None, job=None, experience=None, number=None, teritory=None, salary=None, additionals=None, channel=None):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        update_fields = []
        values = []

        if name is not None:
            update_fields.append("name = %s")
            values.append(name)
        if age is not None:
            update_fields.append("age = %s")
            values.append(age)
        if job is not None:
            update_fields.append("job = %s")
            values.append(job)
        if experience is not None:
            update_fields.append("experience = %s")
            values.append(experience)
        if number is not None:
            update_fields.append("number = %s")
            values.append(number)
        if teritory is not None:
            update_fields.append("teritory = %s")
            values.append(teritory)
        if salary is not None:
            update_fields.append("salary = %s")
            values.append(salary)
        if additionals is not None:
            update_fields.append("additionals = %s")
            values.append(additionals)
        if channel is not None:
            update_fields.append("channel = %s")
            values.append(channel)

        if update_fields:
            query = f"UPDATE ads_employee SET {', '.join(update_fields)} WHERE telegram_id = %s"
            values.append(telegram_id)
            cursor.execute(query, tuple(values))
            db_connection.commit()
            return True
    except mysql.connector.Error as err:
        return False
    finally:
        cursor.close()
        db_connection.close()

def delete_ads_employee(telegram_id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            DELETE FROM ads_employee WHERE telegram_id = %s
        """
        cursor.execute(query, (telegram_id,))
        db_connection.commit()
        return True
    except mysql.connector.Error as err:
        return False
    finally:
        cursor.close()
        db_connection.close()

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

def create_ads_partner(partner_data):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            INSERT INTO ads_partner (telegram_id, name, activity, phone_number, territory, additionals, channel) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            partner_data['telegram_id'], 
            partner_data['name'], 
            partner_data['activity'], 
            partner_data['phone_number'], 
            partner_data['territory'], 
            partner_data['additionals'], 
            partner_data['channel']
        ))
        db_connection.commit()
        new_id = cursor.lastrowid
        return new_id

    except mysql.connector.Error as err:
        return False
    finally:
        cursor.close()
        db_connection.close()


def get_ads_partner(id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            SELECT * FROM ads_partner WHERE id = %s
        """
        cursor.execute(query, (id,))
        partner = cursor.fetchone()
        return partner
    except mysql.connector.Error as err:
        return None
    finally:
        cursor.close()
        db_connection.close()

def update_ads_partner(telegram_id, name=None, job=None, number=None, teritory=None, additionals=None, channel=None):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        update_fields = []
        values = []

        if name is not None:
            update_fields.append("name = %s")
            values.append(name)
        if job is not None:
            update_fields.append("job = %s")
            values.append(job)
        if number is not None:
            update_fields.append("number = %s")
            values.append(number)
        if teritory is not None:
            update_fields.append("teritory = %s")
            values.append(teritory)
        if additionals is not None:
            update_fields.append("additionals = %s")
            values.append(additionals)
        if channel is not None:
            update_fields.append("channel = %s")
            values.append(channel)

        if update_fields:
            query = f"UPDATE ads_partner SET {', '.join(update_fields)} WHERE telegram_id = %s"
            values.append(telegram_id)
            cursor.execute(query, tuple(values))
            db_connection.commit()
            return True
    except mysql.connector.Error as err:
        return False
    finally:
        cursor.close()
        db_connection.close()

def delete_ads_partner(telegram_id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = """
            DELETE FROM ads_partner WHERE telegram_id = %s
        """
        cursor.execute(query, (telegram_id,))
        db_connection.commit()
        return True
    except mysql.connector.Error as err:
        return False
    finally:
        cursor.close()
        db_connection.close()

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################