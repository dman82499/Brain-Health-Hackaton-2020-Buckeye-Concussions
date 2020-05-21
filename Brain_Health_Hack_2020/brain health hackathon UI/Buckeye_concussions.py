# -*- coding: utf-8 -*-
'''
Buckeye Hackathon 2019 Concussion project
Buckeye concussions
==============
Code given is used from the template Containers, from the kivy example templates module
installed via website

'''
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
import kivy.uix.pagelayout
import kivy.uix.scrollview
import kivy.core.window

import kivy
kivy.require('1.8.0')


class RootWidget(BoxLayout):
    '''Create a controller that receives a custom widget from the kv lang file.
    Add an action to be called from a kv file.
    '''

    container = ObjectProperty(None)


class BuckeyeConApp(App):

    '''This is the app itself'''

    def build(self):
        '''This method loads the root.kv file automatically

        :rtype: none
        '''
        # loading the content of root.kv
        self.root = Builder.load_file('kv/root.kv')
        Window.clearcolor = (1, 1, 1, 1)

    def next_screen(self, screen):
        '''Clear container and load the given screen object from file in kv
        folder.

        :param screen: name of the screen object made from the loaded .kv file
        :type screen: str
        :rtype: none
    '''

        filename = screen + '.kv'
        # unload the content of the .kv file
        # reason: it could have data from previous calls
        Builder.unload_file('kv/' + filename)
        # clear the container
        self.root.clear_widgets()
        # load the content of the .kv file
        screen = Builder.load_file('kv/' + filename)
        # add the content of the .kv file to the container
        self.root.add_widget(screen)


if __name__ == '__main__':
    '''Start the application'''

    BuckeyeConApp().run()
