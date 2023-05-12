import os.path
import json

import flaskr.cloud.set_parameters as sp
def get_info_transfer(hours, minutes, folder_drive, folder_azure, use_json=True):
    
    if use_json:
        if os.path.exists(sp.PARAMETERS_TRANSFER):
            with open(sp.PARAMETERS_TRANSFER, "r") as f:
                json_content = f.read()
                parameters = json.loads(json_content)

            if (hours is None or hours == parameters["hours"]) and \
                minutes is None or minutes == parameters["minutes"] and \
                (folder_drive is None or folder_drive == parameters["folder_drive"]) and \
                (folder_azure is None or folder_azure == parameters["folder_azure"]):

                config_parameters = {parameters["hours"], parameters["minutes"], \
                                    parameters["folder_drive"], parameters["folder_azure"]}
                return config_parameters
            
            use_json = False

    if hours is not None and minutes is not None and folder_drive is not None and \
        folder_azure is not None:
        
        parameters = {"hours": hours, "minutes": minutes, "folder_drive": folder_drive,\
                    "folder_azure": folder_azure}
        with open(sp.PARAMETERS_TRANSFER, "w") as f:
            json.dump(parameters, f)
    
    return parameters