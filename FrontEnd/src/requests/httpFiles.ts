const FetchDataFile: FC<_Props> = async ({
    _endPoint,
    _isHttps = false,
    _parse = false,
    _method = "GET",
    _dialer,
    _http,
    _body,
    _headers = {
      "Content-Type": "application/json",
    },
    _appends,
    _headerSend,
    _headerSendMethods,
    _err = "FAILED, UNABLE TO FETCH",
    _host = "localhost",
    _port = "80",
    _APIBody = "api/v1",
    _signal,
  }) => {
    let resData;
    {
      _isHttps ? (_http = "https") : (_http = "http");
    }
  
    _dialer = `${_http}://${_host}:${_port}/${_APIBody}/${_endPoint}`;
  
    try {
        const _formdata = new FormData();
        //< pass an obj and map the appends by key and val
        _formdata.append("name", userform.name);
        _formdata.append("email", userform.email);
        _formdata.append("photo", userform.photo);
        console.log("Form from PATCH: ", _formdata);
    
      //console.log("from dailer ", _body);
      const _response = await fetch(_dialer, {
        method: _method,
        body: _formdata,
        redirect: "follow",
        credentials: "include",
        signal: _signal,
      });
  
      {
        _parse ? (resData = await _response.json()) : (resData = _response);
      }
      if (_resData.status === "success") {
        showAlert("success", `${_method} Succesfull!`);
      }
      if (!_response.ok) {
        //< _response NOT PARSED
        console.log("from HTTP", _response); //create an obeject and pass it oveer
        httpErrorGenerator(_response);
      }
      return resData;
    } catch (_error) {
      console.log(_error);
      showAlert("error", `Error: [ ${_error} ]\nPlease Try Again Later`);
    }
  };
  
  /////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
  /////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
  type _Props = {
    _endPoint: string;
    _isHttps?: boolean;
    _http?: string;
    _host?: string;
    _port?: string;
    _parse?: boolean;
    _method?: "GET" | "POST" | "DELETE" | "PATCH";
    _headers?: HeadersInit;
    _body?: login | User | NewUser | unknown;
    _headerContentType?: string;
    _headerSend?: boolean;
    _headerSendMethods?: "POST" | "PATCH";
    _dialer?: string;
    _APIBody?: string;
    _err?: string;
    _signal?: any; //RequestInit;
    _appends?: _append[];
  };
  type login = {
    email: string;
    password: string;
  };
  type _append ={
    _key: string
    _data: any;
  }
  
  export default FetchData;
  /////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
  /////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
  import { FC } from "react";
  import { httpErrorGenerator } from "../models/functions/errorHandlers";
  import { NewUser, User } from "../models/types/userType"; //@ts-ignore
  import { showAlert } from "../utility/imports.js";
  