# -*- coding: utf-8 -*-
import hashlib
import uuid


class User:
    def __init__(self):
        self.salt_password = None

    def set_password(self, raw_password):
        salt = uuid.uuid4().hex # 产生随机的盐值
        hashed_password = hashlib.sha512(raw_password + salt).hexdigest()
        self.salt_password = '%s$%s' % (salt, hashed_password) # 将盐和密码保存到数据库，以'$'隔开 
        print 'salt: %s' % salt
        print 'hashed_password: %s' % hashed_password
        print 'salt_password: %s' %  self.salt_password

    def check_password(self, raw_password):
        (salt, hashed_password) = self.salt_password.split('$')
        return hashed_password == hashlib.sha512(raw_password + salt).hexdigest()


if __name__ == '__main__':
    user = User()
    user.set_password('1234')
    assert(user.check_password('1234') == True)
    assert(user.check_password('123') == False)

