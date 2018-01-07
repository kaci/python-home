#!/usr/bin/python3
# -*- coding: utf-8 -*-

import npyscreen


class PhTUI(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", NewsTUI, name="PH News Browser")
        self.addForm("Art", ArtTUI, name="Article")

class NewsTUI(npyscreen.ActionForm):
    def activate(self):
        self.edit()
        self.parentApp.setNextForm("Art")

    def create(self):                
        self.siriOrHal = self.add(npyscreen.SelectOne, values=["Siri", "Cortana", "Hal", "Tay"])

    def on_ok(self):
        toHal = self.parentApp.getForm("Art")        
        toHal.pre.value = self.siriOrHal.values[self.siriOrHal.value[0]]        
        self.parentApp.switchForm("Art")

class ArtTUI(npyscreen.Form):
    def activate(self):
        self.edit()

    def create(self):        
        self.pre = self.add(npyscreen.FixedText)
        self.how_exited_handers[npyscreen.wgwidget.EXITED_ESCAPE] = self.exit_application
    
    def exit_application(self):
        self.parentApp.setNextForm(None)
        self.editing = False

if __name__ == "__main__":
    npyscreen.wrapper(PhTUI().run())
