from pyapp.calc import calc as real_calc
import sys
import zerorpc


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
    s = zerorpc.Server(CalcApi())
    s.bind(addr)
    print("Starting to listen on {address}".format(address=addr))
    try:
        s.run()
    except KeyboardInterrupt:
        print("Terminated by KeyboardInterrupt.")
    

if __name__ == '__main__':
    main()
