from pyapp.calc import calc as real_calc
import sys
import zerorpc
import logging

logging.basicConfig(
    filename='calc.log',
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s %(message)s',
)
logger = logging.getLogger('__name__')


class CalcApi:
    def calc(self, text):
        logger.info("%s", text)
        return real_calc(text)

    def echo(self, text):
        """echo arbitrary text"""
        return text


def main():
    port = 4242
    addr = 'tcp://127.0.0.1:{port}'.format(port=port)
    s = zerorpc.Server(CalcApi())
    s.bind(addr)
    print("Starting to listen on {address}".format(address=addr))
    try:
        s.run()
    except KeyboardInterrupt:
        print("Terminated by KeyboardInterrupt.")
    

if __name__ == '__main__':
    main()
