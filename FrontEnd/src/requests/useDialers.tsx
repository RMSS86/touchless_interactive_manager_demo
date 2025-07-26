//<     ENUMERATE THOSE PLACES YOU'VE USED fETCHDATA FUNCTION
///<    CLASIFY THE TYPES OF REQUEST BEING MADE
////<   DEFINE
import { useQuery } from "@tanstack/react-query";
export async function useQueryDailer({
  e,
  _dialer,
  _sendfetch,
  _fetchMode = "QUERY",
  _queryKey,
  _endPoint,
  _mode,
  _method,
  _signal,
  _success,
  _successMSG,
  _logAction,
  _requestBody,
  _staleTime = FIVE_MINUTES_IN_MILLISECONDS,
  _gcTime = TEN_MINUTES_IN_MILLISECONDS,
  _forForm = false,
  _logable = false,
}: _dialerProps) {
  ////FUNCTIONS////FUNCTIONS////FUNCTIONS////FUNCTIONS////FUNCTIONS////FUNCTIONS///
  ////FUNCTIONS////FUNCTIONS////FUNCTIONS////FUNCTIONS////FUNCTIONS////FUNCTIONS///

  ////FUNCTIONS////FUNCTIONS////FUNCTIONS////FUNCTIONS////FUNCTIONS////FUNCTIONS///
  ////FUNCTIONS////FUNCTIONS////FUNCTIONS////FUNCTIONS////FUNCTIONS////FUNCTIONS///
  if (_forForm) e?.preventDefault(); //< PREVENTING DEFAULT

  //< QUERY MODE
  let _fetchRequest:
    | ReactElement<unknown, string | JSXElementConstructor<any>>
    | Iterable<ReactNode>
    | any;

  const { data, isPending, isError, error } = useQuery({
    queryKey: [_queryKey],
    queryFn: async () => await _sendfetch,
    staleTime: _staleTime, //<
    gcTime: _gcTime, //<
  });

  if (isPending) {
    showAlert("loading", "LOADING...", 1000);
  }
  if (isError) {
    //<  error.info?.message || "Failed to fetch events."}
    showAlert("error", error.info?.message || "Failed to fetch events.", 5000);
  }

  //<
  if (data) {
    if (_logable) console.log("from useQuery Hook: ", data._data);
  }
  const _data = await data._data;
  return _data;

  // return await data._data;
}
// Promise<TData>
/////TYPES/////TYPES/////TYPES/////TYPES/////TYPES/////TYPES/////TYPES////
/////TYPES/////TYPES/////TYPES/////TYPES/////TYPES/////TYPES/////TYPES////
type _dialerProps = {
  e?: { preventDefault: () => void };
  _sendfetch?: any;
  _queryKey?: string;
  _signal?: RequestInit;
  _forForm?: boolean;
  _logable?: boolean;
  _endPoint?: string;
  _success?: string;
  _successMSG?: string;
  _requestBody?: string;
  _mode?: _modes;
  _staleTime?: number;
  _gcTime?: number;
  _logAction?: _logActions;
  _fetchMode?: "QUERY" | "SIMPLE";
  _method?: "GET" | "POST" | "PATCH";
  _dialer?: ReactNode | Promise<ReactNode>;
  _setStater?: React.Dispatch<React.SetStateAction<unknown>>;
};
type _modes =
  | "LOGIN"
  | "LOGOUT"
  | "UPDATE-ME"
  | "UPDATE-PWD"
  | "RESET-PWD"
  | "FORGOT-PWD";
type _logActions = "login" | "logout" | "just-redirect" | "skip";
// //////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////
// //////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////
import {
  JSXElementConstructor,
  ReactElement,
  ReactNode,
  useEffect,
  useRef,
  useState,
} from "react";
import FetchData from "./http.js"; //@ts-ignore
import { showAlert } from "../utility/imports.js";
import {
  TWO_MINUTES_IN_MILLISECONDS,
  FIVE_MINUTES_IN_MILLISECONDS,
  TEN_MINUTES_IN_MILLISECONDS,
} from "../utility/constants/contstants.js";
