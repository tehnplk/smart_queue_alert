from pyfcm import FCMNotification
import socketio
from datetime import datetime
import mysql.connector

###########  config ################

hos_name = "โรงพยาบาลด่านขุนทด"
queue_signal = "http://localhost:19009"
api_key = "AIzaSyBOZuUvtAUY0V3WBwIET9000mn_bmGTCCQ"


### แก้ไขเชื่อมต่อ HIS ###
def con_db_his():
    db = mysql.connector.connect(
        host='192.168.1.250',
        user='admin',
        passwd='208208145',
        db='dkthosdb',
        port=3306
    )
    return db


###########  end-config ################

##########  data_message *** ห้ามแก้ *** ###########
data_message = {
    "click_action": "FLUTTER_NOTIFICATION_CLICK",
    "id": "1",
    "status": "done",
    "screen": "QueuePage"
}


##########  push_alert *** ห้ามแก้ *** ###########
def push_alert(_token, _title, _msg_body):
    return push_service.notify_single_device(
        registration_id=_token,
        message_title=_title,
        message_body=_msg_body,
        data_message=data_message,
        low_priority=False
    )


##########  current_queue_alert *** ห้ามแก้ *** ###########
def current_queue_alert(_q, dep_name):
    sql = f""" SELECT s.token FROM ovst_queue_server o
inner JOIN smart_assis_client s on s.hn = o.hn
WHERE o.date_visit = CURDATE() and o.depq = '{_q}' """
    db = con_db_his()
    cursor = db.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    cursor.close()
    db.close()
    token = "" if row is None else row[0]

    msg_body = f"""หมายเลข {_q} ถึงคิวของท่านแล้ว"""
    resp = push_service.notify_single_device(
        registration_id=token,
        message_title=dep_name,
        message_body=msg_body,
        data_message=data_message,
        low_priority=False
    )
    print(datetime.now(), f"Current queue {_q}", resp)


def ax_alert():
    print(datetime.now(), 'ax_alert')
    dep_name = "หน้าห้องตรวจโรคทั่วไป"
    m, n = 5, 10  # เตือนคนที่เท่าไร กับ เท่าไร

    sql = f""" SELECT q.depq,a.token
                FROM ovst_queue_server q
                inner join ovst o on o.vn = q.vn
                LEFT JOIN smart_assis_client a on a.hn = q.hn
                WHERE q.STATUS = '1'
                AND q.date_visit = CURDATE()
                AND q.stationno IS NULL
                AND q.dep in ('002','051')
                AND o.cur_dep in ('002','051')
                ORDER BY q.time_visit asc LIMIT 10 """
    db = con_db_his()
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    db.close()

    try:
        _q = str(rows[m - 1][0])
        _token = str(rows[m - 1][1])
        _title = f"อีก {m} คิวจะถึงคิวของท่าน"
        _body = f"""{hos_name} หมายเลข {_q} กรุณาไปรอที่บริเวณ{dep_name}"""
        resp = push_alert(_token, _title, _body)
        print(datetime.now(), resp)
    except Exception as e:
        print(datetime.now(), str(e))

    try:
        _q = str(rows[n - 1][0])
        _token = str(rows[n - 1][1])
        _title = f"อีก {n} คิวจะถึงคิวของท่าน"
        _body = f"""{hos_name} หมายเลข {_q} กรุณาไปรอที่บริเวณ{dep_name}"""
        resp = push_alert(_token, _title, _body)
        print(datetime.now(), resp)
    except Exception as e:
        print(datetime.now(), str(e))


def bx_alert():
    print(datetime.now(), 'bx_alert')
    dep_name = "หน้าห้องตรวจโรคทั่วไป"
    m, n = 5, 10  # เตือนคนที่เท่าไร กับ เท่าไร

    sql = f""" SELECT q.depq,a.token
                FROM ovst_queue_server q
                inner join ovst o on o.vn = q.vn
                LEFT JOIN smart_assis_client a on a.hn = q.hn
                WHERE q.STATUS = '1'
                AND q.date_visit = CURDATE()
                AND q.stationno IS NULL
                AND q.dep in ('052','053')
                AND o.cur_dep in ('052','053')
                ORDER BY q.time_visit asc LIMIT 10 """
    db = con_db_his()
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    db.close()

    try:
        _q = str(rows[m - 1][0])
        _token = str(rows[m - 1][1])
        _title = f"อีก {m} คิวจะถึงคิวของท่าน"
        _body = f"""{hos_name} หมายเลข {_q} กรุณาไปรอที่บริเวณ{dep_name}"""
        resp = push_alert(_token, _title, _body)
        print(datetime.now(), resp)
    except Exception as e:
        print(datetime.now(), str(e))

    try:
        _q = str(rows[n - 1][0])
        _token = str(rows[n - 1][1])
        _title = f"อีก {n} คิวจะถึงคิวของท่าน"
        _body = f"""{hos_name} หมายเลข {_q} กรุณาไปรอที่บริเวณ{dep_name}"""
        resp = push_alert(_token, _title, _body)
        print(datetime.now(), resp)
    except Exception as e:
        print(datetime.now(), str(e))


def ay_alert():
    print(datetime.now(), 'ay_alert')
    dep_name = "ห้องตรวจโรคทั่วไป"
    m, n = 5, 10  # เตือนคนที่เท่าไร กับ เท่าไร

    sql = f""" SELECT q.depq,a.token
                FROM ovst_queue_server q
                inner join ovst o on o.vn = q.vn
                LEFT JOIN smart_assis_client a on a.hn = q.hn
                WHERE q.STATUS = '1'
                AND q.date_visit = CURDATE()
                AND q.stationno IS NULL
                AND q.dep in ('003','028','029','046')
                AND o.cur_dep in ('003','028','029','046')
                ORDER BY q.time_visit asc LIMIT 10 """
    db = con_db_his()
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    db.close()

    try:
        _q = str(rows[m - 1][0])
        _token = str(rows[m - 1][1])
        _title = f"อีก {m} คิวจะถึงคิวของท่าน"
        _body = f"""{hos_name} หมายเลข {_q} กรุณาไปรอที่บริเวณ{dep_name}"""
        resp = push_alert(_token, _title, _body)
        print(datetime.now(), resp)
    except Exception as e:
        print(datetime.now(), str(e))

    try:
        _q = str(rows[n - 1][0])
        _token = str(rows[n - 1][1])
        _title = f"อีก {n} คิวจะถึงคิวของท่าน"
        _body = f"""{hos_name} หมายเลข {_q} กรุณาไปรอที่บริเวณ{dep_name}"""
        resp = push_alert(_token, _title, _body)
        print(datetime.now(), resp)
    except Exception as e:
        print(datetime.now(), str(e))


def by_alert():
    print(datetime.now(), 'ay_alert')
    dep_name = "ห้องตรวจโรคทั่วไป"
    m, n = 5, 10  # เตือนคนที่เท่าไร กับ เท่าไร

    sql = f""" SELECT q.depq,a.token
                FROM ovst_queue_server q
                inner join ovst o on o.vn = q.vn
                LEFT JOIN smart_assis_client a on a.hn = q.hn
                WHERE q.STATUS = '1'
                AND q.date_visit = CURDATE()
                AND q.stationno IS NULL
                AND q.dep in ('030','031','032','034')
                AND o.cur_dep in ('030','031','032','034')
                ORDER BY q.time_visit asc LIMIT 10 """
    db = con_db_his()
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    db.close()

    try:
        _q = str(rows[m - 1][0])
        _token = str(rows[m - 1][1])
        _title = f"อีก {m} คิวจะถึงคิวของท่าน"
        _body = f"""{hos_name} หมายเลข {_q} กรุณาไปรอที่บริเวณ{dep_name}"""
        resp = push_alert(_token, _title, _body)
        print(datetime.now(), resp)
    except Exception as e:
        print(datetime.now(), str(e))

    try:
        _q = str(rows[n - 1][0])
        _token = str(rows[n - 1][1])
        _title = f"อีก {n} คิวจะถึงคิวของท่าน"
        _body = f"""{hos_name} หมายเลข {_q} กรุณาไปรอที่บริเวณ{dep_name}"""
        resp = push_alert(_token, _title, _body)
        print(datetime.now(), resp)
    except Exception as e:
        print(datetime.now(), str(e))


def mx_alert():
    print(datetime.now(), 'mx_alert')
    dep_name = "ห้องการเงิน"
    m, n = 5, 10  # เตือนคนที่เท่าไร กับ เท่าไร

    sql = f""" SELECT q.depq,a.token
            FROM ovst_queue_server_dep q
            LEFT JOIN smart_assis_client a on a.hn = q.hn
            WHERE q.date_visit = CURDATE()
            and q.status = '1'
            AND q.stationno IS NULL
            and q.dep_visit = 'bill'
            ORDER BY q.time_visit asc LIMIT 10 """
    db = con_db_his()
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    db.close()

    try:
        _q = str(rows[m - 1][0])
        _token = str(rows[m - 1][1])
        _title = f"อีก {m} คิวจะถึงคิวของท่าน"
        _body = f"""{hos_name} หมายเลข {_q} กรุณาไปรอที่บริเวณ{dep_name}"""
        resp = push_alert(_token, _title, _body)
        print(datetime.now(), resp)
    except Exception as e:
        print(datetime.now(), str(e))

    try:
        _q = str(rows[n - 1][0])
        _token = str(rows[n - 1][1])
        _title = f"อีก {n} คิวจะถึงคิวของท่าน"
        _body = f"""{hos_name} หมายเลข {_q} กรุณาไปรอที่บริเวณ{dep_name}"""
        resp = push_alert(_token, _title, _body)
        print(datetime.now(), resp)
    except Exception as e:
        print(datetime.now(), str(e))


def rx_alert():
    print(datetime.now(), 'rx_alert')
    dep_name = "ห้องจ่ายยา"
    m, n = 5, 10  # เตือนคนที่เท่าไร กับ เท่าไร

    sql = f""" SELECT q.depq,a.token
            FROM ovst_queue_server_dep q
            LEFT JOIN smart_assis_client a on a.hn = q.hn
            WHERE q.date_visit = CURDATE()
            and q.status = '1'
            AND q.stationno IS NULL
            and q.dep_visit = 'drug'
            ORDER BY q.time_visit asc LIMIT 10 """
    db = con_db_his()
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    db.close()

    try:
        _q = str(rows[m - 1][0])
        _token = str(rows[m - 1][1])
        _title = f"อีก {m} คิวจะถึงคิวของท่าน"
        _body = f"""{hos_name} หมายเลข {_q} กรุณาไปรอที่บริเวณ{dep_name}"""
        resp = push_alert(_token, _title, _body)
        print(datetime.now(), resp)
    except Exception as e:
        print(datetime.now(), str(e))

    try:
        _q = str(rows[n - 1][0])
        _token = str(rows[n - 1][1])
        _title = f"อีก {n} คิวจะถึงคิวของท่าน"
        _body = f"""{hos_name} หมายเลข {_q} กรุณาไปรอที่บริเวณ{dep_name}"""
        resp = push_alert(_token, _title, _body)
        print(datetime.now(), resp)
    except Exception as e:
        print(datetime.now(), str(e))


if __name__ == '__main__':

    push_service = FCMNotification(api_key=api_key)
    sio = socketio.Client()
    sio.connect(queue_signal)
    print(datetime.now(), "App Smart Assis Alert Service is Running.")


    ###  รอรับสัญญาณเรียกคิว ###
    @sio.event
    def ax5(_q):
        if _q != 's99999':
            ax_alert()
            current_queue_alert(_q, "หน้าห้องตรวจโรค")  # คิวที่กดเรียก


    @sio.event
    def ax6(_q):
        if _q != 's99999':
            ax_alert()
            current_queue_alert(_q, "หน้าห้องตรวจโรค")  # คิวที่กดเรียก


    @sio.event
    def bx3(_q):
        if _q != 's99999':
            bx_alert()
            current_queue_alert(_q, "หน้าห้องตรวจโรค")  # คิวที่กดเรียก


    @sio.event
    def bx4(_q):
        if _q != 's99999':
            bx_alert()
            current_queue_alert(_q, "หน้าห้องตรวจโรค")  # คิวที่กดเรียก


    @sio.event
    def ay1(_q):
        if _q != 's99999':
            ay_alert()
            current_queue_alert(_q, "หน้าห้องตรวจโรค")  # คิวที่กดเรียก


    @sio.event
    def ay2(_q):
        if _q != 's99999':
            ay_alert()
            current_queue_alert(_q, "หน้าห้องตรวจโรค")  # คิวที่กดเรียก


    @sio.event
    def ay3(_q):
        if _q != 's99999':
            ay_alert()
            current_queue_alert(_q, "หน้าห้องตรวจโรค")  # คิวที่กดเรียก


    @sio.event
    def ay9(_q):
        if _q != 's99999':
            ay_alert()
            current_queue_alert(_q, "หน้าห้องตรวจโรค")  # คิวที่กดเรียก


    @sio.event
    def by4(_q):
        if _q != 's99999':
            by_alert()
            current_queue_alert(_q, "หน้าห้องตรวจโรค")  # คิวที่กดเรียก


    @sio.event
    def by5(_q):
        if _q != 's99999':
            by_alert()
            current_queue_alert(_q, "หน้าห้องตรวจโรค")  # คิวที่กดเรียก


    @sio.event
    def by6(_q):
        if _q != 's99999':
            by_alert()
            current_queue_alert(_q, "หน้าห้องตรวจโรค")  # คิวที่กดเรียก


    @sio.event
    def by7(_q):
        if _q != 's99999':
            by_alert()
            current_queue_alert(_q, "หน้าห้องตรวจโรค")  # คิวที่กดเรียก


    @sio.event
    def mx5(_q):
        if _q != 's99999':
            mx_alert()
            current_queue_alert(_q, "หน้าห้องตรวจโรค")  # คิวที่กดเรียก


    @sio.event
    def rx1(_q):
        if _q != 's99999':
            rx_alert()
            current_queue_alert(_q, "หน้าห้องตรวจโรค")  # คิวที่กดเรียก


    @sio.event
    def rx2(_q):
        if _q != 's99999':
            rx_alert()
            current_queue_alert(_q, "หน้าห้องตรวจโรค")  # คิวที่กดเรียก


    @sio.event
    def rx3(_q):
        if _q != 's99999':
            rx_alert()
            current_queue_alert(_q, "หน้าห้องตรวจโรค")  # คิวที่กดเรียก


    @sio.event
    def rx4(_q):
        if _q != 's99999':
            rx_alert()
            current_queue_alert(_q, "หน้าห้องตรวจโรค")  # คิวที่กดเรียก
