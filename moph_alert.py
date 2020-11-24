import requests
import json
import socketio
from datetime import datetime
import mysql.connector

###########  config ################

hos_name = "โรงพยาบาลด่านขุนทด"
queue_signal = "http://www.smartqplk.com:19009"
api_key = "AIzaSyBOZuUvtAUY0V3WBwIET9000mn_bmGTCCQ"
uri_alert = "https://mophconnect.go.th/api/alert"


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

def moph_push(_q, _line, _hn, _pt_name, _dep_name):
    _date = str(datetime.now())[:-7]
    msg = {
        "userId": f"{_line}",
        "hospitalName": "โรงพยาบาลสมาร์ทคิว",
        "origin": "กระทรวงสาธารณสุข",
        "queueNumber": f"{_q}",
        "patientName": f"{_pt_name}",
        "appointmentDate": _date,
        "appointmentTime": f"ถึงคิวของท่านแล้ว กรุณามาที่บริเวณ{_dep_name}",
        "backgroundColor": "#fcba03",
        "header": f"{_dep_name}",
        "detailsLinkLabel": "ดูรายละเอียดเพิ่มเติม",
        "detailsLink": f"https://www.smartqplk.com?hn={_hn}",
        "currentQueueLinkLabel": "ดูคิวปัจจุบัน",
        "currentQueueLink": f"https://www.smartqplk.com?hn={_hn}"
    }
    body = json.dumps(msg)
    try:
        resp = requests.post(url=uri_alert, data=body)
    except Exception as e:
        resp = str(e)
        pass
    return resp


### ส่งแจ้งเตือนให้มา จุดซักประวัติ ###
def sc_alert():
    dep_name = "จุดซักประวัติ"
    dep_code = "010"
    q_signal = "sc"
    m, n = 5, 10

    sql = f""" SELECT q.depq,a.moph_line_id ,concat(a.pname,a.fname,' ',a.lname) pt_name ,a.hn
                   FROM ovst_queue_server q
                   inner join ovst o on o.vn = q.vn
                   LEFT JOIN smart_moph_connect_member a on a.hn = q.hn
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
    print(datetime.now(), f"Patient at {q_signal} {dep_code} {dep_name}  =  {len(rows)}")

    try:
        _q = str(rows[m - 1][0])
        _line = str(rows[m - 1][1])
        _name = str(rows[m - 1][2])
        _hn = str(rows[m - 1][3])
        _dep_name = dep_name
        resp = moph_push(_q,_line,_hn,_)
    except Exception as e:
        resp = str(e)
    print(datetime.now(), resp)


if __name__ == '__main__':
    sio = socketio.Client()
    sio.connect("http://www.smartqplk.com:19009")
    print("Monitoring...... Socket IO")


    @sio.event
    def sc1(_q):
        print(datetime.now(), f"sc1 calling {_q}")
        sc_alert()
