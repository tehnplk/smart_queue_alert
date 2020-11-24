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
    print(datetime.now(), "calling current queue ", resp)


##########  data_message *** ห้ามแก้ *** ###########
data_message = {
    "click_action": "FLUTTER_NOTIFICATION_CLICK",
    "id": "1",
    "status": "done",
    "screen": "QueuePage"
}

"""
Note : 
-เตือนให้มา ซักประวัติ A (ax) 1-6
-เตือนให้มา ห้องตรวจ A (ay) 1-3,9

-เตือนให้มา ซักประวัติ B (bx) 1-6
-เตือนให้มา ห้องตรวจ B (by) 4-7

-เตือนนให้มา รับยา (rx) 1-5
"""


#### เตือนให้มา ซักประวัติ A (ax) ####
def ax_alert():
    # return None
    ## config ##
    dep_code = "010"
    dep_name = "จุดซักประวัติ A"
    q_signal = "ax"
    m, n = 5, 10  # เตือนคนที่เท่าไร กับ เท่าไร
    ## end-config ##

    sql = f""" SELECT q.depq,a.token
                FROM ovst_queue_server q
                inner join ovst o on o.vn = q.vn
                LEFT JOIN smart_assis_client a on a.hn = q.hn
                WHERE q.STATUS = '1'
                AND q.date_visit = CURDATE()
                AND q.stationno IS NULL
                AND q.dep = '{dep_code}'
                AND o.cur_dep = '{dep_code}'
                ORDER BY q.time_visit asc LIMIT {n} """
    db = con_db_his()
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    db.close()
    print(datetime.now(), f"Calling {q_signal} {dep_code}  =  {len(rows)}")

    try:
        _q = str(rows[m - 1][0])
        _token = str(rows[m - 1][1])
        _title = f"อีก {m} คิวจะถึงคิวของท่าน"
        _body = f"""{hos_name} หมายเลข {_q} กรุณาไปรอที่บริเวณ{dep_name}"""
        resp = push_alert(_token, _title, _body)
        print(datetime.now(), _q, q_signal, resp)
    except Exception as e:
        print(datetime.now(), str(e))

    try:
        _q = str(rows[n - 1][0])
        _token = str(rows[n - 1][1])
        _title = f"อีก {n} คิวจะถึงคิวของท่าน"
        _body = f"""{hos_name} หมายเลข {_q} กรุณาไปรอที่บริเวณ{dep_name}"""
        resp = push_alert(_token, _title, _body)
        print(datetime.now(), _q, q_signal, resp)
    except Exception as e:
        print(datetime.now(), str(e))


#### เตือนให้มา ห้องตรวจ A (ay) ####
def ay_alert():
    # return None
    ## config ##
    dep_code = "014"
    dep_name = "หน้าห้องตรวจ A"
    q_signal = "ay"
    m, n = 5, 10  # เตือนคนที่เท่าไร กับ เท่าไร
    ## end-config ##

    sql = f""" SELECT q.depq,a.token
                FROM ovst_queue_server q
                inner join ovst o on o.vn = q.vn
                LEFT JOIN smart_assis_client a on a.hn = q.hn
                WHERE q.STATUS = '1'
                AND q.date_visit = CURDATE()
                AND q.stationno IS NULL
                AND q.dep = '{dep_code}'
                AND o.cur_dep = '{dep_code}'
                ORDER BY q.time_visit asc LIMIT {n} """
    db = con_db_his()
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    db.close()
    print(datetime.now(), f"Calling {q_signal} {dep_code}  =  {len(rows)}")

    try:
        _q = str(rows[m - 1][0])
        _token = str(rows[m - 1][1])
        _title = f"อีก {m} คิวจะถึงคิวของท่าน"
        _body = f"""{hos_name} หมายเลข {_q} กรุณาไปรอที่บริเวณ{dep_name}"""
        resp = push_alert(_token, _title, _body)
        print(datetime.now(), _q, q_signal, resp)
    except Exception as e:
        print(datetime.now(), str(e))

    try:
        _q = str(rows[n - 1][0])
        _token = str(rows[n - 1][1])
        _title = f"อีก {n} คิวจะถึงคิวของท่าน"
        _body = f"""{hos_name} หมายเลข {_q} กรุณาไปรอที่บริเวณ{dep_name}"""
        resp = push_alert(_token, _title, _body)
        print(datetime.now(), _q, q_signal, resp)
    except Exception as e:
        print(datetime.now(), str(e))


#### เตือนให้มา ซักประวัติ B (bx) ####
def bx_alert():
    return None
    ## config ##
    dep_code = "010"
    dep_name = "จุดซักประวัติ B"
    q_signal = "bx"
    m, n = 5, 10  # เตือนคนที่เท่าไร กับ เท่าไร
    ## end-config ##

    sql = f""" SELECT q.depq,a.token
                FROM ovst_queue_server q
                inner join ovst o on o.vn = q.vn
                LEFT JOIN smart_assis_client a on a.hn = q.hn
                WHERE q.STATUS = '1'
                AND q.date_visit = CURDATE()
                AND q.stationno IS NULL
                AND q.dep = '{dep_code}'
                AND o.cur_dep = '{dep_code}'
                ORDER BY q.time_visit asc LIMIT {n} """
    db = con_db_his()
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    db.close()
    print(datetime.now(), f"Calling {q_signal} {dep_code}  =  {len(rows)}")

    try:
        _q = str(rows[m - 1][0])
        _token = str(rows[m - 1][1])
        _title = f"อีก {m} คิวจะถึงคิวของท่าน"
        _body = f"""{hos_name} หมายเลข {_q} กรุณาไปรอที่บริเวณ{dep_name}"""
        resp = push_alert(_token, _title, _body)
        print(datetime.now(), _q, q_signal, resp)
    except Exception as e:
        print(datetime.now(), str(e))

    try:
        _q = str(rows[n - 1][0])
        _token = str(rows[n - 1][1])
        _title = f"อีก {n} คิวจะถึงคิวของท่าน"
        _body = f"""{hos_name} หมายเลข {_q} กรุณาไปรอที่บริเวณ{dep_name}"""
        resp = push_alert(_token, _title, _body)
        print(datetime.now(), _q, q_signal, resp)
    except Exception as e:
        print(datetime.now(), str(e))


#### เตือนให้มา ห้องตรวจ B (by) ####
def by_alert():
    return None
    ## config ##
    dep_code = "010"
    dep_name = "หน้าห้องตรวจ B"
    q_signal = "by"
    m, n = 5, 10  # เตือนคนที่เท่าไร กับ เท่าไร
    ## end-config ##

    sql = f""" SELECT q.depq,a.token
                FROM ovst_queue_server q
                inner join ovst o on o.vn = q.vn
                LEFT JOIN smart_assis_client a on a.hn = q.hn
                WHERE q.STATUS = '1'
                AND q.date_visit = CURDATE()
                AND q.stationno IS NULL
                AND q.dep = '{dep_code}'
                AND o.cur_dep = '{dep_code}'
                ORDER BY q.time_visit asc LIMIT {n} """
    db = con_db_his()
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    db.close()
    print(datetime.now(), f"Calling {q_signal} {dep_code}  =  {len(rows)}")

    try:
        _q = str(rows[m - 1][0])
        _token = str(rows[m - 1][1])
        _title = f"อีก {m} คิวจะถึงคิวของท่าน"
        _body = f"""{hos_name} หมายเลข {_q} กรุณาไปรอที่บริเวณ{dep_name}"""
        resp = push_alert(_token, _title, _body)
        print(datetime.now(), _q, q_signal, resp)
    except Exception as e:
        print(datetime.now(), str(e))

    try:
        _q = str(rows[n - 1][0])
        _token = str(rows[n - 1][1])
        _title = f"อีก {n} คิวจะถึงคิวของท่าน"
        _body = f"""{hos_name} หมายเลข {_q} กรุณาไปรอที่บริเวณ{dep_name}"""
        resp = push_alert(_token, _title, _body)
        print(datetime.now(), _q, q_signal, resp)
    except Exception as e:
        print(datetime.now(), str(e))


#### เตือนให้มา รับยาๅ A (rx) ####
def rx_alert():
    # return None
    ## config ##
    dep_code = "030"
    dep_name = "ห้องจ่ายยา"
    q_signal = "rx"
    m, n = 5, 10  # เตือนคนที่เท่าไร กับ เท่าไร
    ## end-config ##

    sql = f""" SELECT q.depq,a.token
                FROM ovst_queue_server q
                inner join ovst o on o.vn = q.vn
                LEFT JOIN smart_assis_client a on a.hn = q.hn
                WHERE q.STATUS = '1'
                AND q.date_visit = CURDATE()
                AND q.stationno IS NULL
                AND q.dep = '{dep_code}'
                AND o.cur_dep = '{dep_code}'
                ORDER BY q.time_visit asc LIMIT {n} """
    db = con_db_his()
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    db.close()
    print(datetime.now(), f"Calling {q_signal} {dep_code}  =  {len(rows)}")

    try:
        _q = str(rows[m - 1][0])
        _token = str(rows[m - 1][1])
        _title = f"อีก {m} คิวจะถึงคิวของท่าน"
        _body = f"""{hos_name} หมายเลข {_q} กรุณาไปรอที่บริเวณ{dep_name}"""
        resp = push_alert(_token, _title, _body)
        print(datetime.now(), _q, q_signal, resp)
    except Exception as e:
        print(datetime.now(), str(e))

    try:
        _q = str(rows[n - 1][0])
        _token = str(rows[n - 1][1])
        _title = f"อีก {n} คิวจะถึงคิวของท่าน"
        _body = f"""{hos_name} หมายเลข {_q} กรุณาไปรอที่บริเวณ{dep_name}"""
        resp = push_alert(_token, _title, _body)
        print(datetime.now(), _q, q_signal, resp)
    except Exception as e:
        print(datetime.now(), str(e))


if __name__ == '__main__':

    push_service = FCMNotification(api_key=api_key)
    sio = socketio.Client()
    sio.connect(queue_signal)
    print(datetime.now(), "App Smart Assis Alert Service is Running.")

    """
    Note : 
    -เตือนให้มา ซักประวัติ A (ax) 1-6
    -เตือนให้มา ห้องตรวจ A (ay) 1-3,9

    -เตือนให้มา ซักประวัติ B (bx) 1-6
    -เตือนให้มา ห้องตรวจ B (by) 4-7

    -เตือนนให้มา รับยา (rx) 1-5
    """


    @sio.event
    def ax1(_q):
        if _q != 's99999':
            print(datetime.now(), "ax1 is calling ", _q.upper())
            current_queue_alert(_q, "จุดซักประวัติ A")  # คิวที่กดเรียก
            ax_alert()


    @sio.event
    def ax2(_q):
        if _q != 's99999':
            print(datetime.now(), "ax2 is calling ", _q.upper())
            current_queue_alert(_q, "จุดซักประวัติ A")  # คิวที่กดเรียก
            ax_alert()


    @sio.event
    def ax3(_q):
        if _q != 's99999':
            print(datetime.now(), "ax3 is calling ", _q.upper())
            current_queue_alert(_q, "จุดซักประวัติ A")  # คิวที่กดเรียก
            ax_alert()


    @sio.event
    def ax4(_q):
        if _q != 's99999':
            print(datetime.now(), "ax4 is calling ", _q.upper())
            current_queue_alert(_q, "จุดซักประวัติ A")  # คิวที่กดเรียก
            ax_alert()


    @sio.event
    def ax5(_q):
        if _q != 's99999':
            print(datetime.now(), "ax5 is calling ", _q.upper())
            current_queue_alert(_q, "จุดซักประวัติ A")  # คิวที่กดเรียก
            ax_alert()


    @sio.event
    def ax6(_q):
        if _q != 's99999':
            print(datetime.now(), "ax6 is calling ", _q.upper())
            current_queue_alert(_q, "จุดซักประวัติ A")  # คิวที่กดเรียก
            ax_alert()


    @sio.event
    def ay1(_q):
        if _q != 's99999':
            print(datetime.now(), "ay1 is calling ", _q.upper())
            current_queue_alert(_q, "หน้าห้องตรวจ A")  # คิวที่กดเรียก
            ay_alert()


    @sio.event
    def ay2(_q):
        if _q != 's99999':
            print(datetime.now(), "ay2 is calling ", _q.upper())
            current_queue_alert(_q, "หน้าห้องตรวจ A")  # คิวที่กดเรียก
            ay_alert()


    @sio.event
    def ay3(_q):
        if _q != 's99999':
            print(datetime.now(), "ay3 is calling ", _q.upper())
            current_queue_alert(_q, "หน้าห้องตรวจ A")  # คิวที่กดเรียก
            ay_alert()


    @sio.event
    def ay9(_q):
        if _q != 's99999':
            print(datetime.now(), "ay9 is calling ", _q.upper())
            current_queue_alert(_q, "หน้าห้องตรวจ A")  # คิวที่กดเรียก
            ay_alert()


    @sio.event
    def rx1(_q):
        if _q != 's99999':
            print(datetime.now(), "rx1 is calling ", _q.upper())
            current_queue_alert(_q, "ห้องจ่ายยา")  # คิวที่กดเรียก
            rx_alert()


    @sio.event
    def rx2(_q):
        if _q != 's99999':
            print(datetime.now(), "rx2 is calling ", _q.upper())
            current_queue_alert(_q, "ห้องจ่ายยา")  # คิวที่กดเรียก
            rx_alert()


    @sio.event
    def rx3(_q):
        if _q != 's99999':
            print(datetime.now(), "rx3 is calling ", _q.upper())
            current_queue_alert(_q, "ห้องจ่ายยา")  # คิวที่กดเรียก
            rx_alert()


    @sio.event
    def rx4(_q):
        if _q != 's99999':
            print(datetime.now(), "rx4 is calling ", _q.upper())
            current_queue_alert(_q, "ห้องจ่ายยา")  # คิวที่กดเรียก
            rx_alert()


    @sio.event
    def rx5(_q):
        if _q != 's99999':
            print(datetime.now(), "rx5 is calling ", _q.upper())
            current_queue_alert(_q, "ห้องจ่ายยา")  # คิวที่กดเรียก
            rx_alert()
