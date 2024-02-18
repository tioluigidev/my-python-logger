from logger import Logger
import time

logger= Logger()

logger.clear()

with logger.set_status('Processing one thing...') as status:
  time.sleep(2)

with logger.set_status('Processing another thing...') as status:
  time.sleep(2)
  logger.update_status(status, 'Still processing...')
  time.sleep(2)  
  logger.append_status(status, ' [green][OK][/]')

with logger.set_status('Processing 3 things...') as status:
  time.sleep(1)
  logger.append_status(status, '[green][OK][/] ')
  time.sleep(1)
  logger.append_status(status, '[blue][OK][/] ')
  time.sleep(1)
  logger.append_status(status, '[yellow][OK][/]') 
  time.sleep(1) 

logger.info('This is an info message')
time.sleep(1)
logger.debug('This is a debug message')
time.sleep(1)
logger.warning('This is a warning message')
time.sleep(1)
logger.error('This is an error message')