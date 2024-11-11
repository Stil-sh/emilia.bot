def send_message(vk, peer_id, message="", attachment="", reply_to=None):
    """Отправить сообщение"""
    vk.messages.send(
        peer_id=peer_id, message=message, 
        attachment=attachment, reply_to=reply_to, random_id=0
    )


def edit_message(vk, peer_id, message_id, message="", attachment=""):
    """Изменить сообщение"""
    vk.messages.edit(
        peer_id=peer_id, message=message, 
        attachment=attachment, message_id=message_id, random_id=0
    )
