from mycroft import MycroftSkill, intent_file_handler


class EvenimenteAzi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('azi.evenimente.intent')
    def handle_azi_evenimente(self, message):
        astazi = ''

        self.speak_dialog('azi.evenimente', data={
            'astazi': astazi
        })


def create_skill():
    return EvenimenteAzi()

