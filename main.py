from controller import Controller
import configparser
if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("config.ini")
    try:
        to_run = int(config.get("program", "to_run"))
    except:
        print("Wrong configurations")
    controller: Controller = Controller()

    if(to_run == 0):
        controller.call_request()
    else:
        controller.check_urls(controller.request.request_list)
