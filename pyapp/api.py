import sys
import zerorpc
import logging

from pyapp.calc import calc as real_calc

logging.basicConfig(
    filename='calc.log',
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s %(message)s',
)
logger = logging.getLogger('__name__')


class CalcApi:
    def calc(self, text):
        try:
            return real_calc(text)
        except Exception as exc:
            return 0.0

    def echo(self, text):
        """echo arbitrary text"""
        return text


def main():
    port = 4242
    addr = 'tcp://127.0.0.1:{port}'.format(port=port)
    client = zerorpc.Client()
    client.connect(addr)
    print("Connecting on {address}".format(address=addr))
    ca = CalcApi()
    answer = ""
    while True:
        try:
            formula = client.update(answer)
            answer = ca.calc(formula)
            logger.info("{} => {}".format(formula, answer))
        except KeyboardInterrupt:
            logger.info("Terminated by KeyboardInterrupt.")
            break
        except Exception as exc:
            logger.exception(exc)
            break
    

if __name__ == '__main__':
    main()
