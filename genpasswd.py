#!/usr/bin/python

"""Generate a somewhat random password which is difficult to mess up.

   def genpasswd(l = 9, sepspace = 0, sepchar = '-'):
       Returning a passwort to the caller.

       l:        length of password to generate
       sepspace: interval at which seperators will be inserted
       sepspace: seperator to be used

       Examples:

       genpasswd(11, 3):      '54G Y8A 46D'
       genpasswd(11, 3, ' '): 'PXB CGC D5P'
       genpasswd(11):         'KCPTHSG9LBC'

       Note:

       This passwords are of low crypographic quality. They were designed
       to be resistent against typos when copying them from paper
       to a Web form. Don't expect any real entropy from them.

       
       Authors:

       This Software was written by drt@un.bewaff.net for the
       twisd AG, Bonn, Germany. The twisd
       AG kindly donated it as Freie Software.
       
   """

__version__ = '$Id: genpasswd.py,v 1.1 2002/05/23 19:20:07 drt Exp $'

__copyright__ = """(c) 2001 twisd AG, Bonn - http://www.twisd.de/
further distribution is granted under the terms of LGPL or classical
MIT Licence."""


import random

source = '23456789ABCDFGHKLPQRSTXYZabdefghpqrty'

def genpasswd(l = 9, sepspace = 0, sepchar = '-'):
    """Generate a pseudo - random password.

    The password will be l chars long. If sepspace is not 0 there
    will be inserted a seperator every sepspace chars. The
    default sepchar is '-'.
    """
    
    ret = ''

    sepspace += 1
    while 1:
        ret += source[random.randrange(len(source))]
        if len(ret) >= l:
            break
        if (sepspace != 1) and ((len(ret) + 1 )  % sepspace == 0):
            ret += sepchar
            
    return ret

def test():
    random.seed(23)
    data = genpasswd(11, 3)
    print "genpasswd(11, 3):     ", data
    assert data == '54G-Y8A-46D'
    data = genpasswd(11, 3, ' ')
    print "genpasswd(11, 3, ' '):", data
    assert data == 'PXB CGC D5P'
    data = genpasswd(11)
    print "genpasswd(11):        ", data
    assert data == 'KCPTHSG9LBC'

if __name__ == '__main__':
  import sys
  sys.stdout.write(genpasswd(11, 3))
  
