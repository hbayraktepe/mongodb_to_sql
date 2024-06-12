import time

import schedule

from data_transfer import DataTransfer


def job():
    transfer = DataTransfer()
    transfer.transfer_data()


schedule.every().hour.do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)
