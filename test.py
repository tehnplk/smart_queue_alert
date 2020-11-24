from pyfcm import FCMNotification

api_key = "AIzaSyBOZuUvtAUY0V3WBwIET9000mn_bmGTCCQ"

data_message = {
    "click_action": "FLUTTER_NOTIFICATION_CLICK",
    "id": "1",
    "status": "done",
    "screen": "QueuePage"
}


def push_alert(_token, _title, _msg_body):
    return push_service.notify_single_device(
        registration_id=_token,
        message_title=_title,
        message_body=_msg_body,
        data_message=data_message,
        low_priority=False
    )


if __name__ == '__main__':
    _title = f"อีก 5 คิวจะถึงคิวของท่าน"
    _msg_body = f"""หมายเลข A000 กรุณาไปรอที่บริเวณ จุดทดสอบ"""
    _token = "fqHeYGvaiMU:APA91bFE-nVe6uGURPvhN3WzEiHcHtiQUFHpgOE-BIApYvMpKLl3g3lF6v0PBYnRpdVyVJXN4DutG7cEBj5tyVuXortc7n4IFiqWVj21B38-SCDby6cRKE8pRRaWS3qp4UHIS3kyYJAK"

    push_service = FCMNotification(api_key=api_key)
    push_alert(_token, _title, _msg_body)
