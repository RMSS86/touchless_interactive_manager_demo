//> LOGOUT CUSTOM HOOK
export const useLogOut = async (
  //> VRABILES INPUT TYPES DECLARATIONS
  _userSetter: React.Dispatch<React.SetStateAction<User | null>>,
  _modalCloser: () => void,
  _navigator: void | Promise<void>,
  _endPoint: string = "users/logout",
  _method: string = "GET",
  _loggable: boolean = false
) => {

  try { //> TRY TO FETCH DATA FROM BACKEND USING CUSTOM FETCHER
    const _response: any = await FetchData({
      _endPoint: _endPoint,
      _method: "GET",
    });
    const _resData = await _response.json(); //> IF DATA GO AHEAD SIR!
    if (_loggable) console.log("from log out", _resData); //> LOGGER
    //> ON SUCCESS PROCEED TO THE USER STEP PIPELINE
    if (_resData.status === "success") {
      _userSetter(_userDefault); //< MODIFY LOCAL STORAGE
      _modalCloser; //> CLOSES THE MODAL WITH ANIMATION [ AND REF ]
      //> ENSURES NO DATA IN LOCAL STORAGE FROM PREVIOUS USER PERSISTS
      //useLocalUser({ _action: "remove", _storageKey: "user" });
      showAlert("success", "Succesflly Logged Out!"); //> UI SUCCESS ALERT
      logActions({ //> COORDINATES UI ACCTIONS SUCH AS NAVIGATE TO HOMEPAGE
        _action: "logout",
        _direct: () => _navigator,
      });
    }
  } catch (err) {
    showAlert("error", err); //> ON ERROR NOTIFIES USER THROUGH UI
    if (_loggable) console.log(err); //> LOGGER TO CONSOLE IF TRUE
  }
};

import FetchData from "../../requests/http";
import { useUserContext } from "../../store/UserContext";
import { _userDefault, User } from "../../utility/data/data";
import { logActions } from "../functions/userLogActions";
import { useLocalUser } from "./useLocalUser"; //@ts-ignore
import { showAlert } from "../../utility/imports.js";
import { useNavigate } from "react-router";
