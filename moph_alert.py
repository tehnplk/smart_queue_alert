import requests
import json
import socketio


# SEARCH TECHNOLOGY 2020#

def get_patient_from_q(_q):
    return "lind_id", "pt.name"


def alert_to_moph_connect(q_number, line_id, pt_name):
    msg = {
        "userId": f"{line_id}",
        "hospitalName": "โรงพยาบาลสมาร์ทคิว",
        "origin": "กระทรวงสาธารณสุข",
        "queueNumber": f"{q_number}",
        "patientName": f"{pt_name}",
        "appointmentDate": "2020-08-13",
        "appointmentTime": "ถึงคิวของท่านแล้ว กรุณามาที่บริเวณห้องจ่ายยา",
        "backgroundColor": "#fcba03",
        "header": "ถึงคิวรับยา",
        "detailsLinkLabel": "ดูรายละเอียดเพิ่มเติม",
        "detailsLink": "https://www.smartqplk.com",
        "currentQueueLinkLabel": "ดูคิวปัจจุบัน",
        "currentQueueLink": "https://www.smartqplk.com"
    }

    body = json.dumps(msg)
    res = None
    try:
        API = "https://mophconnect.go.th/api/alert"
        res = requests.post(url=API, data=body)
    except Exception as e:
        res = str(e)
        pass
    print(res)


if __name__ == '__main__':
    sio = socketio.Client()
    sio.connect("http://www.smartqplk.com:19009")
    print("Monitoring...... Socket IO")


    @sio.event
    def sc1(q):
        print(f"ช่องสัญญาณที่ 1 หมายเลข {q}")
        q_number = f"หมายเลข {q}"
        pt_name = "นายสมชาย สบายดี"
        line_id = "5f3495441f9fcfcfe667c115"
        alert_to_moph_connect(q_number, line_id, pt_name)


    @sio.event
    def sc2(q):
        print(f"ช่องสัญญาณที่ 2 หมายเลข {q}")
        q_number = f"หมายเลข {q}"
        pt_name = "นายสมชาย สบายดี"
        line_id = "5f3495441f9fcfcfe667c115"
        alert_to_moph_connect(q_number, line_id, pt_name)
