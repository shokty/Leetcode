from threading import Barrier

class Foo(object):
    def __init__(self):
        self.first = Barrier(2)
        self.second = Barrier(2)
        pass

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first.wait()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        self.first.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second.wait()

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        self.second.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()