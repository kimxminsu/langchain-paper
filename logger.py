# 시스템 활동 기록 처리
from datetime import datetime
class Logger:


    def log(self, input, message):
        now = datetime.now()
        self.time = now.strftime("%D %H:%M:%S")
        try:
            with open('LangchainLog.txt', 'a') as file:
                file.write(f'[{self.time}] Q:{input} \n A:{message}\n\n')
        except:
            with open('LangchainLog.txt', 'a') as file:
                file.write(f'[{self.time}]: 입출력 오류')
