from datetime import datetime
import pytz


## will need to change this so that it writes to a DB
def add_weight_point(weight):
    file_name = "weight"
    try:
        with open(file_name, 'a') as f:
            f.write(weight + ", ")
            tz = pytz.timezone('America/Los_Angeles')
            local_now = datetime.now(tz)
            dt_string = str(local_now.date()) + ' ' +  str(local_now.time())
            f.write(dt_string + "\n")
    except:
        print ("Weight sad :-(")
        pass

if __name__ == "__main__":
    add_weight_point("0.0")
