from pyfcm import FCMNotification

api_key = "AIzaSyBOZuUvtAUY0V3WBwIET9000mn_bmGTCCQ"
push_service = FCMNotification(api_key=api_key)
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
    _title = f"ทดสอบ3 อีก 1 คิวจะถึงคิวของท่าน"
    _msg_body = f"""หมายเลข A000 กรุณาไปรอที่บริเวณ จุดทดสอบ3"""
    _token = "fsesCPEAFf0:APA91bG95AnMCWUkofrjtXIG3zjJkbfzkOZuvTXceTf3j30rV4FBdFJZt5oYVSNae_PD8N_B0_OVGoMNR0P2li6xjYkjwjalUhckB7GjMPcL95Rc7X-ucGXma2Uixyw9y4SBkDGDpty_"

    resp = push_alert(_token, _title, _msg_body)
    print(resp)
