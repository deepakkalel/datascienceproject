#from src folder's datascience sub folder it will import logger details (present in __init__.py file) 
from src.datascience import logger 

#below msg will print and confirm if logging code working correctly or not
logger.info("welcome to our custom logging data science")
