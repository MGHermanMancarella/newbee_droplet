from utilities.db_utils import query_tech_stack
from utilities.utils import freq_count
from app import conn

def gimme_tech_stack ():
    data = query_tech_stack()
    stack = freq_count(data)
    print(stack)

gimme_tech_stack()