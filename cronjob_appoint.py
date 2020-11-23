from pyfcm import FCMNotification
import mysql.connector


def con_db():
    db = mysql.connector.connect(
        host='192.168.1.254',
        user='sa',
        passwd='sa',
        db='his',
        port=3306
    )
    return db


if __name__ == '__main__':
    _test_token = 'c2ruTDl0lFk:APA91bH6zrdYwW9DiOz76PFkdLAkFMStd831XM1dFgqlQF-WM8Q5_QiG_meJ5Um091qegZf-M79XuzxR6p3cyf-Qb6KYr0qzy9brzv1t1o8MY6XPje9tyOtEWXwRyAtoOPsjm96vM1tK'

    _message_payload = {
        "click_action": "FLUTTER_NOTIFICATION_CLICK",
        "id": "1",
        "status": "done",
        "screen": "AppointPage",
    }

    api_key = "AIzaSyBOZuUvtAUY0V3WBwIET9000mn_bmGTCCQ"
    push_service = FCMNotification(api_key=api_key)

    sql = """ SELECT a.token from oapp o
INNER JOIN smart_assis_client a on a.hn = o.hn 
where o.nextdate = CURDATE() + 1 """

    tokens = list()
    tokens.append(_test_token)

    db = con_db()
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        tokens.append(row[0])
    cursor.close()
    db.close()

    res = push_service.notify_multiple_devices(
        registration_ids=tokens,
        message_title="เตือนวันหมอนัด",
        message_body="กดเพื่อดูรายละเอียด",
        data_message=_message_payload,
        low_priority=False

    )

    print(res)
