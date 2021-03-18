from pyfcm import FCMNotification

api_key = "AAAA1bq8cok:APA91bEwnfLAUz5FQaFbCj9SB8iDkpKBYO78vZ9Ar3jx_9F8RwsjRLDRR4jHZGaEgUWxDiTYsynwv2PNhkSVsxnSRr0a37JBmi1RAoa2bVZ0d5wnA_saDViOcFcS_tOwQp-CRmMIcvwS"

push_service = FCMNotification(api_key=api_key)
data_message = {
    "click_action": "FLUTTER_NOTIFICATION_CLICK",
    "id": "1",
    "status": "done",
    "screen": "NewsPage"
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
    _title = f"ทดสอบ อีก 10 คิวจะถึงคิวของท่าน"
    _msg_body = f"""หมายเลข Q001 กรุณาไปรอที่บริเวณ จุดซักประวัติ"""
    _token = "depeVgO_f7y0FLgJQSejzd:APA91bFcnVNNjKa1fy5jRsR3Vpsx0_3uONWKzoZ9fvxjrO5zZTH7z41kecMLLLurNDCmSf28vOSc2KBghKaR0n5-1cjq6etfHLGFPm_VaOhUZB6hYIqJFuE57ZQLpuz0Ufjrr8LIENSH"
    resp = push_alert(_token, _title, _msg_body)
    print(resp)
