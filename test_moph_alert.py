import requests
import json
import socketio
from datetime import datetime
import mysql.connector

###########  config ################

HOS_NAME = "โรงพยาบาลแก้งคร้อ"
URI_ALERT = "https://mophconnect.go.th/api/alert"
URI_QUE_ALERT = "mophconnect.go.th/api/queue/notify"

###########  end-config ################

def moph_push(_q, _line, _hn, _pt_name, _dep_name):
    _date = str(datetime.now())[:-7]
    msg = {
        "userId": f"{_line}",
        "hospitalName": f"{HOS_NAME}",
        "origin": "กระทรวงสาธารณสุข",
        "queueNumber": f"{_q}",
        "patientName": f"{_pt_name}",
        "appointmentDate": _date,
        "appointmentTime": f"ถึงคิวของท่านแล้ว กรุณามาที่บริเวณ{_dep_name}",
        "backgroundColor": "#ED146F",
        "header": f"{_dep_name}",
        "detailsLinkLabel": "ดูรายละเอียดเพิ่มเติม",
        "detailsLink": f"https://www.smartqplk.com?hn={_hn}",
        "currentQueueLinkLabel": "ดูคิวปัจจุบัน",
        "currentQueueLink": f"https://www.smartqplk.com?hn={_hn}"
    }

    msg = {
        "userId": _line,
        "hospitalName": "โรงพยาบาลแก้งคร้อ",
        "origin": "กระทรวงสาธารณสุข",
        "queueNumber": "พรุ่งนี้ท่านมีนัด",
        "patientName": "นายทดสอบ ระบบ",
        "appointmentDate": "2020-12-30",
        "appointmentTime": "นัดที่: ห้องเจาะเลือด\r\nกรุณางดน้ำงดอาหารหลัง 20.00 น.",
        "backgroundColor": "#96facf",
        "detailsLink": "https://mophconnect.go.th",
        "currentQueueLink": "https://mophconnect.go.th"
    }

    body = json.dumps(msg)
    try:
        resp = requests.post(url=URI_ALERT, data=body)
    except Exception as e:
        resp = str(e)
        pass
    return resp


if __name__ == '__main__':
    _uuid = "5fe05f31f4dc687f63adcd4f"
    #_uuid = "5f3495441f9fcfcfe667c115"
    r = moph_push("A002", _uuid, "0000001", "นายทดสอบ ระบบ", "ห้องจ่ายยา")
    print(repr(r))
