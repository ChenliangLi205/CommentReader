# -*- coding: utf-8 -*-

class CommentProcessor(object):
    @staticmethod
    def deleteWhiteSpace(text):
        return text.replace(" ", "")
