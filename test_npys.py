#!/usr/bin/python3
# -*- coding: utf-8 -*-

import npyscreen, ph

url  = 'https://prohardver.hu'

class myEmployeeForm(npyscreen.Form):
    #def afterEditing(self):
    #    self.parentApp.setNextForm(None)
    
    def exit_application(self):
        self.parentApp.setNextForm(None)
        self.editing = False
    
    def create(self):
        self.myName = self.add(npyscreen.FixedText, value = 'sok szöveg')
        self.myName = self.add(npyscreen.FixedText, value = 'ujabb szöveg')
        self.add_handlers({'p':self.spawn_notify_popup})
        self.how_exited_handers[npyscreen.wgwidget.EXITED_ESCAPE] = self.exit_application
    
    def spawn_notify_popup(self, code_of_key_pressed):
        message_to_display = 'I popped up'
        npyscreen.notify_wait(message_to_display, title='Popup Title')        

    
class MyApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', myEmployeeForm, name='Szöveges PH bongesző')

if __name__ == '__main__':
    #ph.ph_news(url)
    TestApp = MyApplication().run()
