export const logActions = async ({ _action, _direct }: _actionProps) => {
  switch (_action) {
    case "login":
      return _direct;
    case "logout":
      return _direct;
    case "password-reset":
      return _direct;
    default:
      return _direct;
  }
};

// export async function _sendUserRequest({
//   e,
//   _mode,
//   _method,
//   _APItarget,
//   _requestBody,
//   _logable = false,
//   _success = "success",
//   _successMSG = "Succesfully Completed!",
//   _logAction,
//   _setStater,
// }: _requestProps) {
//   e.preventDefault();
//   let _response;
//   switch (_mode) {
//     case "LOGIN":
//        _response = _reDialer({
//         _APItarget: "users/login",
//         _method: "POST",
//         _requestBody: _requestBody,
//         _loger: false,
//         _mode: "POST",
//       });

//       return _response;
//     case "LOGOUT":
//       _response = _reDialer({
//         _APItarget = "users/logout";
//         _method = "GET";
//         _loger: false,
//         _requestBody: _requestBody,

//         _mode: "GET",
//       });

//       return _response;
//     case "UPDATE-ME":
//       return;
//     case "UPDATE-PWD":
//       return;
//     case "RESET-PWD":
//       return;
//     case "FORGOT-PWD":
//       return;
//     default:
//   }
// }

// const _reDialer: FC<_redailerProps> = async ({
//   _mode,
//   _APItarget,
//   _method,
//   _requestBody,
//   _loger,
// }) => {
//   let _resData;
//   let _options;
//   switch (_method) {
//     case "GET":
//       _options = {
//         _endPoint: _APItarget, ///<
//         _method: _method, ///<
//       };
//       return _options;
//     case "POST":
//       _options = {
//         _endPoint: _APItarget, ///<
//         _method: _method, ///<
//         _body: _requestBody, ///<
//       };
//       return _options;
//     case "PATCH":
//       _options = {
//         _endPoint: _APItarget, ///<
//         _method: _method, ///<
//         _body: _requestBody, ///<
//       };
//       return _options;
//     default:
//       _options = {
//         _endPoint: _APItarget, ///<
//         _method: _method, ///<
//         _body: _requestBody, ///<
//       };
//   }

//   try {
//     const _response: any = await FetchData(_options);
//     _resData = await _response.json();
//     {
//       _loger && console.log(_resData);
//     }
//     return _resData;

//     // _setStater;
//     // if (_resData.status === _success) {
//     //   showAlert(_success, _successMSG);
//     //   // logActions({
//     //   //   _action: "login",
//     //   //   _user: globalUser,
//     //   //   _direct: _navigate("/tours"),
//     //   // });
//     //   ///< LOG-ACTIONS
//     // }
//     return _resData;
//   } catch (err) {
//     console.log(err);
//     showAlert("error", "Sorry, Something Happend...");
//   }
// };

///////LOCAL TYPES///////LOCAL TYPES///////LOCAL TYPES///////LOCAL TYPES////////
///////LOCAL TYPES///////LOCAL TYPES///////LOCAL TYPES///////LOCAL TYPES////////
type _requestProps = {
  e: { preventDefault: () => void };
  _mode?: _modes;
  _method: _methods;
  _APItarget: string;
  _requestBody: string;
  _logable: boolean;
  _successMSG?: string;
  _success: string;
  _logAction: _logActions;
  _setStater: React.Dispatch<React.SetStateAction<unknown>>;
};
type _modes =
  | "LOGIN"
  | "LOGOUT"
  | "UPDATE-ME"
  | "UPDATE-PWD"
  | "RESET-PWD"
  | "FORGOT-PWD";
type _methods = "GET" | "POST" | "PATCH";
type _logActions = "login" | "logout" | "just-redirect" | "skip";
type _actionProps = {
  _user?: string;
  _action: "login" | "logout" | "password-reset";
  _direct: () => void;
};
type _redailerProps = {
  _mode: _methods;
  _APItarget: string;
  _method: _methods;
  _requestBody: string;
  _loger: boolean;
};
/////IMPORTS/////IMPORTS/////IMPORTS/////IMPORTS/////IMPORTS/////IMPORTS/////IMPORTS////
/////IMPORTS/////IMPORTS/////IMPORTS/////IMPORTS/////IMPORTS/////IMPORTS/////IMPORTS////
//@ts-ignore
import { Link, useNavigate } from "react-router-dom";
import FetchData from "../../requests/http"; //@ts-ignore
import { showAlert } from "../../utility/imports.js";
import { FC } from "react";
import { User } from "../types/userType.js";
import { _userDefault } from "../../utility/data/data.js";

// // if (_mode === "LOGIN") {
// //   const _user = _resData.data.user;
// //   const _userToken = _resData.token;
// //   _setStater({
// //     _id: _user._id,
// //     _role: _user.role,
// //     _active: true,
// //     _name: _user.name,
// //     _email: _user.email,
// //     _passwordChangedAt: _user.passwordChangedAt,
// //     _token: _userToken,
// //     _imgDir: "",
// //     _img: "user-1.jpg",
// //   });
// //   {
// //     _logable && console.log(_user);
// //   }
// // }
