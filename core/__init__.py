import datetime

class SystemInfo:
   def __init__():
       pass

   @staticmethod
   def get_time():
        now = datetime.datetime.now()
        answer = 'São {} horas e {} minutos'.format(now.hour, now.minute)
        return answer
   
   @staticmethod
   def get_second():
       now = datetime.datetime.now()
       answer_second = now.second
       return answer_second